# step2:keep moving snake
#use tracer and update method

from turtle import Turtle,Screen
import time 


screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0) #turn off tracer
starting_pos=[(0,0),(-20,0),(-40,0)]
snake=[]
for position in starting_pos:
    new_segment=Turtle("square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(position)
    snake.append(new_segment)

#call update to refresh screen after segment creation
#now full snake moves together,NOT piece by piece but entire snake

game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1) #snake too fast,to slow it down,see what is happening

    for seg_num in range(len(snake)-1,0,-1):
        new_x=snake[seg_num-1].xcor() #second to last segment
        new_y=snake[seg_num-1].ycor()
        snake[seg_num].goto(new_x,new_y)

    snake[0].forward(20)




screen.exitonclick()
