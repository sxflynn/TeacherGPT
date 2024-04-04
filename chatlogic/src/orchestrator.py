import json
import asyncio
from typing import List, Optional, Type
from gql import Client as GQLClient
from pydantic import BaseModel, Field, ValidationError
from src.templates import TemplateManager
from src.graphql import GQLAgent, GQLQueryModel
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
    student_id: int = Field(..., alias='studentId')
    first_name: str = Field(..., alias='firstName')
    middle_name: str = Field(..., alias='middleName')
    last_name: str = Field(..., alias='lastName')
    sex: str = Field(..., alias='sex')
    dob: str = Field(..., alias='dob')
    email: str = Field(..., alias='email')
    ohio_ssid: str = Field(..., alias='ohioSsid')

class FamilyMember(BaseModel):
    family_member_id: int = Field(..., alias='familyMemberId')
    first_name: str = Field(..., alias='firstName')
    middle_name: str = Field(..., alias='middleName')
    last_name: str = Field(..., alias='lastName')
    email: str = Field(..., alias='email')
    phone_number: str = Field(..., alias='phoneNumber')

class Staff(BaseModel):
    staff_id: int = Field(..., alias='staffId')
    first_name: str = Field(..., alias='firstName')
    middle_name: str = Field(..., alias='middleName')
    last_name: str = Field(..., alias='lastName')
    email: str = Field(..., alias='email')
    position: str = Field(..., alias='position')
   
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
        self.enough_context:bool = False
        self.api_descriptions = """
            API Name: attendance
            What information is available: Can look up attendance events for specific dates and specific students, such as knowing what exact attendance event happened on a specific day.

            API Name: attendanceSummary
            What information is available: Can look up general attendance statistics for a date range and a specific student.

            API Name: familyGroup
            What information is available: Can look up which family members are related to specific students, which family members are emergency pickups or parent/guardians of specific students and what their relationship is to the student.
            
            API Name: course
            What information is available: Can look up basic course information in the school, including searching course titles, searching courses by student ID, searching courses by teacher, and listing the students enrolled in the course.
            
            """
        self.prompt_mapping = {
            "people":"people_finder_prompt",
            "student": "student_general_prompt",
            "attendance": "attendance_general_prompt",
            "attendanceSummary":"attendance_statistics_prompt",
            "familyMember":"family_member_general_prompt",
            "familyGroup":"family_group_general_prompt",
            "staff":"staff_general_prompt",
            "course":"course_general_prompt"
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
    
    def _count_people_list(self):
        return (len(self.student_list) + len(self.family_member_list) + len(self.staff_list))

    async def _check_for_names(self) -> bool:
        response_text = await self._send_prompt('id_gateway_prompt', user_prompt = self.user_prompt)
        return response_text.lower().strip().startswith('yes')
    
    async def _check_for_satisfactory_data(self) -> bool:
        response_text = await self._send_prompt('final_answer_inspection', 
                                                user_prompt = self.user_prompt,
                                                retrieved_data = self.id_context,
                                                api_descriptions = self.api_descriptions)
        return response_text.lower().strip().startswith('yes')

    def _generate_list_of_people(self) -> str:
        if not self.student_list and not self.family_member_list and not self.staff_list:
            return "No data was found on any of the looked up people."
        list_of_people = "These are the people that you must make API calls for:\n\n"

        if not self.student_list:
            list_of_people += "No student data was found for API calls.\n"
        else:
            for student in self.student_list:
                student_info = self._print_model_record(student)
                list_of_people += student_info

        if not self.family_member_list:
            list_of_people += "No family member data available for API calls.\n"
        else:
            for family_member in self.family_member_list:
                family_member_info = self._print_model_record(family_member)
                list_of_people += family_member_info

        if not self.staff_list:
            list_of_people += "No staff data available for API calls.\n"
        else:
            for staff in self.staff_list:
                staff_info = self._print_model_record(staff)
                list_of_people += staff_info

        return list_of_people

    async def _fetch_api_decision(self) -> str:
        list_of_people = "" if not self._count_people_list() else self._generate_list_of_people()
        people_apis = "" if self._count_people_list() else """
            API Name: student
            What information is available: Primarily used to lookup basic facts about a student's name, student ID number, email, sex, date of birth. Special queries exist to find students by birth month, and to count the number of students by sex.
            What information is not available: The Student API does not have direct access to related data about grades, behavior, attendance, and other broader topics. It only has access to personal information listed above.
            Do not call on the Student API for any information that is otherwise available in other APIs.
            
            API Name: familyMember
            What information is available: Can search for a family member based on their personal details, such as looking up their name, phone number.
            Do not use to search for family members relationships with students.

            API Name: staff
            What information is available: Can search for a staff member based on a first middle or last name, their email and their position title.        
                """
        return await self._send_prompt('orchestrator_prompt',
                user_prompt=self.user_prompt, 
                api_descriptions = self.api_descriptions, 
                people_apis=people_apis, 
                list_of_people = list_of_people, 
                json_mode=True
            )

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
    
    async def _prompt_for_people(self) -> List[GQLQueryModel]:
        response_json = await self._send_prompt('people_finder_prompt', user_prompt=self.user_prompt, json_mode=True)
        try:
            response_data = json.loads(response_json)["data"]
            validated_data_list = [GQLQueryModel(**item) for item in response_data]
        except ValidationError as e:
            print("Error validating response from people_finder_prompt:", e)
            raise
        return validated_data_list
    
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

    def _generate__pydantic_object(self, data: dict, model_class: Type[BaseModel]) -> BaseModel:
        return model_class.model_validate(data)

    async def _handle_person(self, gql_query_model_of_person):
        person_type = self._categorize_query_by_prefix(gql_query_model_of_person)
        gqlworker = GQLAgent(
            self.gqlclient,
            task_key=person_type,
            task=None,
            user_prompt=self.user_prompt,
            system_prompt=self.system_prompt
            )
        gqlworker_data = await gqlworker.get_data_single_prompt(external_gql_model=gql_query_model_of_person, data_only=True)
        print("gqlworker data in _handle_person: " + str(gqlworker_data))
        first_value = next(iter(gqlworker_data.values()), None)
        if first_value is not None and not first_value:  # Checks for empty results and appends to id_context
            empty_search_result_statement = TemplateManager.render_application_template('no_results_found',person_type = person_type, query = gql_query_model_of_person.query)
            self.id_context += empty_search_result_statement
        else:
            if gqlworker_data and 'student' in person_type:
                student_data_list_raw = next(iter(gqlworker_data.values()), [])
                for student in student_data_list_raw:
                    new_student = self._generate__pydantic_object(student, Student)
                    self.student_list.append(new_student)
            if gqlworker_data and 'family' in person_type:
                family_member_data_list_raw = next(iter(gqlworker_data.values()), [])
                for family_member in family_member_data_list_raw:
                    new_family_member = self._generate__pydantic_object(family_member, FamilyMember)
                    self.family_member_list.append(new_family_member)
            if gqlworker_data and 'staff' in person_type:
                staff_data_list_raw = next(iter(gqlworker_data.values()), [])
                for staff in staff_data_list_raw:
                    new_staff = self._generate__pydantic_object(staff, Staff)
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
           
    def _print_model_record(self, model_instance: BaseModel) -> str:
        model_name = model_instance.__class__.__name__
        lines = [f"{model_name} {field.replace('_', ' ').title()}: {getattr(model_instance, field)}"
                for field in model_instance.model_fields]
        return "\n".join(lines)
        
    def _categorize_query_by_prefix(self, gql_query_model: GQLQueryModel) -> str:
        query = gql_query_model.query
        if query.startswith('student'):
            return 'student'
        elif query.startswith('staff'):
            return 'staff'
        elif query.startswith('family'):
            return 'familyMember'
        else:
            return 'unknown'  # Default case if none of the prefixes match   
    
    # def _append_model_records_to_context(self, model_list: List[BaseModel], header: str):
    #     if model_list:
    #         model_records = [self._print_model_record(model) for model in model_list]
    #         full_model_records = "\n".join(model_records)
    #         self.id_context += f"\n{header} data to help answer the question:\n" + full_model_records
            
    def _append_model_records_to_context(self, model_list: List[BaseModel], header: str):
        if model_list:
            model_records = [self._print_model_record(model) for model in model_list]
            full_model_records = "\n\n".join(model_records)
            self.id_context += f"\n{header} data to help answer the question:\n\n" + full_model_records

              
    async def run_orchestration(self):
        if settings.bypass_has_people:
            print("## BYPASS MODE: FORCING HAS_PEOPLE TO TRUE")
            self.has_people = True
        else:
            print('### CHECKING IF THIS IS A PROMPT CONTAINS NAMES')
            self.has_people = await self._check_for_names()

        if self.has_people:
            print("##PROMPT HAS PEOPLE --- PROMPTING FOR PEOPLE##")
            all_gql_models_of_people = await self._prompt_for_people() #gql query objects list
            await asyncio.gather(*(self._handle_person(gql_model_of_person) for gql_model_of_person in all_gql_models_of_people))
           
            self._append_model_records_to_context(self.student_list, "Student")
            self._append_model_records_to_context(self.family_member_list, "Family Member")
            self._append_model_records_to_context(self.staff_list, "Staff/Teacher")
        
        self.enough_context = await self._check_for_satisfactory_data()
        if self.enough_context:
            print("## ENOUGH CONTEXT FOUND, SKIPPING APIS")
            return
        print("##NOT ENOUGH CONTEXT, PROMPTING FOR APIS##")
        api_task_list = await self._prompt_for_apis()
        await asyncio.gather(*(self._handle_call(api_call) for api_call in api_task_list))