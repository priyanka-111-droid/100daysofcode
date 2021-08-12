#########<<<<FIRST CLASS FUNCTIONS(basics before learning decorators)>>>>>>#####
#Python is a language that is said to have first class functions because it treats functions like first-class objects

#First class object(Programming):
#This is an entity that supports operations available to other entities.
#These operations include being assigned to a variable ,being passed as an argument and being returned from a function.



#----------------Assign a function to a variable--------------#
def square(x):
    return x*x


f=square(5)
print(square)
print(f)

# () means executing function
# Here we don't want to execute function
# We are setting variable f equal to function NOT executed. 
# Hence variable f CAN be treated as a function.
f=square 
print(square)
print(f)
print(f(5))



#----------------Pass function as an argument-------------------#
def my_map(func,arg_list):
    result=[]
    for i in arg_list:
        result.append(func(i))
    return result

#passing function square defined above as an argument
squares_result=my_map(square, [1,2,3,4,5])
print(squares_result)



#---------------Return function from another function------------#
def outer_func(message):
    def inner_func():
        print("Message :",message)
    
    #no () as we don't want this function to execute
    return inner_func


greeting=outer_func("Hi!")
#now variable greeting can be treated like function inner_func()
greeting()


# The outer_func() function was called with the string "Hi" 
# and the returned function was bound to the name greeting. 
# On calling greeting(), the message was still remembered although 
# we had already finished executing the outer_func() function.
# This technique by which some data ("Hi" in this case) gets attached to the code 
# is called CLOSURE in Python.


# A closure is an inner function that remembers and has access to variables in the local scope
# in which it was created even after the outer function has finished executing











