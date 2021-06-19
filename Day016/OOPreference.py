'''CREATING CLASS'''

class Car():
    pass

'''CREATING INSTANCE OF CLASS AND STORE IN VARIABLE(INSTANTIATION)'''

ford=Car()  
print(ford) 
# This is describing the class that the instance was built from “Car,” 
# and the location in memory that the class itself is stored 

'''CREATE MULTIPLE INSTANCES FROM SAME CLASS'''

audi=Car()
print(hash(ford))
print(hash(audi))
# These numbers are a numerical representation of the variables’
# location in memory. Meaning that although the two variables are created from the same
# source, they are stored as separate entities within the program.


'''DECLARING AND ACCESSING ATTRIBUTES'''

class Car():
    color="red"     # all car objects will have this color attribute and its' value
    sound="beep"    # all car objects will have this sound attribute and its' value

ford = Car( )
print(ford.color) # use'dot syntax' to access object's attribute

'''CHANGING INSTANCE ATTRIBUTES'''
ford.color = "blue" # from now on the value of fords color is blue,this does not affect other instances
print(ford.color) 


'''USING __init__() METHOD'''

# using the init method to give instances personalized attributes upon creation

class Car( ):
    def __init__(self, color):
        self.color = color # sets the attribute color to thevalue passed in

ford = Car("blue") # instantiating a Car class with the color blue
print(ford.color)

#self keyword is how objects created from same source are identified
# When you want to instantiate an object with personalized attributes, you need to have the init
# method declared and use the self keyword to save each attributes value.


'''GLOBAL ATTRIBUTES vs INSTANCE ATTRIBUTES'''

# Global attributes 
# 1.can be referenced by the class directly and all its instances.
# 2.If an attribute is declared inside of a class,but not within the init method,it is a global attribute.

# Instance attributes:
# 1.instance attributes (which are defined within the init method)can only be accessed by the class instances.  
# 2.Any attributes declared within the init method using the self keyword are instance attributes

class Car( ):
    sound = "beep" # global attribute, accessible through the class itself
    def __init__(self, color):
        self.color = "blue" # instance specific attribute, not accessible through the class itself
        
print(Car.sound)
# print(Car.color) won't work, 
# as color is only available to instances of the Car class, not the class itself

ford = Car("blue")
print(ford.sound, ford.color) # color will work as this is an instance


'''DEFINING AND CALLING METHOD'''
class Dog( ):
    def makeSound(self):
        print("bark")


sam = Dog( )      
sam.makeSound( )   # dot syntax to access method 

# When declaring a method that you intend to access
# through instances, you must use the self parameter in the definition. Without the self
# keyword, the method can only be accessed by the class itself


'''ACCESSING CLASS ATTRIBUTES IN METHODS'''

class Dog( ):
    sound = "bark"
    def makeSound(self):
        print(self.sound) # self required to access attributes defined in the class

    
sam = Dog( )
sam.makeSound( )

'''STATIC METHODS'''
# Like global attributes, you may have methods that are accessible through the class itself
# rather than an instance of the class. These may also be known as static methods.

class Dog( ):
    sound = "bark"
    def makeSound(self):
        print(self.sound)
    def printInfo( ):
        print("I am a dog.")


Dog.printInfo( ) # able to run printInfo method because it does not include self parameter
# Dog.makeSound( ) would produce error, self is in reference to instances only
sam = Dog( )
sam.makeSound( ) # able to access, self can reference the instance of sam
# sam.printInfo( ) will produce error, instances require the self parameter to access methods

'''PASSING ARGUMENTS INTO METHODS'''

# When these arguments are passed in, they do not need to be
# referenced with the self parameter, as they are not attributes, but rather temporary
# variables that the method can use:


class Dog( ):
    def showAge(self, age):
        print(age) # does not need self, age is referencing the parameter not an attribute


sam = Dog( )
sam.showAge( 6 ) # passing the integer 6 as an argument to the showAge method


'''PASSING SETTERS AND GETTERS'''
# They are methods that you
# create to re-declare attribute values and return attribute values

# using methods to set or return attribute values, proper programming practice
class Dog( ):
    name = ' ' # would normally use init method to declare, this is for testing purposes
    def setName(self, new_name):
        self.name = new_name # declares the new value for the name attribute
    def getName(self):
        return self.name # returns the value of the name attribute

    
sam = Dog( )
sam.setName("Sammi")
print( sam.getName( ) ) # prints the returned value of self.name


'''METHODS CALLING METHODS'''

# When calling a method from another method, you need to use the self parameter

class Dog( ):
    age = 6
    def getAge(self):
        return self.age
    def printInfo(self):
        if self.getAge( ) < 10: # need self to call other method for an instance
            print("Puppy!")

            
sam = Dog( )
sam.printInfo( )