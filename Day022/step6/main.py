
from turtle import Screen,Turtle 
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
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
scoreboard=Scoreboard()


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
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #Detect collision with top or bottom part of screen
    
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    #Detect collision with paddle
    
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()

    #detect R paddle misses
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()  #right player misses,left gets point

    #detect L paddle misses
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
