from collections import defaultdict
import csv
import json
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
    math_percentage: str | float
    reading_grade: str
    reading_percentage:str | float
    social_studies_grade: str
    social_studies_percentage: str | float
    writing_grade: str
    writing_percentage:str | float
    science_grade: str
    science_percentage:str | float

class IEPAndGoals(BaseModel):
    student_email: str
    iep_summary: str
    iep_goals: list[str]
    iep_accomodations: list[str]


    
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
    line_count = 0
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
        line_count += 1
    return student_score_list

def _truncate_to_one_decimal(number: float) -> float:
    return int(number * 10) / 10.0

def _to_letter_grade(score:float) -> str:
    grades = [
        (97, "A+"),
        (93, "A"),
        (90, "A-"),
        (87, "B+"),
        (83, "B"),
        (80, "B-"),
        (77, "C+"),
        (73, "C"),
        (70, "C-"),
        (67, "D+"),
        (63, "D"),
        (60, "D-"),
        (0,  "F")
    ]
    for threshold, letter in grades:
        if score >= threshold:
            return letter
    return "F"  # Default to F if no other grade is matched

def _aggregate_scores(scores: list[StudentScore]) -> defaultdict[str, dict[str, float]]:
    courses = defaultdict(lambda: {'total_points_earned': 0, 'total_possible_points': 0})
    for score in scores:
        assignment_value = score.points_earned / score.percentage_score if score.percentage_score != 0 else 0
        courses[score.course_name]['total_points_earned'] += score.points_earned
        courses[score.course_name]['total_possible_points'] += assignment_value
    return courses

def _create_and_assign_grades(email: str, courses: defaultdict[str, dict[str, float]]) -> ReportCard:
    report_card = ReportCard(
        student_email=email,
        math_grade='', math_percentage=0,
        reading_grade='', reading_percentage=0,
        social_studies_grade='', social_studies_percentage=0,
        writing_grade='', writing_percentage=0,
        science_grade='', science_percentage=0
    )
    for course, data in courses.items():
        if data['total_possible_points'] > 0:
            percentage = (data['total_points_earned'] / data['total_possible_points']) * 100
        else:
            percentage = 0
        grade = _to_letter_grade(percentage)
        formatted_percentage = f"{_truncate_to_one_decimal(percentage)}%"

        if 'math' in course.lower():
            report_card.math_grade = grade
            report_card.math_percentage = formatted_percentage
        elif 'reading' in course.lower():
            report_card.reading_grade = grade
            report_card.reading_percentage = formatted_percentage
        elif 'history' in course.lower():
            report_card.social_studies_grade = grade
            report_card.social_studies_percentage = formatted_percentage
        elif 'writing' in course.lower():
            report_card.writing_grade = grade
            report_card.writing_percentage = formatted_percentage
        elif 'science' in course.lower():
            report_card.science_grade = grade
            report_card.science_percentage = formatted_percentage
    return report_card

def calculate_grades(student_scores: list[StudentScore]) -> dict[str, ReportCard]:
    report_cards: dict[str, ReportCard] = {}
    scores_by_student = defaultdict(list)
    for score in student_scores:
        scores_by_student[score.student_email].append(score)
    for email, scores in scores_by_student.items():
        courses = _aggregate_scores(scores)
        report_card = _create_and_assign_grades(email, courses)
        report_cards[email] = report_card
    return report_cards

def get_iep_keywords(category:str) -> str:
    iep_keywords = {
    "Specific Learning Disabilities": [
        "Dyslexia", "Reading comprehension", "Math reasoning", "Writing skills", "Learning strategies"
    ],
    "Other Health Impaired": [
        "ADHD", "Chronic illnesses", "Medication management", "Attendance flexibility", "Energy management"
    ],
    "Speech And Language": [
        "Articulation", "Expressive language", "Receptive language", "Communication aids", "Speech therapy"
    ],
    "Autism": [
        "Social skills", "Behavioral interventions", "Sensory processing", "Communication strategies", "Routine stability"
    ],
    "Intellectual Disabilities": [
        "Adaptive skills", "Functional academics", "Daily living activities", "Social development", "Cognitive development"
    ],
    "Emotional Disturbance": [
        "Behavioral goals", "Emotional regulation", "Counseling services", "Social interaction", "Crisis plan"
    ],
    "Multiple Disabilities": [
        "Integrated therapies", "Assistive technology", "Individualized instruction", "Mobility training", "Health management"
    ],
    "Developmental Delay": [
        "Early intervention", "Cognitive skills", "Physical development", "Social-emotional skills", "Language skills"
    ],
    "Hearing Impairments": [
        "Hearing aids", "Sign language", "Lip reading", "Auditory training", "Communication access"
    ],
    "Traumatic Brain Injury": [
        "Cognitive rehabilitation", "Memory aids", "Physical therapy", "Neurological assessment", "Behavioral adaptations"
    ],
    "Orthopedic Impairments": [
        "Physical accessibility", "Mobility aids", "Physical therapy", "Adaptive equipment", "Motor skills"
    ],
    "Visual Impairments": [
        "Braille", "Visual aids", "Orientation and mobility", "Low vision aids", "Accessible materials"
    ],
    "Deaf Blindness": [
        "Tactile communication methods", "Braille plus", "Orientation and mobility", "Assistive technologies", "Combined sensory strategies"
    ]
}
    if category in iep_keywords:
        return ', '.join(iep_keywords[category])
    else:
        raise ValueError(f"Category '{category}' not found. Please provide a valid IEP category.")

