'''
Exercise -1:
Use turtle module and draw a square
'''
from turtle import Turtle,Screen

#turtle object
my_turtle=Turtle()
my_turtle.shape("turtle")
# my_turtle.forward(100)
# my_turtle.right(90)
# my_turtle.forward(100)
# my_turtle.right(90)
# my_turtle.forward(100)
# my_turtle.right(90)
# my_turtle.forward(100)

for x in range(4):
    my_turtle.right(90)
    my_turtle.forward(100)


#screen object
my_screen=Screen()
my_screen.exitonclick()