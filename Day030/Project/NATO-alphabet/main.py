import pandas
data=pandas.read_csv("Day030/Project/NATO-alphabet/nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:(already done in day 26)
phonetic_dict={ row.letter:row.code for (index,row) in data.iterrows()}
# print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.(already done in day 26)
# word=input("Enter a word :").upper()
# result=[phonetic_dict[x]  for x in word]
# print(result)

#TODO 3.If user enters numbers or anything not a alphabet,get a message saying "Sorry,only letters in alphabet please."
#This will keep displaying till user enters a valid word

def generate_phonetic():
    word=input("Enter a word :").upper()
    try:
        result=[phonetic_dict[x]  for x in word]
    except KeyError:
        print("Sorry,only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(result)



generate_phonetic()
