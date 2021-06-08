# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")



###<<SOLUTION>>>###
age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")

#1.Fixed indentation(due to red underlines)
#2.After running code,found out another error,hence made age as int 
#3.Now make it as f string to print value and not {age}
