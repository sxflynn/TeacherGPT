import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import AgentType, initialize_agent, load_tools

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

langchain_tracing_v2 = os.environ.get('LANGCHAIN_TRACING_V2')
langchain_api_key = os.environ.get('LANGCHAIN_API_KEY')

llm = ChatOpenAI(openai_api_key=os.environ.get("OPENAI_API_KEY"))

tools = load_tools(
    ["graphql"],
    graphql_endpoint="http://localhost:8080/graphql",
)

agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

suffix = "Search for the student with the last name Prince stored in the graphql database"

graphql_fields = """
studentsByLastName(lastName: $lastName) {
        studentId
        firstName
        middleName
        lastName
        sex
        dob
        email
        ohioSsid
    }
"""

agent.run(suffix + graphql_fields)