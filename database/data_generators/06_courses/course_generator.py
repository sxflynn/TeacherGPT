import csv
from typing import List
from pydantic import BaseModel

class Course(BaseModel):
    course_name: str
    lead_teacher_id: str # select staff_id from staff WHERE position LIKE '8th Grade History%'
    grade_level_id: str # select grade_level_id from grade_levels WHERE grade_level_name LIKE '8%'

GRADE_LEVELS_LIST = ["6th","7th","8th"]
SUBJECT_LIST = ["Math","Science","History","Reading","Writing"]

def create_course_string_list() -> list[str]:
    course_list = []
    for grade in GRADE_LEVELS_LIST:
        for subject in SUBJECT_LIST:
            course_list.append(f"{grade} Grade {subject}")
    return course_list

def generate_single_course(course_name:str) -> Course:
    course_number = course_name[0]
    new_course = Course(
        course_name = course_name,
        lead_teacher_id=f"SELECT staff_id FROM staff WHERE position LIKE '{course_name}%'",
        grade_level_id=f"SELECT grade_level_id FROM grade_levels WHERE grade_level_name LIKE '{course_number}%'"
    )
    return new_course

def create_course_list_from_model(course_string_list:list[str]) -> List[Course]:
    course_list:List[Course] = []
    for course_string in course_string_list:
        new_course = generate_single_course(course_string)
        course_list.append(new_course)
    return course_list
    
def generate_course_inserts(course_list: List[Course]) -> str:
    values_list = []
    for course in course_list:
        values_list.append(f"('{course.course_name}', ({course.lead_teacher_id}), ({course.grade_level_id}) )")
    values = ",\n".join(values_list)
    return f'INSERT INTO "course" ("course_name", "lead_teacher_id", "grade_level_id") VALUES\n{values};\n'

def filter_student_courses(student, course_list: List[Course]):
    student_grade = student["grade_level"]
    filtered_courses = [course for course in course_list if student_grade in course.course_name]
    return filtered_courses

def generate_student_course_insert(student, filtered_course_list: List[Course]) -> str:
    values_list = []
    student_email = student["email"]  # 'atwhitehead29@titanacademy.edu'
    for course in filtered_course_list:
        course_name = course.course_name.replace("'", "''")
        values_list.append(f"((SELECT student_id FROM student WHERE email = '{student_email}'), (SELECT course_id FROM course WHERE course_name = '{course_name}'))")
    values = ",\n".join(values_list)
    return f"{values}"

def generate_all_course_student_inserts(student_list):
    pass

def read_student_data(file_name):
    students = []
    with open(file_name, mode='r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            students.append(row)
    return students

def main():
    course_list_string = create_course_string_list()
    course_list = create_course_list_from_model(course_list_string)
    course_sql_inserts = generate_course_inserts(course_list)
    course_insert_file_name = 'course-insert.sql'
    with open(course_insert_file_name, encoding="utf-8", mode='w', newline='') as sql_file:
        sql_file.write(course_sql_inserts)
    student_csv_file_name = '../03_student/students.csv'
    student_data = read_student_data(student_csv_file_name)
    course_student_inserts = []
    for student in student_data:
        student_courses = filter_student_courses(student, course_list)
        student_insert = generate_student_course_insert(student,student_courses)
        course_student_inserts.append(student_insert)
    
    student_course_sql = generate_insert_statement("course_student", ["student_id", "course_id"], course_student_inserts)
    course_student_insert_file_name = 'course-student-insert.sql'
    with open(course_student_insert_file_name, encoding="utf-8", mode='w', newline='') as sql_file:
        sql_file.write(student_course_sql)
    
# Helper to generate an INSERT SQL statement
def generate_insert_statement(table_name, columns, values):
    columns_formatted = ', '.join([f'"{column}"' for column in columns])
    values_formatted = ',\n'.join(values)
    return f'INSERT INTO "{table_name}" ({columns_formatted})\nVALUES\n{values_formatted};\n\n'

if __name__ == "__main__":
    main()