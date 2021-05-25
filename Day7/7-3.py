###<<<STEP 3>>>###
'''
Make sure that user can keep guessing letters
So use a loop
'''
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
end_of_game=False

while not end_of_game:    #so while it is not end of the game,repeat all these steps.

    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    print(display)
    
    if "_" not in display:   #in keyword to see if it is in list
        #now user has won
        end_of_game=True     #now you can exit the while loop as condition has been changed


print("You have won")
