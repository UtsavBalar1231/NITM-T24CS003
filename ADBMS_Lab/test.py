from tinydb import TinyDB, Query
from statistics import mean
from tabulate import tabulate

db = TinyDB("db.json")

students = db.table("students")
all_students = students.all()
student_names_emails = [(s["Name"], s["Email"]) for s in all_students]
print("Retrieve the names and email addresses of all students:")
print(tabulate(student_names_emails, headers=["Name", "Email"], tablefmt="grid"))

courses = db.table("courses")
high_credit_courses = courses.search(Query().Credits > 3)
print("Find the courses that have more than three credits:")
print(
    tabulate(
        [(c["CourseID"], c["CourseName"], c["Credits"]) for c in high_credit_courses],
        headers=["CourseID", "CourseName", "Credits"],
        tablefmt="grid",
    )
)

exams = db.table("exams")
scheduled_exams = exams.search(Query().ExamDate > "2023-11-15")
print("List the exams scheduled after November 15, 2023:")
print(
    tabulate(
        [
            (e["ExamID"], e["ExamDate"], e["ExamTime"], e["Location"])
            for e in scheduled_exams
        ],
        headers=["ExamID", "ExamDate", "ExamTime", "Location"],
        tablefmt="grid",
    )
)

faculty = db.table("faculty")
math_faculty = faculty.search(Query().Department == "Mathematics")
print("Get the faculty members who work in the 'Mathematics' department:")
print(
    tabulate(
        [
            (f["FacultyID"], f["Name"], f["Email"], f["Phone"], f["Department"])
            for f in math_faculty
        ],
        headers=["FacultyID", "Name", "Email", "Phone", "Department"],
        tablefmt="grid",
    )
)

enrollment = db.table("enrollment")
student_courses = [(e["StudentID"], e["CourseID"]) for e in enrollment.all()]
print("Retrieve the courses that each student is enrolled in:")
print(tabulate(student_courses, headers=["StudentID", "CourseID"], tablefmt="grid"))

exam_results = db.table("exam_results")
exam_ids = {r["ExamID"] for r in exam_results.all()}
average_scores = {
    exam_id: mean([r["Score"] for r in exam_results.search(Query().ExamID == exam_id)])
    for exam_id in exam_ids
}
print("Find the average score for each exam:")
print(
    tabulate(
        [(exam_id, avg) for exam_id, avg in average_scores.items()],
        headers=["ExamID", "Average Score"],
        tablefmt="grid",
    )
)

high_scorers = {r["StudentID"] for r in exam_results.search(Query().Score > 90)}
print("List the students who scored above 90 on any exam:")
print(tabulate([(s,) for s in high_scorers], headers=["StudentID"], tablefmt="grid"))

teaching = db.table("teaching")
faculty_teach_counts = {}
for t in teaching.all():
    faculty_teach_counts[t["FacultyID"]] = (
        faculty_teach_counts.get(t["FacultyID"], 0) + 1
    )
multi_course_faculty = [f for f, count in faculty_teach_counts.items() if count > 1]
print("Retrieve the faculty members who teach multiple courses:")
print(
    tabulate(
        [(f,) for f in multi_course_faculty], headers=["FacultyID"], tablefmt="grid"
    )
)

exam_registration = db.table("exam_registration")
registered_students = {r["StudentID"] for r in exam_registration.all()}
unregistered_students = [
    s["StudentID"] for s in all_students if s["StudentID"] not in registered_students
]
print("Find the students who have not registered for any exams:")
print(
    tabulate(
        [(s,) for s in unregistered_students], headers=["StudentID"], tablefmt="grid"
    )
)

course_enrollment_counts = {}
for e in enrollment.all():
    course_enrollment_counts[e["CourseID"]] = (
        course_enrollment_counts.get(e["CourseID"], 0) + 1
    )
print("Retrieve the total number of enrollments for each course:")
print(
    tabulate(
        [(course_id, count) for course_id, count in course_enrollment_counts.items()],
        headers=["CourseID", "Enrollments"],
        tablefmt="grid",
    )
)

history_course = courses.get(Query().CourseName == "History")
history_students = [
    e["StudentID"]
    for e in enrollment.search(Query().CourseID == history_course["CourseID"])
]
print("Find the students who are enrolled in the 'History' course:")
print(
    tabulate([(s,) for s in history_students], headers=["StudentID"], tablefmt="grid")
)

