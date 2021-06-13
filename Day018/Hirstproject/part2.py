#Hirst project-part 2
#Drawing dots of the painting. 

from part1 import colour_list
import turtle as t
import random 

#need to write colormode() to make sure turtle can read rgb values.
t.colormode(255)

#creating turtle object tim
tim=t.Turtle()
tim.penup()
tim.speed("fastest")
#initially position starts from bottom left part of screen
posx=-220
posy=-200

#we will be painting 10 rows of spots
for rows in range(10):
    tim.setposition(posx,posy)
    for x in colour_list:
        tim.dot(20,random.choice(colour_list))
        tim.penup()
        tim.forward(50)
    #after each row,increase position of y by 40 units upward for next row
    posy+=40

# screen object
my_screen=t.Screen()
my_screen.exitonclick()



