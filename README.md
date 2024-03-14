![teachergpt_icon](https://github.com/sxflynn/TeacherGPT/assets/2034081/629df040-8548-40e0-a7a3-0965c0cb03b8)

# TeacherGPT

A GPT chatbot for teachers that uses retrieval-augmentation  to answer questions about their students.

## Project Status
> ⚠️ This project is in active development and is not yet a minimally viable product (MVP).

## Demo video
> ⚠️ At this time, functionality is limited to only basic student information.



https://github.com/sxflynn/TeacherGPT/assets/2034081/225c88d9-ad9e-44d6-973c-a72b23a43a96


## Aim

The aim of this project is to build a technical demonstration where teachers can use AI to save time on context-driven tasks. It uses a fictional school database to simulate a chatbot interacting with real school data.

## Tech stack

* 💻 A web frontend, built in React, with a GPT-like chat interface that interacts with the LLM inference engine

* 🐍 Python-based server running FastAPI which implements retrieval augmented generation (RAG) logic, such as orchestration, agents and tool prompting. Uses GraphQL to retrieve data from Java server and the OpenAI library to connect to an LLM inference endpoint.

* ☕ Java server running Spring Data JPA that interfaces with the PostgreSQL data store. Uses `spring-boot-starter-graphql` dependency to create GraphQL resolvers and schemas.

* 🗄️🐘 PostgreSQL database that contains data for fictional students including attendance, grades, behavior, enrollment and special education.

## How to use

### Download the project
 - Git clone the repo
```
git clone https://github.com/sxflynn/TeacherGPT.git
```
 - `cd` into the repo
 ```Bash
 cd TeacherGPT
```
 - use `ls` to verify the working directory
```
ls
```
 - You should see:
 ```
 LICENSE  README.md  chatlogic   database 
 docker-compose.yml   schooldb  titanweb
 ```

### Prepare `.env` file
- Rename the `.env.example` file to `.env`.
```
mv .env.example .env
```
 - Open `.env` in a text editor
```
OPENAI_API_KEY="..."
ANYSCALE_API_KEY="..."
TOGETHERAI_API_KEY="..."
```
 - Obtain a key from one of the services above and put it in that file surrounded by quotes.
 ```
 OPENAI_API_KEY="your-secret-key-in-quotes"
 ```
  - You can change from OpenAI to TogetherAI or AnyScale, just make sure to change the configuration.
```
DEFAULT_SERVICE=TogetherAi
```
or
```
DEFAULT_SERVICE=AnyScale
```

### Use Docker
- Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)

