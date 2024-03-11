import json
import asyncio
from typing import List, Optional
from gql import gql, Client as GQLClient
from pydantic import BaseModel, ValidationError
from src.graphql import GQLAgent
from src.prompt import LLMPrompt, extractContent

prompt_mapping = {
    "student": "student_general_prompt",
    "attendance": "attendance_general_prompt",
}

class ApiDecision(BaseModel):
    api: str
    query: Optional[str] = None
    reason: Optional[str] = None
    
class Identification(BaseModel):
    person_type: str
    query: str
   
class Student(BaseModel):
    student_id: int
    first_name: str
    middle_name: str
    last_name: str
    sex: str
    dob: str
    email: str
    ohio_ssid: str    
   
class Orchestrator:
    def __init__(self, gqlclient:GQLClient, user_prompt, prompts_file, system_prompt):
        self.gqlclient = gqlclient
        self.user_prompt = user_prompt
        self.prompts_file = prompts_file
        self.system_prompt = system_prompt
        self.student_list:List[Student] = []
        self.id_context = ""
        self.collected_data = []
        self.prompt_mapping = {
            "student": "student_general_prompt",
            "attendance": "attendance_general_prompt",
        }
        
    async def _send_prompt(self, prompt_key: str, json_mode: bool = False) -> str:
        prompt_details = self.prompts_file.get(prompt_key).get('text')
        prompt_engine = LLMPrompt(
            prompt=prompt_details + self.user_prompt,
            system_prompt=self.system_prompt,
            async_client=True
        )
        if json_mode:
            response = await prompt_engine.send_async(json_mode=True)
        else:
            response = await prompt_engine.send_async()
        return extractContent(response)
    
    async def _check_for_names(self) -> bool:
        response_text = await self._send_prompt('id_gateway_prompt')
        return response_text.lower().startswith('yes')

    async def _fetch_api_decision(self) -> str:
        return await self._send_prompt('orchestrator_prompt', json_mode=True)

    async def _fetch_people_list(self) -> str:
        return await self._send_prompt('identification_prompt', json_mode=True)
    
    async def _prompt_for_apis(self, has_people) -> List[ApiDecision]:
        raw_decision_list = await self._fetch_api_decision()
        print("raw decision list is: " + str(raw_decision_list))
        try:
            decision_data = json.loads(raw_decision_list)["data"]
            validated_decision_list = [ApiDecision(**item) for item in decision_data]
        except ValidationError as e:
            print("raw_decision_list couldn't validate: ", raw_decision_list)
            raise ValidationError(f"The AI failed to give a JSON object with fields and variables.: {e}") from e
        return validated_decision_list

    async def _prompt_for_people(self) -> List[Identification]:
        raw_people_list = await self._fetch_people_list()
        print("raw people list is: " + str(raw_people_list))
        try:
            people_data = json.loads(raw_people_list)["data"]
            validated_people_list = [Identification(**item) for item in people_data]
        except ValidationError as e:
            print("raw_people_list couldn't validate: ", raw_people_list)
            raise ValidationError(f"The AI failed to give a JSON object with people type and query.: {e}") from e
        return validated_people_list
    
    async def _fetch_id_summary(self, gqlworker_data:str) -> str:
        id_summary_engine = LLMPrompt(
            prompt=(gqlworker_data + self.prompts_file.get('identification_summary').get('text')),
            system_prompt=self.system_prompt,
            async_client=True
            )
        response = await id_summary_engine.send_async()
        return extractContent(response)
    
    async def _handle_call(self, api_call:ApiDecision):
        print(f"## HANDLE CALL OF {api_call.api} JUST CALLED")
        print(f"## NOW CALLING {api_call.api} API")
        print(f"## QUERY: {api_call.query} API")
        if api_call.api in ["none", "inaccessible"]:
            self.collected_data.append(api_call.reason)
        else:
            gqlworker_data = await self._gql_retriever(task_key=api_call.api, query=api_call.query)
            if gqlworker_data:
                self.collected_data.append(gqlworker_data)
                print("## NOW ADDING TO COLLECTED DATA: {gqlworker_data}")
            
    async def _handle_person(self, person):
        if person.person_type in ["none"]:
            return
        gqlworker_data = await self._gql_retriever(task_key=person.person_type, query=person.query, data_only=True)
        print("gqlworker data in _handle_person: " + str(gqlworker_data))
        if gqlworker_data and 'student' in person.person_type:
            student_data = next(iter(gqlworker_data.values()))[0]
            new_student = Student(
                student_id=student_data.get('studentId', ''),
                first_name=student_data.get('firstName', ''),
                middle_name=student_data.get('middleName', ''),
                last_name=student_data.get('lastName', ''),
                sex=student_data.get('sex', ''),
                dob=student_data.get('dob', ''),
                email=student_data.get('email', ''),
                ohio_ssid=student_data.get('ohioSsid', '') 
            )
            return new_student
            
    async def _gql_retriever(self, task_key:str, query:str, data_only=False):
        task = self.prompt_mapping.get(task_key, None)
        gqlworker = GQLAgent(
            self.gqlclient,
            prompts_file=self.prompts_file,
            task_key=task_key,
            task=task,
            user_prompt=query + (self.id_context if self.id_context is not None else ""),
            system_prompt=self.system_prompt
            )
        gqlworker_data = await gqlworker.get_data_single_prompt(data_only)
        return gqlworker_data
    
    async def run_orchestration(self):
        print('### CHECKING IF THIS IS A PROMPT CONTAINS NAMES')
        has_people:bool = await self._check_for_names()
        
        if has_people:
            print("##PROMPT HAS PEOPLE --- PROMPTING FOR PEOPLE##")
            people = await self._prompt_for_people()
            for person in people:
                print(f"## NOW CALLING {person.person_type} API AS PART OF ID PROCESS")
                print(f"## QUERY: {person.query}")
                new_student = await self._handle_person(person)
                self.student_list.append(new_student)
                id_summary = str(new_student)
                self.id_context += "\n Additional Student context: \n" + id_summary
        
        print("##PROMPTING FOR APIS##")
        api_task_list = await self._prompt_for_apis(has_people)
        await asyncio.gather(*(self._handle_call(api_call) for api_call in api_task_list))