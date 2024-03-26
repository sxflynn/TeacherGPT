import csv

# Define the CSV file name (assuming the CSV file is in the same directory as this script)
csv_file_name = 'students.csv'

# Define the SQL output file name
sql_file_name = 'grade-level-students-insert.sql'

sql_lines = []
with open(csv_file_name, mode='r', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for row in csv_reader:
        email = row['email']
        grade_level = row['grade_level']
        grade_name = f"{grade_level}th Grade"
        sql_line = f"((SELECT \"student_id\" FROM \"student\" WHERE \"email\" = '{email}'), (SELECT \"grade_level_id\" FROM \"grade_levels\" WHERE \"grade_level_name\" = '{grade_name}'))"
        sql_lines.append(sql_line)
        
# Write the SQL insert statements to the output file
with open(sql_file_name, mode='w', newline='') as sql_file:
    sql_file.write('INSERT INTO "student_grade_levels" ("student_id", "grade_level_id")\nVALUES\n')
    sql_file.write(',\n'.join(sql_lines))
    sql_file.write(';\n')