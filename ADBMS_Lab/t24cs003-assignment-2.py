from tinydb import TinyDB, Query
import os

if os.path.exists("db.json"):
    os.remove("db.json")

db = TinyDB("db.json")

# Tables
students_table = db.table("students")
courses_table = db.table("courses")
exam_table = db.table("exams")
faculty_table = db.table("faculty")
enrollment_table = db.table("enrollment")
teaching_table = db.table("teaching")
exam_registration_table = db.table("exam_registration")
exam_results_table = db.table("exam_results")

# Inserting sample data
students_table.insert_multiple(
    [
        {
            "StudentID": 1,
            "Name": "abcd",
            "Email": "abcd@test.com",
            "Phone": "325870489",
            "Address": "Surat",
        },
        {
            "StudentID": 2,
            "Name": "efgh",
            "Email": "efgh@test.com",
            "Phone": "408320174",
            "Address": "Dehli",
        },
        {
            "StudentID": 3,
            "Name": "Utsav Balar",
            "Email": "utsav@balar.com",
            "Phone": "123456789",
            "Address": "Umpling",
        },
        {
            "StudentID": 4,
            "Name": "lmno",
            "Email": "lmno@test.com",
            "Phone": "985973232",
            "Address": "Vadodra",
        },
        {
            "StudentID": 5,
            "Name": "pqrs",
            "Email": "pqrs@test.com",
            "Phone": "325870489",
            "Address": "Assam",
        },
        {
            "StudentID": 6,
            "Name": "tuvw",
            "Email": "tuvw@test.com",
            "Phone": "483112984",
            "Address": "Tamil Nadu",
        },
        {
            "StudentID": 7,
            "Name": "xyz",
            "Email": "xyz@test.com",
            "Phone": "324982309",
            "Address": "Punjab",
        },
        {
            "StudentID": 8,
            "Name": "ijkl",
            "Email": "ijkl@test.com",
            "Phone": "918321473",
            "Address": "Mumbai",
        },
    ]
)

courses_table.insert_multiple(
    [
        {
            "CourseID": 701,
            "CourseName": "Advanced Engineering Mathematics",
            "Credits": 4,
        },
        {
            "CourseID": 501,
            "CourseName": "Advanced Algorithms and Complexity",
            "Credits": 4,
        },
        {"CourseID": 503, "CourseName": "Advanced Database Systems", "Credits": 4},
        {"CourseID": 555, "CourseName": "Advanced Programming Lab", "Credits": 4},
        {"CourseID": 553, "CourseName": "Advanced Databases Systems Lab", "Credits": 4},
        {"CourseID": 511, "CourseName": "Digital Image processing", "Credits": 4},
        {"CourseID": 517, "CourseName": "Soft Computing Mathematics", "Credits": 4},
    ]
)

exam_table.insert_multiple(
    [
        {
            "ExamID": 1,
            "ExamDate": "2024-09-15",
            "ExamTime": "10:00",
            "Location": "CR12",
        },
        {
            "ExamID": 2,
            "ExamDate": "2024-09-05",
            "ExamTime": "10:00",
            "Location": "CR11",
        },
        {
            "ExamID": 3,
            "ExamDate": "2024-09-25",
            "ExamTime": "10:00",
            "Location": "CR12",
        },
        {
            "ExamID": 4,
            "ExamDate": "2024-09-16",
            "ExamTime": "10:00",
            "Location": "CR11",
        },
        {
            "ExamID": 5,
            "ExamDate": "2024-09-15",
            "ExamTime": "10:00",
            "Location": "CR12",
        },
        {
            "ExamID": 6,
            "ExamDate": "2024-09-15",
            "ExamTime": "10:00",
            "Location": "CR11",
        },
    ]
)

faculty_table.insert_multiple(
    [
        {
            "FacultyID": 101,
            "Name": "Rizzvik Sharam",
            "Email": "rizz@sharma.com",
            "Phone": "987654321",
            "Department": "Mathematics",
        },
        {
            "FacultyID": 102,
            "Name": "Rohil Khan",
            "Email": "rohil@khan.com",
            "Phone": "947560821",
            "Department": "Computer Vision",
        },
        {
            "FacultyID": 103,
            "Name": "Runganko Dosa",
            "Email": "dosaruganko@mail.com",
            "Phone": "6934738422",
            "Department": "Soft Computing",
        },
        {
            "FacultyID": 104,
            "Name": "Kumari Ashu",
            "Email": "ashukumari@mail.com",
            "Phone": "5876094585",
            "Department": "Advanced Algorithms and Complexity",
        },
        {
            "FacultyID": 105,
            "Name": "Ustav blyat",
            "Email": "blyatutsav@mail.com",
            "Phone": "9407658934",
            "Department": "Advanced Databases Systems",
        },
    ]
)

enrollment_table.insert_multiple(
    [
        {
            "EnrollmentID": 1,
            "StudentID": 1,
            "CourseID": 701,
            "EnrollmentDate": "2024-05-15",
        },
        {
            "EnrollmentID": 2,
            "StudentID": 2,
            "CourseID": 701,
            "EnrollmentDate": "2024-05-15",
        },
        {
            "EnrollmentID": 4,
            "StudentID": 3,
            "CourseID": 701,
            "EnrollmentDate": "2024-05-15",
        },
        {
            "EnrollmentID": 5,
            "StudentID": 4,
            "CourseID": 701,
            "EnrollmentDate": "2024-05-15",
        },
        {
            "EnrollmentID": 6,
            "StudentID": 5,
            "CourseID": 701,
            "EnrollmentDate": "2024-05-15",
        },
        {
            "EnrollmentID": 7,
            "StudentID": 6,
            "CourseID": 701,
            "EnrollmentDate": "2024-05-15",
        },
    ]
)

