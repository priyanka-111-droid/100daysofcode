
import math

def painting_wall(wall_h,wall_w):
    #type casting as float as wall height and width can be a float too
    
    number_of_cans=(float(wall_h)*float(wall_w))/5
    #using ceil as we need to round UP
    #ceil always gives answer in float so to get integer answer,we type cast it to int

    print(f"You'll need {int(math.ceil(number_of_cans))} cans of paint")

#USING HARDCODED VALUES AS ARGUMENTS(to test our program with sample input and output)
#positional argument
#painting_wall(3,9)
#keyword argument
#painting_wall(wall_w=9,wall_h=3) 

#USING USER DEFINED VALUES AS ARGUMENTS
test_h=input("Enter wall's height :")
test_w=input("Enter wall's width :")
#positional argument
#painting_wall(test_h,test_w)
#keyword argument
painting_wall(wall_h=test_h,wall_w=test_w)
# painting_wall(wall_w=test_w,wall_h=test_h) this is also right as order can be changed for keyword argument


#We can also use same variable name in argument as used in the parameter
#But in function call,it can be confusing as to which variable we are assigning to what
#So try to avoid the below method
# wall_h=input("Enter wall's height :")
# wall_w=input("Enter wall's width :")
# painting_wall(wall_h=wall_h,wall_w=wall_w) 


#REMEMBER:
#use math.ceil to round up
#use math.floor to round down
#use round to round to nearest integer
