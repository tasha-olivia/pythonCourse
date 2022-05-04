student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione":99,
    "Draco": 74,
    "Nerville": 62,
}
print(student_scores)

student_grade = {}
for key in student_scores:
    score = student_scores[key]
    if score >= 91:
        student_grade[key] = "Outstanding"
    elif score >= 81 and score <= 90:
        student_grade[key] = "Exceeds expectation"
    elif score >= 71 and score <= 80:
        student_grade[key] = "Acceptable"
    else :
        student_grade[key] = "Fail"
print(student_grade)
    