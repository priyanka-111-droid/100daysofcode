import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance=random.randint(1,6)
        if(random_chance)==1:
            new_car=Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.goto((280,random.randint(-250,250)))
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def go_left(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed+=MOVE_INCREMENT



        

    
