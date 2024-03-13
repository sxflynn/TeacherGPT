import time
from datetime import datetime
from contextlib import asynccontextmanager
import uvicorn # For debugging
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from gql import Client as GQLClient
from gql.transport.aiohttp import AIOHTTPTransport
from src.templates import TemplateManager
from src.config import settings
from src.prompt import LLMPrompt, PromptInput, extractContent
from src.orchestrator import Orchestrator
from src.graphql import ensure_graphql_server_is_healthy

def create_graphql_client() -> GQLClient:
    transport = AIOHTTPTransport(url=settings.graphql_url)
    gqlclient = GQLClient(transport=transport, fetch_schema_from_transport=True)
    return gqlclient

@asynccontextmanager
async def lifespan(fastapiapp: FastAPI):
    fastapiapp.state.graphql_client = create_graphql_client()
    await ensure_graphql_server_is_healthy(fastapiapp.state.graphql_client)
    await fastapiapp.state.graphql_client.connect_async() # reconnecting=True
    yield
    # Cleanup below
    await fastapiapp.state.graphql_client.close_async()

app = FastAPI(lifespan=lifespan)

async def relevancy_check(userprompt:str) -> str:
    prompt_engine = LLMPrompt(
        prompt=TemplateManager.render_template('gateway_prompt', teacher_prompt = userprompt),
        system_prompt=TemplateManager.get_system_prompt(),
        async_client=True
        )
    response = await prompt_engine.send_async()
    response_text = extractContent(response)
    return response_text
     
async def get_relevant_prompt(websocket: WebSocket) -> str:
    data = await websocket.receive_text()
    prompt_object = PromptInput.model_validate_json(data)
    relevancy_answer = await relevancy_check(prompt_object.prompt)
    if relevancy_answer.lower().startswith('proceed'):
        return prompt_object.prompt
    await websocket.send_text(relevancy_answer)
    await websocket.close()
    return None

async def output_final_response(websocket: WebSocket, input_user_prompt, collected_data) -> str:
    final_answer_prompt = TemplateManager.render_template('final_answer_prompt', input_user_prompt = input_user_prompt, collected_data = str(collected_data))
    final_answer_engine = LLMPrompt(
        prompt=final_answer_prompt,
        system_prompt=TemplateManager.get_system_prompt()
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
        system_prompt=TemplateManager.get_system_prompt(),
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