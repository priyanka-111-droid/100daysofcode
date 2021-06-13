import turtle as t

my_turtle=t.Turtle()
#lift turtle up and move it somewhere else
my_turtle.penup()
#shifting it somewhere in top left part of screen
my_turtle.setposition(-60,100)
#put turtle down so that it can draw again
my_turtle.pendown()

#for shape eg.pentagon,angle made=360/number of sides(5)


for num_side in range(3,11):
    for _ in range(num_side):
        angle=360/num_side
        my_turtle.forward(100)
        my_turtle.right(angle)



# screen object
my_screen=t.Screen()
my_screen.exitonclick()