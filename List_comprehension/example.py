import pandas

dictionary = {
    "student" : ["kaushal","Hari","Sita", "Gita"],
    "marks" : [10, 20, 80, 66]
    }

data_frame = pandas.DataFrame(dictionary)
print(data_frame)

# Looping through rows of a data frame 
for (index, row) in data_frame.iterrows():
    if row.student == "kaushal":
        print(row.student)