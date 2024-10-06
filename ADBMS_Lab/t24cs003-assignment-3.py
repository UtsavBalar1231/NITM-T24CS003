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
            "Name": "John Doe",
            "Email": "john.doe@example.com",
            "Phone": "123-456-7890",
            "Address": "123 Main St",
        },
        {
            "StudentID": 2,
            "Name": "Jane Smith",
            "Email": "jane.smith@example.com",
            "Phone": "987-654-3210",
            "Address": "456 Elm St",
        },
        {
            "StudentID": 3,
            "Name": "Robert Johnson",
            "Email": "robert.j@example.com",
            "Phone": "555-123-4567",
            "Address": "789 Oak Ave",
        },
        {
            "StudentID": 4,
            "Name": "Emily White",
            "Email": "emily.white@example.com",
            "Phone": "111-222-3333",
            "Address": "567 Pine St",
        },
        {
            "StudentID": 5,
            "Name": "Michael Lee",
            "Email": "michael.lee@example.com",
            "Phone": "333-444-5555",
            "Address": "789 Cedar Dr",
        },
        {
            "StudentID": 6,
            "Name": "Sarah Brown",
            "Email": "sarah.brown@example.com",
            "Phone": "555-666-7777",
            "Address": "890 Willow Ln",
        },
        {
            "StudentID": 7,
            "Name": "David Clark",
            "Email": "david.clark@example.com",
            "Phone": "777-888-9999",
            "Address": "123 Birch Ave",
        },
        {
            "StudentID": 8,
            "Name": "Melissa Turner",
            "Email": "melissa.turner@example.com",
            "Phone": "888-999-0000",
            "Address": "456 Redwood Rd",
        },
    ]
)

courses_table.insert_multiple(
    [
        {"CourseID": 101, "CourseName": "Mathematics", "Credits": 3},
        {"CourseID": 102, "CourseName": "History", "Credits": 4},
        {"CourseID": 103, "CourseName": "Computer Science", "Credits": 3},
        {"CourseID": 104, "CourseName": "Literature", "Credits": 3},
        {"CourseID": 105, "CourseName": "Chemistry", "Credits": 4},
        {"CourseID": 106, "CourseName": "Physics", "Credits": 4},
        {"CourseID": 107, "CourseName": "Economics", "Credits": 3},
        {"CourseID": 108, "CourseName": "Biology", "Credits": 4},
    ]
)

exam_table.insert_multiple(
    [
        {
            "ExamID": 201,
            "ExamDate": "2023-11-10",
            "ExamTime": "09:00 AM",
            "Location": "Exam Hall A",
        },
        {
            "ExamID": 202,
            "ExamDate": "2023-11-12",
            "ExamTime": "02:00 PM",
            "Location": "Exam Hall B",
        },
        {
            "ExamID": 203,
            "ExamDate": "2023-11-15",
            "ExamTime": "10:30 AM",
            "Location": "Exam Hall C",
        },
        {
            "ExamID": 204,
            "ExamDate": "2023-11-18",
            "ExamTime": "03:15 PM",
            "Location": "Exam Hall D",
        },
        {
            "ExamID": 205,
            "ExamDate": "2023-11-20",
            "ExamTime": "01:00 PM",
            "Location": "Exam Hall E",
        },
    ]
)

faculty_table.insert_multiple(
    [
        {
            "FacultyID": 301,
            "Name": "Dr. Smith",
            "Email": "smith@example.com",
            "Phone": "111-222-3333",
            "Department": "Mathematics",
        },
        {
            "FacultyID": 302,
            "Name": "Prof. Johnson",
            "Email": "johnson@example.com",
            "Phone": "444-555-6666",
            "Department": "History",
        },
        {
            "FacultyID": 303,
            "Name": "Prof. Brown",
            "Email": "brown@example.com",
            "Phone": "777-888-9999",
            "Department": "Computer Science",
        },
        {
            "FacultyID": 304,
            "Name": "Dr. Parker",
            "Email": "parker@example.com",
            "Phone": "888-777-6666",
            "Department": "Chemistry",
        },
        {
            "FacultyID": 305,
            "Name": "Prof. Adams",
            "Email": "adams@example.com",
            "Phone": "999-888-7777",
            "Department": "Physics",
        },
        {
            "FacultyID": 306,
            "Name": "Dr. Wilson",
            "Email": "wilson@example.com",
            "Phone": "555-444-3333",
            "Department": "Economics",
        },
        {
            "FacultyID": 307,
            "Name": "Prof. Davis",
            "Email": "davis@example.com",
            "Phone": "333-222-1111",
            "Department": "Biology",
        },
        {
            "FacultyID": 308,
            "Name": "Dr. Turner",
            "Email": "turner@example.com",
            "Phone": "222-333-4444",
            "Department": "Literature",
        },
    ]
)

