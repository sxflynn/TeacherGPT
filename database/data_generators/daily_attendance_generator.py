import csv
import random
from datetime import datetime, timedelta

# Define the CSV file name
csv_file_name = 'demo-student.csv'

# Define the SQL output file name
sql_file_name = 'daily-attendance-insert.sql'

# School year dates
start_date = datetime(2023, 9, 1)
end_date = datetime(2024, 5, 30)

# Function to generate all weekdays in the school year
def generate_school_days(start, end):
    day = start
    while day <= end:
        if day.weekday() < 5:  # Monday to Friday are weekdays
            yield day
        day += timedelta(days=1)

# Function to generate attendance data for a student
def generate_attendance_data(email, attendance_rates):
    sql_lines = []
    for day in generate_school_days(start_date, end_date):
        attendance_chance = random.random()
        day_str = day.strftime('%Y-%m-%d')

        if attendance_chance <= attendance_rates['full']:
            attendance_type = 'Full Attendance'
            arrival = 'NULL'
            departure = 'NULL'
        elif attendance_chance <= attendance_rates['partial']:
            attendance_type = random.choice(['Partial Excused Absence', 'Partial Unexcused Absence'])
            if random.random() < 0.5:
                arrival = f"'{day_str} {random.randint(9, 11)}:{str(random.randint(0, 59)).zfill(2)}:00-05:00'"
                departure = f"'{day_str} 15:00:00-05:00'"
            else:
                arrival = f"'{day_str} 08:00:00-05:00'"
                departure = f"'{day_str} {random.randint(12, 14)}:{str(random.randint(0, 59)).zfill(2)}:00-05:00'"
        else:
            attendance_type = random.choice(['Unexcused Absence', 'Excused Absence'])
            arrival = 'NULL'
            departure = 'NULL'

        sql_line = f"((SELECT student_id FROM student WHERE email = '{email}'), '{day_str}', (SELECT attendance_type_id FROM attendance_type WHERE attendance_type = '{attendance_type}'), {arrival}, {departure}, NULL)"
        sql_lines.append(sql_line)
    return sql_lines

# Define attendance rates
full_attendance_rate = 0.9  # 90% chance for full attendance
partial_attendance_rate = 0.95  # Additional 5% chance for partial attendance

# Read the CSV file and prepare the SQL insert statements
all_sql_lines = []
with open(csv_file_name, mode='r', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for row in csv_reader:
        email = row['email']
        # Randomly decide attendance rate for each student
        attendance_profile = random.random()
        if attendance_profile < 0.1:  # 10% students with 100% attendance
            attendance_rates = {'full': 1, 'partial': 1}
        elif attendance_profile < 0.8:  # 70% students with more than 85% attendance
            attendance_rates = {'full': full_attendance_rate, 'partial': partial_attendance_rate}
        else:  # Remaining 20% with varied attendance
            attendance_rates = {'full': random.uniform(0.5, 0.85), 'partial': partial_attendance_rate}

        attendance_data = generate_attendance_data(email, attendance_rates)
        all_sql_lines.extend(attendance_data)

# Write the SQL insert statements to the output file
with open(sql_file_name, mode='w', newline='') as sql_file:
    sql_file.write('INSERT INTO "daily_attendance" ("student_id", "date", "attendance_type", "arrival", "departure", "excuse_note") VALUES\n')
    sql_file.write(',\n'.join(all_sql_lines))
    sql_file.write(';\n')

print(f"SQL insert statements have been written to {sql_file_name}.")