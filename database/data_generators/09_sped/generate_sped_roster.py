import csv
import random
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

class SpedRoster(BaseModel):
    student: Student
    has_iep: bool = False
    has_504: bool = False
    
class SpedCategories(BaseModel):
    sped_category:str
    
class StudentSpedCategories(BaseModel):
    student: SpedRoster
    category: SpedCategories
    

# Source of probabilities:
# https://education.ohio.gov/getattachment/About/Annual-Reports/Special-Education-Implementation-Legislative-Report-SY21-22.pdf

PROBABILITY_IN_SPED = .16
PROBABILITY_504 = 0.023

CATEGORY_PROBABILITIES = {
    "specific_learning_disabilities": 0.3518,
    "other_health_impaired": 0.1880,
    "speech_and_language": 0.1375,
    "autism": 0.1169,
    "intellectual_disabilities": 0.0666,
    "emotional_disturbance": 0.0499,
    "multiple_disabilities": 0.0466,
    "developmental_delay": 0.0231,
    "hearing_impairments": 0.0074,
    "traumatic_brain_injury": 0.0055,
    "orthopedic_impairments": 0.0051,
    "visual_impairments": 0.0034,
    "deaf_blindness": 0.0003
}

def convert_snake_to_capitalized(key:str) -> str:
    return ' '.join(word.capitalize() for word in key.split('_'))

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

def generate_sped_roster(student_list: list[Student]) -> list[SpedRoster]:
    sped_roster_list:list[SpedRoster] = []
    for student in student_list:
        has_iep = random.random() < PROBABILITY_IN_SPED
        has_504 = random.random() < PROBABILITY_504
        if has_iep or has_504:
            new_sped_enrollment = SpedRoster(
                student=student,
                has_iep=has_iep,
                has_504=has_504
            )
            sped_roster_list.append(new_sped_enrollment)
    return sped_roster_list

def create_category_list(probabilities:dict[str,float]) -> list[SpedCategories]:
    sped_categories_list:list[SpedCategories] = []
    for category in probabilities:
        sped_categories_list.append(SpedCategories(
            sped_category=convert_snake_to_capitalized(category)
        ))
    return sped_categories_list

def _assign_single_category(shuffled_categories:list[tuple[str, float]]) -> SpedCategories:
    for category, probability in shuffled_categories:
        if random.random() < probability:
            return SpedCategories(sped_category=convert_snake_to_capitalized(category))
    return None

def _ensure_at_least_one_category(assigned_category, shuffled_categories):
    if assigned_category is None:
        category_name, _ = random.choice(shuffled_categories)
        return SpedCategories(sped_category=convert_snake_to_capitalized(category_name))
    return assigned_category

def add_sped_category(sped_roster_list:list[SpedRoster]):
    student_sped_category_list:list[StudentSpedCategories] = []
    for sped_student in sped_roster_list:
        if not sped_student.has_iep:
            continue
        shuffled_categories = [(cat, prob) for cat, prob in CATEGORY_PROBABILITIES.items() if cat != "multiple_disabilities"]
        random.shuffle(shuffled_categories)
        assigned_category = _assign_single_category(shuffled_categories)
        ensured_category = _ensure_at_least_one_category(assigned_category, shuffled_categories)
        student_sped_category_list.append(StudentSpedCategories(
            student=sped_student,
            category=ensured_category
        ))
    return student_sped_category_list

def summarize_sped_statistics(student_roster: list[StudentSpedCategories]) -> str:
    category_count = {}  # Dictionary to store the count of each category
    student_count = len(student_roster)
    # Iterate through the student roster to count categories
    for student_category in student_roster:
        # Assume each student can have multiple categories
        category_name = student_category.category.sped_category  # Get the category name
        if category_name in category_count:
            category_count[category_name] += 1
        else:
            category_count[category_name] = 1

    # Format the summary string
    summary_lines = []
    summary_lines.append(f"{student_count} in SPED")
    for category, count in category_count.items():
        percentage:float = round(count/student_count * 100, ndigits=3)
        summary_lines.append(f"{percentage}% - {category}: {count} students")
        
    summary_string = "\n".join(summary_lines)
    return summary_string

def _generate_sped_categories_sql_value_from_object(sped_category:SpedCategories) -> str:
    return f"('{sped_category.sped_category}')"

def generate_sped_categories_sql_values(sped_category_list:list[SpedCategories]) -> list[str]:
    values:list[str] = []
    for category in sped_category_list:
        values.append(_generate_sped_categories_sql_value_from_object(category))
    return values

def _generate_sped_roster_sql_value_from_object(sped_roster:SpedRoster) -> str:
    return f"((SELECT student_id FROM student WHERE email = '{sped_roster.student.email}'), {sped_roster.has_iep},{sped_roster.has_504})"

def generate_sped_roster_sql_values(sped_roster_list:list[SpedRoster]) -> list[str]:
    values:list[str] = []
    for student in sped_roster_list:
        values.append(_generate_sped_roster_sql_value_from_object(student))
    return values

def _generate_student_sped_roster_sql_value_from_object(student_sped_category:StudentSpedCategories) -> str:
    return f"((SELECT student_id FROM student WHERE email = '{student_sped_category.student.student.email}'), (SELECT category_id FROM sped_categories WHERE sped_category = '{student_sped_category.category.sped_category}'))"

def generate_student_sped_categories_sql_values(student_sped_category_roster:list[StudentSpedCategories]) -> str:
    values:list[str] = []
    for student in student_sped_category_roster:
        values.append(_generate_student_sped_roster_sql_value_from_object(student))
    return values

def generate_insert_statement(table_name, columns: list[str], values: list[str]) -> str:
    def chunked_list(lst, n):
        for i in range(0, len(lst), n):
            yield lst[i:i + n]
    columns_formatted = ', '.join([f'"{column}"' for column in columns])
    values_chunks = list(chunked_list(values, 1000))
    insert_statements = []
    for chunk in values_chunks:
        values_formatted = ',\n'.join(chunk)
        insert_statements.append(f'INSERT INTO "{table_name}" ({columns_formatted})\nVALUES\n{values_formatted};\n\n')
    return ''.join(insert_statements)

def main():
    STUDENT_CSV_FILE_NAME = '../03_student/students.csv'
    sped_inserts_file_name = 'sped-inserts.sql'
    student_list = parse_students_from_csv(STUDENT_CSV_FILE_NAME)
    sped_roster_list = generate_sped_roster(student_list)
    sped_category_list = create_category_list(CATEGORY_PROBABILITIES)
    sped_roster_with_categories = add_sped_category(sped_roster_list)
    print(summarize_sped_statistics(sped_roster_with_categories))
    
    # SpedRoster inserts
    sped_roster_insert_statement = generate_insert_statement("sped_roster",["student_id","has_iep","has_504"],generate_sped_roster_sql_values(sped_roster_list))
    
    # SpedCategory inserts
    sped_category_insert_statement = generate_insert_statement("sped_categories", ["sped_category"],generate_sped_categories_sql_values(sped_category_list))
    
    # StudentSpedCategories inserts
    student_sped_categories_insert_statement = generate_insert_statement("students_sped_categories",["student_id","category_id"],generate_student_sped_categories_sql_values(sped_roster_with_categories))    
    
    print(sped_roster_insert_statement) 
    print(sped_category_insert_statement)   
    print(student_sped_categories_insert_statement)
    
    with open(sped_inserts_file_name, encoding="utf-8", mode='w', newline='') as sql_file:
        sql_file.write(sped_roster_insert_statement + '\n' + sped_category_insert_statement + '\n' + student_sped_categories_insert_statement)

if __name__ == "__main__":
    main()