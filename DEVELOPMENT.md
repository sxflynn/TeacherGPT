## React Website
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

## Python FastAPI server

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


## Domain Progress


|                    | SQL Schema | Data generator | SQL data | Entity | Repository | Service | Controller | GraphQL | Prompt Template |
|--------------------|------------|----------------|----------|--------|------------|---------|------------|---------|-----------------|
| Student            |      ✅     |        ✅       |     ✅    |    ✅   |      ✅     |    ✅    |      ✅     |    ✅    |        ✅        |
| Enrollment         |      ✅      |        ✅        |    ✅      |        |            |         |            |         |                 |
| Family Member      |      ✅     |        ✅       |     ✅    |    ✅   |      ✅     |    ✅    |      ✅     |    ✅    |        ✅        |
| Family Group       |      ✅     |        ✅       |     ✅    |    ✅   |      ✅     |    ✅    |      ✅     |    ✅    |        ✅        |
| Relationship Type  |      ✅     |                |     ✅    |    ✅   |            |         |            |         |                 |
| Daily Attendance   |      ✅     |        ✅       |     ✅    |    ✅   |      ✅     |    ✅    |      ✅     |    ✅    |        ✅        |
| Attendance Type    |      ✅     |        ✅       |     ✅    |    ✅   |      ✅     |    ✅    |      ✅     |    ✅    |        ✅        |
| Staff              |     ✅       |       ✅         |    ✅      |   ✅     |     ✅       |     ✅    |      ✅      |     ✅    |         ✅        |
| Department         |            |                |          |        |            |         |            |         |                 |
| Grade Level        |     ✅       |       ✅         |     ✅     |   ✅     |     ✅       |    ✅     |      ✅      |    ✅     |         ✅        |
| Course             |      ✅      |        ✅        |    ✅      |    ✅    |      ✅      |     ✅    |      ✅      |     ✅    |         ✅        |
| Course Rosters     |      ✅      |         ✅       |    ✅      |        |            |         |            |         |                 |
| Assignment         |     ✅       |        ✅        |    ✅      |     ✅   |      ✅      |     ✅    |      ✅      |    ✅     |                 |
| Assignment Types   |            |                |          |        |            |         |            |         |                 |
| Student Scores     |       ✅     |        ✅        |     ✅     |     ✅   |   ✅          |  ✅        |  ✅           | ✅         |                |
| SPED Roster        |       ✅     |        ✅        |      ✅    |        |            |         |            |         |                 |
| SPED Categories    |        ✅    |        ✅        |      ✅    |        |            |         |            |         |                 |
| IEP                |            |                |          |        |            |         |            |         |                 |
| IEP Goals          |            |                |          |        |            |         |            |         |                 |
| IEP Accomodations  |            |                |          |        |            |         |            |         |                 |
| ETR                |            |                |          |        |            |         |            |         |                 |
| Behavior Referrals |            |                |          |        |            |         |            |         |                 |
| Behavior Plans     |            |                |          |        |            |         |            |         |                 |
| Suspensions        |            |                |          |        |            |         |            |         |                 |
| Expulsions         |            |                |          |        |            |         |            |         |                 |
| Period List        |            |                |          |        |            |         |            |         |                 |
| Rooms              |            |                |          |        |            |         |            |         |                 |