import pandas

data = pandas.read_csv("sqirrel_data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260527.csv")

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(cinamon_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "fur_color": ["Gray", "cinamon", "black"],
    "count": ["grey_squirrels_count","cinamon_squirrels_count","black_squirrels_count"]
}
data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("sqirrel_data/squirrel_count.csv")