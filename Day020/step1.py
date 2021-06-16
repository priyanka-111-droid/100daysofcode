#Step 1:setting screen and creating snake body

from turtle import Turtle,Screen
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake game")


#1.create 3 white squares(turtles) lined up next to each other

# segment_1=Turtle("square")
# segment_1.color("white")


# segment_2=Turtle("square")
# segment_2.color("white")
# segment_2.goto(-20,0)

# segment_3=Turtle("square")
# segment_3.color("white")
# segment_2.goto(-40,0)

starting_pos=[(0,0),(-20,0),(-40,0)]
for position in starting_pos:
    new_segment=Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)


screen.exitonclick()
