#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER="[name]"

#using absolute linking(based on MY MACHINE ONLY)
with open("C:/Users/Admin/Documents/GitHub/100daysofcode/Day024/mailmergerproject/Input/Names/invited_names.txt") as names_f:  
    names=names_f.readlines()  #list of names


with open("C:/Users/Admin/Documents/GitHub/100daysofcode/Day024/mailmergerproject/Input/Letters/starting_letter.txt") as letter_f:
    letter_contents=letter_f.read()
    for name in names:
        stripped_name=name.strip()
        new_letter=letter_contents.replace(PLACEHOLDER,stripped_name)
        # print(new_letter)
        with open(f"C:/Users/Admin/Documents/GitHub/100daysofcode/Day024/mailmergerproject/Output/ReadyToSend/letter_for_{stripped_name}.txt",mode="w") as completed_letter:
            completed_letter.write(new_letter)




  




       



        
    



