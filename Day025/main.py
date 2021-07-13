# Open weather_data.csv(already given) and use readlines() to create list called data that has values from .csv file

# with open ("Day025\weather_data.csv") as f:
#     data=f.readlines()
#     print(data)
    

# using csv
import csv
with open("Day025\weather_data.csv") as data_file:
    #create new list having all temperatures of csv file
    temperature=[]
    data=csv.reader(data_file)
    for row in data:
        # print(row)
        if(row[1]!="temp"):
            temperature.append(int(row[1]))

    print(temperature)



#for more data,we use pandas-python data analysis library for tabulular data,
import pandas 
data=pandas.read_csv("Day025\weather_data.csv")
print(data)
