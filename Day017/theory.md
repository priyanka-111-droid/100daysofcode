# Creating our own class 
Let us say we are creating a User blueprint(class) for a user on Instagram.

## Creating  object from class

        class User:
            #If you declare a class or function with semicolon and leave it empty,
            #python gives an error saying indent expected.
            #If you want to leave class or function empty,use pass
            #We want to leave my User class empty for now so,

            pass

        #object creation from class
        user_1=User()
        user_2=User()


## Creating attributes,class constructors and ` __init__()` function


### Attributes

        user_1.id="001"
        user_1.username="xyz"
        print(user1.id)
        user_2.id="007"
        user_2.username="Bond"

### Constructor

Part of class that specifies what happens if object is constructed.This is also called initializing an object or setting variables to starting values.

        class User:
            def __init__(self):
                print("New user being created")

                #each time object being created(user_1 and user_2 in this case),above line is printed.
        
### Setting attributes in constructor

If we are creating lot of objects with same attributes,

        class User:
            def__init__(self,user_id,username):
                #self:actual object being created
                #user_id,username:parameters passed in to initialize object when object is constructed from class
                #use  parameters to set object's attributes

                self.id=user_id
                self.username=username


        user_1=User("001","xyz")
        user_2=User("007","Bond")
        print(user_1.id)

### Setting attributes to 0

Let's say that we want to keep track of number of followers and following for each user in Instagram.Initially both  will be 0.Instead of passing a followers parameter into the ` __init__() ` for each object we can set a default value of 0 as shown below.


        class User:
            def__init__(self,user_id,username):

                self.id=user_id
                self.username=username
                self.followers=0
                self.following=0


        user_1=User("001","xyz")
        user_2=User("007","Bond")
        print(user_1.followers)  #gives 0
        print(user_1.following) #gives 0


## Creating Methods in class

Let's say that we want our users to follow each other.
Now,A method unlike a function, always need to have self parameter as first parameter.When method is called,it knows object that called it.

self keyword is way to refer to object created from class inside class blueprint.

        class User:
            def__init__(self,user_id,username):

                self.id=user_id
                self.username=username
                self.followers=0
                self.following=0

            def follow(self,user):
                #person we are following increases number of followers
                user.followers+=1
                #our following increases 
                self.following+=1

        
        user_1=User("001","xyz")
        user_2=User("007","Bond")
        user_1.follow(user_2)
        print(user_1.followers) #0
        print(user_1.following) #1
        print(user_2.followers) #1
        print(user_2.following) #0
        







