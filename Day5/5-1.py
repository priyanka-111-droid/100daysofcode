#for loops and lists
# fruits=["Apple","Peach","Pear"]
# for fruit in fruits:
#     print(fruit)  #for each value in list,it prints it
# You don't need to set fruit variable to 0 before use as it is a loop variable
#Don't set user input variables and loop variables to 0
#remaining variables you need to set it to 0


#########<<<<<<Program>>>>######
'''
Average Height exercise
Input height separated by space
Calculate avg student height and round off to nearest whole number
'''
#METHOD 1:using loops
student_heights=input("Input a list of student heights :\n").split()
number_of_students=0 #declare to 0 else garbage value will be there
totalsum=0
for x in range(0,len(student_heights)):
    student_heights[x]=int(student_heights[x]) #converting string height to int
    totalsum=totalsum+student_heights[x]
    number_of_students+=1

avg=totalsum/number_of_students
print(round(int(avg)))

#METHOD 2:no loops 
#in python you can get sum of list items using sum()
# avg = sum(student_heights)/len(student_heights)
# print(round(int(avg)))

