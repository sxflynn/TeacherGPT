import random
# import math
from typing import List, Optional
from faker import Faker
from pydantic import BaseModel
from names_90s import MALE_NAMES, FEMALE_NAMES

class StaffMember(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    email: Optional[str] = None
    position: Optional[str] = None
    
    def update_position(self, additional_title: str):
        if self.position:
            self.position += f", {additional_title}"
        else:
            self.position = additional_title

NUMBER_OF_STUDENTS = 235
TEACHING_STAFF_TO_STUDENT_RATIO = 18
GRADE_LEVELS_LIST = ["6th","7th","8th"]
SUBJECT_LIST = ["Math","Science","History","Reading","Writing"]

fake = Faker()

def random_90s_name(gender_int = random.randint(0,1)):
    return random.choice(FEMALE_NAMES) if gender_int == 0 else random.choice(MALE_NAMES)

def generate_unique_email(first_name, last_name):
    domain = "@titanacademy.edu"
    return f"{first_name.lower()}.{last_name.lower()}{domain}"

def generate_teacher(assignments):
    GENDER = 0 if random.random() < 0.65 else 1
    new_teacher = StaffMember(
            first_name=random_90s_name(GENDER),
            middle_name=random_90s_name(GENDER),
            last_name=fake.last_name()
        )
    new_teacher.email = generate_unique_email(new_teacher.first_name, new_teacher.last_name)
    try:
        new_teacher.position = next(assignments)
    except StopIteration:
        print("Not enough assignments for the number of staff.")
    return new_teacher

def create_teachers(number_of_staff) -> List[StaffMember]:
    teachers = []
    teacher_assignments = []
    for grade in GRADE_LEVELS_LIST:
        for subject in SUBJECT_LIST:
            teacher_assignments.append(f"{grade} Grade {subject} Teacher")

    assignments = iter(teacher_assignments)  # Create an iterator from the assignments list
    for new_teacher in range(number_of_staff):
        new_teacher = generate_teacher(assignments)
        teachers.append(new_teacher)
    return teachers

def quote_sql_string(s):
    """Formats a Python string for SQL insertion, handling None values and escaping characters."""
    return 'NULL' if s is None else f"'{s.replace("'", "''")}'"

def teacher_to_sql_values(teacher):
    """Converts a StaffMember instance to a SQL tuple string using model_dump."""
    teacher_dict = teacher.model_dump(exclude_none=True)
    values = [
        quote_sql_string(teacher_dict.get('first_name')),
        quote_sql_string(teacher_dict.get('middle_name')),
        quote_sql_string(teacher_dict.get('last_name')),
        quote_sql_string(teacher_dict.get('email')),
        quote_sql_string(teacher_dict.get('position'))
    ]
    return f"({', '.join(values)})"

def insert_grade_levels_with_chairs(grade_levels: list[str], teachers: List[StaffMember]) -> str:
    values_list = []
    chair_emails = []  # Track chair emails to modify positions later
    for grade in grade_levels:
        eligible_teachers = [t for t in teachers if f'{grade} Grade' in t.position]
        if not eligible_teachers:
            continue
        chair_teacher = random.choice(eligible_teachers)
        chair_teacher.update_position(f"{grade} Grade Level Chair")
        chair_emails.append(chair_teacher.email)
        values_list.append(f"('{grade} Grade', (SELECT staff_id FROM staff WHERE email = '{chair_teacher.email}'))")
    values = ",\n".join(values_list)
    return f'INSERT INTO "grade_levels" ("grade_level_name", "grade_level_chair") VALUES\n{values};\n', chair_emails

def generate_staff_grade_level_inserts(grade_levels: list[str], teachers: List[StaffMember]) -> str:
    values_list = []
    for grade in grade_levels:
        for teacher in teachers:
            if f'{grade} Grade' in teacher.position:
                values_list.append(f"((SELECT grade_level_id FROM grade_levels WHERE grade_level_name = '{grade} Grade'), (SELECT staff_id FROM staff WHERE email = '{teacher.email}'))")
    values = ",\n".join(values_list)
    return f'INSERT INTO "staff_grade_levels" ("grade_level_id", "staff_id") VALUES\n{values};\n'

def main():
    number_of_staff = round(NUMBER_OF_STUDENTS / TEACHING_STAFF_TO_STUDENT_RATIO)
    teachers = create_teachers(number_of_staff)
    
    # Generate inserts for grade levels and capture chair emails
    grade_level_inserts, chair_emails = insert_grade_levels_with_chairs(GRADE_LEVELS_LIST, teachers)
    
    # Update teacher positions to include grade level chair titles
    for teacher in teachers:
        if teacher.email in chair_emails:
            # Extract grade from the teacher's position
            grade = teacher.position.split(' ')[0]
            chair_designation = f"{grade} Grade Level Chair"
            if chair_designation not in teacher.position:  # Check to prevent duplication
                teacher.position += f", {chair_designation}"
    
    # Now that chair positions are updated, generate staff inserts
    staff_inserts = [teacher_to_sql_values(teacher) for teacher in teachers]
    staff_sql_inserts = generate_insert_statement("staff", ["first_name", "middle_name", "last_name", "email", "position"], staff_inserts)
    
    staff_grade_level_inserts = generate_staff_grade_level_inserts(GRADE_LEVELS_LIST, teachers)
    
    all_sql_inserts = staff_sql_inserts + "\n" + grade_level_inserts + "\n" + staff_grade_level_inserts
    sql_file_name = 'staff-insert.sql'
    with open(sql_file_name, encoding="utf-8", mode='w', newline='') as sql_file:
        sql_file.write(all_sql_inserts)

def generate_insert_statement(table_name, columns, values):
    columns_formatted = ', '.join([f'"{column}"' for column in columns])
    values_formatted = ',\n'.join(values)
    return f'INSERT INTO "{table_name}" ({columns_formatted})\nVALUES\n{values_formatted};\n\n'

# CLASS_SIZE_MAX = 30
# STARTING_GRADE = 6
# ENDING_GRADE = 8
# PERIODS_IN_SCHOOL_DAY = 7
# ADVISORY_PERIOD_PER_TEACHER = 1
# LUNCH_RECESS_PERIOD = 1
# number_of_grade_levels = ENDING_GRADE-STARTING_GRADE+1
# students_per_grade = math.floor(NUMBER_OF_STUDENTS / number_of_grade_levels)
# total_classrooms_needed = math.ceil(NUMBER_OF_STUDENTS / CLASS_SIZE_MAX)
# classrooms_per_grade = math.ceil(students_per_grade / CLASS_SIZE_MAX)
# teaching_periods_per_teacher = classrooms_per_grade  # Assuming a teacher teaches one class per subject per grade
# approx_class_size = round(NUMBER_OF_STUDENTS/total_classrooms_needed)
# planning_periods_per_teacher = PERIODS_IN_SCHOOL_DAY - (teaching_periods_per_teacher + ADVISORY_PERIOD_PER_TEACHER + LUNCH_RECESS_PERIOD)

if __name__ == "__main__":
    main()
