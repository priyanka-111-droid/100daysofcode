##<<<Project:Caesar Cipher-part 1>>>##

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text,shift_amount):

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    #text="zulu"
    #shift = 5
    #cipher_text = "ezqz"
    #print output: "The encoded text is ezqz"
    cipher_text="" #initialize string before use else it might have garbage value

    #running for loop through string text
    for letter in plain_text:
        #METHOD 1:using index()

        #from alphabet list,get index(starts from 0)of each letter present in text
        position = alphabet.index(letter)
        #get new position by adding position and shift
        new_position = position+shift_amount
        #get new letter at the new position in alphabet list 
        #In case text has letters at end of alphabet list like zulu with letter z,
        #after adding shift,we can get index out of range error
        #since new_position is OUT of alphabet list
        #Hence we do new_position-26(number of lowercase alphabets) so that z+5 will give us letter 'e'
        #In python index can be negative 
        #so for any letter whose new_position is IN the alphabet list,letter-26 will give that letter again
        #Thus, this can work for letters like x,y,z at end of list and letters like a,b,c,d too

        cipher_letter=alphabet[new_position-26] 
        #add new letter to cipher text
        cipher_text = cipher_text + cipher_letter


        # METHOD 2:using ord() and chr()
        
        #we do not need alphabet list for this method...
        # ord(letter) : gives ascii value of letter
        # chr(number) : gives character at that ascii value
        # cipher_letter=chr(ord(letter)+shift)    #convert to ascii using ord(),shift it,then get new cipher letter using chr()
        # if(cipher_letter <'a'or cipher_letter>'z'): #if cipher letter is not from a to z
        #     cipher_letter=chr((ord(letter)+shift)-26) #get new cipher letter by subtracting 26 
        # cipher_text=cipher_text+cipher_letter  #concat each cipher letter into cipher_text


    print(f"The encoded text is {cipher_text}")
    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list



#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

encrypt(plain_text=text,shift_amount=shift) 