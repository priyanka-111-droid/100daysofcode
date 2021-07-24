#type hints so that when we use function later in code we know datatype of parameters it accepts and returns.
def police_check(age:int)->bool:
    if age>18:
        can_drive=True

    else:
        can_drive=False

    return can_drive

# print(police_check(12))
# print(police_check(19))



#This will give error as string instead of int
# if(police_check("twelve")):
#     print("You may pass")
# else:
#     print("Pay a fine")


# if(police_check(19)):
#     print("You may pass")
# else:
#     print("Pay a fine")

