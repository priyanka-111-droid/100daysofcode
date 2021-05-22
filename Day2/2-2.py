#MATH OPERATIONS ORDER OF EVALUATION
#Way to remember : PEMDASLR(LR-left to right associativity)
#()---->Parenthesis(P) have highest precedence(priority)
# **---->Exponents(E) have 2nd highest precedence
# *,/(division-->float answer)-->Multiplication(M) and Division(D) have next highest precedence.While choosing between M and D ,go left to right(LR)
# +,- --->Addition(A),Subtraction(S) have last precedence.While choosing between A and S,go left to right (LR)
#print(3*(3+3)/3-3) gives 3


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
