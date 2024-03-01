import logging
from typing import Dict, Optional, Union, Any
from gql import gql, Client as GQLClient
from pydantic import BaseModel, ValidationError
from src.prompt import LLMPrompt, extractContent

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

class GQLForm(BaseModel):
    fields: Union[list[str], str]
    variables: dict[str, str]

class GQLQueryModel(BaseModel):
    query: str
    fields: Union[list[str], str]
    variables: Optional[dict[str, Any]] = None

class GQLStudentAgent:
    def __init__(self, client: GQLClient, prompts_file, task, user_prompt:str,system_prompt:str):
        self.gqlclient = client
        self.prompts_file = prompts_file
        self.task = task
        self.user_prompt = user_prompt
        self.system_prompt=system_prompt
    
    def _fetch_fields(self, task_prompt, user_prompt) -> str:
        task_engine = LLMPrompt(
            prompt=(task_prompt + user_prompt),
            system_prompt=self.system_prompt
            )
        return extractContent(task_engine.send())
    
    def _generate_final_response(self, gql_query_response: Dict[str,Any]) -> str:
        final_response = ("The teacher asked the question " 
        + str(self.user_prompt) \
        + " and this is the data that this AI agent retrieved from the database to answer the question: " \
        + str(gql_query_response))
        return final_response
    
    async def get_data_single_prompt(self):
        gql_raw_data = self._fetch_fields(task_prompt=self._get_task_prompt(),user_prompt=self.user_prompt) ## stores query json object with shape of GQLQueryModel
        try:
            validated_gql_query = GQLQueryModel.model_validate_json(gql_raw_data) #now the json is a pydantic object
            print("validated_gql_query is: " + str(validated_gql_query))
        except ValidationError as e:
            print ("gql_raw_data couldn't validate: ", str(gql_raw_data))
            raise ValidationError(f"The AI failed to give a JSON object with fields and variables.: {e}") from e
        stringquery = self._generate_raw_gql_query(validated_gql_query)
        query_phrase = gql(stringquery)
        gql_query_response = await self.gqlclient.execute_async(query_phrase)
        return self._generate_final_response(gql_query_response)
    
    def _generate_raw_gql_query(self, gql_data: GQLQueryModel) -> str:
        all_fields = ['studentId', 'firstName', 'middleName', 'lastName', 'sex', 'dob', 'email', 'ohioSsid']
        fields_query_part = '' if gql_data.fields == 'none' else \
                            ' '.join(all_fields) if gql_data.fields == 'all' else \
                            ' '.join(gql_data.fields)
        # Construct the variables part of the query if variables are provided
        if gql_data.variables:
            variables_part = ', '.join([f'{k}: "{v}"' if isinstance(v, str) else f'{k}: {v}' for k, v in gql_data.variables.items()])
            if fields_query_part:
                query = f"""query {gql_data.query} {{
                    {gql_data.query}({variables_part}) {{
                        {fields_query_part}
                    }}
                }}"""
            else:
                query = f"""query {gql_data.query} {{
                    {gql_data.query}({variables_part})
                }}"""
        else:
            # Construct the query without variables, assuming fields might still be none
            if fields_query_part:
                query = f"""query {gql_data.query} {{
                    {gql_data.query} {{
                        {fields_query_part}
                    }}
                }}"""
            else:
                query = f"""query {gql_data.query} {{
                    {gql_data.query}
                }}"""
        print ("raw generated gql query is " + str(query))
        return query
    
    def _get_task_prompt(self):
        return self.prompts_file.get(self.task).get('text')