teaching_table.insert_multiple(
    [
        {"TeachingID": 1, "FacultyID": 101, "CourseID": 701},
        {"TeachingID": 2, "FacultyID": 102, "CourseID": 511},
        {"TeachingID": 3, "FacultyID": 103, "CourseID": 517},
        {"TeachingID": 4, "FacultyID": 104, "CourseID": 501},
        {"TeachingID": 5, "FacultyID": 105, "CourseID": 503},
        {"TeachingID": 6, "FacultyID": 104, "CourseID": 555},
        {"TeachingID": 7, "FacultyID": 104, "CourseID": 553},
    ]
)

exam_registration_table.insert_multiple(
    [
        { "RegistrationID": 1, "StudentID": 1, "ExamID": 1, "RegistrationDate": "2024-08-25", },
        { "RegistrationID": 2, "StudentID": 2, "ExamID": 1, "RegistrationDate": "2024-08-05", },
        { "RegistrationID": 3, "StudentID": 3, "ExamID": 1, "RegistrationDate": "2024-08-15", },
        { "RegistrationID": 4, "StudentID": 4, "ExamID": 1, "RegistrationDate": "2024-08-25", },
        { "RegistrationID": 5, "StudentID": 5, "ExamID": 1, "RegistrationDate": "2024-08-15", },
        { "RegistrationID": 6, "StudentID": 6, "ExamID": 1, "RegistrationDate": "2024-08-05", },
    ]
)

exam_results_table.insert_multiple([
    {"ResultID": 1, "StudentID": 1, "ExamID": 1, "Score": 88.50},
    {"ResultID": 2, "StudentID": 2, "ExamID": 1, "Score": 58.00},
    {"ResultID": 3, "StudentID": 3, "ExamID": 1, "Score": 80.00},
    {"ResultID": 4, "StudentID": 4, "ExamID": 1, "Score": 98.25},
    {"ResultID": 5, "StudentID": 5, "ExamID": 1, "Score": 18.50},
    {"ResultID": 6, "StudentID": 6, "ExamID": 1, "Score": 68.75},
    ])

# Querying data
Student = Query()
students = students_table.all()

# Adjusting column widths for better alignment
print("\n\n\tStudents Table\n")
print(f"{'StudentID':<10} | {'Name':<15} | {'Email':<25} | {'Phone':<12} | {'Address'}")
print("-" * 70)
for student in students:
    print(
        f"{student['StudentID']:<10} | {student['Name']:<15} | {student['Email']:<25} | {student['Phone']:<12} | {student['Address']}"
    )

Course = Query()
courses = courses_table.all()

print("\n\n\tCourses Table")
print(f"\n{'CourseID':<10} | {'CourseName':<35} | {'Credits':<7}")
print("-" * 60)
for course in courses:
    print(
        f"{course['CourseID']:<10} | {course['CourseName']:<35} | {course['Credits']}"
    )

Exam = Query()
exams = exam_table.all()

print("\n\n\tExams Table")
print(f"\n{'ExamID':<10} | {'ExamDate':<15} | {'ExamTime':<10} | {'Location'}")
print("-" * 50)
for exam in exams:
    print(
        f"{exam['ExamID']:<10} | {exam['ExamDate']:<15} | {exam['ExamTime']:<10} | {exam['Location']}"
    )

Faculty = Query()
faculties = faculty_table.all()

print("\n\n\tFaculty Table")
print(
    f"\n{'FacultyID':<10} | {'Name':<15} | {'Email':<25} | {'Phone':<12} | {'Department'}"
)
print("-" * 70)
for faculty in faculties:
    print(
        f"{faculty['FacultyID']:<10} | {faculty['Name']:<15} | {faculty['Email']:<25} | {faculty['Phone']:<12} | {faculty['Department']}"
    )

Enrollment = Query()
enrollements = enrollment_table.all()

print("\n\n\tEnrollement Table")
print(
    f"\n{'EnrollmentID':<15} | {'StudentID':<10} | {'CourseID':<10} | {'EnrollmentDate'}"
)
print("-" * 60)
for enrollment in enrollements:
    print(
        f"{enrollment['EnrollmentID']:<15} | {enrollment['StudentID']:<10} | {enrollment['CourseID']:<10} | {enrollment['EnrollmentDate']}"
    )

Teaching = Query()
teachers = teaching_table.all()

print("\n\n\tTeachers Table")
print(f"\n{'TeachingID':<10} | {'FacultyID':<10} | {'CourseID'}")
print("-" * 40)
for teacher in teachers:
    print(
        f"{teacher['TeachingID']:<10} | {teacher['FacultyID']:<10} | {teacher['CourseID']}"
    )

Exam_registration = Query()
registrations = exam_registration_table.all()

print("\n\n\tRegistration Table")
print(
    f"\n{'RegistrationID':<15} | {'StudentID':<10} | {'ExamID':<10} | {'RegistrationDate'}"
)
print("-" * 60)
for registration in registrations:
    print(
        f"{registration['RegistrationID']:<15} | {registration['StudentID']:<10} | {registration['ExamID']:<10} | {registration['RegistrationDate']}"
    )

Exam_results = Query()
results = exam_results_table.all()

print("\n\n\tResults Table")
print(f"\n{'ResultID':<10} | {'StudentID':<10} | {'ExamID':<10} | {'Score'}")
print("-" * 50)
for result in results:
    print(
        f"{result['ResultID']:<10} | {result['StudentID']:<10} | {result['ExamID']:<10} | {result['Score']}"
    )
