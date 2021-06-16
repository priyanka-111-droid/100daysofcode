#step 4:adding control using keyboard keys

from turtle import Screen
from snake import Snake
import time 


screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0) #turn off tracer


snake_obj=Snake()

#adding control using keyboard arrow keys
screen.listen()
screen.onkey(snake_obj.up,"Up")
screen.onkey(snake_obj.down,"Down")
screen.onkey(snake_obj.left,"Left")
screen.onkey(snake_obj.right,"Right")



game_is_on=True 
while game_is_on:
    screen.update()
    time.sleep(0.1)  
    snake_obj.move()
    


screen.exitonclick()