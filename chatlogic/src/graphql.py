from typing import Union
from gql import gql, Client
from pydantic import BaseModel, ValidationError
from src.prompt import LLMPrompt, extractContent

class GQLForm(BaseModel):
    fields: Union[list[str], str]
    variables: dict[str, str]

class GQLStudentAgent:
    def __init__(self, client: Client, prompts, task, user_prompt,system_prompt):
        self.client = client
        self.prompts = prompts
        self.task = task
        self.user_prompt = user_prompt
        self.system_prompt=system_prompt
    
    def get_task_prompt(self):
        return self.prompts.get(self.task).get('text')
    
    async def get_data(self):
        gql_data = self.fetch_fields(task_prompt=self.get_task_prompt(),user_prompt=self.user_prompt)
        try:
            gql_data = GQLForm.model_validate_json(gql_data)
        except ValidationError as e:
            raise ValidationError(f"The AI failed to give a JSON object with fields and variables.: {e}") from e
        variables = gql_data.variables
        all_student_fields = [
            'studentId',
            'firstName',
            'middleName',
            'lastName',
            'sex',
            'dob',
            'email',
            'ohioSsid'
        ]
        
        fields = gql_data.fields if gql_data.fields != 'all' else all_student_fields
        fields_query_part = ' '.join(fields)
        get_by_last_name = gql(f"""
            query StudentsByLastName($lastName: String!) {{
            studentsByLastName(lastName: $lastName) {{
                {fields_query_part}
            }}
        }}
        """)
        task_result = await self.client.execute_async(get_by_last_name, variable_values=variables)
        return task_result
    
    def fetch_fields(self, task_prompt, user_prompt):
        task_engine = LLMPrompt(
            prompt=(task_prompt + user_prompt),
            system_prompt=self.system_prompt
            )
        return extractContent(task_engine.send())