import json
import os
import asyncio
import openai
from dotenv import load_dotenv
from fastapi import FastAPI, Response, WebSocket
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from src.config import Config, LLMClient, Template
from src.prompt import LLMPrompt

app = FastAPI()

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# last_name_prompt = "Tell me everything about student with last name Bell"
# print(last_name_prompt)

class PromptInput(BaseModel):
    prompt: str
    
class PromptResponse(BaseModel):
    response: str

@app.post("/prompt")
def run_prompt(teacher_prompt:PromptInput) -> PromptResponse:
    # GraphQL client
    graphql_url = os.getenv('GRAPHQL_URL')
    transport = AIOHTTPTransport(url=graphql_url)
    client = Client(transport=transport, fetch_schema_from_transport=True)
    default_service = os.getenv('DEFAULT_SERVICE', 'OpenAI')
    llmclient = LLMClient(Config(default_service))
    global_system_prompt = Template.get_prompt_text('global_system_prompt')
    
    skip_gateway = False
    if not skip_gateway:
        # Related to education, teaching, or specific student data
        gateway_prompt = Template.get_prompt_text('gateway_prompt')
        prompt_engine = LLMPrompt(llmclient, (gateway_prompt + teacher_prompt.prompt), global_system_prompt)
        gateway_answer = prompt_engine.send()
        if "Proceed" not in gateway_answer:
            return PromptResponse(response="This is a generic question. Just use Google/ChatGPT")
    else:
        # Skip the gateway logic and proceed directly
        print("\033[93mGateway prompt skipped (Development Mode)\033[0m")
    
    graphql_student_last_name_prompt = Template.get_prompt_text('gql_student_by_last_name')
    student_last_name_engine = LLMPrompt(llmclient, (graphql_student_last_name_prompt + teacher_prompt.prompt), global_system_prompt)
    student_last_name_json = student_last_name_engine.send()
    try:
        gql_data = json.loads(student_last_name_json)
    except:
        return PromptResponse(response="There wasn't any student data in the query")
    variables = gql_data['variables']
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
    
    if gql_data['fields'] == 'all':
        fields = all_student_fields
    else:
        fields = gql_data['fields']
    fields_query_part = ' '.join(fields)
    get_by_last_name = gql(f"""
        query StudentsByLastName($lastName: String!) {{
        studentsByLastName(lastName: $lastName) {{
            {fields_query_part}
        }}
    }}
    """)
    student_by_last_name_gql_result = client.execute(get_by_last_name, variable_values=variables)
    graphql_student_last_name_prompt = Template.get_prompt_text('gql_student_by_last_name_answer')
    student_last_name_engine.prompt = (str(student_by_last_name_gql_result) + graphql_student_last_name_prompt + str(teacher_prompt))
    final_answer = student_last_name_engine.send()
    final_response = PromptResponse(response=final_answer)
    return final_response


@app.websocket("/promptstreaming")
async def streamprompt(websocket: WebSocket):
    await websocket.accept()
    data = await websocket.receive_text()
    prompt_object = PromptInput.model_validate_json(data)
    llmclient = LLMClient(Config("TogetherAi"))
    prompt = LLMPrompt(llmclient,prompt_object.prompt,"You are a helpful assistant.")
    response = prompt.send(stream=True)
    for chunk in response:
        content = chunk.choices[0].delta.content
        await websocket.send_text(content)  
        prompt.chunks_list.append(content)
    prompt.response_text = ''.join(prompt.chunks_list)
    await websocket.close()

app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)