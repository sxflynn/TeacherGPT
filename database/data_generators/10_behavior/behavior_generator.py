import random
from collections import defaultdict
import csv
import json
import os
import pprint
import re
from jinja2 import Template
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


# create behavior profile(all_students)
# create carveout for sped students with ED

    
#* generate all behavior referrals (all_students, all_staff, all_dates, all_courses)

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
        # Join the list into a single string with commas
        goals_accommodations_str = ", ".join(student.sped_goals_accommodations)
        return (
            f"{student.first_name} is on the Special Education roster, "
            f"with the IEP category of {student.sped_category} and has the "
            f"following goals and accommodations: {goals_accommodations_str}"
        )
    else:
        return ""

def get_scenario(staff_member:StaffMember) -> str:
    random_num = random.random()
    if random_num < .2:
        if random.random() < .5:
            return "in the lunch cafeteria"
        else:
            return "outside on the recess area"
    return f"{ staff_member.position } class"

def build_prompt(template:Template, student:Student, report_cards, staff_member:StaffMember) -> str:
    return template.render(student=student,
                report_card = report_cards[student.email],
                staff_member = staff_member
                )

def get_template() -> Template:
    return Template(
    """    
    Write this behavior report from the point of view of the teacher {{ staff_member.first_name }} {{ staff_member.last_name }}
    Your position is {{ staff_member.position }} in the school. The location where the behavior incident occured was {{ scenario }}
    
    The fictional student you need to write a behavior referral report for:
    Student name: {{ student.first_name }} {{ student.last_name }}
    Date of Birth: {{ student.dob }}
    Sex/Gender: {{ student.sex }}
    Grade Level: {{ student.grade_level }}
    
    {{ iep_statement }}
    
    This is {{ student.first_name }}'s report card:
    Math Grade: {{ report_card.math_grade }} {{report_card.math_percentage }}
    Reading Grade: {{ report_card.reading_grade }} {{ report_card.reading_percentage }}
    Social Studies Grade {{ report_card.social_studies_grade }} {{ report_card.social_studies_percentage }}
    Writing Grade: {{ report_card.writing_grade }} {{ report_card.writing_percentage }}
    Science Grade: {{ report_card.science_grade }} {{ report_card.science_percentage }}
        
    Output a JSON object that will form this shape:
    {
        "student_report": "You will write the student report here",
        "internal_report": "You will write the internal report here"
    }
    
    You must include ALL of the elements of the JSON. You must include "student_report", and "internal_report"
    """
    )

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

    scenario = get_scenario(staff_list[0])
    
    print(scenario)
    
    # generate all behavior referrals and plans (all_students, all_staff, all_dates, all_courses)
    
    
    
    
    pass

if __name__ == "__main__":
    main()
