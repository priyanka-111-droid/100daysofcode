####<<<<PROGRAM>>>>####
'''
Fizzbuzz program:
1.print all numbers from 1 to 100
2.if divisible by 3,print "Fizz" instead of number
3.When divisible by 5,print "Buzz" instead of number
4.If divisible by 3 and 5,print "FizzBuzz" instead of number
'''
#METHOD 1:
# for x in range(0,101):
#     if(x%3==0 and x%5!=0):
#         print("Fizz")
#     elif(x%5==0 and x%3!=0):
#         print("Buzz")
#     elif(x%3==0 and x%5==0):
#         print("FizzBuzz")
#     else:
#         print(x)

#METHOD 2:better way
for x in range(0,101):
    if(x%3==0 and x%5==0):  
        print("FizzBuzz")
    #print the next 2 cases after "FizzBuzz" case as they have no overlap of results
    elif(x%3==0):           
        print("Fizz")
    elif(x%5==0):
        print("Buzz")
    else:
        print(x)
#if we printed x%3==0 first,numbers like 15 would have been printed as "Fizz" 
# so it would have never reached the "Fizzbuzz" case without != case as seen in method 1

#Mistake:
#avoid unnecessary use of logical operators like and
#try to change cases in if else to avoid overlap
