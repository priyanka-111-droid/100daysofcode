# APPENDING CONTENT TO WHAT WAS ALREADY THERE IN read.txt
#Usually when we write something,it replaces content already there
#But with append,we can add new lines as well.

#Add absolute path to the txt file based on where file is located in YOUR MACHINE
with open("C:/Users/Admin/Documents/GitHub/100daysofcode/Day024/practicefiles/read.txt",mode="a") as f:
    f.write("\nI just added this text now...")

#Now when you open read.txt file,you can see previous content AND this new line..