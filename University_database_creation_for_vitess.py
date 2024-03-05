from faker import Faker
import random
import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="404@Db#",
    database="university_db"
)
cursor = conn.cursor()

# Instantiate Faker object
faker = Faker('en_IN')  # Set locale to generate Indian regional data

# Insert realistic records into Departments table
departments = ['Computer Science', 'Electrical Engineering', 'Mechanical Engineering', 'Civil Engineering', 'Chemical Engineering', 'Biotechnology', 'Physics', 'Chemistry', 'Mathematics', 'Economics']
for department in departments:
    cursor.execute("INSERT INTO Departments (name) VALUES (%s)", (department,))

# Insert realistic records into Branches table
branches = [('Main Campus', 'New Delhi'), ('East Campus', 'Kolkata'), ('West Campus', 'Mumbai'), ('North Campus', 'Chandigarh'), ('South Campus', 'Chennai')]
for branch in branches:
    cursor.execute("INSERT INTO Branches (name, location) VALUES (%s, %s)", branch)

# Dictionary to map departments to corresponding courses
department_courses = {
    'Computer Science': ['Data Structures', 'Algorithms', 'Database Systems', 'Computer Networks', 'Software Engineering'],
    'Electrical Engineering': ['Circuit Theory', 'Electromagnetic Fields', 'Power Systems', 'Control Systems', 'Digital Signal Processing'],
    'Mechanical Engineering': ['Thermodynamics', 'Fluid Mechanics', 'Mechanics of Materials', 'Manufacturing Processes', 'Automobile Engineering'],
    'Civil Engineering': ['Structural Analysis', 'Geotechnical Engineering', 'Transportation Engineering', 'Environmental Engineering', 'Construction Management'],
    'Chemical Engineering': ['Chemical Reaction Engineering', 'Mass Transfer Operations', 'Heat Transfer Operations', 'Process Dynamics and Control', 'Chemical Process Design'],
    'Biotechnology': ['Bioprocess Engineering', 'Molecular Biology', 'Genetic Engineering', 'Bioinformatics', 'Biomedical Engineering'],
    'Physics': ['Classical Mechanics', 'Quantum Mechanics', 'Electromagnetism', 'Statistical Mechanics', 'Astrophysics'],
    'Chemistry': ['Inorganic Chemistry', 'Organic Chemistry', 'Physical Chemistry', 'Analytical Chemistry', 'Biochemistry'],
    'Mathematics': ['Calculus', 'Linear Algebra', 'Differential Equations', 'Probability Theory', 'Numerical Methods'],
    'Economics': ['Microeconomics', 'Macroeconomics', 'International Economics', 'Econometrics', 'Development Economics']
}

# Insert realistic records into Courses table with proper integration with Departments
for department, courses in department_courses.items():
    department_id = departments.index(department) + 1
    for course_title in courses:
        branch_id = random.randint(1, 5)  # Assuming 5 branches
        cursor.execute("INSERT INTO Courses (title, department_id, branch_id) VALUES (%s, %s, %s)", (course_title, department_id, branch_id))

# Insert realistic records into Students table
for _ in range(2000000):
    name = faker.name()
    email = faker.email()
    department_id = random.randint(1, 10)  # Assuming 10 departments
    branch_id = random.randint(1, 5)  # Assuming 5 branches
    cursor.execute("INSERT INTO Students (name, email, department_id, branch_id) VALUES (%s, %s, %s, %s)", (name, email, department_id, branch_id))

# Insert realistic records into Enrollments table
for _ in range(2000000):
    student_id = random.randint(1, 2000000)
    course_id = random.randint(1, 2000000)
    grade = random.choice(['A', 'B', 'C', 'D', 'E'])
    branch_id = random.randint(1, 5)  # Assuming 5 branches
    cursor.execute("INSERT INTO Enrollments (student_id, course_id, grade, branch_id) VALUES (%s, %s, %s, %s)", (student_id, course_id, grade, branch_id))

# Commit changes and close connection
conn.commit()
conn.close()
