from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()  #only track score,no need to see turtle 
        self.l_score=0
        self.r_score=0
        self.update_scoreboard()


    #call update_board() with score 0,0 in the beginning and also when each player scores a point
    def update_scoreboard(self):
        self.clear()  #to clear up previous score,display new one
        self.goto(-100,200) #left player's score
        self.write(self.l_score,align="center",font=("Courier",80,"normal"))
        self.goto(100,200)  #right player score
        self.write(self.r_score,align="center",font=("Courier",80,"normal"))

        
    def l_point(self):
        self.l_score+=1  #increase score,update scoreboard
        self.update_scoreboard()

    def r_point(self):
        self.r_score+=1  #increase score,update scoreboard
        self.update_scoreboard()
