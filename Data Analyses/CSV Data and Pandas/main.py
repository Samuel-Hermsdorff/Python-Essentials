# with open("weather_data.csv") as weather_file:
#     weather_data = weather_file.readlines()
    # for data in weather_data:
    #     data_formatted = data.strip()
    #     weather_data[weather_data.index(data)] = data_formatted

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         temperatures.append(row[1])
#     temperatures.pop(0)
#     for temp in temperatures:
#         temperatures[temperatures.index(temp)] = float(temp)
#     print(temperatures)

# import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))

# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# total = 0
# temp_list = data["temp"].to_list()
# for temp in temp_list:
#     total += int(temp)

# average = total / len(temp_list)
# print(average)

# print(data["temp"].mean())

# print(data["temp"].max())

# print(data.condition)

# # get Data in row:
# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)

# temp_in_celcius = monday.temp * 9/5 + 32
# print(temp_in_celcius)

# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)

import pandas as pd

squirrel_data = pd.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

full_colors_list = squirrel_data["Primary Fur Color"].to_list()

colors_list = []
for item in full_colors_list:
    if item not in colors_list:
        colors_list.append(item)

colors_list_cleaned = pd.Series(colors_list).dropna().values
new_colors_list = []
for _ in colors_list_cleaned:
    new_colors_list.append(_)

count_list = []
for color in new_colors_list:
    count_list.append(full_colors_list.count(color))

colors_dic = {
    "Fur Color": new_colors_list,
    "Count": count_list
}

colors_count = pd.DataFrame(colors_dic)
print(colors_count)
colors_count.to_csv("squirrel_count")