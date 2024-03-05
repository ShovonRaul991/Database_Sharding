import mysql.connector
from datetime import datetime, timedelta
from faker import Faker

# Create Faker object for Indian data
fake = Faker('en_IN')

# Function to generate unique student ID
def generate_student_id(branch, admission_year, course_id, course_count):
    return f"{branch}{admission_year}{course_id}{course_count:04}"

# Function to calculate passout year
def calculate_passout_year(admission_year):
    return admission_year + 4

# Dictionary mapping courses to relevant subjects

course_subject_mapping = {
    "CSE": ["Data Structures", "Algorithms", "Database Systems", "Operating Systems", "Computer Networks"],
    "MEC": ["Mechanics", "Thermodynamics", "Material Science", "Fluid Mechanics", "Machine Design"],
    "ECE": ["Digital Electronics", "Signals and Systems", "Communication Systems", "Microprocessors", "Control Systems"],
    "EEE": ["Circuit Theory", "Electrical Machines", "Power Systems", "Renewable Energy", "Instrumentation"],
    "CIV": ["Structural Analysis", "Geotechnical Engineering", "Transportation Engineering", "Environmental Engineering", "Construction Management"],
    "CHE": ["Chemical Kinetics", "Thermodynamics", "Mass Transfer", "Process Control", "Biochemical Engineering"],
    "AER": ["Aerodynamics", "Aircraft Structures", "Propulsion", "Flight Dynamics", "Avionics"],
    "MBA": ["Marketing Management", "Financial Management", "Human Resource Management", "Operations Management", "Strategic Management"],
    "BBA": ["Business Communication", "Organizational Behavior", "Marketing Fundamentals", "Financial Accounting", "Operations Management"],
    "LAW": ["Constitutional Law", "Criminal Law", "Contract Law", "Property Law", "Corporate Law"],
    "ARC": ["Architectural Design", "Building Construction", "Architectural Theory", "History of Architecture", "Urban Planning"],
    "PHY": ["Classical Mechanics", "Quantum Mechanics", "Electromagnetism", "Thermodynamics and Statistical Mechanics", "Solid State Physics"],
    "MAT": ["Calculus", "Linear Algebra", "Differential Equations", "Probability and Statistics", "Discrete Mathematics"],
    "BIO": ["Cell Biology", "Genetics", "Ecology", "Evolutionary Biology", "Microbiology"],
    "CHM": ["General Chemistry", "Organic Chemistry", "Inorganic Chemistry", "Physical Chemistry", "Analytical Chemistry"],
    "MED": ["Anatomy", "Physiology", "Pathology", "Pharmacology", "Microbiology"],
    "PHI": ["Ethics", "Logic", "Metaphysics", "Epistemology", "Political Philosophy"],
    "PSY": ["Cognitive Psychology", "Social Psychology", "Developmental Psychology", "Abnormal Psychology", "Industrial-Organizational Psychology"],
    "EDU": ["Educational Psychology", "Curriculum Development", "Teaching Methods", "Educational Technology", "Special Education"],
    "ECO": ["Microeconomics", "Macroeconomics", "International Economics", "Development Economics", "Econometrics"],
    "ENG": ["English Literature", "Creative Writing", "Linguistics", "World Literature", "American Literature"],
    "HIS": ["Ancient History", "Medieval History", "Modern History", "European History", "World History"],
    "GEO": ["Physical Geography", "Human Geography", "Geographic Information Systems", "Environmental Geography", "Remote Sensing"],
    "CSA": ["Computer Science and Applications", "Data Structures", "Algorithms", "Database Management Systems", "Operating Systems", "Web Development"],
    "ECO": ["Economics", "Microeconomics", "Macroeconomics", "International Economics", "Development Economics"],
    "HOT": ["Hotel Management", "Hospitality Management", "Food and Beverage Management", "Front Office Operations", "Housekeeping Operations"],
    "ENV": ["Environmental Science", "Ecology", "Environmental Management", "Climate Change", "Sustainable Development"],
    "FAS": ["Fine Arts", "Painting", "Sculpture", "Drawing", "Art History"],
    "COM": ["Commerce", "Accounting", "Finance", "Business Law", "Marketing"],
    "MUS": ["Music", "Music Theory", "Music History", "Music Composition", "Music Performance"],
    "PHO": ["Photography", "Digital Photography", "Portrait Photography", "Landscape Photography", "Photojournalism"],
    "THG": ["Theater and Performing Arts", "Acting", "Dance", "Directing", "Stagecraft"],
    "LIT": ["Literature", "English Literature", "American Literature", "World Literature", "Literary Theory"],
    "MKT": ["Marketing", "Market Research", "Consumer Behavior", "Advertising", "Brand Management"],
    "NRS": ["Nursing", "Anatomy", "Physiology", "Pharmacology", "Nursing Ethics"],
    "PHY": ["Physiotherapy", "Anatomy", "Physiology", "Kinesiology", "Rehabilitation Techniques"],
    "PTM": ["Physical Education", "Sports Science", "Exercise Physiology", "Sports Psychology", "Coaching and Leadership"],
    "POL": ["Political Science", "Comparative Politics", "International Relations", "Political Theory", "Public Administration"],
    "FIL": ["Film Studies", "Film History", "Cinematography", "Film Theory", "Film Production"],
    "AST": ["Astrology", "Natal Astrology", "Horoscopic Astrology", "Vedic Astrology", "Astrological Counseling"],
    "CHE": ["Chef Training", "Culinary Arts", "Baking and Pastry", "Gastronomy", "Food Safety and Sanitation"],
    "CUL": ["Culinary Arts", "Cooking Techniques", "Menu Planning", "Food Presentation", "Food Service Management"],
    "GRA": ["Graphic Design", "Typography", "Logo Design", "Illustration", "Web Design"],
    "JOU": ["Journalism", "News Writing", "Investigative Journalism", "Broadcast Journalism", "Digital Journalism"],
    "VIS": ["Visual Arts", "Drawing", "Painting", "Sculpture", "Printmaking"]
}


