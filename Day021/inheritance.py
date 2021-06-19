# Demo of how inheritance works
#One class inherits attributes and methods from another class

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):   #Fish class inherits from Animal class
    def __init__(self):
        super().__init__()    #Fish class inherits from super class(Animal class)

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.breathe()

