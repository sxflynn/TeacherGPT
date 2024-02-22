import os
from src.config import Config, Client, Template
from src.prompt import Prompt

teacher_prompt_input = "What info is there about Monty?"

def main(teacher_prompt=teacher_prompt_input):
    client = Client(Config("TogetherAi"))
    global_system_prompt = Template.get_prompt_text('global_system_prompt')
    
    skip_gateway = True
    if not skip_gateway:
        # Related to education, teaching, or specific student data
        gateway_prompt = Template.get_prompt_text('gateway_prompt')
        prompt_engine = Prompt(client, (gateway_prompt + teacher_prompt), global_system_prompt, verbose=True)
        gateway_answer = prompt_engine.send()
        if "Proceed" in gateway_answer:
            print("Let's keep going!")
        else:
            print("\033[93mJust use ChatGPT\033[0m")
            return  # Exit the function early if gateway check fails
    else:
        # Skip the gateway logic and proceed directly
        print("\033[93mGateway prompt skipped (Development Mode)\033[0m")


main()