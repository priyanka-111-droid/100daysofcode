FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()  #only track level,no need to see turtle 
        self.level=0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()  #to clear up previous score,display new one
        self.goto(-260,260) # player's level
        self.write(f"Level {self.level}",align="left",font=FONT)
        

    def point(self):
        self.level+=1  #increase score,update scoreboard
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="center",font=FONT)

