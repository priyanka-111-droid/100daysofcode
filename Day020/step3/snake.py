from turtle import Turtle 

#constant
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20

class Snake:
    def __init__(self):
        self.snake=[]
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment=Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.snake.append(new_segment) #referring to attribute snake


    def move(self):
        for seg_num in range(len(self.snake)-1,0,-1):
            new_x=self.snake[seg_num-1].xcor() #second to last segment
            new_y=self.snake[seg_num-1].ycor()
            self.snake[seg_num].goto(new_x,new_y)
        self.snake[0].forward(MOVE_DISTANCE)






