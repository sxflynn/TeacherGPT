![teachergpt_icon](https://github.com/sxflynn/TeacherGPT/assets/2034081/629df040-8548-40e0-a7a3-0965c0cb03b8)

# TeacherGPT

A GPT chatbot for teachers that uses retrieval-augmentation  to answer questions about their students.

## Project Status
> ⚠️ This project ceased active development on April 21, 2024. Pull requests are still welcomed and will be given consideration.

## Demo video

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
- After waiting several minutes for the database to initialize, go to [http://localhost:5173/gpt](http://localhost:5173/gpt) to begin using the chat interface. You might have to `docker compose down` and then `docker compose up` again for it to start up correctly.

## Development
> For detailed instructions on how to develop, contribute and monitor progress on each table entity, please view [DEVELOPMENT.md](DEVELOPMENT.md)

## How to contribute

If you are passionate about helping teachers remove data barriers to their work and want to contribute to an open project, here are some ways you can help:

- If you have an idea, question or comment, please use the Discussions tab.
- If you have technical expertise in any of the areas of the proposed tech stack, please introduce yourself and how you'd be interested in helping.
- If you have K-12 teaching experience, please introduce yourself and how you'd be interested in helping.
- As the product becomes more mature, please test the product and contribute issues and pull requests.

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
