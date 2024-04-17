import csv
import os
import pprint
import re
from pydantic import BaseModel
from openai import OpenAI
from jinja2 import Template



class Student(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    dob: str
    sex: str
    email: str
    ohio_ssid: str
    grade_level: int

class SpedRoster(BaseModel):
    student: Student
    has_iep: bool = False
    has_504: bool = False
        
class StudentSpedCategories(BaseModel):
    student: SpedRoster
    category: str
    
class StudentScore(BaseModel):
    student_email: str
    course_name: str
    assignment_title: str
    points_earned: int
    percentage_score: float
    missing: bool

class ReportCard(BaseModel):
    student_email: str
    math_grade: str
    math_percentage: float
    reading_grade: str
    reading_percentage:float
    social_studies_grade: str
    social_studies_percentage: float
    writing_grade: str
    writing_percentage:float
    science_grade: str
    science_percentage:float
    
def parse_students_from_csv(csv_file_name) -> list[Student]:
    student_list:list[Student] = []
    with open(csv_file_name, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            new_student = Student(
                first_name=row['first_name'],
                middle_name=row['middle_name'],
                last_name=row['last_name'],
                dob=row['dob'],
                sex=row['sex'],
                email=row['email'],
                ohio_ssid=row['ohio_ssid'],
                grade_level=row['grade_level']
            )
            student_list.append(new_student)
    return student_list

def create_email_list_from_sql(file_path: str) -> list[str]:
    with open(file_path, 'r') as file:
        lines = file.readlines()
    email_list: list[str] = []
    for line in lines:
        if not line.startswith(("INSERT INTO", "BEGIN", "COMMIT")):
            match = re.search(r"\(SELECT student_id FROM student WHERE email = '(.*?)'\),", line)
            if match:
                email = match.group(1)
                try:
                    email_list.append(email)
                except ValueError as e:
                    print(f"Error processing line: {line}\n{e}")
    return email_list

def filter_students_by_email(student_list:list[Student], email_list:list[str]) -> list[Student]:
    email_set = set(email_list)
    new_student_list:list[Student] = [student for student in student_list if student.email in email_set]
    return new_student_list

def create_sped_roster_from_sql(student_list:list[Student], file_path: str) -> list[SpedRoster]:
    sped_roster_list: list[SpedRoster] = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
    for line in lines:
        if not line.startswith(("INSERT INTO", "BEGIN", "COMMIT")):
            match = re.search(r"\(SELECT student_id FROM student WHERE email = '(.*)'\), (.*),(.*)\),", line)
            if match:
                email, has_iep, has_504 = match.groups()
                matching_student:Student = next((student for student in student_list if student.email == email), None)
                try:
                    sped_roster_list.append(SpedRoster(
                        student=matching_student,
                        has_504=has_504,
                        has_iep=has_iep
                    ))
                except ValueError as e:
                    print(f"Error processing line: {line}\n{e}")
    return sped_roster_list

def create_student_sped_category_from_sql(sped_roster_list:list[SpedRoster], file_path:str) -> list[StudentSpedCategories]:
    student_sped_categories_list:list[StudentSpedCategories] = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
    for line in lines:
        if not line.startswith(("INSERT INTO", "BEGIN", "COMMIT")):
            match = re.search(r"\(SELECT student_id FROM student WHERE email = '(.*)'\), \(SELECT category_id FROM sped_categories WHERE sped_category = '(.*)'\)\),", line)
            if match:
                email, category = match.groups()
                matching_student:SpedRoster = next((student for student in sped_roster_list if student.student.email == email), None)
                try:
                    student_sped_categories_list.append(StudentSpedCategories(
                        student=matching_student,
                        category=category
                    ))
                except ValueError as e:
                    print(f"Error processing line: {line}\n{e}")
    return student_sped_categories_list

def parse_student_score_from_sql(file_path: str) -> list[StudentScore]:
    student_score_list:list[StudentScore] = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
    for line in lines:
        if not line.startswith(("INSERT INTO", "BEGIN", "COMMIT")):
            match = re.search(r"\(\(SELECT student_id FROM student WHERE email = '(.*)'\), \(SELECT assignment_id FROM assignment WHERE assignment_title = '(.*)' AND course_id = \(SELECT course_id from course WHERE course_name = '(.*)'\)\),(.*),(.*),(.*),", line)
            if match:
                email, assignment_title, course_name, points_earned, percentage_score, missing = match.groups()
                missing_bool = missing.strip() == "True"
                try:
                    student_score_list.append(StudentScore(
                        student_email=email,
                        course_name=course_name,
                        assignment_title=assignment_title,
                        points_earned=int(points_earned),
                        percentage_score=float(percentage_score),
                        missing=missing_bool
                    ))
                except ValueError as e:
                    print(f"Error processing line: {line}\n{e}")
    return student_score_list
    

def main():
    STUDENT_CSV_FILE_NAME = '../03_student/students.csv'
    SPED_ROSTER_SQL_FILE_NAME = 'sped-inserts.sql'
    STUDENT_SCORE_SQL_FILE_NAME = '../08_student_scores/student-score-insert.sql'
    student_list = parse_students_from_csv(STUDENT_CSV_FILE_NAME)
    email_list = create_email_list_from_sql(SPED_ROSTER_SQL_FILE_NAME)
    student_list_sped_filtered = filter_students_by_email(student_list,email_list)    
    sped_roster_list = create_sped_roster_from_sql(student_list_sped_filtered,SPED_ROSTER_SQL_FILE_NAME)
    sped_category_list = create_student_sped_category_from_sql(sped_roster_list,SPED_ROSTER_SQL_FILE_NAME)
    student_score_list = parse_student_score_from_sql(STUDENT_SCORE_SQL_FILE_NAME)
    pprint.pprint(student_score_list[0])
    
    test_student = sped_category_list[0]
    student = test_student.student.student
    diagnosis = test_student.category
    
    template = Template(
    """
    The student you need to write an IEP for is as follows:
    Student name: {{ first_name }} {{ last_name }}
    Date of Birth: {{ dob }}
    Sex/Gender: {{ sex }}
    Grade Level: {{ grade_level }}
    
    The student's diagnosis and IEP category is {{ iep_category }}
    
    """
    )
    
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    prompt = template.render(first_name=student.first_name, 
                    last_name = student.last_name,
                    dob = student.dob,
                    sex = student.sex,
                    grade_level = student.grade_level,
                    iep_category = diagnosis
                    )

    print(prompt)

    # response = client.chat.completions.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
    #     {"role": "system", "content": "You are a helpful assistant."},
    #     {"role": "user", "content": prompt},
    #     ]
    # )
    
    
    
    
if __name__ == "__main__":
    main()