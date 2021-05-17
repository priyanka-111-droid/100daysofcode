#DATATYPES
#STRING #subscript
print("Hello"[0]) 
#concat
print("123"+"345")
#INTEGER
print(123+456)
#len(4867) gives ERROR
#FLOAT
#BOOLEAN-True , False

#HOW TO FIND OUT WHAT TYPE?
num_char=len(input("What is your name"))
print(type(num_char))

#TYPE CONVERSION
new_num_char=str(num_char)
print(type(new_num_char))


##################<<PROGRAM>>###################
'''out of random 2 digit number,add 2 digits'''

num=int(input("Enter two digit number :"))
print(int(str(num)[0])+int(str(num)[1]))

#concat string and int gives error!!!


