from turtle import Screen
from snake import Snake
import time 


screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0) #turn off tracer



#create object snakey from Snake
snake_obj=Snake()

game_is_on=True 
while game_is_on:
    screen.update()
    time.sleep(0.1)  #delay by 0.1sec,refresh screen

    #each time screen refreshes,move snake forward by 20
    snake_obj.move()




screen.exitonclick()