enrollment_table.insert_multiple(
    [
        {
            "EnrollmentID": 1,
            "StudentID": 1,
            "CourseID": 101,
            "EnrollmentDate": "2023-09-01",
        },
        {
            "EnrollmentID": 2,
            "StudentID": 1,
            "CourseID": 102,
            "EnrollmentDate": "2023-09-01",
        },
        {
            "EnrollmentID": 3,
            "StudentID": 2,
            "CourseID": 101,
            "EnrollmentDate": "2023-09-02",
        },
        {
            "EnrollmentID": 4,
            "StudentID": 3,
            "CourseID": 103,
            "EnrollmentDate": "2023-09-03",
        },
        {
            "EnrollmentID": 5,
            "StudentID": 4,
            "CourseID": 104,
            "EnrollmentDate": "2023-09-04",
        },
        {
            "EnrollmentID": 6,
            "StudentID": 5,
            "CourseID": 105,
            "EnrollmentDate": "2023-09-05",
        },
        {
            "EnrollmentID": 7,
            "StudentID": 6,
            "CourseID": 106,
            "EnrollmentDate": "2023-09-06",
        },
        {
            "EnrollmentID": 8,
            "StudentID": 7,
            "CourseID": 107,
            "EnrollmentDate": "2023-09-07",
        },
        {
            "EnrollmentID": 9,
            "StudentID": 8,
            "CourseID": 108,
            "EnrollmentDate": "2023-09-08",
        },
    ]
)

teaching_table.insert_multiple(
    [
        {"TeachingID": 1, "FacultyID": 301, "CourseID": 101},
        {"TeachingID": 2, "FacultyID": 302, "CourseID": 102},
        {"TeachingID": 3, "FacultyID": 303, "CourseID": 103},
        {"TeachingID": 4, "FacultyID": 304, "CourseID": 104},
        {"TeachingID": 5, "FacultyID": 305, "CourseID": 105},
        {"TeachingID": 6, "FacultyID": 306, "CourseID": 106},
        {"TeachingID": 7, "FacultyID": 307, "CourseID": 107},
        {"TeachingID": 8, "FacultyID": 308, "CourseID": 108},
    ]
)

exam_registration_table.insert_multiple(
    [
        {
            "RegistrationID": 101,
            "StudentID": 1,
            "ExamID": 201,
            "RegistrationDate": "2023-10-15",
        },
        {
            "RegistrationID": 102,
            "StudentID": 2,
            "ExamID": 201,
            "RegistrationDate": "2023-10-16",
        },
        {
            "RegistrationID": 103,
            "StudentID": 3,
            "ExamID": 202,
            "RegistrationDate": "2023-10-17",
        },
        {
            "RegistrationID": 104,
            "StudentID": 4,
            "ExamID": 203,
            "RegistrationDate": "2023-10-18",
        },
        {
            "RegistrationID": 105,
            "StudentID": 5,
            "ExamID": 204,
            "RegistrationDate": "2023-10-19",
        },
        {
            "RegistrationID": 106,
            "StudentID": 6,
            "ExamID": 205,
            "RegistrationDate": "2023-10-20",
        },
        {
            "RegistrationID": 107,
            "StudentID": 7,
            "ExamID": 201,
            "RegistrationDate": "2023-10-21",
        },
        {
            "RegistrationID": 108,
            "StudentID": 8,
            "ExamID": 202,
            "RegistrationDate": "2023-10-22",
        },
    ]
)

exam_results_table.insert_multiple(
    [
        {"ResultID": 501, "StudentID": 1, "ExamID": 201, "Score": 92.5},
        {"ResultID": 502, "StudentID": 2, "ExamID": 201, "Score": 88.0},
        {"ResultID": 503, "StudentID": 3, "ExamID": 202, "Score": 95.5},
        {"ResultID": 504, "StudentID": 4, "ExamID": 203, "Score": 89.0},
        {"ResultID": 505, "StudentID": 5, "ExamID": 204, "Score": 94.5},
        {"ResultID": 506, "StudentID": 6, "ExamID": 205, "Score": 91.0},
        {"ResultID": 507, "StudentID": 7, "ExamID": 201, "Score": 87.5},
    ]
)

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
