# year = input("Which year do you want to check?")
# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")


###<<SOLUTION>>###

year = (input("Which year do you want to check?"))
#print(type(year))
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")


#1.Run the code once,we get error due to variable year
#2.Checking type of year,we find that it is string
#3.So we need int input for year as we have to use %
