#TODO 1:Create separate Paddle class and move all paddle funcionality to that class
#TODO 2:then instantiate objects r_paddle and l_paddle from that class.

from turtle import Screen,Turtle 
from paddle import Paddle


screen=Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong game")

screen.tracer(0) #to turn off animation

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0)) #pass tuple for location of paddle


#move up and down with keystrokes
screen.listen()
screen.onkey(r_paddle.go_up,"Up")  
screen.onkey(r_paddle.go_down,"Down") 
screen.onkey(l_paddle.go_up,"w") 
screen.onkey(l_paddle.go_down,"s") 


#for paddle to go directly to position instead of starting from centre then moving there
#while loop as for each time game is on,we want paddle to go to initial position directly
game_is_on=True
while game_is_on:
    screen.update()


screen.exitonclick()
