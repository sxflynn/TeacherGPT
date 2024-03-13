import logging
import asyncio
from typing import Dict, Optional, Union, Any
from gql import gql, Client as GQLClient
from gql.transport.exceptions import TransportQueryError
from graphql import GraphQLError
from pydantic import BaseModel, ValidationError
from src.prompt import LLMPrompt, extractContent
from src.templates import TemplateManager

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

async def ping_graphql_server(client: GQLClient):
    ping_query = gql("""
        query Ping {
            ping
        }
    """)
    try:
        response = await client.execute_async(ping_query)
        return response.get("ping") == "Healthy"
    except Exception as e:
        print(f"Failed to ping GraphQL server: {e}")
        return False

async def ensure_graphql_server_is_healthy(client: GQLClient, max_retries: int = 5, wait_seconds: int = 5):
    for _ in range(max_retries):
        if await ping_graphql_server(client):
            return
        else:
            print(f"Waiting for {wait_seconds} seconds before retrying...")
            await asyncio.sleep(wait_seconds)
    raise Exception("Failed to confirm GraphQL server health after multiple retries.")


class GQLQueryModel(BaseModel):
    query: str
    fields: Union[list[str], str]
    variables: Optional[dict[str, Any]] = None

class GQLAgent:
    def __init__(self, client: GQLClient, task:str, user_prompt:str,system_prompt:str, task_key:str):
        self.gqlclient = client
        self.task = task
        self.task_key = task_key
        self.user_prompt = user_prompt
        self.system_prompt=system_prompt
        self.all_fields_mapping = {
            "student": ["studentId", "firstName", "middleName", "lastName", "sex", "dob", "email", "ohioSsid"],
            "attendance": ["date","dailyAttendanceId","arrival","departure","excuseNote"]
            }
        self.mandatory_fields_mapping = {
            "student": ["studentId", "firstName", "lastName"],
            "attendance": ["attendanceType { attendanceType }"],
            }
        self.all_fields = self._get_all_fields(task_key)
        self.lock = asyncio.Lock()
    
    async def execute_query(self, query):
        async with self.lock:  # Ensure only one coroutine accesses this block at a time
            return await self.gqlclient.session.execute(query)
    
    def _get_all_fields(self, task_key):
        if task_key not in self.all_fields_mapping:
            raise ValueError(f"Task key '{task_key}' is not defined in all_fields_mapping.")
        standard_fields = self.all_fields_mapping.get(task_key, [])
        mandatory_fields = self.mandatory_fields_mapping.get(task_key, [])
        combined_fields = list(set(standard_fields + mandatory_fields))
        return combined_fields
    
    async def _fetch_fields(self) -> str:
        task_engine = LLMPrompt(
            prompt=TemplateManager.render_template(template_name=self.task, user_prompt=self.user_prompt),
            system_prompt=self.system_prompt,
            async_client=True
            )
        response = await task_engine.send_async(json_mode=True)
        return extractContent(response)
    
    def _generate_final_response(self, gql_query_response: Dict[str,Any]) -> str:
        final_response = ("The teacher asked the question " 
        + str(self.user_prompt) \
        + " and this is the data that this AI agent retrieved from the database to answer the question: " \
        + str(gql_query_response))
        return final_response
    
    async def _llm_check_query_logic(self, stringquery):
        check_query_prompt = TemplateManager.render_template(template_name='check_query_prompt')
        combined_prompt = check_query_prompt + self.user_prompt + '\n' + stringquery
        check_query_engine = LLMPrompt(system_prompt=self.system_prompt,
                  prompt=combined_prompt,
                  async_client=True
                  )
        response = await check_query_engine.send_async()
        response_return = extractContent(response)
        print(f"## IS THE GRAPHQL QUERY {stringquery} LOGICALLY SOUND?")
        print(f"## RESPONSE: {response_return}")
        return response_return
        
    async def get_data_single_prompt(self,data_only=False):
        max_retries = 2
        attempts = 0
        while attempts <= max_retries:
            try:
                gql_raw_query_builder = await self._fetch_fields()
                validated_gql_query_args = GQLQueryModel.model_validate_json(gql_raw_query_builder)                
                stringquery = self._generate_complete_gql_query(validated_gql_query_args)
                
                # Performance issues with this code
                # is_logical_query = await self._llm_check_query_logic(stringquery)
                # if is_logical_query.startswith("No"):
                #     print(f"## GQL checker did not like the stringquery {stringquery}! Making it redo.")
                #     self.user_prompt += "\n GraphQL query did not accurately transcribe the data from the context. Please adjust the query."
                #     attempts += 1
                #     continue
                
                query_phrase = gql(stringquery)
                gql_query_response = await self.execute_query(query_phrase)
                if data_only:
                    return gql_query_response
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
        if gql_data.fields == 'all':
            fields_query_part = ' '.join(self.all_fields)
        else:
            if self.task_key in self.mandatory_fields_mapping:
                mandatory_fields = self.mandatory_fields_mapping[self.task_key]
                for field in mandatory_fields:
                    if field not in gql_data.fields:
                        gql_data.fields.append(field)
                        
            int_fields = ["count", "average", "sum"]
            if not any(keyword in gql_data.query.lower() for keyword in int_fields) and gql_data.fields == 'none':
                gql_data.fields = self.all_fields
            fields_query_part = '' if gql_data.fields == 'none' else ' '.join(gql_data.fields)
            
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