import os
from dotenv import load_dotenv
from src.config import Config, Client
from src.prompt import Prompt

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

config = Config("OpenAI")
client = Client(config)

# print(prompt(client, "What model are you?", global_system))

global_system_prompt = """You are a helpful AI assistant for teachers at Titan Academy, a middle school.
Focus on education only. Do everything you can to provide useful information for the teacher.
If you are uncertain about any facts, then make sure to tell the teacher that you aren't sure.
"""

teacher_prompt = "How do add 4 numbers together"


# Related to education, teaching, or specific student data
gateway_prompt = """
You will be presented with a prompt by a teacher. The prompt should be related to teaching, education or school data.
If the prompt has no relation to teaching, education or school data, then respond with the exact words: "ChatGPT". Even if the prompt has a relation to schools, teaching and education, determine whether or not
the prompt requires looking up data in the Titan Academy school database. If it's a general question that a general LLM model like ChatGPT
could answer from its general knowledge, then respond with the exact words "ChatGPT". If the teacher prompt is both related to education, teaching, or school data
and seems like it would require looking up information in the school database, then respond with the exact word: "Proceed"

Here are some example responses:
Teacher: Help me compose a text to Alyssa's mom.
AI Assistant: Proceed
Reasoning: Specific student data is required to fulfill this request, so we will proceed with a database lookup.

Teacher: What's a good lesson plan for teaching the Civil War?
AI Assistant: ChatGPT
Reasoning: No specific student data or context was requested, so the teacher should just use ChatGPT to answer that question.

Teacher: How should I differentiate my Civil War lesson for tomorrow's 1st period class?
AI Assistant: Proceed
Reasoning: In order to assist with this task, the AI Assistant will need to lookup school data in the database.

Here is the teacher prompt:
"""

prompt_engine = Prompt(client,(gateway_prompt+teacher_prompt),global_system_prompt,verbose=True)
prompt_engine.send()