import os
from dotenv import load_dotenv
from config import Config, Client

def get_response(response):
    return response.choices[0].message.content

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

config = Config("OpenAI")
client = Client(config)

response = client.client.chat.completions.create(
    model=config.selected_model,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What model are you?"},
        ],
)

print(get_response(response))