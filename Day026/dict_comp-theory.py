#Dictionary comprehension
#new_dict={new_key:new_value for (key,value) in dict.items() if test}
import random


names=["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
#TODO 1:From above given names,generate random score for each name
student_scores={x:random.randint(1,100) for x in names}
print(student_scores)

#TODO 2:create new dictionary having students with scores more than or equal to 60.
passed_students={key:value for (key,value) in student_scores.items() if value>=60}
print(passed_students)