- In your terminal `cd` into the repo and type:
```
docker compose up
```
- After waiting several minutes, go to [http://localhost:5173/gpt](http://localhost:5173/gpt) to begin using the chat interface.


## Development

### React Website
 - `cd` into `titanweb`
```
cd titanweb
```
 - Install dependencies
```
npm install
```
 - Start the web server
```
npm run dev
```
 - Go to [http://localhost:5173](http://localhost:5173) to view the school database website.

 - Go to [http://localhost:8080/graphiql](http://localhost:8080/graphiql) to test the GraphQL endpoints.

Here is an example query to test it:
```
query GetAllStudents {
  allStudents {
    studentId
    firstName
    lastName
    sex
    dob
    email
    ohioSsid
  }
}
```
You should expect this response:
```
{
  "data": {
    "allStudents": [
      {
        "studentId": "1",
        "firstName": "Monty",
        "lastName": "Anthony",
        "sex": "M",
        "dob": "2010-03-18",
        "email": "moanthony28@titanacademy.edu",
        "ohioSsid": "WW4542553"
      },
      {
        "studentId": "2",
        "firstName": "Lacey",
        "lastName": "Baldwin",
        "sex": "F",
        "dob": "2009-11-09",
        "email": "labaldwin28@titanacademy.edu",
        "ohioSsid": "QE2954355"
      },
      (etc)
```

### Python FastAPI server

- Install Python version >= 3.11
- Add your OpenAI/AnyScale/TogetherAI keys to the `.env` file
- `cd` into `chatlogic` 
```
cd chatlogic
```
- Set up a virtual environment
```
python3 -m venv .venv
```
- Activate the virtual environment (macOS/Linux)
```Bash
source .venv/bin/activate
```
- Install the dependencies
```
pip install -r requirements.txt
```
- Start the FastAPI server
```
uvicorn main:app --reload
```
 - When finished, deactivate the virtual environment
 ```
deactivate
 ```

## How to contribute

If you are passionate about helping teachers remove data barriers to their work and want to contribute to an open project, here are some ways you can help:

- If you have an idea, question or comment, please use the Discussions tab.
- If you have technical expertise in any of the areas of the proposed tech stack, please introduce yourself and how you'd be interested in helping.
- If you have K-12 teaching experience, please introduce yourself and how you'd be interested in helping.
- As the product becomes more mature, please test the product and contribute issues and pull requests.

## Sample prompts
Once the product is built, these are the kinds of prompt interactions that a teacher would be able to have.

Teacher:

> **I am teaching my 3.10 lesson on Tuesday. Help me differentiate it for students with IEPs and other services.**

TeacherGPT:

> For your 3.10 lesson on paragraph writing, it's important to tailor the assignment to meet the diverse needs of your students, especially those with IEPs and other support services. Here are some suggestions for differentiation:
>
>For Jamie, who struggles with writing fluency, consider allowing the use of a speech-to-text tool to help them articulate their ideas without the barrier of typing or handwriting.
>
> For Alex, who has difficulty organizing thoughts, provide a graphic organizer. This tool can help them structure their paragraph with a clear beginning, middle, and end.
>
> For Taylor, who may need more time to process and write, extend the assignment deadline and break down the task into smaller, manageable steps with individual mini-deadlines.
>
> For Jordan, who excels in creative thinking but struggles with grammar, focus less on penalizing grammatical errors and more on the content and organization of ideas. You can also pair Jordan with a peer for peer-review sessions where they can get feedback on their grammar in a supportive setting.
>
> For Casey, who has an IEP focusing on reading comprehension, provide a written example of a well-structured paragraph and review it together. Highlighting each part of the paragraph (topic sentence, supporting details, conclusion) can serve as a model for their own writing.
>
> Remember, the goal is to provide the right supports so each student can successfully express their ideas through writing. Encourage peer support, use technology as an aid, and offer personalized feedback to guide each student through the writing process.

Teacher:

> **Compose a text message that I could send to Liliana's parents that summarizes her grades and behavior from the last 3 weeks. Also tell me their phone number.**

TeacherGPT:

> Emilia González Montes is the primary contact and her number is 614-504-3445
>
> Here is the text:
>
> Hi Emilia,
>
> I hope you're well! Just wanted to share a quick update on Liliana. In the last 3 weeks, she's made great strides. In Math, her test scores have improved from a B- to a solid B+, and in Science, she's consistently maintaining an A-. She has earned 3 sets of behavior dollars for excellent participation in ELA, contributing to a rise in her grade to an A, and in History, she's engaging well, securing a B+.
>
> Let me know if you have any questions or thoughts!


Teacher:

> **I am subbing for Mr. Estrada's 2nd period history class tomorrow. What sorts of behavior and academic issues might I expect from the class to help me be more prepared?**

TeacherGPT:

>Substituting for Mr. Estrada's 2nd period history class, you might encounter a mix of behaviors and academic performance levels:
>
>Behavior Dollars: According to our behavior database, Jasmyne has been earning a significant number of behavior dollars for her positive contributions and engagement in class discussions. On the other hand, Ray has accumulated a few demerits recently for being off-task and using his phone during lessons.
>
>Grade Trends: The academic database shows a range of grade trends. For example, Elena has shown steady improvement in her grades, moving from a C+ average at the start of the term to a current B+. Conversely, Carlos has experienced a slight decline, going from a B to a B- average, possibly indicating a need for additional support or motivation.
>
>Participation: Students like Sophia are noted for their consistent participation and willingness to engage in group work, making her a potential ally in fostering a collaborative classroom environment. In contrast, Alex might be more reserved, rarely volunteering information unless prompted directly.
>
>Homework Submission: The database indicates that Nathan has a perfect record of submitting homework ontime and often receives commendation for the quality of his work. On the flip side, Olivia has missed several homework deadlines, which might reflect in her overall grade and understanding of the material.
>
>Special Accommodations: Students such as Liam have flagged accommodations in the database, necessitating specific strategies like extra time for assignments or preferential seating to aid his learning experience.
>
>By preparing for these varied academic and behavioral profiles, you can tailor your approach to meet the diverse needs of Mr. Estrada's 2nd period history class. Utilizing engagement strategies like interactive discussions, group projects, and individualized support where needed will help maintain a positive and productive classroom atmosphere.

Teacher:

> **List 5 students that are close to failing my math class and for each student list 3 graded homework assignments that are eligible to be redone.**

TeacherGPT:

> Student: Jordan
>
> Homework 1: Algebraic Expressions
> * Assigned: September 10th
> * Turned In: September 15th
> * Score: 58%
>
> Homework 2: Linear Equations
> * Assigned: September 20th
> * Turned In: September 25th
> * Score: 62%
>
> Homework 3: Quadratic Functions
> * Assigned: October 1st
> * Turned In: October 6th
> * Score: 60%
>
> Student: Alex
> * Homework 1: Geometry Basics
> * Assigned: September 12th
> * Turned In: September 17th
> * Score: 55%
>
> Homework 2: Angles and Intersecting Lines
> * Assigned: September 22nd
> * Turned In: September 27th
> * Score: 58%
>
> Homework 3: Circles and Circumference
> * Assigned: October 3rd
> * Turned In: October 8th
> * Score: 62%
>
> *(etc)*


## Could this product ever be used in a school environment?
The short answer is yes, but there are caveats and considerations.

### Technical hurdles
In order to build this product, we have to combine two concepts:
 - A centralized data store which combines many different school databases into a single location.
 - A retrieval-augented generation (RAG) AI application that can generate responses based on data retrieved from a datastore.

 Both of these pieces have been done independently. For example, [Landing Zone by Converge](https://www.convergeedu.com/landing-zone) is a product that helps schools build central data stores that pull data from various school databases. In addition, there are a multitude of RAG application examples on GitHub that use Langchain, many of which are demonstrated on Youtube.

 It would be technically feasible to combine both of these concepts together to create a RAG application that can retrieve from a centralized school-based data store.

 ### Legal and privacy hurdles
 Is it legal for sensitive student data to be ingested into an AI chatbot, given laws like FERPA? This is not legal advice, but the answer is yes, based on all the Edtech tools that already exist. There is an entire industry of Edtech products that ingest and generate sensitive student data such as grades, IEPs, behavior reports, and more. The key is that these products are only to be used by school staff, and the students. As long as a GPT product is complying with privacy regulations like not storing or training on student data, then there should not be any legal hurdles to implementing the product.

 ### Economic hurdles
 AI RAG applications are very expensive to develop and operate, which is likely one of the largest barriers to its wider adoption. There are three drivers of cost:

#### Cloud computing costs:
LLM inference engines are already quite expensive. A single chat prompt and response could cost over $1 each. If teachers spread the word to each other of the utility of this product, you could easily see costs ballooning. Schools tend to prefer flat annual pricing for Edtech products, but paying per use would be a harder sell.
#### Developer costs:
Even if an Edtech consulting firm could adopt an open source tool like this that provides, it takes a lot of developer time and skill to examine all the school databases and APIs and combine them into a single cohesive database that the AI can use.
#### School staff costs:
Some school data is neatly packaged in obvious databases, like a School Information System which would have student contact information and grades. Other school data might be more haphazard. If a centralized behavior tracking system like [PowerSchool Behavior Support](https://www.powerschool.com/classroom/behavior-support/) isn't being adopted by the school, then you might have teachers creating their own unique data solutions, like a personal Google Sheets to collect behavior data, or a notebook. A school might require teachers to start using a centralized system to do this work in order to enable the use of AI, and having to adjust their workflows would create a burden on teachers.
