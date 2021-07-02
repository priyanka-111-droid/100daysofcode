from turtle import Screen,Turtle

#TODO 1:Set up screen
screen=Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong game")

screen.tracer(0) #to turn off animation

#TODO 2:create a paddle and move paddle up and down
paddle=Turtle()
paddle.shape("square")
paddle.color("white")
#to stretch it so that 20x100 pixels
paddle.shapesize(stretch_wid=5,stretch_len=1)

#to move this paddle

paddle.penup()
paddle.goto(350,0)

def go_up():
    new_y=paddle.ycor()+20
    paddle.goto(paddle.xcor(),new_y)

def go_down():
    new_y=paddle.ycor()-20
    paddle.goto(paddle.xcor(),new_y)


#move up and down with keystrokes
screen.listen()
screen.onkey(go_up,"Up")  #no parenthesis ,else won't work
screen.onkey(go_down,"Down") 


#for paddle to go directly to position instead of starting from centre then moving there
#while loop as for each time game is on,we want paddle to go to initial position directly
game_is_on=True
while game_is_on:
    screen.update()



screen.exitonclick()
