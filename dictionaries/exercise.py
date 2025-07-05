student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades = {}
for keys in student_scores:
    if 100 >= student_scores[keys] > 90:
        student_grades[keys] = "Outstanding" 
    elif 90 >= student_scores[keys] > 80:
        student_grades[keys] = "Beyond expectations"
    elif 80 >= student_scores[keys] > 70:
        student_grades[keys] = "Acceptable"
    elif 70 >= student_scores[keys]:
        student_grades[keys] = "Fail"

print(student_grades)