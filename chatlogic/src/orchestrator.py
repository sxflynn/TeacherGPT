import json
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
   
class Orchestrator:
    def __init__(self, gqlclient:GQLClient, user_prompt, prompts_file, system_prompt):
        self.gqlclient = gqlclient
        self.user_prompt = user_prompt
        self.prompts_file = prompts_file
        self.system_prompt = system_prompt
        self.collected_data = []
        self.prompt_mapping = {
            "student": "student_general_prompt",
            "attendance": "attendance_general_prompt",
        }
        
    def _get_orchestrator_prompt(self) -> str:
        return self.prompts_file.get('orchestrator_prompt').get('text')
      
    def _fetch_api_decision(self) -> str:
        api_decision_engine = LLMPrompt(
            prompt=(self._get_orchestrator_prompt() + self.user_prompt),
            system_prompt=self.system_prompt
            )
        return extractContent(api_decision_engine.send(json_mode=True))  
    
    def _fetch_people_list(self) -> str:
        people_list_engine = LLMPrompt(
            prompt=(self.prompts_file.get('identification_prompt').get('text') + self.user_prompt),
            system_prompt=self.system_prompt
            )
        return extractContent(people_list_engine.send(json_mode=True))
    
    def _prompt_for_apis(self) -> List[ApiDecision]:
        raw_decision_list = self._fetch_api_decision()
        print("raw decision list is: " + str(raw_decision_list))
        try:
            decision_data = json.loads(raw_decision_list)["data"]
            validated_decision_list = [ApiDecision(**item) for item in decision_data]
            print("validated_decision_list is: ", validated_decision_list)
        except ValidationError as e:
            print("raw_decision_list couldn't validate: ", raw_decision_list)
            raise ValidationError(f"The AI failed to give a JSON object with fields and variables.: {e}") from e
        return validated_decision_list
               
    def _prompt_for_people(self) -> List[Identification]:
        raw_people_list = self._fetch_people_list()
        print("raw people list is: " + str(raw_people_list))
        try:
            people_data = json.loads(raw_people_list)["data"]
            validated_people_list = [Identification(**item) for item in people_data]
        except ValidationError as e:
            print("raw_people_list couldn't validate: ", raw_people_list)
            raise ValidationError(f"The AI failed to give a JSON object with people type and query.: {e}") from e
        return validated_people_list
    
    def _fetch_id_summary(self, gqlworker_data:str) -> str:
        id_summary_engine = LLMPrompt(
            prompt=(gqlworker_data + self.prompts_file.get('identification_summary').get('text')),
            system_prompt=self.system_prompt
            )
        return extractContent(id_summary_engine.send())
    
    async def _handle_call(self, api_call):
        if api_call.api in ["none", "inaccessible"]:
            self.collected_data.append(api_call.reason)
        else:
            gqlworker_data = await self._gql_retriever(task_key=api_call.api, query=api_call.query)
            if gqlworker_data:
                self.collected_data.append(gqlworker_data)
            
    async def _handle_person(self, person):
        if person.person_type in ["none"]:
            return
        gqlworker_data = await self._gql_retriever(task_key=person.person_type, query=person.query)
        if gqlworker_data:
            id_summary = self._fetch_id_summary(gqlworker_data)
            self.user_prompt += "\n Additional ID context: \n" + id_summary
            
    async def _gql_retriever(self, task_key, query):
        task = self.prompt_mapping.get(task_key, None)
        gqlworker = GQLAgent(
            self.gqlclient,
            prompts_file=self.prompts_file,
            task_key=task_key,
            task=task,
            user_prompt=query,
            system_prompt=self.system_prompt
            )
        gqlworker_data = await gqlworker.get_data_single_prompt()
        return gqlworker_data
            
    async def run_orchestration(self):
        people = self._prompt_for_people()
        for person in people:
           await self._handle_person(person)
            
        api_task_list = self._prompt_for_apis()
        for api_call in api_task_list:
            await self._handle_call(api_call)