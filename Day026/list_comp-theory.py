#List comprehension
#general format:new_list=[new_item for item in list]
#conditional list comp:new_list=[new_item for item in list if test]

# Instead of for loop,
numbers=[1,2,3]
new_list1=[]
for n in numbers:
    add_1=n+1
    new_list1.append(add_1)
print(new_list1)

# We can write like this:
numbers=[1,2,3]
new_list2=[n+1 for n in numbers] #this is list comprehension
print(new_list2)

# Can also be done to convert string to list:
name="Angela"
letters_list=[letter for letter in name]
print(letters_list)

#All python sequences like list,range,string,tuple have a specific order
#List comprehensions go through items in sequence and perform specific task.

#TODO 1:use list comprehension to loop through range from 1 to 5 and double each number in range.
range_list=[x*2 for x in range(1,6)]
print(range_list)

names=["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
#TODO 2:Use conditional list comprehension to go through list of names already given and print 
#those names of 4 letters or less
short_names=[n for n in names if len(n)<=4]

#TODO 3:From above names given,take names of 5 letters or more and convert to uppercase
long_names=[n.upper() for n in names if n not in short_names]
print(long_names)

numbers_given=[1,1,2,3,5,8,13,21,34,55]
#TODO 4:Create new list where each number from above list is squared
squared_numbers=[x**2 for x in numbers_given]
print(squared_numbers)

#TODO 5:Create new list result having only even numbers from numbers_given list.
result=[x for x in numbers_given if x%2==0]
print(result)
