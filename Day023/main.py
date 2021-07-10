import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
screen.listen()
screen.onkey(player.go_up,"Up") 

car=CarManager()

scoreboard=Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.go_left()

    #detect collision with car
    for c in car.all_cars:
        if c.distance(player)<20:
            game_is_on=False 
            scoreboard.game_over()

    #detect successful crossing
    if(player.reached_top()):
        scoreboard.point()
        player.go_to_start()
        car.level_up()



screen.exitonclick()



# 1.Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle north.

# 2.Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge of the screen. No cars should be generated in the top and bottom 50px of the screen (think of it as a safe zone for our little turtle). Hint: generate a new car only every 5th time the game loop runs.

# 3.Detect when the turtle player collides with a car and stop the game if this happens.

# 4.Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y). When this happens, return the turtle to the starting position and increase the speed of the cars. Hint: think about creating an attribute and using the MOVE_INCREMENT to increase the car speed.

# 5.Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a successful crossing, the level should increase. When the turtle hits a car, GAME OVER should be displayed in the centre. 

