List_of_students = ["kaushal","ram","shyam"]
List_of_students[1] = "Hari"
List_of_students.append("badass")
List_of_students.extend(["Gita","Rita"])
print(List_of_students)
print("the toppr is",List_of_students[0])

# Nested list
first = ["apple","ball","cat"]
second = ["dog","elephant","fish"]
third = [first,second]
print(third[1][1])