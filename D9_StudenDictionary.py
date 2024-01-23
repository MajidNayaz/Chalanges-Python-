students_score = {
    "Ali": 23,
    "Rahim": 89,
    "Salman": 90,
    "Bahram": 100,
    "Samir": 70,
    "Alham": 64
}

students_grade = {}
for student in students_score:
    score = students_score[student]
    if score > 90:
        students_grade [student] = "Outstanding"
    elif score > 80:
        students_grade[student] = "Exceeds Expections"
    elif score > 70:
        students_grade[student] = "Acceptable"
    elif score <= 70:
        students_grade[student] = "Fail"

print(students_grade)