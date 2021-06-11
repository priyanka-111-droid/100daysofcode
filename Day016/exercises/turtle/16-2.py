from turtle import Turtle,Screen

#turtle object from Turtle class
my_turtle=Turtle()
#turtle object's methods
my_turtle.shape("turtle")
my_turtle.color("chartreuse")
my_turtle.forward(100)



#screen object from Screen class
my_screen=Screen()
#screen object's attribute canvheight
print(my_screen.canvheight)
#screen object's method exitonclick()
my_screen.exitonclick()