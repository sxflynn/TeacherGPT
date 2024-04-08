from collections import defaultdict
from datetime import datetime
import re
from typing import List
from pydantic import BaseModel
import pprint

class StudentScore(BaseModel):
    student_id: str
    assignment_id: str
    points_earned: int
    missing: bool

class StudentAttendanceDay(BaseModel):
    email: str
    date: datetime
    attendance_type: str
    absent: bool = False

class StudentProfile(BaseModel):
    email: str
    attendance_rate: float


def parse_sql_file(file_path: str) -> List[StudentAttendanceDay]:
    with open(file_path, 'r') as file:
        lines = file.readlines()
    attendance_data = []
    absence_types = ['Partial Unexcused Absence', 'Partial Excused Absence', 'Full Absence', 'Unexcused Absence', 'Excused Absence']
    for line in lines:
        if not line.startswith(("INSERT INTO", "BEGIN", "COMMIT")):
            # Extract data using regex
            match = re.search(r"email = '(.+?)'.+?'(\d{4}-\d{2}-\d{2})', \(SELECT attendance_type_id FROM attendance_type WHERE attendance_type = '(.+?)'\)", line)
            if match:
                email, date_str, attendance_type = match.groups()
                date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                # Determine if the attendance_type is considered an absence
                absent = attendance_type in absence_types
                attendance_data.append(StudentAttendanceDay(email=email, date=date_obj, attendance_type=attendance_type, absent=absent))
    return attendance_data

def calculate_attendance_rate(attendance_data:List[StudentAttendanceDay]):
    student_days = defaultdict(lambda: {'total': 0, 'absences': 0})
    for record in attendance_data:
        student_days[record.email]['total'] += 1
        if record.absent:
            student_days[record.email]['absences'] += 1
    attendance_rates = {}
    for email, days in student_days.items():
        rate = ((days['total'] - days['absences']) / days['total']) * 100
        attendance_rates[email] = round(rate, 2)
    return attendance_rates

def main():
    student_csv_file_name = '../03_student/students.csv'
    daily_attendance_sql_inserts = '../04_dailyattendance/daily-attendance-insert.sql'
    attendance_data = parse_sql_file(daily_attendance_sql_inserts)
    attendance_rates = calculate_attendance_rate(attendance_data)
    pprint.pprint(attendance_rates)
    print(len(attendance_data))

if __name__ == "__main__":
    main()
