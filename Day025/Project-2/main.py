import turtle,pandas,random
X_INIT=-300
Y_INIT=120
MOVE_DIST=40
FONT = ("Courier", 24, "normal")

screen=turtle.Screen()
screen.title("Score and words missed")
screen.screensize(400,300)
print(screen.screensize())

data=pandas.read_csv("Day025/Project-2/spanish_word.csv")
#making 2 lists having spanish words and english words respectively
spanish_list=data["Spanish"].to_list()
english_list=data["English"].to_list()

#making dictionary where each spanish word is matched with its english meaning
d={spanish_list[i]:english_list[i] for i in range(len(spanish_list))}


number_of_words=10
correct=0
incorrect=0
game=random.sample(spanish_list,number_of_words)



#Incorrect words heading 
heading=turtle.Turtle()
heading.hideturtle()
heading.penup()
heading.goto(-130,180)
heading.write(f"Incorrect words:",align="left",font=FONT)


i=0
while(number_of_words>0):
    guess=screen.textinput(title=f"Correct: {correct} Incorrect: {incorrect}",prompt=f"{game[i]}:").lower()
    if guess==d[game[i]]:
        correct+=1
    else:
        incorrect+=1
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(X_INIT,Y_INIT) 
        t.write(f"{game[i]} : {d[game[i]]}",font=FONT)
        Y_INIT=Y_INIT-MOVE_DIST

    number_of_words-=1
    i+=1

#score display
score=turtle.Turtle()
score.hideturtle()
score.penup()
score.goto(-100,230)
score.write(f"Score:{correct}/10\n",align="left",font=FONT)

screen.exitonclick()




    

        







