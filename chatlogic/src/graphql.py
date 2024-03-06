import logging
from typing import Dict, Optional, Union, Any
from gql import gql, Client as GQLClient
from gql.transport.exceptions import TransportQueryError
from graphql import GraphQLError
from pydantic import BaseModel, ValidationError
from src.prompt import LLMPrompt, extractContent

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

class GQLQueryModel(BaseModel):
    query: str
    fields: Union[list[str], str]
    variables: Optional[dict[str, Any]] = None

class GQLAgent:
    def __init__(self, client: GQLClient, prompts_file, task:str, user_prompt:str,system_prompt:str, task_key:str):
        self.gqlclient = client
        self.prompts_file = prompts_file
        self.task = task
        self.task_key = task_key
        self.user_prompt = user_prompt
        self.system_prompt=system_prompt
        self.all_fields_mapping = {
            "student": ["studentId", "firstName", "middleName", "lastName", "sex", "dob", "email", "ohioSsid"],
            "attendance": ["date","dailyAttendanceId","arrival","departure","excuseNote"]
            }
        self.mandatory_fields_mapping = {
            'attendance': ["attendanceType { attendanceType }"],
            }
        self.all_fields = self._get_all_fields(task_key)
    
    def _get_all_fields(self, task_key):
        if task_key not in self.all_fields_mapping:
            raise ValueError(f"Task key '{task_key}' is not defined in all_fields_mapping.")
        standard_fields = self.all_fields_mapping.get(task_key, [])
        mandatory_fields = self.mandatory_fields_mapping.get(task_key, [])
        combined_fields = list(set(standard_fields + mandatory_fields))
        return combined_fields
    
    def _fetch_fields(self, task_prompt, user_prompt) -> str:
        task_engine = LLMPrompt(
            prompt=(task_prompt + user_prompt),
            system_prompt=self.system_prompt
            )
        return extractContent(task_engine.send(json_mode=True))
    
    def _generate_final_response(self, gql_query_response: Dict[str,Any]) -> str:
        final_response = ("The teacher asked the question " 
        + str(self.user_prompt) \
        + " and this is the data that this AI agent retrieved from the database to answer the question: " \
        + str(gql_query_response))
        return final_response
    
    def _llm_check_query_logic(self, stringquery):
        check_query_engine = LLMPrompt(system_prompt=self.system_prompt,
                  prompt=self.prompts_file.get('check_query_prompt').get('text'),
                  )
        response = check_query_engine.send()
        response_return = extractContent(response)
        print(f"## IS THE GRAPHQL QUERY {stringquery} LOGICALLY SOUND?")
        print(f"## RESPONSE: {response_return}")
        return response_return
        
    async def get_data_single_prompt(self):
        max_retries = 2
        attempts = 0
        while attempts <= max_retries:
            try:
                gql_raw_query_builder = self._fetch_fields(task_prompt=self._get_task_prompt(), user_prompt=self.user_prompt)
                validated_gql_query_args = GQLQueryModel.model_validate_json(gql_raw_query_builder)                
                stringquery = self._generate_complete_gql_query(validated_gql_query_args)
                is_logical_query = self._llm_check_query_logic(stringquery)
                if is_logical_query == "No":
                    print(f"## GQL checker did not like the stringquery {stringquery}! Making it redo.")
                    self.user_prompt += "\n GraphQL query did not accurately transcribe the data from the context. Please adjust the query."
                    attempts += 1
                    continue
                
                query_phrase = gql(stringquery)
                gql_query_response = await self.gqlclient.execute_async(query_phrase)
                return self._generate_final_response(gql_query_response)
            except (GraphQLError, ValidationError, TransportQueryError) as e:
                error_message = self._handle_graphql_errors(e)
                print(f"Error needs fixing: {error_message}")
                if attempts < max_retries:
                    print(f"Attempt {attempts + 1} failed, retrying...")
                    self.user_prompt += f"\n UPDATE: There was an error generating a valid GraphQL query:  {error_message}. Regenerate the GraphQL query object with the goal of avoiding this error. Try using a different query method, arguments and/or field names."
                    attempts += 1
                else:
                    raise e from e
            except Exception as e:
                raise e
        print("Maximum retry attempts reached, unable to complete the operation.")
        
    def _handle_graphql_errors(self, e):
        if isinstance(e, GraphQLError):
            error_message = e.message
        elif isinstance(e, ValidationError):
            error_messages = [err["msg"] for err in e.errors()]
            error_message = "; ".join(error_messages)
        elif isinstance(e, TransportQueryError):
            if e.errors and isinstance(e.errors[0], dict):
                error_message = e.errors[0].get('message', 'An error occurred')
            else:
                error_message = "An error occurred in TransportQueryError without detailed messages."
        else:
            error_message = str(e)
        return error_message
    
    def _generate_complete_gql_query(self, gql_data: GQLQueryModel) -> str:
        if self.task_key in self.mandatory_fields_mapping:
            mandatory_fields = self.mandatory_fields_mapping[self.task_key]
            for field in mandatory_fields:
                if field not in gql_data.fields:
                    gql_data.fields.append(field)
        int_fields = ["count", "average", "sum"]
        if not any(keyword in gql_data.query.lower() for keyword in int_fields) and gql_data.fields == 'none':
            gql_data.fields = self.all_fields
        fields_query_part = '' if gql_data.fields == 'none' else \
                            ' '.join(self.all_fields) if gql_data.fields == 'all' else \
                            ' '.join(gql_data.fields)
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
        print("raw generated gql query is " + str(query))
        return query

    
    def _get_task_prompt(self):
        return self.prompts_file.get(self.task).get('text')