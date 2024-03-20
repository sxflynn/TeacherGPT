import random
import csv
from faker import Faker

# Utility to read student data from a CSV file
def read_student_data(file_name):
    students = []
    with open(file_name, mode='r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            students.append(row)
    return students

# Generates a unique email address
def generate_unique_email(first_name, last_name):
    domain = random.choice(["@gmail.com", "@outlook.com", "@icloud.com"])
    return f"{first_name.lower()}.{last_name.lower()}{random.randint(1,999)}{domain}"

# Generates family members for a given student
def generate_family_members(student, fake):
    family_members = []
    family_groups = []
    student_email = student["email"]
    student_id_insert = f"(SELECT student_id FROM student WHERE email = '{student_email}')"

    if random.random() <= 0.7:  # Adding parents with a probability
        father_info, father_email = generate_parent(fake, student["last_name"], gender="male")
        mother_info, mother_email = generate_parent(fake, student["last_name"], gender="female", is_father=False)
        family_members.extend([father_info, mother_info])
        family_groups.extend([
            generate_family_group_insert(student_id_insert, father_email),
            generate_family_group_insert(student_id_insert, mother_email)
        ])
    else:  # Adding a single parent
        parent_info, parent_email = generate_parent(fake, student["last_name"])
        family_members.append(parent_info)
        family_groups.append(generate_family_group_insert(student_id_insert, parent_email))

    return family_members, family_groups

# Helper to generate a parent's information
def generate_parent(fake, last_name, gender="female", is_father=True):
    first_name = fake.first_name_female() if gender == "female" else fake.first_name_male()
    middle_name = fake.first_name_female() if gender == "female" else fake.first_name_male()
    last_name = last_name if is_father or random.random() <= 0.8 else fake.last_name_female()
    email = generate_unique_email(first_name, last_name)
    phone_number = fake.basic_phone_number()
    # Return the insert value string for the family member and their email for ID lookup
    return (f"('{first_name}', '{middle_name}', '{last_name}', '{email}', '{phone_number}')", email)

# Adjusted to use parent email for ID lookup
def generate_family_group_insert(student_id_insert, parent_email):
    # Sub-select to find the parent ID based on email
    parent_id_insert = f"(SELECT family_member_id FROM family_member WHERE email = '{parent_email}')"
    return f"({student_id_insert}, {parent_id_insert}, TRUE, TRUE, 1)"

# Main logic to orchestrate the generation of SQL statements
def main():
    fake = Faker('en_US')
    students = read_student_data('demo-student.csv')
    family_member_inserts = []
    family_group_inserts = []

    for student in students:
        members, groups = generate_family_members(student, fake)
        family_member_inserts.extend(members)
        family_group_inserts.extend(groups)

    family_member_sql = generate_insert_statement("family_member", ["first_name", "middle_name", "last_name", "email", "phone_number"], family_member_inserts)
    family_group_sql = generate_insert_statement("family_group", ["student_id", "family_member_id", "parent_guardian", "emergency_pickup", "relationship_type_id"], family_group_inserts)
    
    # Additional INSERT statement for the relationship_type table
    relationship_type_sql = 'INSERT INTO "relationship_type" ("relationship_type_id", "relationship_type") VALUES (1, \'Parent/guardian\');\n\n'
    
    # Combine the additional statement with the final SQL
    final_sql = relationship_type_sql + family_member_sql + family_group_sql
    
    # Define the output file name
    sql_file_name = 'family-insert.sql'
    
    # Write the SQL insert statements to the output file
    with open(sql_file_name, mode='w', newline='') as sql_file:
        sql_file.write(final_sql)
    
    print(f"SQL insert statements have been written to {sql_file_name}.")
    
# Helper to generate an INSERT SQL statement
def generate_insert_statement(table_name, columns, values):
    columns_formatted = ', '.join([f'"{column}"' for column in columns])
    values_formatted = ',\n'.join(values)
    return f'INSERT INTO "{table_name}" ({columns_formatted})\nVALUES\n{values_formatted};\n\n'

if __name__ == "__main__":
    main()
