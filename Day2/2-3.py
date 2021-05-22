#NUMBER MANIPULATION
#round
#//(using this instead of / for division gives integer answer)
#shorthand +=,-=,*=,/= means for example x=x+2 is same as x+=2 
#F STRINGS
#Why do u need f strings?
#without it,printing concat of string and different datatype is painful and we would have to do type conversion every time.
#print("Your score is"+str(score))

###########<<<<<PROGRAM>>>>#########
''' 
Life in weeks-
How many days,weeks,months till we reach 90 years of age
and round your  result to nearest whole number
'''
age=input("What is your current age?")
yrs=90-int(age)
days=yrs*365
weeks=yrs*52
months=yrs*12
print(f"You have {days} days left,{weeks} weeks left and {months} months left")
