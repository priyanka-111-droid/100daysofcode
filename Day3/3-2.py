#nested if and elif
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
