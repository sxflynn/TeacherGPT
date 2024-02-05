import csv
import random
from datetime import datetime, timedelta

# Define the CSV file name (assuming the CSV file is in the same directory as this script)
csv_file_name = 'demo-student.csv'

# Define the SQL output file name
sql_file_name = 'enrollment-insert.sql'

# Define the enrollment start and end dates
main_start_date = '2024-08-23'
# Leave end_date as None since the student is still enrolled

# Function to generate a random weekday between two dates
def random_weekday(start_date, end_date):
    days_between = (end_date - start_date).days
    random_days = random.randrange(days_between)  # Pick a random number of days within the range
    random_date = start_date + timedelta(days=random_days)
    # Adjust if the random_date falls on a weekend
    while random_date.weekday() > 4:  # 0 is Monday, 6 is Sunday
        random_date += timedelta(days=1)
    return random_date

# Read the CSV file and prepare the SQL insert statements
sql_lines = []
with open(csv_file_name, mode='r', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for row in csv_reader:
        email = row['email']
        # 90% of the students get the main start date, 10% get a random weekday
        if random.random() < 0.9:
            start_date = main_start_date
        else:
            start_date = random_weekday(datetime(2023, 8, 23), datetime.now()).strftime('%Y-%m-%d')
        sql_line = f"((SELECT \"student_id\" FROM \"student\" WHERE \"email\" = '{email}'), '{start_date}', NULL)"
        sql_lines.append(sql_line)

# Write the SQL insert statements to the output file
with open(sql_file_name, mode='w', newline='') as sql_file:
    sql_file.write('INSERT INTO "school_enrollment" ("student_id", "first_day", "last_day")\nVALUES\n')
    sql_file.write(',\n'.join(sql_lines))
    sql_file.write(';\n')

print(f"SQL insert statements have been written to {sql_file_name}.")
