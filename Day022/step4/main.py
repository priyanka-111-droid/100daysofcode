#TODO 1:create separate Ball class
#TODO 2:instantiate ball object,ball should start from center and then move towards top right each time screen refreshes

from turtle import Screen,Turtle 
from paddle import Paddle
from ball import Ball
import time


screen=Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong game")


#to move paddles and move ball directly to positions instead of starting from center
screen.tracer(0) #to turn off animation

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0)) #pass tuple for location of paddle
ball=Ball()

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
    time.sleep(0.1)
    screen.update()
    ball.move()
    #Detect collision with top or bottom part of screen
    
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()


screen.exitonclick()
