#MATH OPERATIONS
#PEMDASLR(LR-leftright)
#(),
# **,
# *,/(division-->float answer)
# +,-
#print(3*(3+3)/3-3)


########<<<<<PROG>>>>###########
''' BMI calculator 
    BMI=weight(kg)/height^2(m)
    give ans as whole number
'''
height=input("Enter your height in m:")
weight=input("enter your weight in kg :")
#wrong!!!
#print(int(weight/(height**2)))

#convert string to other datatypes esp height
#since most ppl have height between 1 to 2 put that as float
#if we want weight to accept only int,put int else put float

#wrong again as type error!!!
#bmi= weight/float(height)**2

#correct ans :)
bmi= float(weight)/float(height)**2
print(int(bmi)) #for whole number
