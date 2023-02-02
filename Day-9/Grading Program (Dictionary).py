student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}


student_grades = {}

for grade in student_scores:
    student_grades = student_scores

    if student_scores[grade] > 90:
        student_scores[grade] = "Outstanding"
    elif student_scores[grade] > 80:
        student_scores[grade] = "Exceeds Expectations"
    elif student_scores[grade] > 70:
        student_scores[grade] = "Acceptable"
    else:
        student_scores[grade] = "Fail"

print(student_grades)