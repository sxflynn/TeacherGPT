import json
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from src.config import settings, load_prompts
from src.prompt import LLMPrompt, PromptInput, extractContent


def create_graphql_client() -> Client:
    transport = AIOHTTPTransport(url=settings.graphql_url)
    gqlclient = Client(transport=transport, fetch_schema_from_transport=True)
    return gqlclient

@asynccontextmanager
async def lifespan(fastapiapp: FastAPI):
    fastapiapp.state.graphql_client = create_graphql_client()
    fastapiapp.state.prompts = load_prompts()
    yield
    # Cleanup below

app = FastAPI(lifespan=lifespan)

def get_prompt_text(section_name: str) -> str:
    prompts = app.state.prompts
    return prompts.get(section_name, {}).get('text', '')


async def get_graphql_client(request: Request) -> Client:
    return request.app.state.graphql_client

def relevancy_check(userprompt:str) -> bool:
    gateway_prompt = get_prompt_text('gateway_prompt')
    prompt_engine = LLMPrompt(
        prompt=(gateway_prompt + userprompt),
        system_prompt=get_prompt_text('global_system_prompt')
        )
    prompt_engine.send()
    return "Proceed" in extractContent(prompt_engine.response)

async def get_relevant_prompt(websocket: WebSocket) -> str:
    data = await websocket.receive_text()
    prompt_object = PromptInput.model_validate_json(data)
    if relevancy_check(prompt_object.prompt):
        return prompt_object.prompt
    await websocket.send_text("That question doesn't require retrieving student data, please try using Google or ChatGPT.")
    await websocket.close()
    return None

@app.websocket("/promptstreaming")
async def run_prompt(websocket: WebSocket):
    await websocket.accept()
    user_prompt = await get_relevant_prompt(websocket)
    if user_prompt is None:
        return
    gqlclient = websocket.app.state.graphql_client

    # orchestrator = Orchestrator()
    # collected_data = await Orchestrator.receive(user_prompt)
    # final_answer = await Orchestrator.answer(collected_data)
    # for chunk in final_answer:
    #     content = chunk.choices[0].delta.content if chunk.choices and chunk.choices[0].delta.content else ""
    #     await websocket.send_text(content)
    graphql_student_last_name_prompt = get_prompt_text('gql_student_by_last_name')
    student_last_name_engine = LLMPrompt(
        prompt=(graphql_student_last_name_prompt + user_prompt),
        system_prompt=get_prompt_text('global_system_prompt')
        )
    student_last_name_engine.send()
    try:
        gql_data = json.loads(extractContent(student_last_name_engine.response))
    except json.JSONDecodeError:
        await websocket.send_text("Invalid JSON format in the response.")
        await websocket.close()
        return
    except TypeError:
        await websocket.send_text("Unexpected data type. Expected a string or bytes-like object.")
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
    student_by_last_name_gql_result = await gqlclient.execute_async(get_by_last_name, variable_values=variables)
    graphql_student_last_name_prompt = get_prompt_text('gql_student_by_last_name_answer')    
    final_answer_engine = LLMPrompt(
        prompt=(str(student_by_last_name_gql_result) + graphql_student_last_name_prompt + user_prompt),
        system_prompt=get_prompt_text('global_system_prompt')
        )
    final_answer = final_answer_engine.send(stream=True)
    for chunk in final_answer:
        content = chunk.choices[0].delta.content if chunk.choices and chunk.choices[0].delta.content else ""
        await websocket.send_text(content)
        final_answer_engine.chunks_list.append(content)
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