import json
import re 
import asyncio
from typing import List, Optional
from gql import gql, Client as GQLClient
from pydantic import BaseModel, ValidationError
from src.templates import TemplateManager
from src.graphql import GQLAgent
from src.prompt import LLMPrompt, extractContent
from src.config import settings

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
    
class FamilyMember(BaseModel):
    family_member_id: int
    first_name: str
    middle_name: str
    last_name: str
    email: str
    phone_number: str
    
class Staff(BaseModel):
    staff_id: int
    first_name: str
    middle_name: str
    last_name: str
    email: str
    position: str
   
class Orchestrator:
    def __init__(self, gqlclient:GQLClient, user_prompt, system_prompt):
        self.gqlclient = gqlclient
        self.user_prompt = user_prompt
        self.system_prompt = system_prompt
        self.has_people:bool = False
        self.student_list:List[Student] = []
        self.family_member_list:List[FamilyMember] = []
        self.staff_list:List[Staff] = []
        self.id_context = ""
        self.collected_data = []
        self.prompt_mapping = {
            "student": "student_general_prompt",
            "attendance": "attendance_general_prompt",
            "attendanceSummary":"attendance_statistics_prompt",
            "familyMember":"family_member_general_prompt",
            "familyGroup":"family_group_general_prompt",
            "staff":"staff_general_prompt"
        }
    async def _send_prompt(self, prompt_key: str, json_mode: bool = False, **kwargs) -> str:
        prompt_engine = LLMPrompt(
            prompt=TemplateManager.render_llm_template(template_name=prompt_key, **kwargs),
            system_prompt=self.system_prompt,
            async_client=True
        )
        if json_mode:
            response = await prompt_engine.send_async(json_mode=True)    
        else:
            response = await prompt_engine.send_async()
        return extractContent(response,json_mode=json_mode)
    
    async def _check_for_names(self) -> bool:
        response_text = await self._send_prompt('id_gateway_prompt', user_prompt = self.user_prompt)
        return response_text.lower().strip().startswith('yes')

    def _generate_list_of_people(self) -> str:
        if not self.student_list:
            return "No student data available for API calls."

        list_of_people = "These are the people that you must make API calls for:\n\n"
        for student in self.student_list:
            student_info = self._print_student_record(student)
            list_of_people += student_info
        for family_member in self.family_member_list:
            family_member_info = self._print_family_member_record(family_member)
            list_of_people += family_member_info
        for staff in self.staff_list:
            staff_info = self._print_staff_record(staff)
            list_of_people += staff_info
        return list_of_people

    async def _fetch_api_decision(self) -> str:
        list_of_people = "" if not self.has_people else self._generate_list_of_people()
        student_api_name = "" if self.has_people else """
            API Name: student
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
            prompt = TemplateManager.render_llm_template('identification_summary', gqlworker_data=gqlworker_data),
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
    
    def _generate_student_object(self, student) -> Student:
        return Student(
                student_id=student.get('studentId', ''),
                first_name=student.get('firstName', ''),
                middle_name=student.get('middleName', ''),
                last_name=student.get('lastName', ''),
                sex=student.get('sex', ''),
                dob=student.get('dob', ''),
                email=student.get('email', ''),
                ohio_ssid=student.get('ohioSsid', '') 
        )
    
    def _generate_family_member_object(self, family_member) -> FamilyMember:
        return FamilyMember(
                    family_member_id=family_member.get('familyMemberId',''),
                    first_name=family_member.get('firstName',''),
                    middle_name=family_member.get('middleName',''),
                    last_name=family_member.get('lastName',''),
                    email=family_member.get('email',''),
                    phone_number=family_member.get('phoneNumber',''),
                )
    def _generate_staff_object(self, staff) -> Staff:
        return Staff(
            staff_id=staff.get('staffId'),
            first_name=staff.get('firstName'),
            middle_name=staff.get('middleName'),
            last_name=staff.get('lastName'),
            email=staff.get('email'),
            position=staff.get('position')
        )
    
    async def _handle_person(self, person_query):
        if person_query.person_type in ["none"]:
            return
        gqlworker_data = await self._gql_retriever(task_key=person_query.person_type, query=person_query.query, data_only=True)
        print("gqlworker data in _handle_person: " + str(gqlworker_data))
        first_value = next(iter(gqlworker_data.values()), None)
        if first_value is not None and not first_value:  # Checks for empty results and appends to id_context
            empty_search_result_statement = TemplateManager.render_application_template('no_results_found',person_type = person_query.person_type, query = person_query.query)
            self.id_context += empty_search_result_statement
        else:
            if gqlworker_data and 'student' in person_query.person_type:
                student_data_list_raw = next(iter(gqlworker_data.values()), [])
                for student in student_data_list_raw:
                    new_student = self._generate_student_object(student)
                    self.student_list.append(new_student)
            if gqlworker_data and 'familyMember' in person_query.person_type:
                family_member_data_list_raw = next(iter(gqlworker_data.values()), [])
                for family_member in family_member_data_list_raw:
                    new_family_member = self._generate_family_member_object(family_member)
                    self.family_member_list.append(new_family_member)
            if gqlworker_data and 'staff' in person_query.person_type:
                staff_data_list_raw = next(iter(gqlworker_data.values()), [])
                for staff in staff_data_list_raw:
                    new_staff = self._generate_staff_object(staff)
                    self.staff_list.append(new_staff)
            
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
    
    def _print_student_record(self, student:Student) -> str:
        return f"""\
            Student First Name: {student.first_name}
            Student Middle Name: {student.middle_name}
            Student Last Name: {student.last_name}
            Sex: {student.sex}
            Date of Birth: {student.dob}
            Student Email: {student.email}
            Student ID: {student.student_id}
            Ohio SSID: {student.ohio_ssid}\n"""
    
    def _print_family_member_record(self, family_member:FamilyMember) -> str:
        return f"""\
            Family Member ID: {family_member.family_member_id}
            Family Member First Name: {family_member.first_name}
            Family Member Middle Name: {family_member.middle_name}
            Family Member Last Name: {family_member.last_name}
            Family Member Email: {family_member.email}
            Family Member Phone Number: {family_member.phone_number}\n"""
    
    def _print_staff_record(self, staff:Staff) -> str:
        return f"""\
            Staff ID: {staff.staff_id}
            Staff First Name: {staff.first_name}
            Staff Middle Name: {staff.middle_name}
            Staff Last Name: {staff.last_name}
            Staff Email: {staff.email}
            Staff Position: {staff.position}\n"""

    async def run_orchestration(self):
        if settings.bypass_has_people:
            print("## BYPASS MODE: FORCING HAS_PEOPLE TO TRUE")
            self.has_people = True
        else:
            print('### CHECKING IF THIS IS A PROMPT CONTAINS NAMES')
            self.has_people = await self._check_for_names()
        
        if self.has_people:
            print("##PROMPT HAS PEOPLE --- PROMPTING FOR PEOPLE##")
            all_people_queries = await self._prompt_for_people()
            for person_query in all_people_queries:
                print(f"## NOW CALLING {person_query.person_type} API AS PART OF ID PROCESS")
                print(f"## QUERY: {person_query.query}")
                await self._handle_person(person_query)
            
            if self.student_list:
                student_records = []
                for student in self.student_list:
                    student_record = self._print_student_record(student)
                    student_records.append(student_record)
                full_student_records = "\n".join(student_records)
                self.id_context += "\nStudent data to help answer the question:\n" + full_student_records
            
            if self.family_member_list:
                family_member_records = []
                for family_member in self.family_member_list:
                    family_member_record = self._print_family_member_record(family_member)
                    family_member_records.append(family_member_record)
                full_family_member_records = "\n".join(family_member_records)
                self.id_context += "\nFamily Member data to help answer the question:\n" + full_family_member_records
                
            if self.staff_list: 
                staff_records = []
                for staff in self.staff_list:
                    staff_record = self._print_staff_record(staff)
                    staff_records.append(staff_record)
                full_staff_records = "\n".join(staff_records)
                self.id_context += "\nStaff/Teacher data to help answer the question:\n" + full_staff_records
        
        print("##PROMPTING FOR APIS##")
        api_task_list = await self._prompt_for_apis()
        await asyncio.gather(*(self._handle_call(api_call) for api_call in api_task_list))