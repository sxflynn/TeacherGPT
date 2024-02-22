import os
from dotenv import load_dotenv
from config import Config, Client

def get_response(response):
    return response.choices[0].message.content

def prompt(client, prompt, system_prompt):
    response = client.client.chat.completions.create(
        model=config.selected_model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content":prompt},
            ],
    )
    return response

global_system = "You are a helpful AI assistant for teachers."

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

config = Config("TogetherAi")
client = Client(config)

print(get_response(prompt(client, "What model are you?", global_system)))