
####<<<<STEP 1>>>>####
'''Picking random words,checking answers'''

import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word=random.choice(word_list)
print(f"Word chosen is {chosen_word}") #not needed ,just to test program

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess=input("Guess a letter :").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in chosen_word: #run a loop through each letter in the chosen word
    if letter==guess:
        print("Right")   
    else:
        print("Wrong")
