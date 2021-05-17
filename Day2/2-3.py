#NUMBER MANIPULATION
#round,//,shorthand +=
#F STRINGS
#Why do u need f strings?
#without it,printing concat of string and diff datatype is painful
#print("Your score is"+str(score))

###########<<<<<PROGRAM>>>>#######
''' 
Life in weeks-
How many days,weeks,months till we reach 90 years of age
and round result
'''
age=input("What is your current age?")
yrs=90-int(age)
days=yrs*365
weeks=yrs*52
months=yrs*12
print(f"You have {days} days left,{weeks} weeks left and {months} months left")
