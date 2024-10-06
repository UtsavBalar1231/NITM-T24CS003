from tinydb import TinyDB, Query
from statistics import mean

db = TinyDB('db.json')

students = db.table('students')
all_students = students.all()
student_names_emails = [(s['Name'], s['Email']) for s in all_students]
print("Retrieve the names and email addresses of all students:")
print(student_names_emails)

courses = db.table('courses')
high_credit_courses = courses.search(Query().Credits > 3)
print("Find the courses that have more than three credits:")
print(high_credit_courses)

exams = db.table('exams')
scheduled_exams = exams.search(Query().ExamDate > '2023-11-15')
print("List the exams scheduled after November 15, 2023:")
print(scheduled_exams)

faculty = db.table('faculty')
math_faculty = faculty.search(Query().Department == 'Mathematics')
print("Get the faculty members who work in the 'Mathematics' department:")
print(math_faculty)

enrollment = db.table('enrollment')
student_courses = [(e['StudentID'], e['CourseID']) for e in enrollment.all()]
print("Retrieve the courses that each student is enrolled in:")
print(student_courses)

exam_results = db.table('exam_results')
exam_ids = {r['ExamID'] for r in exam_results.all()}
average_scores = {exam_id: mean([r['Score'] for r in exam_results.search(Query().ExamID == exam_id)]) for exam_id in exam_ids}
print("Find the average score for each exam:")
print(average_scores)


high_scorers = {r['StudentID'] for r in exam_results.search(Query().Score > 90)}
print("List the students who scored above 90 on any exam:")
print(high_scorers)

teaching = db.table('teaching')
faculty_teach_counts = {}
for t in teaching.all():
    faculty_teach_counts[t['FacultyID']] = faculty_teach_counts.get(t['FacultyID'], 0) + 1
multi_course_faculty = [f for f, count in faculty_teach_counts.items() if count > 1]
print("Retrieve the faculty members who teach multiple courses:")
print(multi_course_faculty)

exam_registration = db.table('exam_registration')
registered_students = {r['StudentID'] for r in exam_registration.all()}
unregistered_students = [s['StudentID'] for s in all_students if s['StudentID'] not in registered_students]
print("Find the students who have not registered for any exams:")
print(unregistered_students)


course_enrollment_counts = {}
for e in enrollment.all():
    course_enrollment_counts[e['CourseID']] = course_enrollment_counts.get(e['CourseID'], 0) + 1
print("Retrieve the total number of enrollments for each course:")
print(course_enrollment_counts)

history_course = courses.get(Query().CourseName == 'History')
history_students = [e['StudentID'] for e in enrollment.search(Query().CourseID == history_course['CourseID'])]
print("Find the students who are enrolled in the 'History' course:")
print(history_students)

november_exams = exams.search((Query().ExamDate >= '2023-11-01') & (Query().ExamDate <= '2023-11-30'))
november_exams_locations = [(e['ExamDate'], e['Location']) for e in november_exams]
print("Retrieve the exams and their locations scheduled for November 2023:")
print(november_exams_locations)

most_enrolled_course = max(course_enrollment_counts, key=course_enrollment_counts.get)
print("List the courses with the highest number of enrollments:")
print(most_enrolled_course)

student_scores = {}
for r in exam_results.all():
    student_scores[r['StudentID']] = student_scores.get(r['StudentID'], []) + [r['Score']]
average_student_scores = {s: mean(scores) for s, scores in student_scores.items()}
print("Find the average score for each student:")
print(average_student_scores)

exam_ids_with_registrations = {r['ExamID'] for r in exam_registration.all()}
unregistered_exams = [e['ExamID'] for e in exams.all() if e['ExamID'] not in exam_ids_with_registrations]
print("Retrieve the exams that have no registered students:")
print(unregistered_exams)

taught_faculty_ids = {t['FacultyID'] for t in teaching.all()}
untaught_faculty = [f for f in faculty.all() if f['FacultyID'] not in taught_faculty_ids]
print("List the faculty members who have yet to teach any courses:")
print(untaught_faculty)

math_course = courses.get(Query().CourseName == 'Mathematics')['CourseID']
cs_course = courses.get(Query().CourseName == 'Computer Science')['CourseID']
math_students = {e['StudentID'] for e in enrollment.search(Query().CourseID == math_course)}
cs_students = {e['StudentID'] for e in enrollment.search(Query().CourseID == cs_course)}
students_in_both = math_students.intersection(cs_students)
print("Find the students who have registered for exams in both 'Mathematics' and 'Computer Science' departments:")
print(students_in_both)

highest_scores = {}
for r in exam_results.all():
    exam_id = r['ExamID']
    if exam_id not in highest_scores or r['Score'] > highest_scores[exam_id]['Score']:
        highest_scores[exam_id] = r
highest_student_scores = {s['StudentID']: s['Score'] for s in highest_scores.values()}
print("Retrieve the students who scored the highest in each exam:")
print(highest_student_scores)

enrolled_course_ids = {e['CourseID'] for e in enrollment.all()}
unenrolled_courses = [c['CourseID'] for c in courses.all() if c['CourseID'] not in enrolled_course_ids]
print("Find the courses that no student has enrolled in:")
print(unenrolled_courses)

high_enrollment_courses = [course_id for course_id, count in course_enrollment_counts.items() if count > 10]
high_enrollment_faculty = [t['FacultyID'] for t in teaching.search(Query().CourseID.one_of(high_enrollment_courses))]
print("Retrieve the faculty members who teach courses with an average enrollment count above 10:")
print(high_enrollment_faculty)
