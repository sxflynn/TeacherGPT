from collections import defaultdict
from datetime import datetime
import random
import re
import pprint
from typing import Optional
from pydantic import BaseModel

class StudentScore(BaseModel):
    student_id: str
    assignment_id: str
    points_earned: int
    percentage_score: float
    missing: bool

class StudentAttendanceDay(BaseModel):
    email: str
    date: str
    attendance_type: str
    absent: bool = False

class StudentProfile(BaseModel):
    email: str
    attendance_rate: float

class Assignment(BaseModel):
    assignment_title: str
    assignment_type: str
    assignment_value: int
    date_assigned: str
    date_due: str
    course_name: str

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

def parse_assignment_sql_file(file_path: str) -> list[Assignment]:
    with open(file_path, 'r') as file:
        lines = file.readlines()
    assignment_data: list[Assignment] = []
    for line in lines:
        if not line.startswith(("INSERT INTO", "BEGIN", "COMMIT")):
            match = re.search(r"\('(.*?)',\s*'(.*?)','\s*(\d+)',\s*'(\d{4}-\d{2}-\d{2})',\s*'(\d{4}-\d{2}-\d{2})',\s*\(SELECT course_id FROM course WHERE course_name LIKE '(.*?)%'\)\),?", line)
            if match:
                assignment_title, assignment_type, assignment_value, date_assigned, date_due, course_name = match.groups()
                try:
                    assignment_data.append(Assignment(
                        assignment_title=assignment_title,
                        assignment_type=assignment_type,
                        assignment_value=int(assignment_value),
                        date_assigned=date_assigned,
                        date_due=date_due,
                        course_name=course_name
                    ))
                except ValueError as e:
                    print(f"Error processing line: {line}\n{e}")
    return assignment_data

def create_student_profiles(attendance_data: list[StudentAttendanceDay]) -> list[StudentProfile]:
    student_days = defaultdict(lambda: {'total': 0, 'absences': 0})
    for record in attendance_data:
        student_days[record.email]['total'] += 1
        if record.absent:
            student_days[record.email]['absences'] += 1
    student_profiles:list[StudentProfile] = []
    for email, days in student_days.items():
        rate = ((days['total'] - days['absences']) / days['total']) * 100
        attendance_rate = round(rate, 2)
        student_profiles.append(StudentProfile(email=email, attendance_rate=attendance_rate))
    return student_profiles

def get_grade_from_email(email: str) -> str:
    match = re.search(r'(\d{2})@', email)
    if match:
        number = int(match.group(1))
        if number == 27:
            return "8th"
        elif number == 28:
            return "7th"
        elif number == 29:
            return "6th"
    return None

def _filter_attendance_record_by_email(attendance_data: list[StudentAttendanceDay], email: str) -> list[StudentAttendanceDay]:
    return [record for record in attendance_data if record.email == email]

def _filter_student_profiles_by_email(student_profiles: list[StudentProfile], email: str) -> StudentProfile:
    for record in student_profiles:
        if record.email == email:
            return record
    return None

def _filter_assignments_by_day(assignment_data:list[Assignment], date:str) -> list[Assignment]:
    return [record for record in assignment_data if record.date_assigned == date]

def _filter_assignments_by_grade_level(assignment_data:list[Assignment], grade_level:str) -> list[Assignment]:
    return [record for record in assignment_data if record.course_name.startswith(grade_level)] 

def _generate_score(attendance_rate, assignment_value) -> int:
    if attendance_rate >= 90:
        base_score = random.uniform(0.85, 1.0)  
    else:
        base_score = random.uniform(0.5, 1.0)  
    if attendance_rate < 90 and random.random() < 0.95:
        base_score = min(base_score, random.uniform(0.7, 0.95))      
    points_earned = round(base_score * assignment_value)
    return points_earned

