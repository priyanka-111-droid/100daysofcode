###<<<CHALLENGE>>>>###
'''
Hurdles challenge 2:
Reeborg has entered a hurdle race, but he does not know in advance how long the race is.
Make him run the course, following a path similar to the one shown, but stopping at the only flag
that will be shown after the race has started.
What you need to know:
1.The functions move() and turn_left().
2.The condition at_goal() and its negation.
3.How to use a while loop.

Please type the below code in Reeborg editor!
'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    jump()


