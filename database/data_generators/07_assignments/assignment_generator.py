import csv
import random
from datetime import datetime, timedelta
from enum import Enum
from pprint import pprint
from typing import List, Optional
from pydantic import BaseModel

class StudentScore(BaseModel):
    student_id: str
    assignment_id: str
    points_earned: int
    missing: bool

class AssignmentType(str, Enum):
    UNIT_TEST = "Unit Test"
    QUIZ = "Quiz"
    ESSAY = "Essay"
    HOMEWORK = "Homework"

ASSIGNMENT_VALUES = {
    AssignmentType.UNIT_TEST: 30,
    AssignmentType.QUIZ: 15,
    AssignmentType.ESSAY: 10,
    AssignmentType.HOMEWORK: 5,
}

class Assignment(BaseModel):
    assignment_title: Optional[str] = None
    assignment_type: Optional[AssignmentType] = None  # Use AssignmentType enum directly
    assignment_value: Optional[int] = None
    date_assigned: Optional[str] = None
    date_due: Optional[str] = None
    course_id: Optional[str] = None

GRADE_LEVELS_LIST = ["6th", "7th", "8th"]
SUBJECT_LIST = ["Math", "Science", "History", "Reading", "Writing"]
REVIEW_AND_TEST_DAYS = 3

def generate_school_days(start, end):
    day = start
    while day <= end:
        if day.weekday() < 5:
            yield day
        day += timedelta(days=1)

def _convert_date_to_string(date:datetime) -> str:
    return date.strftime('%Y-%m-%d')

def create_course_string_list():
    return [f"{grade} Grade {subject}" for grade in GRADE_LEVELS_LIST for subject in SUBJECT_LIST]

def _divide_school_year_into_units(school_days):
    total_days = len(school_days)
    unit_lengths = []
    while sum(unit_lengths) < total_days:
        unit_length = random.randint(24, 33)
        if sum(unit_lengths) + unit_length > total_days:
            unit_length = total_days - sum(unit_lengths)
        unit_lengths.append(unit_length)
        if len(unit_lengths) == 7:  # Ensure the last unit fills the remainder
            unit_lengths[-1] += total_days - sum(unit_lengths)
            break
    units = []
    start_index = 0
    for length in unit_lengths:
        units.append(school_days[start_index:start_index+length])
        start_index += length
    return units

def _generate_unit_cycles(min_length:int, max_length:int, available_days):
    cycles = []
    while available_days > max_length:
        cycle_length = random.randint(max_length, max_length)
        if available_days - cycle_length >= min_length or available_days - cycle_length == 0:
            cycles.append(cycle_length)
            available_days -= cycle_length
        else:
            break  # Break early to adjust the last cycle for remaining days
    if available_days > 0:
        cycles.append(available_days)
    return cycles

def _create_assignment(assignment_type: AssignmentType, unit_number: int, current_date_index: int, 
                       date_assigned: datetime, date_due: datetime, quiz_number: int = None) -> Assignment:
    if assignment_type == AssignmentType.HOMEWORK:
        assignment_title = f"Unit {unit_number} Day {current_date_index + 1}"
    elif assignment_type == AssignmentType.QUIZ:
        assignment_title = f"Unit {unit_number} Quiz {quiz_number}"
    elif assignment_type == AssignmentType.UNIT_TEST:
        assignment_title = f"Unit {unit_number} Test"
    else:
        raise ValueError(f"Unsupported assignment type: {assignment_type}")
    return Assignment(
        assignment_type=assignment_type,
        assignment_value=ASSIGNMENT_VALUES[assignment_type],
        assignment_title=assignment_title,
        date_assigned=_convert_date_to_string(date_assigned),
        date_due=_convert_date_to_string(date_due)
    )

def _append_cycle_assignments(cycles: List[int], unit_dates: List[datetime], unit_number: int, 
                              total_days: int, review_and_test_days: int) -> List[Assignment]:
    assignments = []
    current_date_index = 0
    quiz_number = 1
    for cycle_length in cycles:
        for _ in range(cycle_length - 1):  # Homework days
            if current_date_index < total_days - review_and_test_days:
                date_assigned = unit_dates[current_date_index]
                date_due = unit_dates[current_date_index + 1]
                assignments.append(_create_assignment(AssignmentType.HOMEWORK, unit_number, current_date_index, date_assigned, date_due))
                current_date_index += 1
        # Add Quiz
        if current_date_index < total_days - review_and_test_days:
            date_assigned = unit_dates[current_date_index]
            assignments.append(_create_assignment(AssignmentType.QUIZ, unit_number, current_date_index, date_assigned, date_assigned, quiz_number))
            current_date_index += 1
            quiz_number += 1
    return assignments