# def _find_record_by_date(attendance_data: list[StudentAttendanceDay], specific_date: str) -> Optional[StudentAttendanceDay]:
#     for record in attendance_data:
#         if record.date == specific_date:
#             return record
#     return None

def _generate_single_student_scores_list(attendance_data:list[StudentAttendanceDay], student_profiles:list[StudentProfile], assignment_data:list[Assignment], email:str) -> list[StudentScore]:
    student_scores:list[StudentScore] = []
    grade = get_grade_from_email(email)
    student_attendance_record = _filter_attendance_record_by_email(attendance_data, email)
    student_profile = _filter_student_profiles_by_email(student_profiles, email)
    grade_level_assignments = _filter_assignments_by_grade_level(assignment_data,grade)
    for day in student_attendance_record:
        daily_assignments = _filter_assignments_by_day(grade_level_assignments,day.date)
        for assignment in daily_assignments: 
            points_earned = _generate_score(attendance_rate=student_profile.attendance_rate,assignment_value=assignment.assignment_value)
            if day.absent:
                points_earned = 0
            percentage_score = round(points_earned / assignment.assignment_value, 2)
            student_scores.append(StudentScore(
                student_id=f"(SELECT student_id FROM student WHERE email = '{email}')",
                assignment_id=f"(SELECT assignment_id FROM assignment WHERE assignment_title = '{assignment.assignment_title}' AND course_id = (SELECT course_id from course WHERE course_name = '{assignment.course_name}'))",
                points_earned=points_earned,
                percentage_score=percentage_score,
                missing=day.absent
            ))
    return student_scores

def generate_all_student_scores(attendance_rates:list[StudentProfile], attendance_data:list[StudentAttendanceDay], assignment_data:list[Assignment]) -> list[StudentScore]:
    all_student_scores:list[StudentScore] = []
    for student in attendance_rates:
        student_scores = _generate_single_student_scores_list(attendance_data, student_profiles=attendance_rates, assignment_data=assignment_data, email=student.email)
        for score in student_scores:
            all_student_scores.append(score)
    return all_student_scores


def _generate_student_score_sql_value_from_object(student_score:StudentScore) -> str:
    return f"({student_score.student_id}, {student_score.assignment_id},{student_score.points_earned},{student_score.percentage_score},{student_score.missing})"

def generate_all_student_score_values(student_scores:list[StudentScore]) -> list[str]:
    values:list[str] = []
    for score in student_scores:
        values.append(_generate_student_score_sql_value_from_object(score))
    return values

def main():
    # student_csv_file_name = '../03_student/students.csv'
    daily_attendance_sql_inserts = '../04_dailyattendance/daily-attendance-insert.sql'
    assignments_inserts = '../07_assignments/assignment-inserts.sql'
    assignment_data = parse_assignment_sql_file(assignments_inserts)
    attendance_data = parse_attendance_sql_file(daily_attendance_sql_inserts)
    student_attendance_rate_profiles = create_student_profiles(attendance_data)
    all_student_scores:list[StudentScore] = generate_all_student_scores(student_attendance_rate_profiles, attendance_data, assignment_data)
    student_score_insert_values = generate_all_student_score_values(all_student_scores)
    print(student_score_insert_values[0])

def generate_insert_statement(table_name, columns:list[str], values):
    columns_formatted = ', '.join([f'"{column}"' for column in columns])
    values_formatted = ',\n'.join(values)
    return f'INSERT INTO "{table_name}" ({columns_formatted})\nVALUES\n{values_formatted};\n\n'

if __name__ == "__main__":
    main()


# INSERT INTO student_score (student_id, assignment_id, points_earned, percentage_score, missing)
# VALUES (
#   (SELECT student_id FROM student WHERE email = 'atwhitehead29@titanacademy.edu'),
#   (SELECT assignment_id FROM assignment WHERE assignment_title = 'Unit 1 Day 1' AND course_id = (SELECT course_id FROM course WHERE course_name = '6th Grade Math')),
#   4,
#   0.8,
#   False
# );
