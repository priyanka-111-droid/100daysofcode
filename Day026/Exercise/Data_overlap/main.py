with open("Day026/Exercise/Data_overlap/file1.txt") as f1:
    f1_contents=f1.readlines()
   
with open("Day026/Exercise/Data_overlap/file1.txt") as f2:
    f2_contents=f2.readlines()


result=[int(x) for x in f1_contents if x in f2_contents]
print(result)