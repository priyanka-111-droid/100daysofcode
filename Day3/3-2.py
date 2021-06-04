#nested if and elif
##<<<PROGRAM>>##
'''
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
It should tell them the interpretation of their BMI based on the BMI value.

BMI value is calculated by dividing a person's weight (in kg) by the square of their height (in m):
Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.

Sample input:
weight = 85
height = 1.75
Calculation:
85 ÷ (1.75 x 1.75) = 27.755102040816325
Sample output:
Your BMI is 28, you are slightly overweight.

Warning you should round the result to the nearest whole number.
The interpretation message needs to include the words in bold from the interpretations above. e.g. underweight, normal weight, overweight, obese, clinically obese.
'''
height=input("Enter your height in m:")
weight=input("enter your weight in kg :")

bmi= float(weight)/float(height)**2

print(bmi) 
if(bmi<18.5):
    print(f"Your BMI is {int(round(bmi))},you are underweight")
elif(bmi>=18.5 and bmi<=25):
    print(f"Your BMI is {int(round(bmi))},you have a normal weight")
elif(bmi>25 and bmi<30):
    print(f"Your BMI is {int(round(bmi))},you are slightly overweight")
elif(bmi>=30 and bmi<35):
    print(f"Your BMI is {int(round(bmi))},you are obese")
else:
    print(f"Your BMI is {int(round(bmi))},you are clinically obese")