def get_template() -> Template:
    return Template(
    """
    Your job is to write a fictional IEP for a fictional student for a simulation of a school for an AI Project.
    Do not refer to AI or fictional schools in your output. Output as if this were a real school.
    
    The fictional student you need to write an IEP for is as follows:
    Student name: {{ student.first_name }} {{ student.last_name }}
    Date of Birth: {{ student.dob }}
    Sex/Gender: {{ student.sex }}
    Grade Level: {{ student.grade_level }}
    
    The student's diagnosis and IEP category is {{ iep_category }}
    
    This is their report card:
    Math Grade: {{ report_card.math_grade }} {{report_card.math_percentage }}
    Reading Grade: {{ report_card.reading_grade }} {{ report_card.reading_percentage }}
    Social Studies Grade {{ report_card.social_studies_grade }} {{ report_card.social_studies_percentage }}
    Writing Grade: {{ report_card.writing_grade }} {{ report_card.writing_percentage }}
    Science Grade: {{ report_card.science_grade }} {{ report_card.science_percentage }}
    
    Generate a fictional/hallucinated 2 paragraph summary of the individual education program (IEP) for {{ student.first_name }} {{ student.last_name }},
    focusing on their objectives in {{ iep_keywords }}.
    Please encapsulate {{ student.first_name }}'s targeted progress in these areas, along with the specialized instruction and services they will receive to help meet their educational goals.
    Also, generate a fictional summary of the accommodations planned for their district and statewide assessments.
    Emphasize key details such as measurement methods and service frequency, while ensuring the summary remains clear and concise.
        
    Output a JSON object that will form this shape:
    {
        "iep_summary":"String type where you output the IEP summary following the instructions above",
        "iep_goals": [
            "Write the first IEP goal here",
            "Write the second IEP goal here",
            "Write the 3rd IEP goal here, etc"
        ],
        "iep_accomodations":[
            "Write the first IEP accomodation here",
            "Write the second IEP accomodation here",
            "Write the 3rd IEP accomodation here, etc"
        ]
    }
    
    You must include ALL of the elements of the JSON. You must include "iep_summary", "iep_goals" and "iep_accomodations"
    """
    )

def create_ieps_and_goals(student_email:str, response_content:dict) -> IEPAndGoals:
    return IEPAndGoals(
            student_email=student_email,
            iep_summary=json.loads(response_content)["iep_summary"],
            iep_accomodations=json.loads(response_content)["iep_accomodations"],
            iep_goals=json.loads(response_content)["iep_goals"]
        )
    
def get_llm_response(client:OpenAI, prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
        ],
        response_format= {"type": "json_object"}
    )
    return response.choices[0].message.content

def build_prompt(template:Template, student_sped:StudentSpedCategories, report_cards) -> str:
    return template.render(student=student_sped.student.student,
                iep_category = student_sped.category,
                report_card = report_cards[student_sped.student.student.email],
                iep_keywords = get_iep_keywords(student_sped.category)
                )
    
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
    report_cards = calculate_grades(student_score_list) # comment out for testing OpenAI
            
    template = get_template()
    
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    counter = 1
    for student_sped in sped_category_list:
        print(f"Processing {counter} of {len(sped_category_list)}")
        if counter > 1:
            break
        prompt = build_prompt(template,student_sped,report_cards)
        counter += 1
        response_content = get_llm_response(client, prompt)
        iep_and_goals = create_ieps_and_goals(student_email=student_sped.student.student.email, response_content=response_content)
        pprint.pprint(iep_and_goals)

if __name__ == "__main__":
    main()