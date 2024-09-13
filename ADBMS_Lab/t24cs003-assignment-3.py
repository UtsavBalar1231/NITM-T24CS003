import sqlite3
import os

# Remove the database file if it exists
db_file = "db.sqlite"
if os.path.exists(db_file):
    os.remove(db_file)

# Connect to SQLite database
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE students (
    StudentID INTEGER PRIMARY KEY,
    Name TEXT,
    Email TEXT,
    Phone TEXT,
    Address TEXT
)
''')

cursor.execute('''
CREATE TABLE courses (
    CourseID INTEGER PRIMARY KEY,
    CourseName TEXT,
    Credits INTEGER
)
''')

cursor.execute('''
CREATE TABLE exams (
    ExamID INTEGER PRIMARY KEY,
    ExamDate TEXT,
    ExamTime TEXT,
    Location TEXT
)
''')

cursor.execute('''
CREATE TABLE faculty (
    FacultyID INTEGER PRIMARY KEY,
    Name TEXT,
    Email TEXT,
    Phone TEXT,
    Department TEXT
)
''')

cursor.execute('''
CREATE TABLE enrollment (
    EnrollmentID INTEGER PRIMARY KEY,
    StudentID INTEGER,
    CourseID INTEGER,
    EnrollmentDate TEXT,
    FOREIGN KEY (StudentID) REFERENCES students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES courses(CourseID)
)
''')

cursor.execute('''
CREATE TABLE teaching (
    TeachingID INTEGER PRIMARY KEY,
    FacultyID INTEGER,
    CourseID INTEGER,
    FOREIGN KEY (FacultyID) REFERENCES faculty(FacultyID),
    FOREIGN KEY (CourseID) REFERENCES courses(CourseID)
)
''')

cursor.execute('''
CREATE TABLE exam_registration (
    RegistrationID INTEGER PRIMARY KEY,
    StudentID INTEGER,
    ExamID INTEGER,
    RegistrationDate TEXT,
    FOREIGN KEY (StudentID) REFERENCES students(StudentID),
    FOREIGN KEY (ExamID) REFERENCES exams(ExamID)
)
''')

cursor.execute('''
CREATE TABLE exam_results (
    ResultID INTEGER PRIMARY KEY,
    StudentID INTEGER,
    ExamID INTEGER,
    Score REAL,
    FOREIGN KEY (StudentID) REFERENCES students(StudentID),
    FOREIGN KEY (ExamID) REFERENCES exams(ExamID)
)
''')

# Insert sample data
cursor.executemany('''
INSERT INTO students (StudentID, Name, Email, Phone, Address) VALUES (?, ?, ?, ?, ?)
''', [
    (1, "abcd", "abcd@test.com", "325870489", "Surat"),
    (2, "efgh", "efgh@test.com", "408320174", "Dehli"),
    (3, "Utsav Balar", "utsav@balar.com", "123456789", "Umpling"),
    (4, "lmno", "lmno@test.com", "985973232", "Vadodra"),
    (5, "pqrs", "pqrs@test.com", "325870489", "Assam"),
    (6, "tuvw", "tuvw@test.com", "483112984", "Tamil Nadu"),
    (7, "xyz", "xyz@test.com", "324982309", "Punjab"),
    (8, "ijkl", "ijkl@test.com", "918321473", "Mumbai"),
])

cursor.executemany('''
INSERT INTO courses (CourseID, CourseName, Credits) VALUES (?, ?, ?)
''', [
    (701, "Advanced Engineering Mathematics", 4),
    (501, "Advanced Algorithms and Complexity", 4),
    (503, "Advanced Database Systems", 4),
    (555, "Advanced Programming Lab", 4),
    (553, "Advanced Databases Systems Lab", 4),
    (511, "Digital Image processing", 4),
    (517, "Soft Computing Mathematics", 4),
])

cursor.executemany('''
INSERT INTO exams (ExamID, ExamDate, ExamTime, Location) VALUES (?, ?, ?, ?)
''', [
    (1, "2024-09-15", "10:00", "CR12"),
    (2, "2024-09-05", "10:00", "CR11"),
    (3, "2024-09-25", "10:00", "CR12"),
    (4, "2024-09-16", "10:00", "CR11"),
    (5, "2024-09-15", "10:00", "CR12"),
    (6, "2024-09-15", "10:00", "CR11"),
])

cursor.executemany('''
INSERT INTO faculty (FacultyID, Name, Email, Phone, Department) VALUES (?, ?, ?, ?, ?)
''', [
    (101, "Rizzvik Sharam", "rizz@sharma.com", "987654321", "Mathematics"),
    (102, "Rohil Khan", "rohil@khan.com", "947560821", "Computer Vision"),
    (103, "Runganko Dosa", "dosaruganko@mail.com", "6934738422", "Soft Computing"),
    (104, "Kumari Ashu", "ashukumari@mail.com", "5876094585", "Advanced Algorithms and Complexity"),
    (105, "Ustav blyat", "blyatutsav@mail.com", "9407658934", "Advanced Databases Systems"),
])

cursor.executemany('''
INSERT INTO enrollment (EnrollmentID, StudentID, CourseID, EnrollmentDate) VALUES (?, ?, ?, ?)
''', [
    (1, 1, 701, "2024-05-15"),
    (2, 2, 701, "2024-05-15"),
    (4, 3, 701, "2024-05-15"),
    (5, 4, 701, "2024-05-15"),
    (6, 5, 701, "2024-05-15"),
    (7, 6, 701, "2024-05-15"),
])

cursor.executemany('''
INSERT INTO teaching (TeachingID, FacultyID, CourseID) VALUES (?, ?, ?)
''', [
    (1, 101, 701),
    (2, 102, 511),
    (3, 103, 517),
    (4, 104, 501),
    (5, 105, 503),
    (6, 104, 555),
    (7, 104, 553),
])

cursor.executemany('''
INSERT INTO exam_registration (RegistrationID, StudentID, ExamID, RegistrationDate) VALUES (?, ?, ?, ?)
''', [
    (1, 1, 1, "2024-08-25"),
    (2, 2, 1, "2024-08-05"),
    (3, 3, 1, "2024-08-15"),
    (4, 4, 1, "2024-08-25"),
    (5, 5, 1, "2024-08-15"),
    (6, 6, 1, "2024-08-05"),
])

cursor.executemany('''
INSERT INTO exam_results (ResultID, StudentID, ExamID, Score) VALUES (?, ?, ?, ?)
''', [
    (1, 1, 1, 88.50),
    (2, 2, 1, 58.00),
    (3, 3, 1, 80.00),
    (4, 4, 1, 98.25),
    (5, 5, 1, 18.50),
    (6, 6, 1, 68.75),
])

# Commit the transactions
conn.commit()

# Querying data and printing results
def print_table(query, headers, column_formats):
    cursor.execute(query)
    rows = cursor.fetchall()
    print(" | ".join(headers))
    print("-" * len(" | ".join(headers)))
    for row in rows:
        print(" | ".join(f"{fmt.format(val)}" for fmt, val in zip(column_formats, row)))

print_table(
    'SELECT * FROM students',
    ['StudentID', 'Name', 'Email', 'Phone', 'Address'],
    ['{:10}', '{:<15}', '{:<25}', '{:<12}', '{:<15}']
)

print_table(
    'SELECT * FROM courses',
    ['CourseID', 'CourseName', 'Credits'],
    ['{:10}', '{:<35}', '{:<7}']
)

print_table(
    'SELECT * FROM exams',
    ['ExamID', 'ExamDate', 'ExamTime', 'Location'],
    ['{:10}', '{:<15}', '{:<10}', '{:<10}']
)

print_table(
    'SELECT * FROM faculty',
    ['FacultyID', 'Name', 'Email', 'Phone', 'Department'],
    ['{:10}', '{:<15}', '{:<25}', '{:<12}', '{:<35}']
)

print_table(
    'SELECT * FROM enrollment',
    ['EnrollmentID', 'StudentID', 'CourseID', 'EnrollmentDate'],
    ['{:15}', '{:10}', '{:10}', '{:<15}']
)

print_table(
    'SELECT * FROM teaching',
    ['TeachingID', 'FacultyID', 'CourseID'],
    ['{:10}', '{:10}', '{:<10}']
)

print_table(
    'SELECT * FROM exam_registration',
    ['RegistrationID', 'StudentID', 'ExamID', 'RegistrationDate'],
    ['{:15}', '{:10}', '{:10}', '{:<15}']

