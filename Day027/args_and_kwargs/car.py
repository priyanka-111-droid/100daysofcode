class Car:
    def __init__(self,**kw):
        # self.make=kw["make"]
        self.make=kw.get("make")
        # self.model=kw["model"]
        self.model=kw.get("model")

        #If we use get instead of square brackets,code won't crash incase we don't pass argument
        #it will just return 0.

my_car=Car(make="Nissan")
print(my_car.model)
