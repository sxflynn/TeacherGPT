import os
from dotenv import load_dotenv
from src.config import Config, Client, Template
from src.prompt import Prompt

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

config = Config("TogetherAi")
client = Client(config)

# print(prompt(client, "What model are you?", global_system))

global_system_prompt = """You are a helpful AI assistant for teachers at Titan Academy, a middle school.
Focus on education only. Do everything you can to provide useful information for the teacher.
If you are uncertain about any facts, then make sure to tell the teacher that you aren't sure.
"""

teacher_prompt = "What is Monty's last name?"


# Related to education, teaching, or specific student data
gateway_prompt = Template.get_prompt_text('gateway_prompt')
print(gateway_prompt)

prompt_engine = Prompt(client,(gateway_prompt+teacher_prompt),global_system_prompt,verbose=True)
gateway_answer = prompt_engine.send()

prompt_engine.prompt="How's it going?"
prompt_engine.send()

if gateway_answer.__contains__("Proceed"):
    print("Let's keep going!")
else:
    print("Just use ChatGPT")
    exit()

print("the next step!")


