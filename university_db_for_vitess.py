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

# Dictionary to map branches to directions
branches = {
    'New Delhi': 'North',
    'Kolkata': 'East',
    'Mumbai': 'West',
    'Chandigarh': 'North',
    'Chennai': 'South'
}

# Insert realistic records into UniversityRecords table
for _ in range(2000000):
    name = faker.name()
    email = faker.email()
    department = random.choice(list(department_courses.keys()))
    course = random.choice(department_courses[department])
    branch_location = random.choice(list(branches.keys()))
    branch_direction = branches[branch_location]
    branch = f"{branch_direction} {branch_location}"
    grade = random.choice(['A', 'B', 'C', 'D', 'E'])

    cursor.execute("INSERT INTO UniversityRecords (name, email, department, branch, course, grade) VALUES (%s, %s, %s, %s, %s, %s)",
                   (name, email, department, branch, course, grade))

# Commit changes and close connection
conn.commit()
conn.close()

print("Data inserted successfully.")
