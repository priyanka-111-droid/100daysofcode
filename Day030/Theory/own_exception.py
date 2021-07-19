#using raise
# try:
#     file=open("Day030/Theory/a_file.txt")
#     a_dictionary={"key":"value"}
#     print(a_dictionary["key"])
    
# except FileNotFoundError:
#     # print("There was an error")
#     #Now just printing is pointless,we need to try and solve this error
#     #Now we use write mode("w") as in case file is not found,it will create file for us
#     file=open("Day030/Theory/a_file.txt","w")
#     file.write("Something")

# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     #as long as errors exist,this will never execute
#     content=file.read()
#     print(content)

# finally:
#     #Even if above code will not raise key error
#     #typing raise KeyError will give us key error

#     raise KeyError

####<<<WHERE WOULD WE RAISE OUR OWN EXCEPTION>>>###
height=float(input("Height: "))
weight=int(input("Weight: "))
if(height>3):
    raise ValueError("Human height should not be over 3 meters")

bmi=weight/(height**2)
print(bmi) 
#Here bmi is calculated correctly
#But it is impossible for a human to be more than 3m tall
#hence we are raising an exception.