import turtle,pandas

screen=turtle.Screen()
screen.title("US States Guessing Game")
screen.bgpic("Day025/Project/blank_states_img.gif")


#Store csv file contents as list
data=pandas.read_csv("Day025/Project/50_states.csv")
data_list=data.state.to_list()
guessed_states=[]
missed_states=[]
incorrect=0  #tracks when user enters wrong spelling or any word that is NOT a US State.

while(len(guessed_states)<50):
    #Ask user to enter name of state,we are using title() to make sure that user can enter lowercase too.
    guess=screen.textinput(title=f"Correct: {len(guessed_states)} Incorrect: {incorrect}",prompt="What's another state's name?").title()

    if guess in data_list:
        #to make sure user does not guess same state again
        if guess not in guessed_states: 
            guessed_states.append(guess)
            #get x and y coordinates from state user has guessed
            info_abt_guess=data[data["state"]==guess]
            x_guess=info_abt_guess["x"]
            y_guess=info_abt_guess["y"]
            #create turtle object and go to that location on map
            t=turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(int(x_guess),int(y_guess)) #convert it to int first!
            t.write(guess)

    elif(guess=="Exit" or guess=="E"):
        break 
    else:
        incorrect+=1



# screen.exitonclick() not needed as now when user types e or exit,we want to close game.

#creates new csv file showing all states we missed.
list_of_all_states=data["state"]
for x in list_of_all_states:
    if x not in guessed_states:
        missed_states.append(x)

d={"Missed states":missed_states} #creating dictionary
new_data=pandas.DataFrame(d)
new_data.to_csv("Day025/Project/states_you_missed.csv")



