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
    iep_accommodations: list[str]
    
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

def _parse_student_score_from_sql(file_path: str) -> list[StudentScore]:
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

def load_or_create_student_scores(file_name: str, sql_file_path: str) -> list[StudentScore]:
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            student_scores = json.load(file)
            return [StudentScore(**score) for score in student_scores]
    else:
        student_scores = _parse_student_score_from_sql(sql_file_path)
        with open(file_name, 'w') as file:
            json.dump([score.model_dump() for score in student_scores], file, indent=4)
        return student_scores

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
        "iep_accommodations":[
            "Write the first IEP accomodation here",
            "Write the second IEP accomodation here",
            "Write the 3rd IEP accomodation here, etc"
        ]
    }
    
    You must include ALL of the elements of the JSON. You must include "iep_summary", "iep_goals" and "iep_aaccommodations"
    """
    )

def create_ieps_and_goals(student_email:str, response_content:dict) -> IEPAndGoals:
    return IEPAndGoals(
            student_email=student_email,
            iep_summary=json.loads(response_content)["iep_summary"],
            iep_accommodations=json.loads(response_content)["iep_accommodations"],
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
    print(response.choices[0].message.content)
    return response.choices[0].message.content

def build_prompt(template:Template, student_sped:StudentSpedCategories, report_cards) -> str:
    return template.render(student=student_sped.student.student,
                iep_category = student_sped.category,
                report_card = report_cards[student_sped.student.student.email],
                iep_keywords = get_iep_keywords(student_sped.category)
                )
    
def generate_single_string_sql_values(list_of_strings: list[str], student_email: str) -> list[str]:
    values = []
    iep_id_insert = f"(SELECT iep_id FROM iep WHERE student_id = (SELECT student_id FROM student WHERE email = '{student_email}'))"
    for single_item in list_of_strings:
        safe_item = single_item.replace("'", "''")
        values.append(f"({iep_id_insert}, '{safe_item}')")
    return values

def generate_iep_sql_value(iep_summary: str, student_email: str) -> str:
    safe_summary = iep_summary.replace("'", "''")
    return f"((SELECT student_id FROM student WHERE email = '{student_email}'), '{safe_summary}')"

def return_mock_response() -> str:
    return """
{
    "iep_summary": "Helen Moore's Individual Education Program (IEP) focuses on enhancing her skills in dyslexia management, reading comprehension, math reasoning, writing proficiency, and learning strategies. Through personalized instruction and support, Helen aims to advance her literacy and numeracy abilities, improve her writing coherence, and develop effective study techniques, building on her strong academic foundation in various subjects.",
    "iep_goals": [
        "Helen will demonstrate improved phonological awareness and decoding skills to manage dyslexia more effectively, achieving at least 90% accuracy in phonetic exercises by the end of the semester.",
        "Helen will enhance her reading comprehension abilities by employing visualization techniques and summarization strategies, aiming to achieve a 10% increase in her reading fluency rate over the academic year.",
        "Helen will strengthen her math reasoning skills through problem-solving tasks and real-world applications, aiming to consistently solve multi-step word problems with 80% accuracy by the end of the school term.",
        "Helen will refine her writing skills, focusing on organization, coherence, and elaboration, with the goal of producing structured essays with varied sentence structures and transitions, reaching a score of 4 out of 5 on a holistic writing rubric by the next reporting period.",
        "Helen will develop effective learning strategies, including time management, note-taking, and self-regulation skills, to enhance her overall academic performance and independence in learning, as evidenced by increased task completion and self-monitoring abilities throughout the school year."
    ],
    "iep_accommodations": [
        "During district and statewide assessments, Helen will be provided with extended time accommodations, allowing her 50% additional time to complete the tests to alleviate time pressure and enable her to demonstrate her knowledge effectively.",
        "For written assignments, Helen will have access to a word processor or speech-to-text software to support her writing process and transcription, ensuring that her ideas are accurately conveyed despite potential spelling or handwriting challenges.",
        "Helen will receive preferential seating in the classroom to minimize distractions and maximize her focus during instruction and assessments, enabling her to engage more effectively with academic tasks and demonstrate her true abilities.",
        "To facilitate comprehension and retention, Helen will be allowed to use graphic organizers and visual aids during lessons and assessments, aiding her in organizing information and making connections between concepts in a structured manner.",
        "In order to support her individualized educational needs, Helen will receive frequent check-ins with a designated support staff member, who will provide additional clarification, feedback, and reinforcement of key concepts presented in class, ensuring her continued progress and understanding of the curriculum."
    ]
}
"""

def main():
    STUDENT_CSV_FILE_NAME = '../03_student/students.csv'
    SPED_ROSTER_SQL_FILE_NAME = 'sped-inserts.sql'
    IEPS_AND_GOALS_SQL_FILE_NAME = 'ieps-and-goals.sql'
    JSON_FILE_NAME = 'student_scores.json'
    STUDENT_SCORE_SQL_FILE_NAME = '../08_student_scores/student-score-insert.sql'

    student_list = parse_students_from_csv(STUDENT_CSV_FILE_NAME)
    email_list = create_email_list_from_sql(SPED_ROSTER_SQL_FILE_NAME)
    student_list_sped_filtered = filter_students_by_email(student_list, email_list)
    sped_roster_list = create_sped_roster_from_sql(student_list_sped_filtered, SPED_ROSTER_SQL_FILE_NAME)
    sped_category_list = create_student_sped_category_from_sql(sped_roster_list, SPED_ROSTER_SQL_FILE_NAME)
    student_score_list = load_or_create_student_scores(sql_file_path=STUDENT_SCORE_SQL_FILE_NAME, file_name=JSON_FILE_NAME)
    report_cards = calculate_grades(student_score_list)

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    template = get_template()

    with open(IEPS_AND_GOALS_SQL_FILE_NAME, 'w') as sql_file:
        sql_file.write('')

    counter = 1
    for student_sped in sped_category_list:
        if counter > 1: # for development
            break
        prompt = build_prompt(template, student_sped, report_cards)
        # response_content = get_llm_response(client, prompt)  # Network call
        response_content = return_mock_response()
        student_iep_and_goals = create_ieps_and_goals(student_email=student_sped.student.student.email, response_content=response_content)

        iep_value_insert = generate_iep_sql_value(student_iep_and_goals.iep_summary, student_iep_and_goals.student_email)
        iep_goals_values_inserts = generate_single_string_sql_values(student_iep_and_goals.iep_goals, student_iep_and_goals.student_email)
        iep_accommodations_values_inserts = generate_single_string_sql_values(student_iep_and_goals.iep_accommodations, student_iep_and_goals.student_email)

        # rewriting file for each loop iteration to store expensive API calls to disk
        with open(IEPS_AND_GOALS_SQL_FILE_NAME, 'a') as sql_file:
            sql_file.write('BEGIN TRANSACTION;\n')
            sql_file.write('INSERT INTO "iep" ("student_id", "iep_summary")\nVALUES\n' + iep_value_insert + ';\n\n')
            sql_file.write('INSERT INTO "iep_goals" ("iep_id", "goal")\nVALUES\n' + ',\n'.join(iep_goals_values_inserts) + ';\n\n')
            sql_file.write('INSERT INTO "iep_accommodations" ("iep_id", "accommodation")\nVALUES\n' + ',\n'.join(iep_accommodations_values_inserts) + ';\n\n')
            sql_file.write('COMMIT;\n\n')
        counter += 1

if __name__ == "__main__":
    main()
