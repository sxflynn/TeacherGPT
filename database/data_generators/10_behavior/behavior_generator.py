import random
from datetime import datetime, timedelta
from collections import defaultdict
import csv
import json
import os
import pprint
import re
from typing import Optional
from jinja2 import Template
from openai import OpenAI
from pydantic import BaseModel

class Student(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    dob: str
    sex: str
    email: str
    ohio_ssid: str
    grade_level: int
    sped_category: str = None
    sped_goals_accommodations: list[str] = []

class StudentAttendanceDay(BaseModel):
    email: str
    date: str
    attendance_type: str
    absent: bool = False

class StaffMember(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    email: str
    position: str
    
class BehaviorReferral(BaseModel):
    student: Student
    reporting_staff: StaffMember
    date: str
    student_report: str
    internal_report: str
    summary: str

class BehaviorPlan(BaseModel):
    student: Student
    plan_description: str
    staff_author: StaffMember
    adoption_date: str
    active: bool
    
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


def _convert_date_to_string(date:datetime) -> str:
    return date.strftime('%Y-%m-%d')

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

def parse_attendance_sql_file(file_path: str) -> list[StudentAttendanceDay]:
    with open(file_path, 'r') as file:
        lines = file.readlines()
    attendance_data:list[StudentAttendanceDay] = []
    absence_types = ['Partial Unexcused Absence', 'Partial Excused Absence', 'Full Absence', 'Unexcused Absence', 'Excused Absence']
    for line in lines:
        if not line.startswith(("INSERT INTO", "BEGIN", "COMMIT")):
            match = re.search(r"email = '(.+?)'.+?'(\d{4}-\d{2}-\d{2})', \(SELECT attendance_type_id FROM attendance_type WHERE attendance_type = '(.+?)'\)", line)
            if match:
                email, date_str, attendance_type = match.groups()
                absent = attendance_type in absence_types
                attendance_data.append(StudentAttendanceDay(email=email, date=date_str, attendance_type=attendance_type, absent=absent))
    return attendance_data


def create_staff_roster_from_sql(file_path: str) -> list[StaffMember]:
    staff_roster_list: list[StaffMember] = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
    for line in lines:
        if not line.startswith(("INSERT INTO", "BEGIN", "COMMIT")):
            match = re.search(r"\('(.*)', '(.*)', '(.*)', '(.*)', '(.*) Teacher.*'\),", line)
            if match:
                first_name, middle_name, last_name, email, position = match.groups()
                try:
                    staff_roster_list.append(StaffMember(
                        first_name=first_name,
                        middle_name=middle_name,
                        last_name=last_name,
                        email=email,
                        position=position
                    ))
                except ValueError as e:
                    print(f"Error processing line: {line}\n{e}")
    return staff_roster_list

def filter_staff_by_grade_level(staff_list:list[StaffMember], grade_level:int) -> list[StaffMember]:
    new_staff_list = [staff for staff in staff_list if _extract_grade_level(staff.position) == grade_level]
    return new_staff_list

def _extract_grade_level(position: str) -> int:
    match = re.search(r'\d+', position)
    if match:
        return int(match.group())
    return -1

def create_sped_roster_from_sql(student_list:list[Student], file_path: str) -> list[Student]:
    updated_students = {student.email: student for student in student_list}
    with open(file_path, 'r') as file:
        lines = file.readlines()
    for line in lines:
        if not line.startswith(("INSERT INTO", "BEGIN", "COMMIT")):
            match = re.search(r"\(\(SELECT student_id FROM student WHERE email = '(.*)'\), \(SELECT category_id FROM sped_categories WHERE sped_category = '(.*)'\)\),", line)
            if match:
                email, sped_category = match.groups()
                if email in updated_students:
                    updated_students[email].sped_category = sped_category
    return list(updated_students.values())

def hydrate_iep_goals_from_sql(student_list: list[Student], iep_file_path: str) -> list[Student]:
    updated_students = {student.email: student for student in student_list}
    with open(iep_file_path, 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        if not line.startswith(("INSERT INTO", "BEGIN", "COMMIT")):
            match = re.search(r"\(\(SELECT iep_id FROM iep WHERE student_id = \(SELECT student_id FROM student WHERE email = '(.*)'\)\), '(.*)'\),",line)
            if match:
                email, accommodation_goal = match.groups()
                if email in updated_students:
                    updated_students[email].sped_goals_accommodations.append(accommodation_goal)
    return list(updated_students.values())

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

def _truncate_to_one_decimal(number: float) -> float:
    return int(number * 10) / 10.0

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


def _calculate_grades(student_scores: list[StudentScore]) -> dict[str, ReportCard]:
    report_cards: dict[str, ReportCard] = {}
    scores_by_student = defaultdict(list)
    for score in student_scores:
        scores_by_student[score.student_email].append(score)
    for email, scores in scores_by_student.items():
        courses = _aggregate_scores(scores)
        report_card = _create_and_assign_grades(email, courses)
        report_cards[email] = report_card
    return report_cards

def get_or_create_report_cards(scores_json_file: str, report_cards_json_file: str, scores_sql_file: str) -> dict[str, ReportCard]:
    if os.path.exists(report_cards_json_file):
        with open(report_cards_json_file, 'r') as file:
            report_cards_data = json.load(file)
            return {email: ReportCard(**data) for email, data in report_cards_data.items()}

    if not os.path.exists(scores_json_file):
        student_scores = _parse_student_score_from_sql(scores_sql_file)
        with open(scores_json_file, 'w') as file:
            json.dump([score.model_dump() for score in student_scores], file, indent=4)
    else:
        with open(scores_json_file, 'r') as file:
            student_scores_data = json.load(file)
            student_scores = [StudentScore(**score) for score in student_scores_data]

    report_cards = _calculate_grades(student_scores)

    with open(report_cards_json_file, 'w') as file:
        json.dump({email: rc.model_dump() for email, rc in report_cards.items()}, file, indent=4)

    return report_cards

def get_iep_statement(student: Student) -> str:
    if student.sped_category and student.sped_goals_accommodations:
        goals_accommodations_str = ", ".join(student.sped_goals_accommodations)
        return (
            f"{student.first_name} is on the Special Education roster, "
            f"with the IEP category of {student.sped_category} and has the "
            f"following goals and accommodations: {goals_accommodations_str}"
        )
    else:
        return ""

def generate_school_days(start, end):
    day = start
    while day <= end:
        if day.weekday() < 5:
            yield day
        day += timedelta(days=1)

def find_absence_status(attendance_records: list[StudentAttendanceDay], email: str, date: str) -> Optional[bool]:
    for record in attendance_records:
        if record.email == email and record.date == date:
            return record.absent
    return None  # or raise an exception, e.g., ValueError("Record not found")


def get_scenario(staff_member:StaffMember) -> str:
    random_num = random.random()
    if random_num < .2:
        if random.random() < .5:
            return "in the lunch cafeteria, which means the behavior has to be really extreme to warrant a referral write-up, usually swearing or fighting"
        else:
            return "outside on the recess area, which means the behavior has to be really extreme to warrant a referral write-up, usually swearing or fighting"
    return f"{ staff_member.position } class"

def build_prompt(template:Template, student:Student, report_cards, staff_member:StaffMember, behavior_profile:str, scenario:str, date_string:str) -> str:
    return template.render(student=student,
                report_card = report_cards[student.email],
                staff_member = staff_member,
                iep_statement = get_iep_statement(student),
                behavior_profile = behavior_profile,
                scenario = scenario,
                date_string = date_string
                )

def get_behavior_archetypes() -> dict[str,str]:
    return {
    "The Escapist": "Often tries to leave the classroom without permission, showing a preference for wandering the halls over attending lessons.",
    "The Agitator": "Deliberately provokes peers and teachers by challenging classroom rules and debating instructions, disrupting the learning process.",
    "The Saboteur": "Intentionally interferes with classroom technology or peers’ work, aiming to disrupt lessons or presentations.",
    "The Gossip": "Spreads rumors and gossip, creating social conflicts and distracting others from academic and social activities.",
    "The Uncooperative": "Shows reluctance or outright refusal to participate in group work or school projects, often hindering team progress and dynamics.",
    "The Distractor": "Regularly distracts peers with off-topic conversations during lessons, hindering the class's ability to focus.",
    "The Rule Tester": "Constantly tests the limits of school rules, often bending them to see how much can be gotten away with without direct defiance.",
    "The Property Misuser": "Uses school equipment and materials inappropriately, often resulting in broken or lost items.",
    "The Space Invader": "Frequently invades personal space of others, making peers uncomfortable with too-close interactions or unwelcome physical contact.",
    "The Attention Seeker": "Engages in exaggerated behaviors or fabricates stories to gain the attention of peers and teachers, often distracting from class activities.",
    "The Disruptor": "Frequently talks out of turn and makes loud noises, disrupting the class environment.",
    "The Bully": "Often involved in verbal and occasional physical altercations with peers, intimidating them in and out of the classroom.",
    "The Prankster": "Engages in practical jokes that sometimes go too far, affecting the safety and comfort of other students.",
    "The Defiant": "Openly refuses to follow instructions and challenges authority, questioning teacher's directives and decisions.",
    "The Vandal": "Responsible for graffiti and damage to school property, leaving behind a trail of defaced desks and walls.",
    "The Cheater": "Frequently caught cheating on tests or plagiarizing assignments, undermining academic integrity.",
    "The Truant": "Regularly skips classes or shows up late, showing a clear disregard for school attendance policies.",
    "The Instigator": "Incites and encourages disruptive behavior among classmates, often leading group disruptions or conspiracies.",
    "The Cyberbully": "Uses social media and other digital platforms to harass peers, spreading rumors and sending hurtful messages.",
    "The Disengaged": "Often appears uninterested or withdrawn, not participating in any school work or activities, and sometimes sleeping in class."
}

def get_template() -> Template:
    return Template(
    """  
    This task is for a fictional school called Titan Academy, as part of an AI project.
    BACKGROUND CONTEXT:      
    School policy: In order for a student at Titan Academy to earn a behavior referral, they must be explicitly warned twice by the teacher in class,
    and upon the 3rd infraction they will be written up and sent to the Administration Office.
    
    Students will receive a verbal warning if they commit any of the following actions: 
    
    1) Not following directions
    2) Talking out of turn
    3) Being willfully off-task
    4) Being out of uniform
    5) Making distracting noise
    6) Being disrespectful to property, like drawing on desks or ripping up school papers
    7) Going on their phone (and the phone will be confiscated)
    8) Being openly disruptive
    
    Students will automatically be written up without any warnings if they commit any of the major offences:
    
    1) Cursing/swearing
    2) Gross disrespect to the staff or another student
    3) Physical contact with staff
    4) Posturing to fight
    5) Making a comment that goes against someone's racial, gender, or religious identity.
    6) Cheating on a graded assignment
    
    The behavior report will contain 3 elements:
    
    1) Student Report: The student report is the teacher's formal write up of the behavior incident.
    A Student Report should contain 3 overall parts of its strcture: what specific actions the student took that made them earn a verbal warning,
    how the teacher tried to support the student by modifying the situation to encourage the student to make the right decisions, 
    and ultimately what happened that led to the student continuing to make bad decisions and earn that 3rd warning and a write up.
    The student's parents will be able to view this report, so make sure to be thorough to justify the teacher's actions.
    
    2) Internal report: The internal report is usually very short and will only be viewed by other staff and administrators. It should only
    contain information that other staff might find useful.
    
    3) Summary: A one-sentence summary of the student report.
    
    Guidelines for Behavior Report Writing:
    Vivid Descriptions: Describe each incident with rich detail. Use expressive language to paint a clear picture of the student's actions and the classroom atmosphere.
    Direct Quotes: Include direct quotes from the student, teachers, or classmates involved to add depth and personal perspective to the events described.
    Dramatic Impact: Emphasize how the behavior affected the entire classroom, including reactions from other students and any interruptions to learning activities. Highlight emotional responses and the broader impact on the day's lesson.
    Narrative Structure: Write the report like a story, with a beginning that sets the scene, a middle that escalates the tension, and a conclusion that resolves the incident. This approach should make the events compelling and memorable.
    Teacher's Insight: Provide insight into the teacher's strategies and emotional journey through the incident. Describe what the teacher tried to do to manage the situation and their reflections on the outcome.
    Teacher emotions: The teacher should be emotionally invested in the student's success, and the success of the school environment.
        
    
    DIRECTIONS:
    
    Write a behavior report from the point of view of the teacher {{ staff_member.first_name }} {{ staff_member.last_name }}
    The date of the report is: {{ date_string }}
    Your position is {{ staff_member.position }} in the Titan Academy School.
    The location/context where the behavior incident occured was {{ scenario }}
    
    The fictional student you need to write a behavior referral report for:
    Student name: {{ student.first_name }} {{ student.last_name }}
    Date of Birth: {{ student.dob }}
    Sex/Gender: {{ student.sex }}
    Grade Level: {{ student.grade_level }}
    
    {{ iep_statement }}
    
    This is the general behavior pattern of this student, so make sure the behavior report follows this:
    {{ behavior_profile }}
    
    This is {{ student.first_name }}'s report card:
    Math Grade: {{ report_card.math_grade }} {{report_card.math_percentage }}
    Reading Grade: {{ report_card.reading_grade }} {{ report_card.reading_percentage }}
    Social Studies Grade {{ report_card.social_studies_grade }} {{ report_card.social_studies_percentage }}
    Writing Grade: {{ report_card.writing_grade }} {{ report_card.writing_percentage }}
    Science Grade: {{ report_card.science_grade }} {{ report_card.science_percentage }}
    
    Output a JSON object that will form this shape:
    {
        "student_report": "You will write the student report here",
        "internal_report": "You will write the internal report here",
        "summary":"A one sentence summary of the behavior report"
    }
    
    You must complete ALL of the elements of the JSON. You must include "student_report", "internal_report" and "summary"
    """
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


def get_mock_response(student_name:str, staff_member_last_name:str, behavior_profile, scenario, day_string) -> dict[str,str]:
    return {
    "student_report": f"Mock Behavior Report for {student_name} on date {day_string} written by {staff_member_last_name}, with behavior profile {behavior_profile}. Scenario: {scenario}",
    "internal_report": "Internal Report",
    "summary": "Summary."
}

def main():
    STUDENT_CSV_FILE_NAME = '../03_student/students.csv'
    STAFF_SQL_FILE_NAME = '../02_staff/staff-insert.sql'
    SPED_ROSTER_SQL_FILE_NAME = '../09_sped/sped-inserts.sql'
    IEPS_AND_GOALS_FILE_NAME = '../09_sped/ieps-and-goals.sql'
    STUDENT_SCORES_JSON_FILE_NAME = 'student_scores.json'
    STUDENT_SCORE_SQL_FILE_NAME = '../08_student_scores/student-score-insert.sql'
    REPORTCARDS_JSON_FILE_NAME = 'report_cards.json'
    DAILY_ATTENDANCE_SQL_FILE_NAME = '../04_dailyattendance/daily-attendance-insert.sql'

    original_student_list = parse_students_from_csv(STUDENT_CSV_FILE_NAME)
    sped_categories_student_list = create_sped_roster_from_sql(original_student_list,SPED_ROSTER_SQL_FILE_NAME)
    student_list_full_sped = hydrate_iep_goals_from_sql(sped_categories_student_list,IEPS_AND_GOALS_FILE_NAME)
    attendance_data = parse_attendance_sql_file(DAILY_ATTENDANCE_SQL_FILE_NAME)
    staff_list = create_staff_roster_from_sql(STAFF_SQL_FILE_NAME)
        
    report_cards = get_or_create_report_cards(
        scores_json_file=STUDENT_SCORES_JSON_FILE_NAME,
        report_cards_json_file=REPORTCARDS_JSON_FILE_NAME,
        scores_sql_file=STUDENT_SCORE_SQL_FILE_NAME
    )
    
    start_date = datetime(2023, 9, 1)
    end_date = datetime(2024, 5, 30)
    school_days:list[datetime] = list(generate_school_days(start_date, end_date))
    archetypes = get_behavior_archetypes()
    archetypes_list = list(archetypes.values())
    template = get_template()
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    
    counter = 1
    for student in student_list_full_sped:
        behavior_temperature = random.random() 
        if behavior_temperature < .7: # 70% of students never get in trouble
            print(f"{student.first_name} {student.last_name} never gets in trouble.")
            continue
        
        high_flyer_status = True if random.random() < .30 else False # of the remaining 30% who do get in trouble, 30% of those are high flyers (9% of the whole school)
        
        behavior_status_text = f"{student.first_name} is a high flyer" if high_flyer_status else f"{student.first_name} only sometimes gets in trouble"
        print(behavior_status_text)
        
        behavior_profile_list = random.sample(archetypes_list, 3)
        grade_level_staff_list = filter_staff_by_grade_level(staff_list,student.grade_level)

        for day in school_days:
            if counter > 2: # for development
                break
            
            if find_absence_status(attendance_data,student.email,_convert_date_to_string(day)):
                print(f"{student.first_name} absent today.")
                continue
            
            if (high_flyer_status and random.random() < .4) or (not high_flyer_status and random.random() < .1): # on any particular day a high flyer has a 40% chance of getting in trouble, a non high flyer 10% chance
                behavior_profile = random.choice(behavior_profile_list)
                staff_member = random.choice(grade_level_staff_list)
                scenario = get_scenario(staff_member)
                day_string = _convert_date_to_string(day)
                prompt = build_prompt(template,student,report_cards,staff_member, behavior_profile, scenario, day_string)
                response_content = get_mock_response(student.first_name, staff_member.last_name, behavior_profile, scenario, day_string)
                # response_content = get_llm_response(client, prompt)  # Network call
                print(response_content)
                counter += 1
    print (counter)
    print (counter / len(school_days))
    
    #Final Todo: Write each LLM call to SQL file

if __name__ == "__main__":
    main()
