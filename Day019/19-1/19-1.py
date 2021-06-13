from turtle import Turtle,Screen 

tim=Turtle()
screen=Screen()

def move_right():
    tim.forward(20)
def move_left():
    tim.backward(20)
def move_clock():
    tim.right(20)
def move_counterclock():
    tim.left(20)
def clear_screen():
    tim.setposition(0,0) #return to center of screen
    tim.setheading(0)   #set turtle pointing to right again(default)
    
    # tim.home()    #this command does both of above commands 
    tim.clear()

screen.listen()
screen.onkey(fun=move_right,key="w")
screen.onkey(fun=move_left,key="s")
screen.onkey(fun=move_clock,key="a")
screen.onkey(fun=move_counterclock,key="d")
screen.onkey(fun=clear_screen,key="c")

screen.exitonclick()
