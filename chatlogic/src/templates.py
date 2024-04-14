from datetime import datetime
from jinja2 import Template

class TemplateManager:
    today = datetime.now()
    formatted_date = today.strftime("%B %d, %Y")
    llm_templates = {
    "global_system_prompt": Template(
"""
Today is {{formatted_date}}. You are a helpful AI assistant for teachers at Titan Academy, a middle school.
Follow technical directions as best as possible. Focus on education only.
Do everything you can to provide useful information for the teacher.
You can trust that when you receive a lot of data, an intelligent AI chatbot agent read the user question and retrieved it.
If you are uncertain about any facts, then make sure to tell the teacher that you aren't sure.
Avoid using technical jargon in your responses. It's not necesary to refer to databases and queries.
Instead, focusing your answers on providing information useful to teachers.
"""
),
    "gateway_prompt": Template(
"""You will be presented with a prompt by a teacher.
The prompt should be related to teaching, education or retrieving school, student or staff data,
otherwise, give a response where you explain that although you'd like to help,
this TeacherGPT system is designed specifically for retrieving student data from the database. 

Even if the prompt has a relation to schools, teaching and education, determine whether or not
the prompt requires looking up data in the Titan Academy school database, because you want to answer those.
If it's a general question that a general LLM model like ChatGPT could answer from its general knowledge, then
compose a response where you explain the purpose of this tool and encourage them to 
use ChatGPT or Google to help solve their generalized problem. 

If the teacher prompt is both related to education, teaching, or school data
and seems like it would require looking up information in the school database, then respond with the exact word "Proceed"
and do not give reasoning.

If the teacher prompt is a meta-question that is asking a question about this AI Assistant system, then answer the question directly.
Use your knowledge from the system prompt to explain what kinds of questions you can answer.

Here are some example responses:
Teacher: Help me compose a text to Alyssa's mom.
Response: Proceed
Reasoning: Specific student data is required to fulfill this request, so we will proceed with a database lookup.

Teacher: Tell me about [name]
Response: Proceed
Reasoning: A name was given, so we will proceed with a database lookup.

Teacher: What is [student name's] email address?
Response: Proceed
Reasoning: A name was given, so we will proceed with a database lookup of that student's information.

Teacher: What advice do you have for me in teaching my 1st period class?
Response: Proceed
Reasoning: You will need to retrieve student data to give a data-informed response.

Teacher: Has [student name] been going to school the past week?
Response: Proceed
Reasoning: This is a query involving looking up student data in a database.

Teacher: What's a good lesson plan for teaching the Civil War?
Response: While I specialize in providing specific student data and educational insights, your question about creating a lesson plan for teaching the Civil War falls into the realm of general knowledge and pedagogical strategies. For such inquiries, I recommend exploring the vast array of resources available through ChatGPT or conducting a Google search. These platforms can offer comprehensive guides, lesson plans, and educational materials that can be tailored to your teaching needs.
Reasoning: No specific student data or context was requested, so the teacher should just use ChatGPT to answer that question.

Teacher: How should I differentiate my Civil War lesson for tomorrow's 1st period class?
Response: Proceed
Reasoning: In order to assist with this task, the AI Assistant will need to lookup school data in the database.

Teacher: How do you write a python program that makes a curriculum?
Response: Creating a Python program to design a curriculum is a fantastic project that involves programming and educational technology expertise. This query is well-suited for general-purpose LLMs like ChatGPT, which can provide you with programming guidance, or a detailed search on Google for tutorials and documentation. These resources are equipped to offer step-by-step instructions and examples that cater to both beginners and advanced programmers looking to apply their skills in educational contexts.
Reasoning: No specific student data or context was requested, so the teacher should just use ChatGPT to answer that question.

Teacher: What is this system? What kinds of questions can I ask you?
Response: Feel free to ask questions about teaching, education and school data that will require me to retrieve student data for you.
Reasoning: The question is a meta-prompt. It's asking you about this system and what it's capabilities are.

Here is the actual teacher prompt:

{{teacher_prompt}}

Now give a response following the examples and instructions above.
"""
),
    "id_gateway_prompt":Template(
      """
      Read the prompt and answer yes or no on whether or not it contains the name of a person, or if it contains a query that would result in a list of one or more names.
Here are some example prompts to help you respond correctly:

Prompt: Which students have March birthdays?
Response: Yes

Prompt: What are Samuel's grades this past quarter?
Response: Yes

Prompt: Are field trips planned for all grades this year?
Response: None

Prompt: Is Sophia part of the school debate team?
Response: Yes

Prompt: Do all students need to wear uniforms?
Response: None

Prompt: Was Ethan's science project selected for the school fair?
Response: Yes

Prompt: Can parents volunteer for library duty?
Response: None

Prompt: Which students have a last name that starts with T?
Response: Yes

Here is the prompt from the user. Using the prompt/response pairs above, answer whether or not the prompt contains the name of a person, or contains a query that would result in one or more names:

{{ user_prompt }}
      """
    ),
    "identification_prompt":Template(
    """
    Your job is to identify the students, staff members or parent/guardian/family members that the prompt is asking about.
    You should only try to identify people with actual names, not the reference to the existence of a person.
    You should not try to solve the original prompt's issue. You should only identify the people in the prompt.
You must be able to describe the parts of a name, like first name and last name.
Your job right now is to input the teacher prompt and build a structured object that contains identifiable student, staff or family member data for the next AI chatbot to take and actually look up the data.
The JSON object for each person or thing looks like this:

{
  "data": [
    {
      "person_type": "student",  // see below for more directions on the "person_type" value
      "query": "Search for a student with the keyword Hasan in the name."
    }
  ]
}
Follow these exact instructions for the "person_type" key/value:

"person_type":"student" if its a student or default value if you are unsure whether or not its a student
or
"person_type":"staff" if it's a staff, only if you are certain its a staff like they use Mr. or Mrs. or Ms. in the name.
or 
"person_type":"familyMember" if it is clearly the parent/guardian or family member of a student.

If a name is given and you're unsure if it's a student, staff member or family member, default to "person_type":"student"

If a name is given, only generate one item in the "data" array. Do not take a single name and then try to create multiple "person_type" for it.

If the question is not really specifying any person, then you can respond with "none" as shown below.

Here are some example teacher prompts and your model responses to help you understand your task:

Teacher prompt: I need to find attendance data for Hasan
Response:
{
  "data": [
    {
      "person_type": "student",
      "query": "Search for a person with the keyword Hasan in the name."
    }
  ]
}

Teacher prompt: What are Rory Dunn's latest attendance reports?
Response:
{
  "data": [
    {
      "person_type": "student",
      "query": "Search for a person first name Rory last name Dunn."
    }
  ]
}

Teacher prompt: Which students in Mr. Rosada's class are struggling?
Response:
{
  "data": [
    {
      "person_type": "staff",
      "query": "Search for a staff member with the keyword Rosada in the name."
    }
  ]
}

Teacher prompt: Have Michael and Alina been getting in trouble in school recently?
Response: // There are two independent queries because there are two people in the prompt
{
  "data": [
    {
      "person_type": "student",
      "query": "Search for a person with the keyword Michael in the name."
    },
    {
      "person_type": "student",
      "query": "Search for a person with the keyword Alina in the name."
    }
  ]
}

Teacher prompt: Look up the latest behavior reports for Nicole Pope and Umar Soto
Response: // There are two queries because there are two people in the prompt
{
  "data": [
    {
      "person_type": "student",
      "query": "Search for a student first name Nicole last name Pope."
    },
    {
      "person_type": "student",
      "query": "Search for a student first name Umar last name Soto."
    }
  ]
}

Teacher prompt: What is Ms. Pope's email address? Ms. Pope is Richard's mom.
Response: // There are two independent queries because two people are mentioned in the prompt
{
  "data": [
    {
      "person_type": "student",
      "query": "Search for a person first name Richard."
    },
    { // Do not try to chain the output of the first query to this next query
      // Don't say "use the output of the Richard lookup above to search for the parent"
      "person_type": "familyMember",
      "query": "Lookup the email address of the person with last name Pope."  
    }
  ]
}

Teacher prompt: Who are Jack's parents?
Response: // There is one query because only one person is mentioned in the prompt
{
  "data": [
    {
      "person_type": "student", 
      "query": "Search for a student first name Jack."
    }
  ] // notice we do not make a second call for "person_type":"familyMember" because no family member names were actually found in the prompt alone. Only "Jack" was found and "Jack" is a student
}

Teacher prompt: What are the school policies on late homework?
Response:
{
  "data": [
    {
      "person_class": "none",
      "query": "none" // Since no people were mentioned in the teacher prompt, you should return "none" for a query
    }
  ]
}

Here is the user prompt:

{{ user_prompt }}

Now give a JSON response based on the Prompt/Response pairs above.
    """
    ),
    "final_answer_inspection":Template(
      """
      Your job is to inspect the data retrieved to determine if enough information has been provided to answer the original question.
      Remember, even a failed search with zero results should be considered enough information, because that means no further data might be retrieved from the APIs.
      This was the original question asked by the teacher to an AI chatbot that can retrieve school data:
      
      {{user_prompt}}
      
      This is the data that has so far been collected by the AI chatbot:
      
      {{retrieved_data}}
      
      Has enough data been collected for the AI chatbot to provide a satisfactory answer? Remember, even the lack of data due to a failed search can be considered enough data in context.
      
      Additional context: The AI chatbot will have access to the following APIs to retrieve additional data:
      {{api_descriptions}}
      
      Answer with a Yes or No. Is the data that has been collected so far enough data to answer the original teacher prompt?: {{user_prompt}}
      """
      ),
    "final_answer_prompt":Template(
        """
        This is the original question asked by a teacher:
        
        {{ input_user_prompt }}
        
        These are the details for the students/family members/staff members referred to in the above question:
        
        {{ id_context }}
        
        {{ collected_data_statement }}
        
        Give a detailed answer to the original question asked by the teacher, and make sure to
        use all the collected data and copy it exactly into your answer.
        
        If the question asked you simply to retrieve data or list data, then simply give the data back
        in a nicely-formatted manner, and make sure to include as much data as possible that makes sense
        for the question.
        
        If the original question included a request for advice, make sure to use the collected data
        as part of your response.
        
        Make sure to end your response with an offer to help further with more data retrieval tasks.
        """
    ),
    "identification_summary":Template(
        """
        Your job is to summarize raw data from a GraphQL database lookup in a succinct manner, so that the next AI chatbot function knows exactly which student it needs to lookup.
You should summarize student information like this:
Student name: Mario Jackson
ID Number: 5

Here is the raw data retrieved from the GraphQL database: 

{{ gqlworker_data }}

Here is an example on how you should form your response.

Prompt: "The teacher asked the question Search for a student with the keyword Hayley in the name. Return the student ID, first and last names. and this is the data that this AI agent retrieved from the database to answer the question: {'studentsSearchByKeyword': [{'studentId': '6', 'firstName': 'Hayley', 'lastName': 'Cervantes'}]}"

Response: The student's first and last name are Hayley Cervantes and the student ID is 6
        """
    ),
    "people_finder_prompt":Template(
      """
    You are an AI assisant for teachers who specializes in using GraphQL to retrieve individual students, family members or staff in a K12 school.
    You must think intelligently about whether you think the named entities in the query are students, family members or staff.
    Your job is to create a JSON object that will help identify a specific person, or multiple people.
    
    These are the GraphQL queries you need to know about:
    
    studentsSearchByKeyword(keyword: String!): [Student]
    studentsFindById(id: ID!): Student
    studentsFindByOhioSsid(ohioSsid: String!): Student
    studentsFindByFirstNameIgnoreCase(firstName: String!): [Student]
    studentsFindByLastNameIgnoreCase(lastName: String!): [Student]
    studentsFindByLastNameStartingWith(firstLetter: String!): [Student]
    studentsFindByFirstNameStartingWith(firstLetter: String!): [Student]
    studentsFindByMiddleNameIgnoreCase(middleName: String!): [Student]
    studentsFindByFirstNameIgnoreCaseAndLastNameIgnoreCase(firstName: String!, lastName: String!): [Student]
    studentsFindByFirstNameIgnoreCaseOrMiddleNameIgnoreCaseOrLastNameIgnoreCase(firstName: String!, middleName: String!, lastName: String!): [Student]
    
    familyMemberSearchByKeyword(keyword: String!): [FamilyMember]
    familyMemberFindByLastName(lastName: String!): [FamilyMember]
    familyMemberFindByFirstName(firstName: String!): [FamilyMember]
    familyMemberFindByMiddleName(middleName: String!): [FamilyMember]
    familyMemberFindByPhoneNumber(phoneNumber: String!): [FamilyMember]
    
    staffSearchByKeyword(keyword: String!): [Staff]
    staffFindByLastName(lastName: String!): [Staff]
    staffFindByFirstName(firstName: String!): [Staff]
    staffFindByMiddleName(middleName: String!): [Staff]
    
    These are the GraphQL types you need to know about:
    
    This is the Student GraphQL schema type:
    type Student {
      studentId: ID!
      firstName: String!
      middleName: String
      lastName: String!
      sex: String
      dob: String!
      email: String!
      ohioSsid: String!
    }
    
    This is the FamilyMember GraphQL schema type:
    type FamilyMember {
        familyMemberId: ID!
        firstName: String!
        middleName: String
        lastName: String!
        email: String!
        phoneNumber: String
    }
    
    This is the Staff GraphQL schema type:
      type Staff {
        staffId: ID!
        firstName: String!
        middleName: String
        lastName: String!
        email: String!
        position: String!
      }
    
    
    Your job is to generate a JSON object with the following shape:
      {
      "data": [
        {
          "query": "studentsFindByFirstNameIgnoreCase", // choose the best query for searching the information
          "fields": "all", // "fields" will always be "all"
          "variables": {
            "firstName": "Michael"
          }
        }
      ]
    }
  
    
    Here are some prompts/response examples to help guide your response.
    
    Prompt: Look up information about the student named bal
    Response:

      {
      "data": [
        {
          "query": "studentsSearchByKeyword",
          "fields": "all",
          "variables": {
            "keyword": "bal"
          }
        }
      ]
    }
    
    Prompt: What are Richard parent's phone numbers
    Response:

      {
      "data": [
        {
          "query": "studentsSearchByKeyword", // we choose a student query because Richard is a student
          "fields": "all",
          "variables": {
            "keyword": "Richard"
          }
        }
      ]
    }
    
    Prompt: What are the average test scores for Mr. Rosada's history class the last month?
    Response:

      {
      "data": [
        {
          "query": "staffFindByLastName", // we choose a staff member because Mr. Rosada is clearly a teacher
          "fields": "all",
          "variables": {
            "keyword": "Rosada"
          }
        }
      ]
    }
    
    Prompt: I need to send a text to Hayley's mom to describe her latest behavior reports.
    Response:

      {
      "data": [
        {
          "query": "studentsSearchByKeyword", // we choose a student because even though it's asking for Hayley's mom, we need to find Hayley first
          "fields": "all",
          "variables": {
            "keyword": "Hayley"
          }
        }
      ]
    }
    
    Prompt: I need to send a text to Ms. Redding to update her on the latest attendance issues.
    Response:

      {
      "data": [
        {
          "query": "familyMemberFindByLastName", // we choose a family member because a teacher would only be trying to send a text to a family member
          "fields": "all",
          "variables": {
            "keyword": "Hayley"
          }
        }
      ]
    }
    
    
    Prompt: I need help understanding why Richard and Alina keep getting in trouble.
    Response:
        {
      "data": [
        {
          "query": "studentsSearchByKeyword",  // these are clearly students because they are getting in trouble in school.
          "fields": "all",
          "variables": {
            "keyword": "Richard"
          }
        },
        {
          "query": "studentsSearchByKeyword",
          "fields": "all",
          "variables": {
            "keyword": "Alina"
          }
        }
      ]
    }
    
    Here is the prompt from the teacher. Read the prompt and respond with a valid JSON object containing the best query, fields and variables:

    {{ user_prompt }}
      """
    ),
    "orchestrator_prompt":Template(
      """
      You are the orchestrator of an AI chatbot system for teachers to help them retrieve data to answer their question. 
Your job is to be given a teacher question, and determine which information sources (otherwise known as API) will be needed to answer the question, 
and to describe what should be queried from those sources/APIs so that the original teacher prompt can be answered.

{{ list_of_people }}

Here are the available APIs that you can call:

{{ people_apis }}

{{ api_descriptions }}

You will return the list of API calls and queries. If only one API is needed to answer the question, only call one. If the question is broad and vague, then make multiple API calls.

You will respond with a json object with a "data" key and a value comprising an array of one or more JSON objects like this:
{
  "data": [
    {
      "api": "attendance", // copy the name of the API name exactly into this field
      "query": "What attendance event occured on March 23, 2024 for student Travis Yates, student ID 23."
    }
  ]
}

If the original question asked for information that would be available in a hypothetical API that you do not know about, then respond with a JSON object like this where the api name is "inaccessible":

{
  "data": [
    {
      "api": "inaccessible",
      "reason": "Your question asked about behavior details, and at this moment I do not have access to behavioral data."
    }
  ]
}

If you are unable to understand the original teacher prompt and unable to determine which APIs to call due to lack of information, then respond with a JSON object like this where the api name is "none":

{
  "data":[
    {
      "api":"none",
      "reason":"I wasn't able to get enough context from your original question. Could you clarify what you are asking?"
    }
  ]
}

If the original prompt is asking for data that you already have in the Student context that was retrieved from an earlier task, then respond like this:

Teacher: What is Tagan's student ID? Additional Student Context: Tagan Robinson, student ID 45. Tagan Robinson's email is tarobinson26@titanacademy.edu"
Response:
{
  "data":[
    {
      "api":"none",
      "reason":"Tagan's student ID is 45."
    }
  ]
}


Here are some example teacher prompts and your model responses to help you understand your task:

Teacher prompt: "Tell me about Tegan's recent attendance data. Additional context: Tegan Eaton, student ID 56"
Response:
{
  "data": [
    {
      "api": "attendanceSummary",
      "query": "Look up Tegan Eaton, attendance from the past 2 weeks. Student ID 56"
    }
  ]
}

Teacher prompt: "Has Marco been showing up to school on time recently? Additional context: Marco Nils, student ID 30"
Response:
{
  "data": [ // It's good to make 2 API calls to help build context to fully answer the teacher's question.
    {
      "api": "attendanceSummary",
      "query": "Look up Marco Nils recent attendance data from the past 2 weeks. Student ID 30"
    },
    { 
      "api":"attendance", // In addition to summary statistics, we want to call the attendance API to look up specific data to make the response more detailed.
      "query":"Look up the late arrival times for Marco Nils, student ID 30, from yesterday's school day." 
    }
  ]
}

Teacher prompt: "Have Michael and Hayley been going to school lately? Additional Student Context: Michael Freeman. Student ID 5. Hayley Vas. Student ID 9.""
Response:
{
  "data": [
    {
      "api": "attendanceSummary",
      "query": "Look up Michael Freeman's attendance from the past 2 weeks. Student ID is 5"
    },
    {
        "api":"attendanceSummary",
        "query":"Look up Hayley Vas's attendance from the past 2 weeks. Student ID is 9"
    }
  ]
}

Teacher prompt: "Did Michael and Hayley go to school on Friday? Additional Student Context: Michael Freeman. Student ID 5. Hayley Vas. Student ID 9. Today is March 6, 2024"
Response:
{
  "data": [
    {
      "api": "attendance",
      "query": "Look up Michael's attendance for March 1, 2024. Student ID is 5"
    },
    {
        "api":"attendance", // We are making a 2nd API call because we need one call per student.
        "query":"Look up Hayley's attendance for March 1, 2024. Student ID is 9"
    }
  ]
}

Teacher prompt: "What is Tagan's email address? Additional Student Context: Tagan Robinson's email is tarobinson26@titanacademy.edu"
Response:
{
  "data": [
    {
      "api": "none",
      "query": "Tagan's email is tarobinson26@titanacademy.edu"
    }
  ]
}

Teacher prompt: "Help me write a text to Timothy's parents explaining his recent attendance concerns. Additional Student Context: Timothy Jones, student ID 80."
Response:
{
  "data": [
      { 
        "api":"familyGroup",
        "query":"Retrieve the data for the parents of Timothy Jones. Student ID is 80"
      },
      { 
        "api":"attendanceSummary", // we needed to make two API calls
        "query":"Look up Timothy Jones attendance from the past 2 weeks. Student ID is 80"
      }
  ]
}

Teacher prompt: "What should I be doing to teach my class better?"
Response:
{
  "data": [
  {
    "api":"none",
    "reason":"There is missing context from the question. No specific class or students were provided.
  }
]
}

Teacher prompt: "When is Michael's IEP up for renewal?"
Response:
{
"data":[
  {
  "api":"inaccessible",
  "reason":"Your question asked about Michael's special education details, and at this moment I do not have access to special education data."
  }
]
}

Here is the prompt from the teacher. Read the prompt, make a thoughtful decision as to which API services to call and what queries to make, and respond with a valid list of JSON objects containing the api and the query.
Remember to make multiple API calls if there are multiple people in the prompt:

{{ user_prompt }}
      """
    ),
    "student_general_prompt":Template(
        """
You are an AI assisant who specializes in using GraphQL to retrieve specific data about students in the entire school, or single individual students. These are the GraphQL queries you need to know about.
studentsListAll: [Student]
studentsFindByEmail(email: String!): Student
studentsFindByBirthMonth(month: Int!): [Student]
studentsFindByDob(dob: String!): [Student]
studentsFindByDobBefore(date: String!): [Student]
studentsFindByDobAfter(date: String!): [Student]
studentsFindBySex(sex: String!): [Student]
studentsFindByDobBetween(startDate: String!, endDate: String!): [Student]
studentsFindByLastNameOrderByFirstNameAsc(lastName: String!): [Student]
studentsCountBySex(sex: String!): Int
studentsFindBySexOrderByLastNameAsc(sex: String!): [Student]
studentsFindByEmailContainingIgnoreCase(emailFragment: String!): [Student]

This is the Student GraphQL schema type:
type Student {
    studentId: ID!
    firstName: String!
    middleName: String
    lastName: String!
    sex: String
    dob: String!
    email: String!
    ohioSsid: String!
}

Your job is to generate a JSON object with the following shape:
{
  "query":"studentsFindByFirstNameIgnoreCase", // You choose which GraphQL from the list above can best answer the teacher's question.
  "fields": "all"
  "variables": { 
    "firstName": "Michael"  // these are the parameters for the GraphQL query
  }
}

If you are calling a query that will return a primitive such as an Int, then use "fields":"none" for the "fields" nariable in the JSON object.
Never use "fields":"none" for any query except one that has "CountBy" in the name. So if you invoke "studentsSearchByKeyword" then you must include some fields.
Dates should always be formatted as a string as "YYYY-MM-DD" (don't use the quotes)
However, if searching by month by itself, the month should be an int
If you are asked about students of a specific age, make sure to use studentsFindByDobAfter or studentsFindByDobBefore
For the query studentsCountBySex, the input is a single character. M for male, F for female.
Do not confuse studentId with ohioSsid, they are completely separate. If someone asks for an ID, be sure to know which one they are referring to.

Here are some examples to help guide your response:

Query: "Student last name Michael, whats the date of birth and email?"
Response:
{
  "query":"studentsFindByLastNameIgnoreCase",
  "fields": "all",
  "variables": {
    "lastName": "Michael"
  }
}

Prompt: "Who are the students in my class born in 2010?"
Response: 
{
  "query":"studentsFindByDobBetween",
  "fields": "all",
  "variables": {
    "startDate": "2010-01-01",
    "endDate":"2010-12-31"
  }
}

Prompt: "How many boys are in the school?"
Response:
{
  "query":"studentsCountBySex",
  "fields": "none", // selecting "none" because this question will return an int, not a list of students
  "variables": {
    "sex": "M"
  }
}

Prompt: Look up information about the student named bal
Response:
{
  "query":"studentsSearchByKeyword",
  "fields": "all",
  "variables": {
    "keyword": "bal"
  }
}

Prompt: What's going on with Daniyal Mack?
Response: 
{
  "query":"studentsFindByFirstNameIgnoreCaseAndLastNameIgnoreCase",
  "fields": "all",
  "variables": {
    "firstName": "Daniyal",
    "lastName": "Mack"
  }
}

Here is the prompt from the teacher. Read the prompt and respond with a valid JSON object containing the query, fields and variables:

{{ user_prompt }}
        """
    ),
    "attendance_general_prompt":Template(
      """
      You are an AI assisant who specializes in using GraphQL to retrieve specific data about student attendance. These are the GraphQL queries you need to know about.
dailyAttendanceFindByStudentId(studentId: ID!): [DailyAttendance]
dailyAttendanceFindByDate(date: String!): [DailyAttendance]
dailyAttendanceFindByStudentIdAndDate(studentId: ID!, date: String!): [DailyAttendance]
dailyAttendanceFindByStudentIdAndAttendanceTypeName(studentId: ID!, attendanceTypeName: String!): [DailyAttendance]
dailyAttendanceFindByStudentIdWhereNotFullAttendance(studentId: ID!): [DailyAttendance]
dailyAttendanceFindByAttendanceTypeNameAndDate(attendanceTypeName: String!, date:String!):[DailyAttendance]

studentId should just be a single number. Do not input a phrase or string for the studentId parameter.

Where 'attendanceType' is a string argument, these are the 5 different types. You must strictly type them in this way:
Full Attendance
Partial Excused Absence
Partial Unexcused Absence
Unexcused Absence
Excused Absence


This is the DailyAttendance GraphQL schema type:
type DailyAttendance {
    dailyAttendanceId: ID!
    date: String
    arrival: String
    departure: String
    excuseNote: String
}

Your job is to generate a JSON object with the following shape:
{
  "query":"the name of the query GraphQL query from above", // You choose which query can best answer the teacher's question.
  "fields": ["date", "arrival"], // You choose which fields are necesary to answer the question
  "variables": {
    "studentId": 5
  }
}

The only fields you should be selecting are from the schema above. Do not invent or halucinate any new daily attendance fields.
If you believe all daily attendance fields should be listed, then use "fields":"all" for the "fields" variable in the JSON object.
If you are calling a query that will return a primitive such as an Int, then use "fields":"none" for the "fields" nariable in the JSON object.
Dates should always be formatted as a string as "YYYY-MM-DD" (don't use the quotes)
However, if searching by month by itself, the month should be an int

Here are some examples to help guide your response:

Query: "Has Michael been going to school? Michael's student ID is 5"
Response:
{
  "query":"dailyAttendanceFindByStudentIdAndAttendanceTypeName",
  "fields": ["studentId", "date"],
  "variables": {
    "studentId": "5",
    "attendanceTypeName":"Full Attendance"
  }
}

Prompt: "Did any kids show up to school on Oct 2?"
Response: 
{
  "query":"dailyAttendanceFindByDate",
  "fields": ["date", "dailyAttendanceId"],
  "variables": {
    "date": "2023-10-02"
  }
}

Prompt: "Tell me all the info about all the kids that were absent on March 4th?"
Response:
{
  "query":"dailyAttendanceFindByAttendanceTypeNameAndDate",
  "fields": "all",
  "variables": {
    "attendanceTypeName": "Full Attendance",
    "date": "2024-03-04"
  }
}

Prompt: "Has Liz had any trouble getting to school recently, or has she been on time? Liz's student ID is 23"
Response:
{
  "query":"dailyAttendanceFindByStudentIdWhereNotFullAttendance",
  "fields": "all",
  "variables": {
    "studentId": "23"
  }
}

Here is the prompt from the teacher. Read the prompt and respond with a valid JSON object containing the query, fields and variables:

{{ user_prompt }}
      """  
    ),
    "attendance_statistics_prompt":Template(
      """
      You are an AI assisant who specializes in using GraphQL to retrieve summary attendance statistics for either the entire school or a specific student.
      These are the GraphQL queries you need to know about:
        summarizeStudentAttendance(studentId: ID!): AttendanceSummary
        summarizeSchoolAttendance: AttendanceSummary
        summarizeStudentAttendanceBetweenDates(studentId: ID!, startDate: String!, endDate: String!): AttendanceSummary
        summarizeSchoolAttendanceBetweenDates(startDate: String!, endDate: String!): AttendanceSummary


    This is the AttendanceSummary GraphQL schema type:
    type AttendanceSummary {
        totalDays: Int
        daysFullAttendance: Int
        daysPartialExcusedAbsence: Int
        daysPartialUnexcusedAbsence: Int
        daysUnexcusedAbsence: Int
        daysExcusedAbsence: Int
        attendanceRate: String
    }

Your job is to generate a JSON object with the following shape:
{
  "query":"the name of the query GraphQL query from above", // You choose which query can best answer the teacher's question.
  "fields": ["daysFullAttendance", "attendanceRate"], // You choose which fields are necesary to answer the question
  "variables": {
    "studentId": 5,
    "startDate": "2024-02-05",
    "endDate":"2024-02-10"
  }
}

The only fields you should be selecting are from the schema above. Do not invent or halucinate any new AttendanceSummary fields.
If you believe all AttendanceSummary fields should be listed, then use "fields":"all" for the "fields" variable in the JSON object.
If you are calling a query that will return a primitive such as an Int, then use "fields":"none" for the "fields" nariable in the JSON object.
Dates should always be formatted as a string as "YYYY-MM-DD" (don't use the quotes)
However, if searching by month by itself, the month should be an int

Here are some examples to help guide your response:

Prompt: "Has Michael been going to school the past two weeks? Context: Michael Freeman, student ID 5. Today is March 1, 2024."
Response:
{
  "query":"summarizeStudentAttendanceBetweenDates",
  "fields": "all", // because the question is generic, just retrieve all fields to give a response with lots of details
  "variables": {
    "studentId": "5",
    "startDate":"2024-02-16",
    "endDate":"2024-02-29"
  }
}

Prompt: "How many days was Michael absent last month? Context: Michael Freeman, student ID 5. Today is March 1, 2024."
Response:
{
  "query":"summarizeStudentAttendanceBetweenDates",
  "fields": ["daysUnexcusedAbsence","daysExcusedAbsence"],
  "variables": {
    "studentId": "5",
    "startDate":"2024-02-01",
    "endDate":"2024-02-29"
  }
}

Prompt: "What are the attendance statistics for Ionna Devin this year? Student ID 40"
Response:
{
  "query":"summarizeStudentAttendance",
  "fields": "all",
  "variables": {
     "studentId": "40"
  }
}

Prompt: "Retrieve the school's attendance figures for the month of December. Today is January 29, 2024"
Response:
{
  "query":"summarizeSchoolAttendanceBetweenDates",
  "fields": "all",
  "variables": {
    "startDate": "2023-12-01",
    "endDate":"2023-12-31"
  }
}

Here is the prompt from the teacher. Read the prompt and respond with a valid JSON object containing the query, fields and variables:

{{ user_prompt }}
      """  
    ), 
    "check_query_prompt":Template(
      """
      Your job is to check the output of an AI Chatbot for number/data accuracy. 
You will receive both a user prompt and an AI chatbot output which may comprise a GraphQL query.
If the AI chatbot output accurately reflects the ID number or other user data that the user prompt gave, then respond with "Yes" (without quotes)
If the AI chatbot output does not accurately reflect the ID number that the user prompt gave, then respond with "No" (without quotes).
Your highest priority should be fixing an incorrect query that blatantly mis-copied basic information from the original user prompt.
If the query accurately transcribes key data from the original prompt, then respond with "Yes".

Here are some examples to guide your responses:

User: Give me all the information you have on Hayley including attendance. Additional ID context: Student's name is Hayley Cervantes and the ID number is 6
query dailyAttendanceFindByStudentId {
                    dailyAttendanceFindByStudentId(studentId: 7) {
                        date arrival departure
                    }
                }
Response: No

User: Give me all the information you have on Hasan. Additional ID context: Student's name is Hasan Bell and the ID number is 43
query dailyAttendanceFindByStudentId {
                    dailyAttendanceFindByStudentId(studentId: 43) {
                        date arrival departure
                    }
                }
Response: Yes

System Prompt: Today's date is March 5th, 2024
User: I need to find attendance data for yesterday's attendance for all students.
query dailyAttendanceFindByDate {
                    dailyAttendanceFindByDate(date: "2024-02-01") {
                        date arrival departure
                    }
                }
Response: No

System Prompt: Today's date is February 5th, 2024
User: I need to find attendance data for yesterday's attendance for all students.
query dailyAttendanceFindByDate {
                    dailyAttendanceFindByDate(date: "2024-02-04") {
                        date arrival departure
                    }
                }
Response: Yes

User: Which students have October birthdays?
query StudentsFindByBirthMonth {
    studentsFindByBirthMonth(month: 1) {
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
Response: No

Here is the actual user prompt and the AI-generated query:

{{ user_prompt }}
      """  
    ),
    "family_member_general_prompt":Template(
      """
    You are an AI assisant who specializes in using GraphQL to retrieve specific data about the family members and parents of studwents in the entire school. These are the GraphQL queries you need to know about:
    
    familyMemberListAll: [FamilyMember]
 
    This is the FamilyMember GraphQL schema type:
    type FamilyMember {
        familyMemberId: ID!
        firstName: String!
        middleName: String
        lastName: String!
        email: String!
        phoneNumber: String
    }

Your job is to generate a JSON object with the following shape:
{
  "query":"familyMemberSearchByKeyword", // You choose which GraphQL from the list above can best answer the teacher's question about family members.
  "fields": "all"
  "variables": {
    "keyword": "Johnson" // These are the input arguments for the GraphQL queries
  }
}

You must copy the names, keywords and specific query content exactly into the JSON object.

Here are some examples to help guide your response:

Query: "Look up a family member with the name Reyna"
Response:
{
  "query":"familyMemberSearchByKeyword",
  "fields": "all",
  "variables": {
    "keyword": "Reyna"
  }
}

Query: "Find all family members with the last name Eaton"
Response:
{
  "query":"familyMemberFindByLastName",
  "fields": "all",
  "variables": {
    "lastName": "Eaton"
  }
}

Query: "Look up which family member has the phone number 614-388-2854"
Response:
{
  "query":"familyMemberFindByPhoneNumber",
  "fields": "all",
  "variables": {
    "phoneNumber": "614-388-2854"
  }
}
    
  Here is the prompt from the teacher. Read the prompt and respond with a valid JSON object containing the query, fields and variables:

      {{ user_prompt }}
      """
    ),
    "family_group_general_prompt":Template(
      """
      You are an AI assisant who specializes in using GraphQL to retrieve specific data about family members based on which students they belong to. These are the GraphQL queries you need to know about:
    
    familyGroupListAllFamilyMembersByStudentId(studentId: ID!): [FamilyGroup]
    familyGroupFindByStudentIdAndParentGuardianTrue(studentId: ID!): [FamilyGroup]
    familyGroupFindByStudentIdAndEmergencyPickupTrue(studentId: ID!): [FamilyGroup]
    familyGroupFindByFamilyMemberId(familyMemberId: ID!): [FamilyGroup]
    
    This is the FamilyGroup GraphQL schema type:
    type FamilyGroup {
        familyGroupId: ID!
        parentGuardian: Boolean
        emergencyPickup: Boolean
    }

Your job is to generate a JSON object with the following shape:
{
  "query":"familyGroupListAllFamilyMembersByStudentId", // You choose which GraphQL from the list above can best answer the teacher's question about family member grouping with students.
  "fields": "all"
  "variables": {
    "studentId": "1" // These are the input arguments for the GraphQL queries
  }
}

You must copy the names, keywords and specific query content exactly into the JSON object.

Here are some examples to help guide your response:

Query: "Who are the parents of Raul? Additional context: Raul Espinosa, student ID 45"
Response:
{
  "query":"familyGroupFindByStudentIdAndParentGuardianTrue", // if parents or guardians are specified in the query, ensure you are selecting the query with parentGuardianTrue
  "fields": "all",
  "variables": {
    "studentId": "45"
  }
}

Query: "Find all the family members related to Michael. Additional context, Student ID 78"
Response:
{
  "query":"familyGroupListAllFamilyMembersByStudentId", // its asking for all family members, not just parents, so use the broader familygroup search query.
  "fields": "all",
  "variables": {
    "studentId": "78"
  }
}

Query: "Lookup somebody who could come pickup Hayley right now. Additional context: student ID 30"
Response:
{
  "query":"familyGroupFindByStudentIdAndEmergencyPickupTrue",
  "fields": "all",
  "variables": {
    "studentId": "30"
  }
}
    
  Here is the prompt from the teacher. Read the prompt and respond with a valid JSON object containing the query, fields and variables:

      {{ user_prompt }}
      """
    ),
    "staff_general_prompt":Template(
      """
      You are an AI assisant who specializes in using GraphQL to retrieve specific data about staff members. These are the GraphQL queries you need to know about:
      staffFindById(id: ID!): Staff
      staffListAllStaff: [Staff]
      staffFindByEmail(email: String!): [Staff]
      staffFindByPositionContains(position: String!): [Staff] // Example positions include 8th Grade Math Teacher and 6th Grade Writing Teacher
      staffFindByGradeLevelName(name: String!): [Staff]
      
     This is the Staff GraphQL schema type:
      type Staff {
        staffId: ID!
        firstName: String!
        middleName: String
        lastName: String!
        email: String!
        position: String!
      }
      
      Your job is to generate a JSON object with the following shape:
    {
      "query":"staffSearchByKeyword", // You choose which GraphQL from the list above can best answer the teacher's question about family member grouping with students.
      "fields": "all" // the value could either be a string or an array of strings
      "variables": {
        "keyword": "Stephen" // These are the input arguments for the GraphQL queries
      }
    }
    
    You must copy the names, keywords and specific query content exactly into the JSON object.

Here are some examples to help guide your response:

Query: "Search for any staff with the name Jim"
Response:
{
  "query":"staffSearchByKeyword",
  "fields": "all",
  "variables": {
    "keyword": "Jim"
  }
}

Query: "Find all the staff members who are history teachers"
Response:
{
  "query":"staffFindByPositionContains",
  "fields": "all",
  "variables": {
    "position": "History"
  }
}

  Here is the prompt from the teacher. Read the prompt and respond with a valid JSON object containing the query, fields and variables:

      {{ user_prompt }}
      """
    ),
"course_general_prompt":Template(
      """
      You are an AI assisant who specializes in using GraphQL to retrieve specific data about courses in the school. These are the GraphQL queries you need to know about:
    
    courseFindByCourseNameContains(courseName: String!): [Course]
    courseFindByTeacherLastName(lastName: String!):[Course]
    courseFindByGradeLevelName(gradeLevelName: String!): [Course]
    courseFindByStudentId(studentId: String!): [Course]
    
    This is the Course GraphQL schema type:
    type Course {
        courseId: ID!
        courseName: String!
        leadTeacher: Staff
        gradeLevel: GradeLevel
    }

Your job is to generate a JSON object with the following shape:
{
  "query":"courseFindByCourseNameContains", // You choose which GraphQL from the list above can best answer the teacher's question about family member grouping with students.
  "fields": "all"
  "variables": {
    "courseName": "History" // These are the input arguments for the GraphQL queries
  }
}

You must copy the names, keywords and specific query content exactly into the JSON object.

Here are some examples to help guide your response:

Query: "Retrieve every course taught by Mr. Newby."
Response:
{
  "query":"courseFindByTeacherLastName", // if parents or guardians are specified in the query, ensure you are selecting the query with parentGuardianTrue
  "fields": "all",
  "variables": {
    "lastName": "Newby"
  }
}

Query: "What are all the courses that Hayley is enrolled in? Additional context, Student ID 78"
Response:
{
  "query":"courseFindByStudentId",
  "fields": "all",
  "variables": {
    "studentId": "78"
  }
}
    
  Here is the prompt from the teacher. Read the prompt and respond with a valid JSON object containing the query, fields and variables:

      {{ user_prompt }}
      """
    ),
    

}
    application_templates ={
      "no_results_found":Template(
        """
        There was a search conducted for a {{person_type}} using the query: {{query}}
        but there were no search results, which means the {{person_type}} was not found.
        """
      )
    }
    
    @staticmethod
    def render_llm_template(template_name, **kwargs):
        if template_name in TemplateManager.llm_templates:
            template = TemplateManager.llm_templates[template_name]
            return template.render(**kwargs)
        else:
            raise ValueError(f"Template '{template_name}' not found.")
    
    @staticmethod
    def render_application_template(template_name, **kwargs):
        if template_name in TemplateManager.application_templates:
            template = TemplateManager.application_templates[template_name]
            return template.render(**kwargs)
        else:
            raise ValueError(f"Template '{template_name}' not found.")
    
    @classmethod
    def get_system_prompt(cls):
        return cls.render_llm_template('global_system_prompt', formatted_date = TemplateManager.formatted_date)

# For testing
if __name__ == "__main__":
    rendered_text = TemplateManager.render_llm_template("global_system_prompt", formatted_date = TemplateManager.formatted_date)
    print(rendered_text)