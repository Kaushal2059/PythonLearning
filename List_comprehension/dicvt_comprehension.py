import random 
import pandas

# Example for dictionary comprehension
names = ["Kaushal","Hari","Gita","Sita","Ram","Mandal"]
students_scores = {student:random.randint(1,100) for student in names}
# print(students_scores)

dictionary = {
    'Kaushal': 32,
    'Hari': 61, 
    'Gita': 59,
    'Sita': 36,
    'Ram': 78,
    'Mandal': 82,
    }

passed_students = {key:value for (key,value) in dictionary.items() if value <= 60}
# print(passed_students)

student = pandas.DataFrame(dictionary)
print(student)

