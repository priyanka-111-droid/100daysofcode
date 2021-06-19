# Demo of how inheritance works
#One class inherits attributes and methods from another class

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):   #Fish class inherits from Animal class
    def __init__(self):
        super().__init__()    #using super() method to declare inherited attributes

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.breathe()

# Overriding methods defined in super class
class Animal( ):
    def makeSound(self):
        print("roar")
class Dog(Animal):
    def makeSound(self):
        print("bark")
    
    
sam, lion = Dog( ), Animal( ) # declaring multiple variables on a single line
sam.makeSound( ) # overriding will call the makeSound method in Dog
lion.makeSound( ) # no overriding occurs as Animal does not inherit anything



