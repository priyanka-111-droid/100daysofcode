#DATATYPES - are classification of data items
#can be string(str),integer(int),floating point number(float),boolean(bool)
#STRING subscript
print("Hello"[0]) # H
#concat
print("123"+"345")# 123345
#INTEGER
print(123+456)
#len(4867) gives ERROR as 4867 is an integer not string
#FLOAT-decimal values
#BOOLEAN-True , False

#HOW TO FIND OUT WHAT TYPE?
num_char=len(input("What is your name"))
print(type(num_char))

#TYPE CONVERSION
new_num_char=str(num_char)
print(type(new_num_char))


##################<<PROGRAM>>###################
'''Input a 2 digit number,add its 2 digits'''

num=int(input("Enter two digit number :"))
print(int(str(num)[0])+int(str(num)[1]))

#We use str() type conversion to extract digit at 0th subscript and 1st subscript 
#Then we convert it to int because we need to add the two digits .
#concat string and int gives error!!!


