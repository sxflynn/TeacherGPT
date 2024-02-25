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
from src.prompt import LLMPrompt, extractContent

app = FastAPI()

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# last_name_prompt = "Tell me everything about student with last name Bell"
# print(last_name_prompt)

class PromptInput(BaseModel):
    prompt: str
    
@app.websocket("/promptstreaming")
async def run_prompt(websocket: WebSocket):
    await websocket.accept()
    data = await websocket.receive_text()
    prompt_object = PromptInput.model_validate_json(data)
    # GraphQL client
    graphql_url = os.getenv('GRAPHQL_URL')
    transport = AIOHTTPTransport(url=graphql_url)
    client = Client(transport=transport, fetch_schema_from_transport=True)
    default_service = os.getenv('DEFAULT_SERVICE', 'OpenAI')
    llmclient = LLMClient(Config(default_service))
    global_system_prompt = Template.get_prompt_text('global_system_prompt')
    
    skip_gateway = False
    if not skip_gateway:
        gateway_prompt = Template.get_prompt_text('gateway_prompt')
        prompt_engine = LLMPrompt(llmclient, (gateway_prompt + prompt_object.prompt), global_system_prompt)
        prompt_engine.send()
        if "Proceed" not in extractContent(prompt_engine.response):
            await websocket.send_text("This is a generic question. Just use Google/ChatGPT")
            await websocket.close()
            return
    else:
        await websocket.send_text("\033[93mGateway prompt skipped (Development Mode)\033[0m")
    
    graphql_student_last_name_prompt = Template.get_prompt_text('gql_student_by_last_name')
    student_last_name_engine = LLMPrompt(llmclient, (graphql_student_last_name_prompt + prompt_object.prompt), global_system_prompt)
    student_last_name_engine.send()
    try:
        gql_data = json.loads(extractContent(student_last_name_engine.response))
    except:
        await websocket.send_text("There wasn't any student data in the query")
        await websocket.close()
        return
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
    student_by_last_name_gql_result = await client.execute_async(get_by_last_name, variable_values=variables)
    graphql_student_last_name_prompt = Template.get_prompt_text('gql_student_by_last_name_answer')
    final_answer_prompt = (str(student_by_last_name_gql_result) + graphql_student_last_name_prompt + prompt_object.prompt)
    
    final_answer_engine = LLMPrompt(llmclient,final_answer_prompt,global_system_prompt)
    final_answer = final_answer_engine.send(stream=True)
    for chunk in final_answer:
        await websocket.send_text(chunk.choices[0].delta.content)
        final_answer_engine.chunks_list.append(chunk.choices[0].delta.content)
    final_answer_engine.response_text = ''.join(final_answer_engine.chunks_list)
    await websocket.close()
    return

app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)