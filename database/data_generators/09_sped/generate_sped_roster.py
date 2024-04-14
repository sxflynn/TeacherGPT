import csv
import random
import pprint
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
    category: list[SpedCategories]
    

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
    sped_roster_list = []
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

def _assign_multiple_categories(shuffled_categories:list[tuple[str, float]]) -> list[SpedCategories]:
    categories = []
    attempts = 0
    while len(categories) < 2:
        random.shuffle(shuffled_categories)
        for category, probability in shuffled_categories:
            if random.random() < probability:
                if all(c.sped_category != convert_snake_to_capitalized(category) for c in categories):
                    categories.append(SpedCategories(sped_category=convert_snake_to_capitalized(category)))
                if len(categories) >= 2:
                    return categories
        attempts += 1
        if attempts > 10:
            while len(categories) < 2:
                random_category = random.choice(shuffled_categories)
                if all(c.sped_category != convert_snake_to_capitalized(random_category[0]) for c in categories):
                    categories.append(SpedCategories(sped_category=convert_snake_to_capitalized(random_category[0])))
            break
    return categories

def _assign_single_category(shuffled_categories:list[tuple[str, float]]) -> list[SpedCategories]:
    categories = []
    for category, probability in shuffled_categories:
        if random.random() < probability:
            categories.append(SpedCategories(sped_category=convert_snake_to_capitalized(category)))
            break
    return categories

def _ensure_at_least_one_category(categories, shuffled_categories:list[tuple[str, float]]) -> list[SpedCategories]:
    if not categories:
        category = random.choice(list(shuffled_categories))
        categories.append(SpedCategories(sped_category=convert_snake_to_capitalized(category[0])))
    return categories

def add_sped_category(sped_roster_list: list[SpedRoster]) -> list[StudentSpedCategories]:
    student_sped_category_list: list[StudentSpedCategories] = []
    for sped_student in sped_roster_list:
        if not sped_student.has_iep:
            continue
        has_multiple_categories: bool = random.random() < CATEGORY_PROBABILITIES["multiple_disabilities"]
        shuffled_categories = [(cat, prob) for cat, prob in CATEGORY_PROBABILITIES.items() if cat != "multiple_disabilities"]
        random.shuffle(shuffled_categories)
        if has_multiple_categories:
            categories = _assign_multiple_categories(shuffled_categories)
        else:
            categories = _assign_single_category(shuffled_categories)
            categories = _ensure_at_least_one_category(categories, shuffled_categories)
        student_sped_category_list.append(StudentSpedCategories(
            student=sped_student,
            category=categories
        ))
    return student_sped_category_list

def main():
    STUDENT_CSV_FILE_NAME = '../03_student/students.csv'
    student_list = parse_students_from_csv(STUDENT_CSV_FILE_NAME)
    sped_roster_list = generate_sped_roster(student_list)
    sped_category_list = create_category_list(CATEGORY_PROBABILITIES)
    sped_roster_with_categories = add_sped_category(sped_roster_list)

if __name__ == "__main__":
    main()