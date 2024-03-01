from typing import Optional, Union
from gql import gql, Client as GQLClient
from pydantic import BaseModel, ValidationError
from src.prompt import LLMPrompt, extractContent

class GQLForm(BaseModel):
    fields: Union[list[str], str]
    variables: dict[str, str]

class GQLQueryModel(BaseModel):
    query: str
    fields: Union[list[str], str]
    variables: Optional[dict[str, str]] = None


class GQLStudentAgent:
    def __init__(self, client: GQLClient, prompts_file, task, user_prompt,system_prompt):
        self.gqlclient = client
        self.prompts_file = prompts_file
        self.task = task
        self.user_prompt = user_prompt
        self.system_prompt=system_prompt
    
    def fetch_fields(self, task_prompt, user_prompt) -> str:
        task_engine = LLMPrompt(
            prompt=(task_prompt + user_prompt),
            system_prompt=self.system_prompt
            )
        return extractContent(task_engine.send())
    
    async def get_data_single_prompt(self):
        gql_raw_data = self.fetch_fields(task_prompt=self.get_task_prompt(),user_prompt=self.user_prompt) ## stores query json object with shape of GQLQueryModel
        try:
            validated_gql_query = GQLQueryModel.model_validate_json(gql_raw_data) #now the json is a pydantic object
        except ValidationError as e:
            raise ValidationError(f"The AI failed to give a JSON object with fields and variables.: {e}") from e
        stringquery = self.generate_raw_gql_query(validated_gql_query)
        query_phrase = gql(stringquery)
        gql_query_response = await self.gqlclient.execute_async(query_phrase)
        return gql_query_response
    
    
    def generate_raw_gql_query(self, gql_data: GQLQueryModel) -> str:
        # Define a list of all possible fields (adjust based on your GraphQL schema).
        all_fields = ['studentId', 'firstName', 'middleName', 'lastName', 'sex', 'dob', 'email', 'ohioSsid']
        
        # Condense the determination of fields into one line
        fields_query_part = ' '.join(all_fields if gql_data.fields == 'all' else gql_data.fields)
        
        # Construct the variables part of the query if variables are provided
        if gql_data.variables:
            variables_part = ', '.join([f'{k}: "{v}"' for k, v in gql_data.variables.items()])
            query = f"""query {gql_data.query} {{
                {gql_data.query}({variables_part}) {{
                    {fields_query_part}
                }}
            }}"""
        else:
            # Construct the query without variables
            query = f"""query {gql_data.query} {{
                {gql_data.query} {{
                    {fields_query_part}
                }}
            }}"""
        
        return query

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    async def get_data(self):
        gql_raw_data = self.fetch_fields(task_prompt=self.get_task_prompt(),user_prompt=self.user_prompt)
        try:
            gql_form_data = GQLForm.model_validate_json(gql_raw_data)
        except ValidationError as e:
            raise ValidationError(f"The AI failed to give a JSON object with fields and variables.: {e}") from e
        task_result = await self.fetch_data(gql_form_data)
        return task_result
    
    def get_task_prompt(self):
        return self.prompts_file.get(self.task).get('text')
    

    
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