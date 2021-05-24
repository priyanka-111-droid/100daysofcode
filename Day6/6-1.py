###<<<CHALLENGE>>>###
'''
To jump hurdles and carry Reborg from (x,y)=(1,1) to (13,1)
Basic level - use move() and turn_left()
Advanced level-define function named jump() and use that

#Please write the code below in Reeborg's world text editor !
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

#total 6 steps being repeated so (1,7) or (0,6) both are accepted   
for robot in range(1,7):
    jump()

