import csv
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


def main():
    STUDENT_CSV_FILE_NAME = '../03_student/students.csv'
    student_list = parse_students_from_csv(STUDENT_CSV_FILE_NAME)
    
    
if __name__ == "__main__":
    main()