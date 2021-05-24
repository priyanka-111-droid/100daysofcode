###<<<CHALLENGE>>>###
'''
Hurdle race 3:
Reeborg has entered a hurdle race. Make him run the course, following the path shown.
The position and number of hurdles changes each time this world is reloaded.
What you need to know
1.The functions move() and turn_left().
2.The conditions front_is_clear() or wall_in_front(), at_goal(), and their negation.
3.How to use a while loop and an if statement.

Please type this solution in Reeborg python editor!
'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()