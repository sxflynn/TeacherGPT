import time
from datetime import datetime
from contextlib import asynccontextmanager
import uvicorn # For debugging
import backoff
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from gql import Client as GQLClient
from gql.transport.aiohttp import AIOHTTPTransport
from aiohttp.client_exceptions import ClientConnectorError
from aiohttp import ClientOSError
from src.config import settings, load_prompts
from src.prompt import LLMPrompt, PromptInput, extractContent
from src.orchestrator import Orchestrator

async def connect_with_retry(client: GQLClient):
    await client.connect_async(reconnecting=True)
    
@backoff.on_exception(backoff.expo,
                      (ClientConnectorError,
                      ClientOSError),
                      max_tries=15,  # Maximum number of retries
                      max_time=30,  # Maximum time to retry for in seconds
                      jitter=backoff.full_jitter)  # Apply jitter to wait times
async def safe_connect(client: GQLClient):
    await connect_with_retry(client)

def create_graphql_client() -> GQLClient:
    transport = AIOHTTPTransport(url=settings.graphql_url)
    gqlclient = GQLClient(transport=transport, fetch_schema_from_transport=True)
    return gqlclient

@asynccontextmanager
async def lifespan(fastapiapp: FastAPI):
    fastapiapp.state.graphql_client = create_graphql_client()
    await safe_connect(fastapiapp.state.graphql_client)
    fastapiapp.state.prompts = load_prompts()
    yield
    # Cleanup below
    await fastapiapp.state.graphql_client.close_async()

app = FastAPI(lifespan=lifespan)

def get_prompt_text(section_name: str) -> str:
    prompts = app.state.prompts
    return prompts.get(section_name, {}).get('text', '')

def get_system_prompt() -> str:
    today = datetime.now()
    formatted_date = today.strftime("%B %d, %Y")
    prompts = app.state.prompts
    system_prompt = (f"Today is {formatted_date}. " + prompts.get('global_system_prompt', {}).get('text', ''))
    return system_prompt

async def relevancy_check(userprompt:str) -> bool:
    gateway_prompt = get_prompt_text('gateway_prompt')
    prompt_engine = LLMPrompt(
        prompt=(gateway_prompt + userprompt),
        system_prompt=get_system_prompt(),
        async_client=True
        )
    response = await prompt_engine.send_async()
    return "Proceed" in extractContent(response)

async def get_relevant_prompt(websocket: WebSocket) -> str:
    data = await websocket.receive_text()
    prompt_object = PromptInput.model_validate_json(data)
    if await relevancy_check(prompt_object.prompt):
        return prompt_object.prompt
    await websocket.send_text("That question doesn't require retrieving student data, please try using Google or ChatGPT.")
    await websocket.close()
    return None

async def output_final_response(websocket: WebSocket, input_user_prompt, collected_data) -> str:
    final_answer_prompt = get_prompt_text('final_answer_prompt')
    final_answer_engine = LLMPrompt(
        prompt=(str(collected_data) + final_answer_prompt + input_user_prompt),
        system_prompt=get_system_prompt()
        )
    print("## FINAL PROMPT: " + final_answer_engine.prompt)
    final_answer = final_answer_engine.send(stream=True)
    for chunk in final_answer:
        content = chunk.choices[0].delta.content if chunk.choices and chunk.choices[0].delta.content else ""
        await websocket.send_text(content)
        final_answer_engine.chunks_list.append(content)
    final_answer_engine.response_text = ''.join(final_answer_engine.chunks_list)
    await websocket.close()
    return None

@app.websocket("/promptstreaming")
async def run_prompt(websocket: WebSocket):    
    start = time.time()
    await websocket.accept()
    input_user_prompt = await get_relevant_prompt(websocket)
    if input_user_prompt is None:
        return
    gqlclient = websocket.app.state.graphql_client
    orchestrator = Orchestrator(
        gqlclient,
        user_prompt=input_user_prompt,
        system_prompt=get_system_prompt(),
        prompts_file=websocket.app.state.prompts
        )
    await orchestrator.run_orchestration()
    end = time.time()
    elapsed_time = (end - start)
    print(f"Time elapsed: {elapsed_time:.2f} seconds")
    await output_final_response(websocket,input_user_prompt, orchestrator.collected_data)
    return

app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)
# Debugging mode
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)