# Dictionary mapping course IDs to course names
course_id_mapping = {
    "CSE": "Computer Science and Engineering",
    "MEC": "Mechanical Engineering",
    "ECE": "Electronics and Communication Engineering",
    "EEE": "Electrical and Electronics Engineering",
    "CIV": "Civil Engineering",
    "CHE": "Chemical Engineering",
    "AER": "Aeronautical Engineering",
    "MBA": "Master of Business Administration",
    "BBA": "Bachelor of Business Administration",
    "LAW": "Bachelor of Laws",
    "ARC": "Architecture",
    "PHY": "Physics",
    "MAT": "Mathematics",
    "BIO": "Biology",
    "CHM": "Chemistry",
    "MED": "Medicine",
    "PHI": "Philosophy",
    "PSY": "Psychology",
    "EDU": "Education",
    "ECO": "Economics",
    "ENG": "English",
    "HIS": "History",
    "GEO": "Geography",
    "CSA": "Computer Science and Applications",
    "ECO": "E-Commerce",
    "HOT": "Hotel Management",
    "ENV": "Environmental Science",
    "FAS": "Fine Arts",
    "COM": "Commerce",
    "MUS": "Music",
    "PHO": "Photography",
    "THG": "Theater and Performing Arts",
    "LIT": "Literature",
    "MKT": "Marketing",
    "NRS": "Nursing",
    "PHY": "Physiotherapy",
    "PTM": "Physical Education",
    "POL": "Political Science",
    "FIL": "Film Studies",
    "AST": "Astrology",
    "CHE": "Chef Training",
    "CUL": "Culinary Arts",
    "GRA": "Graphic Design",
    "JOU": "Journalism",
    "VIS": "Visual Arts"
}

# List of university branches
university_branches = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# List of relevant course IDs
relevant_course_ids = list(course_id_mapping.keys())[:25]

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="404@Db#",
    database="SR_University"
)

cursor = conn.cursor()

# Set to store generated student IDs
generated_ids = set()

# Insert 3,000,000 records into the Students table
record_count = 0
while record_count < 3000000:
    branch = fake.random_element(university_branches)
    admission_year = fake.random_int(min=2001, max=2023)
    course_id = fake.random_element(relevant_course_ids)
    course_count = record_count + 1
    while True:
        student_id = generate_student_id(branch, admission_year, course_id, course_count)
        if student_id not in generated_ids:
            generated_ids.add(student_id)
            break
    date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=20)
    passout_year = calculate_passout_year(admission_year)
    family_income = fake.random_int(min=50000, max=1000000)
    course_name = course_id_mapping[course_id]
    subject_name = fake.random_element(course_subject_mapping[course_id])

    # Generate fake data
    student_name = fake.name()
    email = fake.email()
    phone_number = fake.phone_number()
    father_name = fake.name()
    mother_name = fake.name()
    student_address = fake.address()

    # Insert record into the database
    insert_query = "INSERT INTO Students (StudentID, StudentName, Email, PhoneNumber, DateOfBirth, FatherName, MotherName, FamilyIncome, StudentAddress, CourseName, SubjectName, PassoutYear, UniversityBranchName) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (student_id, student_name, email, phone_number, date_of_birth, father_name, mother_name, family_income, student_address, course_name, subject_name, passout_year, branch)
    cursor.execute(insert_query, values)

    record_count += 1

# Commit the transaction and close the connection
conn.commit()
conn.close()
