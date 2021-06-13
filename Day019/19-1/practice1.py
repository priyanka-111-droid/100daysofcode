#practice-1
#using event listener listen()

from turtle import Turtle,Screen

tim=Turtle()
screen=Screen()

def move_forward():
    tim.forward(10)

screen.listen()

#only if I hit space bar,move_forward() should be called
screen.onkey(fun=move_forward,key="space")
#Also tip:when you are using methods we have not created like onkey()
#use keyword arguments instead of positional arguments


screen.exitonclick()

