# with open("handling_csv/weather_data.csv") as data:
#     datas = data.readlines()
#     print(datas)

# import csv

# with open("handling_csv/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# print(temperatures)
    

import pandas 

data = pandas.read_csv("handling_csv/weather_data.csv")
# dict_data = data.to_dict() # Converts data to dictionary
# # print(dict_data)

# temperature_list = data["temp"].to_list() # To convert data into list\

# # sum = 0
# # terms = len(temperature_list)
# # for data in temperature_list:
# #     sum += data

# # average = sum/terms
# # print(average)

# # OR
# average2 = sum(temperature_list) / len(temperature_list)
# print(average2)

# # Using pandas
# average3 = data["temp"].mean()
# print(f"third average {average3}")

# highest = data["temp"].max()
# print(f"highest is {highest}")

# # Another way of getting hold of the column is
# print(data.condition)

# # Get data row
# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()]) # TO get the column with maximum temp

monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp_F = monday_temp *  9/5 + 32
print(monday_temp_F)

# Create a dataframe from scratch
data_dict = {
    "Students":["Hari", "Gita", "Sita"],
    "scores": [76,75,70]
}
data = pandas.DataFrame(data_dict)
data.to_csv("handling_csv/new_data.csv")