import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
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

graphql_fields = """
allStudents {
        studentId
        firstName
        middleName
        lastName
        sex
        dob
        email
        ohioSsid
        dailyAttendance {
            date
            arrival
            departure
            excuseNote
        }
    }
"""

suffix = "Search for all the students stored in the graphql database that has this schema"

agent.run(suffix + graphql_fields)

# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are world class technical documentation writer."),
#     ("user", "{input}")
# ])
# output_parser = StrOutputParser()
# chain = prompt | llm  | output_parser

# print(chain.invoke({"input": "how can langsmith help with testing?"}))