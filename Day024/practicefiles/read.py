# #OPENING FILE AND READING CONTENTS ALREADY PRESENT IN IT...
# #First, python opens the file
# # use the full, absolute path of your OWN MACHINE, instead of a "relative" path 
# # if you are getting file or directory not found error 
# #You can get absolute path from file explorer.

# file = open("C:/Users/Admin/Documents/GitHub/100daysofcode/Day024/practicefiles/read.txt")


# #file contents are being read and printed.
# contents=file.read()
# print(contents)


# #close the file when done
# file.close()


#OTHER WAY TO OPEN FILE:
#Now we don't need to close file each time

with open("C:/Users/Admin/Documents/GitHub/100daysofcode/Day024/practicefiles/read.txt") as f:
    contents=f.read()
    print(contents)


