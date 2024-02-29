from typing import Union
from gql import gql, Client as GQLClient
from pydantic import BaseModel, ValidationError
from src.prompt import LLMPrompt, extractContent

class GQLForm(BaseModel):
    fields: Union[list[str], str]
    variables: dict[str, str]

class GQLStudentAgent:
    def __init__(self, client: GQLClient, prompts, task, user_prompt,system_prompt):
        self.gqlclient = client
        self.prompts = prompts
        self.task = task
        self.user_prompt = user_prompt
        self.system_prompt=system_prompt
    
    def get_task_prompt(self):
        return self.prompts.get(self.task).get('text')
    
    async def get_data(self):
        gql_raw_data = self.fetch_fields(task_prompt=self.get_task_prompt(),user_prompt=self.user_prompt)
        try:
            gql_form_data = GQLForm.model_validate_json(gql_raw_data)
        except ValidationError as e:
            raise ValidationError(f"The AI failed to give a JSON object with fields and variables.: {e}") from e
        task_result = await self.fetch_data(gql_form_data)
        return task_result
        
    def fetch_fields(self, task_prompt, user_prompt):
        task_engine = LLMPrompt(
            prompt=(task_prompt + user_prompt),
            system_prompt=self.system_prompt
            )
        return extractContent(task_engine.send())
    
    async def fetch_data(self, gql_form_data):
        variables = gql_form_data.variables
        all_query_fields = [
            'studentId',
            'firstName',
            'middleName',
            'lastName',
            'sex',
            'dob',
            'email',
            'ohioSsid'
        ]
        fields = gql_form_data.fields if gql_form_data.fields != 'all' else all_query_fields
        fields_query_part = ' '.join(fields)
        query_phrase = gql(f"""
            query studentsFindByLastNameIgnoreCase($lastName: String!) {{
            studentsFindByLastNameIgnoreCase(lastName: $lastName) {{
                {fields_query_part}
            }}
        }}
        """)
        task_result = await self.gqlclient.execute_async(query_phrase, variable_values=variables)
        return task_result