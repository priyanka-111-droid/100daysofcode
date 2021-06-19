
'''
Create a Dog class that has one global attribute and two instance level
attributes. The global attribute should be “species” with a value of “Canine.”
The two instance attributes should be “name” and “breed.” Then instantiate
two dog objects, a Husky named Sammi and a Chocolate Lab named Casey.
'''
class Dog():
    species="Canine"
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed

dog1=Dog("Sammi","Husky")
dog2=Dog("Casey","Chocolate Lab")


# species is global attribute so can be referenced by the class directly and all its instances.
print(Dog.species)

print(dog1.name)
print(dog1.breed)
print(dog1.species)

print(dog2.name)
print(dog2.breed)
print(dog2.species)