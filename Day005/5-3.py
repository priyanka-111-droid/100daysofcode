#for loop with range function
#for number in range(a,b,c):
#    print(number)
#prints all numbers from a to b-1 with an increment of c

###<<<PROGRAM>>>####
'''
sum of all even numbers from 1 to 100 including 1 and 100
There should be only 1 print statement at the end
Also use range()
'''
s=0
#METHOD 1:
# for x in range(2,101,2):
#     s=s+x


#METHOD 2:
for x in range(1,101):
    if(x%2==0): #if number divisible by 2
        s=s+x 

print(s)