#Project:password generator
'''
generates a password that is secure
'''
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#level 1:order of password is letters->symbols->number
# str=""
# for x in range(1,nr_letters+1):
#     str=str+ random.choice(letters)

# for x in range(1,nr_symbols+1):
#     str=str+random.choice(symbols)

# for x in range(1,nr_numbers+1):
#     str=str+random.choice(numbers)

# print(str)

#level 2:order randomized
pas=[]
for x in range(1,nr_letters+1):
    pas=pas+ random.choice(letters)

for x in range(1,nr_symbols+1):
    pas=pas+random.choice(symbols)

for x in range(1,nr_numbers+1):
    pas=pas+random.choice(numbers)

random.shuffle(pas) #shuffles order of list elements
print(pas) #prints list

password=""
for x in pas:
    password+=x #converting list to string

print(password) #prints string password