def _append_final_review_and_test(unit_dates: List[datetime], unit_number: int) -> List[Assignment]:
    """Appends review days and unit test at the end of the unit."""
    assignments = []
    for i in range(1, 4):
        assignment_type = AssignmentType.HOMEWORK if i < 3 else AssignmentType.UNIT_TEST
        date_assigned = unit_dates[-3 + i - 1]
        date_due = date_assigned if assignment_type == AssignmentType.UNIT_TEST else unit_dates[-3 + i]
        assignments.append(Assignment(
            assignment_type=assignment_type,
            assignment_value=ASSIGNMENT_VALUES[assignment_type],
            assignment_title=f"Unit {unit_number} Review Day {i}" if i < 3 else f"Unit {unit_number} Unit Test",
            date_assigned=_convert_date_to_string(date_assigned),
            date_due=_convert_date_to_string(date_due)
        ))
    return assignments

def _generate_unit_assignments(unit_dates: List[datetime], unit_number: int) -> List[Assignment]:
    total_days = len(unit_dates)
    review_and_test_days = 3  # 2 review days + 1 unit test day
    available_days = total_days - review_and_test_days
    cycles = _generate_unit_cycles(5, 8, available_days)
    assignments = _append_cycle_assignments(cycles, unit_dates, unit_number, total_days, review_and_test_days)
    assignments += _append_final_review_and_test(unit_dates, unit_number)
    return assignments

def _generate_course_year_assignments(school_days:list[datetime]) -> List[List[Assignment]]:
    unit_dates = _divide_school_year_into_units(school_days)
    hydrated_units = []
    for i, unit in enumerate(unit_dates, start=1):
        new_unit = _generate_unit_assignments(unit, unit_number=i)
        hydrated_units.append(new_unit)
    return hydrated_units

def _generate_assignment_sql_value_from_object(assignment:Assignment, course_name:str) -> str:
    assignment_title = assignment.assignment_title
    assignment_type = assignment.assignment_type.value
    assignment_value = assignment.assignment_value
    date_assigned = assignment.date_assigned
    date_due = assignment.date_due
    course_id = f"(SELECT course_id FROM course WHERE course_name LIKE '{course_name}%')"
    return f"('{assignment_title}', '{assignment_type}','{assignment_value}','{date_assigned}','{date_due}',{course_id})"

def generate_all_daily_assignments_all_subjects(school_days:list[datetime], subjects:list[str]) -> list[str,list[str]]:
    assignments_by_day = {subject: ['' for _ in school_days] for subject in subjects}
    for subject in subjects:
        unit_sequences = _generate_course_year_assignments(school_days)
        for unit_assignment_list in unit_sequences:
            for assignment in unit_assignment_list:
                day_index = school_days.index(datetime.strptime(assignment.date_assigned, '%Y-%m-%d'))
                assignments_by_day[subject][day_index] = f"{assignment.assignment_title}"
    return assignments_by_day

def generate_all_daily_assignment_sql_values(school_days:list[datetime], subjects:list[str]):
    values = []
    for subject in subjects:
        unit_sequences = _generate_course_year_assignments(school_days)
        for unit_assignment_list in unit_sequences:
            for assignment in unit_assignment_list:
                values.append(_generate_assignment_sql_value_from_object(assignment,course_name=subject))
    return values


def main():
    start_date = datetime(2023, 9, 1)
    end_date = datetime(2024, 5, 30)
    school_days:list[datetime] = list(generate_school_days(start_date, end_date))
    subjects = create_course_string_list()
    assignments_by_day = generate_all_daily_assignments_all_subjects(school_days, subjects)

    values_list = generate_all_daily_assignment_sql_values(school_days,subjects)

    assignment_insert_statement = generate_insert_statement("assignment",["assignment_title","assignment_type","assignment_value","date_assigned","date_due","course_id"], values_list)
    assignment_inserts_file_name = 'assignment-inserts.sql'
    with open(assignment_inserts_file_name, encoding="utf-8", mode='w', newline='') as sql_file:
        sql_file.write(assignment_insert_statement)

    headers = ['Date'] + subjects
    with open("school-calendar-with-assignments.csv", mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(headers)
        for i, day in enumerate(school_days):
            row = [day.strftime('%Y-%m-%d')]
            for subject in subjects:
                row.append(assignments_by_day[subject][i])
            csv_writer.writerow(row)
            
    print("Generated school calendar with assignments.")

def generate_insert_statement(table_name, columns:list[str], values):
    columns_formatted = ', '.join([f'"{column}"' for column in columns])
    values_formatted = ',\n'.join(values)
    return f'INSERT INTO "{table_name}" ({columns_formatted})\nVALUES\n{values_formatted};\n\n'

if __name__ == "__main__":
    main()
