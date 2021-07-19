#WRITING IN OUR FILE:
#Now we can add text into our file write.txt when we run this program

#Add absolute path to the txt file based on where file is located in YOUR MACHINE
with open("C:/Users/Admin/Documents/GitHub/100daysofcode/Day024/practicefiles/write.txt",mode="w") as f:
    f.write("I just wrote this text now...")

#Also remember,in write mode("w") when the file we want to write into DOES NOT EXIST,
#python will create it for us. 