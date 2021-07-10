from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90) #facing north
        self.go_to_start()

    
    def go_up(self):
        self.forward(MOVE_DISTANCE)


    def reached_top(self):
        if self.ycor()>FINISH_LINE_Y:
            return True 
        else:
            return False
            
    def go_to_start(self):
        self.goto(STARTING_POSITION)





