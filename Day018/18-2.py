import turtle as t

my_turtle=t.Turtle()


my_turtle.penup()

#make turtle's initial position towards left of screen instaed of centre
# my_turtle.goto(-300,0)
my_turtle.setposition(-300,0)


for _ in range(15):   
    #can use _ or x both allowed
    #we use _ instead of variable if we
    # are not going to be using variable much inside loop

    my_turtle.pendown()
    my_turtle.forward(20)
    my_turtle.penup()
    my_turtle.forward(20)



# screen object
my_screen=t.Screen()
my_screen.exitonclick()