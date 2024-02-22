import json
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from src.config import Config, LLMClient, Template
from src.prompt import Prompt

teacher_prompt_input = "What info is there about Monty?"


# GraphQL client
transport = AIOHTTPTransport(url="http://localhost:8080/graphql")
client = Client(transport=transport, fetch_schema_from_transport=True)

query = gql(
    """
    query StudentsByLastName {
    allStudents {
        studentId
        firstName
        middleName
        lastName
        sex
        dob
        email
        ohioSsid
    }
}
"""
)


def main(teacher_prompt=teacher_prompt_input):
    llmclient = LLMClient(Config("OpenAI"))
    global_system_prompt = Template.get_prompt_text('global_system_prompt')
    
    skip_gateway = True
    if not skip_gateway:
        # Related to education, teaching, or specific student data
        gateway_prompt = Template.get_prompt_text('gateway_prompt')
        prompt_engine = Prompt(llmclient, (gateway_prompt + teacher_prompt), global_system_prompt, verbose=False)
        gateway_answer = prompt_engine.send()
        if "Proceed" in gateway_answer:
            print("Let's keep going!")
        else:
            print("\033[93mJust use ChatGPT\033[0m")
            return  # Exit the function early if gateway check fails
    else:
        # Skip the gateway logic and proceed directly
        print("\033[93mGateway prompt skipped (Development Mode)\033[0m")
    
    print("Ask a question about students, using their last name. Some last names include Anthony, Baldwin and Bell. Available user fields are first, middle, last names, sex, dob, email, ohioSSID: ", end="\n")
    # last_name_prompt = input()
    last_name_prompt = "Tell me everything about student with last name Bell"
    print(last_name_prompt)

    graphql_student_last_name_prompt = Template.get_prompt_text('gql_student_by_last_name')
    student_last_name_engine = Prompt(llmclient, (graphql_student_last_name_prompt + last_name_prompt), global_system_prompt, verbose=False)
    student_last_name_json = student_last_name_engine.send()
    gql_data = json.loads(student_last_name_json)
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
    student_by_last_name_gql_result = client.execute(get_by_last_name, variable_values=variables)
    graphql_student_last_name_prompt = Template.get_prompt_text('gql_student_by_last_name_answer')
    student_last_name_engine.prompt = (str(student_by_last_name_gql_result) + graphql_student_last_name_prompt + last_name_prompt)
    final_answer = student_last_name_engine.send()
    print(final_answer)

main()