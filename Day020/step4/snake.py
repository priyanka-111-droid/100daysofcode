#step 4-adding controls for snake.up,snake.down,snake.left and snake.right
#also checked that if snake is moving right,it can't move left,if moving up,can't move down(opposite direction)
#as per rules of game

from turtle import Turtle 

#constant
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0


class Snake:
    def __init__(self):
        self.snake=[]
        self.create_snake()
        #since we will keep using head of snake,separate attribute
        self.head=self.snake[0]


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
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        #changing head of snake to point north
        if(self.head.heading()!=DOWN):
            self.head.setheading(UP)
        # self.snake[0].left(90)  also correct
       
    def down(self):
        if(self.head.heading()!=UP):  #turtle has heading method
            self.head.setheading(DOWN)
    def right(self):
        if(self.head.heading()!=LEFT):
            self.head.setheading(RIGHT)
    def left(self):
        if(self.head.heading()!=RIGHT):
            self.head.setheading(LEFT)


        







