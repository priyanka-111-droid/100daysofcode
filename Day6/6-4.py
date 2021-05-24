###<<<CHALLENGE>>>###
'''
Reeborg has entered a hurdle race. Make him run the course, following the path shown.
The position, the height and the number of hurdles changes each time this world is reloaded.

Please type in Reeborg python editor!
'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    while wall_on_right():
        move()
        
    turn_right()
    move()
    turn_right()
    
    while front_is_clear():
        move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
   