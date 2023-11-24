#Assignment 1 - Text to morse code converter

morse_dictionary={
    "a":".-","b":"-...","c":"-.-.","d":"-..",
    "e":".","f":"..-.","g":"--.","h":"....",
    "i":"..","j":".---","k":"-.-","l":".-..",
    "m":"--","n":"-.","o":"---","p":".--.",
    "q":"--.-","r":".-.","s":"...","t":"-",
    "u":"..-","v":"...-","w":".--","x":"-..-",
    "y":"-.--","z":"--.."
}


def text_to_morse():
    s = input("Please enter text: ").lower()
    new_str=""
    for char in s:
        new_str+=morse_dictionary[char]

    print(f"Morse code : {new_str}")



def welcome():
    print('''
        ###############<<<<<<<<<<<<<<TEXT2MORSE>>>>>>>>>>>>>#################
          
                            Welcome to text 2 morse !!!
        ''')
    
    while True:
        choice = int(input("Enter 1 to enter text and 2 to exit."))
        if choice==1:
            text_to_morse()
        else:
            break
    
    print("Thank you! have a nice day ahead :)")


welcome()
