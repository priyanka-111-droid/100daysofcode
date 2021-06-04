####<<<<PROGRAM>>>####
'''
Highest score:
Input list of scores separated by space
get highest score
don't use min or max functions
'''

student_scores=input("Input list of scores").split()
for n in range(0,len(student_scores)):
    student_scores[n]=int(student_scores[n])

max=0 #let max be 0
for n in student_scores: 
    if(n>max):   #if a score in the  list is more than max
        max=n    #assignment operator(=) works from right to left so that score in list(n) is now assigned to max

print(max)