exams = db.table("exams")
november_exams = exams.search(
    (Query().ExamDate >= "2023-11-01") & (Query().ExamDate <= "2023-11-30")
)
november_exams_locations = [(e["ExamDate"], e["Location"]) for e in november_exams]
print("Retrieve the exams and their locations scheduled for November 2023:")
print(
    tabulate(
        november_exams_locations, headers=["ExamDate", "Location"], tablefmt="grid"
    )
)

course_enrollment_counts = {}
for e in enrollment.all():
    course_enrollment_counts[e["CourseID"]] = (
        course_enrollment_counts.get(e["CourseID"], 0) + 1
    )
most_enrolled_course = max(course_enrollment_counts, key=course_enrollment_counts.get)
print("List the courses with the highest number of enrollments:")
print(
    tabulate(
        [(most_enrolled_course, course_enrollment_counts[most_enrolled_course])],
        headers=["CourseID", "Enrollments"],
        tablefmt="grid",
    )
)

exam_results = db.table("exam_results")
student_scores = {}
for r in exam_results.all():
    student_scores[r["StudentID"]] = student_scores.get(r["StudentID"], []) + [
        r["Score"]
    ]
average_student_scores = {s: mean(scores) for s, scores in student_scores.items()}
print("Find the average score for each student:")
print(
    tabulate(
        [(s, avg) for s, avg in average_student_scores.items()],
        headers=["StudentID", "Average Score"],
        tablefmt="grid",
    )
)

exam_registration = db.table("exam_registration")
exam_ids_with_registrations = {r["ExamID"] for r in exam_registration.all()}
unregistered_exams = [
    e["ExamID"] for e in exams.all() if e["ExamID"] not in exam_ids_with_registrations
]
print("Retrieve the exams that have no registered students:")
print(tabulate([(e,) for e in unregistered_exams], headers=["ExamID"], tablefmt="grid"))

faculty = db.table("faculty")
teaching = db.table("teaching")

taught_faculty_ids = {t["FacultyID"] for t in teaching.all()}
untaught_faculty = [
    f for f in faculty.all() if f["FacultyID"] not in taught_faculty_ids
]
print("List the faculty members who have yet to teach any courses:")
print(
    tabulate(
        [(f["FacultyID"], f["Name"]) for f in untaught_faculty],
        headers=["FacultyID", "Name"],
        tablefmt="grid",
    )
)

math_course = courses.get(Query().CourseName == "Mathematics")["CourseID"]
cs_course = courses.get(Query().CourseName == "Computer Science")["CourseID"]
math_students = {
    e["StudentID"] for e in enrollment.search(Query().CourseID == math_course)
}
cs_students = {e["StudentID"] for e in enrollment.search(Query().CourseID == cs_course)}
students_in_both = math_students.intersection(cs_students)
print(
    "Find the students who have registered for exams in both 'Mathematics' and 'Computer Science' departments:"
)
print(
    tabulate([(s,) for s in students_in_both], headers=["StudentID"], tablefmt="grid")
)

highest_scores = {}
for r in exam_results.all():
    exam_id = r["ExamID"]
    if exam_id not in highest_scores or r["Score"] > highest_scores[exam_id]["Score"]:
        highest_scores[exam_id] = r
highest_student_scores = {s["StudentID"]: s["Score"] for s in highest_scores.values()}
print("Retrieve the students who scored the highest in each exam:")
print(
    tabulate(
        [(s, score) for s, score in highest_student_scores.items()],
        headers=["StudentID", "Highest Score"],
        tablefmt="grid",
    )
)

enrolled_course_ids = {e["CourseID"] for e in enrollment.all()}
unenrolled_courses = [
    c["CourseID"] for c in courses.all() if c["CourseID"] not in enrolled_course_ids
]
print("Find the courses that no student has enrolled in:")
print(
    tabulate([(c,) for c in unenrolled_courses], headers=["CourseID"], tablefmt="grid")
)

high_enrollment_courses = [
    course_id for course_id, count in course_enrollment_counts.items() if count > 10
]
high_enrollment_faculty = [
    t["FacultyID"]
    for t in teaching.search(Query().CourseID.one_of(high_enrollment_courses))
]
print(
    "Retrieve the faculty members who teach courses with an average enrollment count above 10:"
)
print(
    tabulate(
        [(f,) for f in high_enrollment_faculty], headers=["FacultyID"], tablefmt="grid"
    )
)
