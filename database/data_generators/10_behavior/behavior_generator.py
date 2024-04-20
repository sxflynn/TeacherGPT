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
    

def main():
    pass

if __name__ == "__main__":
    main()
