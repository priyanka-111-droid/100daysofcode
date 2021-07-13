import pandas
data=pandas.read_csv("Day025/Exercise/Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colors=["Gray","Cinnamon","Black"]

count=[]
for x in colors:
    each_squirrel_count=len(data[data["Primary Fur Color"]==x])
    count.append(each_squirrel_count)

#make dictionary from two lists(colors,count)
d={"Fur Color":colors,"Count":count}
# print(d)

#convert dictionary to dataframe
new_data=pandas.DataFrame(d)
# print(new_data)


#Creating new csv file squirrel_count.csv and storing our dataframe there
new_data.to_csv("Day025/Exercise/squirrel_count.csv")

