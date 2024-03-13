import json
import asyncio
from typing import List, Optional
from gql import gql, Client as GQLClient
from pydantic import BaseModel, ValidationError
from src.templates import TemplateManager
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
    def __init__(self, gqlclient:GQLClient, user_prompt, system_prompt):
        self.gqlclient = gqlclient
        self.user_prompt = user_prompt
        self.system_prompt = system_prompt
        self.has_people:bool = False
        self.student_list:List[Student] = []
        self.id_context = ""
        self.collected_data = []
        self.prompt_mapping = {
            "student": "student_general_prompt",
            "attendance": "attendance_general_prompt",
        }
        
    async def _send_prompt(self, prompt_key: str, json_mode: bool = False, **kwargs) -> str:
        prompt_engine = LLMPrompt(
            prompt=TemplateManager.render_template(template_name=prompt_key, **kwargs),
            system_prompt=self.system_prompt,
            async_client=True
        )
        if json_mode:
            response = await prompt_engine.send_async(json_mode=True)
        else:
            response = await prompt_engine.send_async()
        return extractContent(response)
    
    async def _check_for_names(self) -> bool:
        response_text = await self._send_prompt('id_gateway_prompt', user_prompt = self.user_prompt)
        return response_text.lower().startswith('yes')

    def _generate_list_of_people(self) -> str:
        if not self.student_list:
            return "No student data available for API calls."

        list_of_people = "These are the students that you must make API calls for:\n\n"
        for student in self.student_list:
            student_info = (
                f"First Name: {student.first_name}\n"
                f"Middle Name: {student.middle_name}\n"
                f"Last Name: {student.last_name}\n"
                f"Sex: {student.sex}\n"
                f"Date of Birth: {student.dob}\n"
                f"Email: {student.email}\n"
                f"Student ID: {student.student_id}\n"
                f"Ohio SSID: {student.ohio_ssid}\n\n"
            )
            list_of_people += student_info
        return list_of_people

    async def _fetch_api_decision(self) -> str:
        list_of_people = "" if not self.has_people else self._generate_list_of_people()
        student_api_name = "" if self.has_people else """
            API Name: Student API
            Name for the JSON key: student
            What information is available: Primarily used to lookup basic facts about a student's name, student ID number, email, sex, date of birth. Special queries exist to find students by birth month, and to count the number of students by sex.
            What information is not available: The Student API does not have direct access to related data about grades, behavior, attendance, and other broader topics. It only has access to personal information listed above.
            Do not call on the Student API for any information that is otherwise available in other APIs.
                """
        return await self._send_prompt('orchestrator_prompt', user_prompt=self.user_prompt, student_api_name=student_api_name, list_of_people = list_of_people, json_mode=True)

    async def _fetch_people_list(self) -> str:
        return await self._send_prompt('identification_prompt', user_prompt = self.user_prompt, json_mode=True)

    async def _prompt_for_apis(self) -> List[ApiDecision]:
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
    
    # unused function?
    async def _fetch_id_summary(self, gqlworker_data:str) -> str:
        id_summary_engine = LLMPrompt(
            prompt = TemplateManager.render_template('identification_summary', gqlworker_data=gqlworker_data),
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
            
    async def _handle_person(self, person) -> List[Student]:
        if person.person_type in ["none"]:
            return
        gqlworker_data = await self._gql_retriever(task_key=person.person_type, query=person.query, data_only=True)
        print("gqlworker data in _handle_person: " + str(gqlworker_data))
        if gqlworker_data and 'student' in person.person_type:
            student_data_list_raw = next(iter(gqlworker_data.values()), [])
            for student in student_data_list_raw:
                new_student = Student(
                student_id=student.get('studentId', ''),
                first_name=student.get('firstName', ''),
                middle_name=student.get('middleName', ''),
                last_name=student.get('lastName', ''),
                sex=student.get('sex', ''),
                dob=student.get('dob', ''),
                email=student.get('email', ''),
                ohio_ssid=student.get('ohioSsid', '') 
            )
                self.student_list.append(new_student)
            
    async def _gql_retriever(self, task_key:str, query:str, data_only=False):
        task = self.prompt_mapping.get(task_key, None)
        gqlworker = GQLAgent(
            self.gqlclient,
            task_key=task_key,
            task=task,
            user_prompt=query + (self.id_context if self.id_context is not None else ""),
            system_prompt=self.system_prompt
            )
        gqlworker_data = await gqlworker.get_data_single_prompt(data_only)
        return gqlworker_data
    
    async def run_orchestration(self):
        print('### CHECKING IF THIS IS A PROMPT CONTAINS NAMES')
        self.has_people = await self._check_for_names()
        
        if self.has_people:
            print("##PROMPT HAS PEOPLE --- PROMPTING FOR PEOPLE##")
            people = await self._prompt_for_people()
            for person in people:
                print(f"## NOW CALLING {person.person_type} API AS PART OF ID PROCESS")
                print(f"## QUERY: {person.query}")
                await self._handle_person(person)
            
            # Update the ID context only once after all people have been processed
            if self.student_list:  # Check if the student_list is not empty
                student_records = []
                for student in self.student_list:
                    student_record = f"""\
                        First Name: {student.first_name}
                        Middle Name: {student.middle_name}
                        Last Name: {student.last_name}
                        Sex: {student.sex}
                        Date of Birth: {student.dob}
                        Email: {student.email}
                        Student ID: {student.student_id}
                        Ohio SSID: {student.ohio_ssid}\n"""
                    student_records.append(student_record)
                
                # Combining the student records into a single string with separators
                full_student_records = "\n".join(student_records)
                
                # Prepending the header to the full student records string
                self.id_context += "\nStudent Data to help answer the question:\n" + full_student_records
        
        print("##PROMPTING FOR APIS##")
        api_task_list = await self._prompt_for_apis()
        await asyncio.gather(*(self._handle_call(api_call) for api_call in api_task_list))