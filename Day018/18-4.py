import turtle as t
import random

my_turtle=t.Turtle()
angle=[0,90,180,270]
my_turtle.pensize(5) #Set the line thickness to width
my_turtle.pencolor("green")#we can also change pen colour


for _ in range(100):
    my_turtle.forward(30)
    my_turtle.setheading(random.choice(angle))


# screen object
my_screen=t.Screen()
my_screen.exitonclick()