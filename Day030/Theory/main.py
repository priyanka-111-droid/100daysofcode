###<<<EXCEPTIONS WE HAVE COME ACROSS>>>###

#What happens when We try to open file that DOES NOT EXIST
#We get FileNotFoundError
# with open("Day030/Theory/a_file.txt") as file:
#     file.read()

#KeyError
# a_dictionary={"key":"value"}
# value=a_dictionary["non_existent_key"]

#IndexError
# fruit_list=["Apple","Banana","Pear"]
# fruit=fruit_list[3]

#TypeError
# text="abc"
# print(text+5)

###<<<HOW TO CATCH EXCEPTIONS>>>###
# using keywords:
# 1.try:block of code that MIGHT CAUSE exception
# 2.except:do this if there WAS an exception thrown due to above try block
# 3.else:do this if there were NO exceptions
# 4.finally:do this no matter WHAT happens

######<<<IMPLEMENTATION>>>######
try:
    file=open("Day030/Theory/a_file.txt")
    a_dictionary={"key":"value"}
    # print(a_dictionary["sdfeff"])
    print(a_dictionary["key"])
    
except FileNotFoundError:
    # print("There was an error")
    #Now just printing is pointless,we need to try and solve this error
    #Now we use write mode("w") as in case file is not found,it will create file for us
    file=open("Day030/Theory/a_file.txt","w")
    file.write("Something")

except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    #as long as errors exist,this will never execute

    #Now if we change "sdfeff" to "key" which actually exists in a_dictionary
    #else block will run
    content=file.read()
    print(content)

finally:
    file.close()
    print("File was closed")
