import random
import string
import csv
from datetime import datetime, timedelta
from typing import List
from pydantic import BaseModel
from faker import Faker
from names_2010 import MALE_NAMES, FEMALE_NAMES

class Student(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    dob: str
    sex: str
    email: str = ""
    ohio_ssid: str
    grade_level: int # for CSV, not SQL

def return_current_academic_year() -> int:
    current_date = datetime.now()
    start_academic_year = current_date.year if current_date.month >= 8 else current_date.year - 1
    return start_academic_year

def calculate_graduation_year(current_grade: int) -> int:
    current_academic_year = return_current_academic_year()
    grades_to_graduation = 12 - current_grade
    graduation_year = current_academic_year + grades_to_graduation
    return graduation_year

def generate_random_2010_name(gender_int = random.randint(0,1)) -> str:
    return random.choice(FEMALE_NAMES) if gender_int == 0 else random.choice(MALE_NAMES)

def generate_email(student: Student) -> str:
    first_char = student.first_name.lower()[0]
    middle_char = student.middle_name.lower()[0]
    domain = "@titanacademy.edu"
    graduation_year = calculate_graduation_year(student.grade_level)
    last_two_digits = str(graduation_year)[-2:]
    return f"{first_char}{middle_char}{student.last_name.lower()}{last_two_digits}{domain}"

def generate_random_birthday(academic_year: int) -> str:
    START_MONTH, START_DAY = 8, 1
    start_date = datetime(academic_year - 1, START_MONTH, START_DAY)
    END_MONTH, END_DAY = 7, 31
    end_date = datetime(academic_year, END_MONTH, END_DAY)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randint(0, days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date.strftime("%Y-%m-%d")
    
def generate_random_ohio_ssid() -> str:
    NUM_OF_LETTERS = 2
    letters = ''.join(random.choices(string.ascii_uppercase, k=NUM_OF_LETTERS))
    NUM_OF_NUMBERS = 7
    digits = ''.join(random.choices(string.digits, k=NUM_OF_NUMBERS))
    return letters + digits

def generate_student(gender_int, academic_year, grade_level) -> Student:
    GENDER = gender_int
    SEX = 'F' if gender_int == 0 else 'M'
    new_student = Student(
        first_name = generate_random_2010_name(GENDER),
        middle_name = generate_random_2010_name(GENDER),
        last_name = fake.last_name(),
        dob = generate_random_birthday(academic_year),
        sex = SEX,
        ohio_ssid = generate_random_ohio_ssid(),
        grade_level=grade_level
)
    new_student.email = generate_email(new_student)
    return new_student

def generate_student_list(quantity: int, academic_birth_years: range, grade_range: range) -> List[Student]:
    num_years = len(academic_birth_years)
    students_per_year = quantity // num_years
    remaining_students = quantity % num_years

    student_list: List[Student] = []
    for index, year in enumerate(academic_birth_years):
        grade_level = list(grade_range)[index]
        students_this_year = students_per_year + (1 if remaining_students > 0 else 0)
        if remaining_students > 0:
            remaining_students -= 1
        for _ in range(students_this_year):
            GENDER = 0 if random.random() < 0.5 else 1
            new_student = generate_student(GENDER, academic_year=year, grade_level=grade_level)
            student_list.append(new_student)
    return student_list

def quote_sql_string(s) -> str:
    """Formats a Python string for SQL insertion, handling None values and escaping characters."""
    return 'NULL' if s is None else f"'{s.replace("'", "''")}'"

def student_to_sql_values(student) -> str:
    """Converts a Student instance to a SQL tuple string using model_dump."""
    student_dict = student.model_dump(exclude_none=True)
    values = [
        quote_sql_string(student_dict.get('first_name')),
        quote_sql_string(student_dict.get('middle_name')),
        quote_sql_string(student_dict.get('last_name')),
        quote_sql_string(student_dict.get('dob')),
        quote_sql_string(student_dict.get('sex')),
        quote_sql_string(student_dict.get('email')),
        quote_sql_string(student_dict.get('ohio_ssid'))
        # grade level deliberately missing from SQL inserts because the student table doesn't include grade level
        # grade level will be included in the exported .csv file to simplify the other data generators
    ]
    return f"({', '.join(values)})"
    
def generate_insert_statement(table_name, columns, values) -> str:
    columns_formatted = ', '.join([f'"{column}"' for column in columns])
    values_formatted = ',\n'.join(values)
    return f'INSERT INTO "{table_name}" ({columns_formatted})\nVALUES\n{values_formatted};\n\n'

def write_students_to_csv(students: List[Student], filename: str = 'students.csv'):
    headers = ['first_name', 'middle_name', 'last_name', 'dob', 'sex', 'email', 'ohio_ssid', 'grade_level']    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(headers)
        for student in students:
            # Write the student data
            csv_writer.writerow([
                student.first_name, student.middle_name, student.last_name, 
                student.dob, student.sex, student.email, student.ohio_ssid, 
                student.grade_level
                
            ])

fake = Faker()

academic_birth_year_list = range(2010, 2013)  # 2012 is exclusive, so it will be 2010-2012
grade_level_list = range(6, 9) # 9 is exclusive, so it will be 6-8
reversed_academic_birth_year_list = list(reversed(academic_birth_year_list))


new_student_list = generate_student_list(250, reversed_academic_birth_year_list, grade_level_list)
student_inserts = [student_to_sql_values(student) for student in new_student_list]

student_sql_inserts = generate_insert_statement("student", ["first_name","middle_name","last_name","dob","sex","email","ohio_ssid"], student_inserts)

all_sql_inserts = student_sql_inserts
sql_file_name = 'student-insert.sql'
with open(sql_file_name, encoding="utf-8", mode='w', newline='') as sql_file:
    sql_file.write(all_sql_inserts)

# Generate the CSV file which includes the grade level column
write_students_to_csv(new_student_list, 'students.csv')
