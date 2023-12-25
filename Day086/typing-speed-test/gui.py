import tkinter as tk
from time import time
from prompts import prompt_data
import random


YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
question_counter = 1 #by default 1, since we start with 1 question.
total_gross_wpm = 0
total_net_wpm = 0
total_accuracy = 0
start_time=0
end_time=0
prompt=""
total_typed_text=""


def download_story():
    file = open("./story.txt", "a")
    file.write(total_typed_text)
    file.close()
    

def display_result():
    next_button.config(state=tk.DISABLED)
    done_button.config(state=tk.DISABLED)
    gross_wpm_value.config(text=f"Gross Typing speed: {total_gross_wpm / float(question_counter):.2f} gross WPM")
    net_wpm_value.config(text=f"Net typing speed: {total_net_wpm / float(question_counter):.2f} net WPM")
    accuracy_value.config(text=f"Accuracy: {total_accuracy / float(question_counter):.2f}%")

    #enable the download story option for user to see their story.
    download_button.config(state='active')


def each_question():
    global total_gross_wpm, total_net_wpm, total_accuracy, total_typed_text

    # Gross WPM calculation
    typed_text = entry_field.get("1.0", "end-1c")  # Get text from the Text widget
    end_time = time()
    time_elapsed = end_time - start_time
    time_elapsed_in_min = time_elapsed / 60
    characters_typed = len(typed_text)
    word_count = characters_typed / 5
    gross_wpm = word_count / time_elapsed_in_min


    # Net WPM calculation
    errors = sum(1 for char1, char2 in zip(typed_text, prompt) if char1 != char2)
    correct_chars = characters_typed - errors
    net_wpm = (correct_chars / 5) / (time_elapsed_in_min) 

    # Accuracy calculation
    # Avoid division by zero and correct accuracy calculation
    if characters_typed > 0:
        accuracy = (correct_chars / characters_typed) * 100
    else:
        accuracy = 0


    total_gross_wpm += gross_wpm
    total_net_wpm += net_wpm
    total_accuracy += accuracy

    total_typed_text+=typed_text+"\n"

    display_result()
    
    




def next_question():
    global prompt
    global start_time, question_counter, end_time
    global total_gross_wpm, total_net_wpm, total_accuracy,total_typed_text


    typed_text = entry_field.get("1.0", "end-1c")
    characters_typed = len(typed_text)

    # Capture the end time for the current question
    end_time = time()

    # Calculate the gross WPM for the current question
    time_elapsed = end_time - start_time
    time_elapsed_in_min = time_elapsed / 60
    word_count = characters_typed / 5
    gross_wpm = word_count / time_elapsed_in_min


    # Net WPM calculation
    errors = sum(1 for char1, char2 in zip(typed_text, prompt) if char1 != char2)
    correct_chars = characters_typed - errors
    net_wpm = (correct_chars / 5) / (time_elapsed_in_min) 

    # Accuracy calculation
    # Avoid division by zero and correct accuracy calculation
    if characters_typed > 0:
        accuracy = (correct_chars / characters_typed) * 100
    else:
        accuracy = 0

    #calculate totals
    total_gross_wpm += gross_wpm
    total_net_wpm += net_wpm
    total_accuracy += accuracy

    #combine all typed text to form story
    total_typed_text+=typed_text+"\n"

    #increment number of questions by 1
    question_counter+=1

    # Reset the start time for the new question
    start_time = time()

    # Reset the entry field
    entry_field.delete("1.0", "end")

    # Display the next question
    new_prompt = random.choice(prompt_data)["sentence"]
    prompt = new_prompt
    prompt_label.config(text=prompt)






# ------------- UI set up -------------#
window = tk.Tk()
start_time=time()
window.title("Typing Speed test")
window.config(padx=70, pady=50, bg=YELLOW)

instruction_label = tk.Label(
    text="Enter as fast as possible", bg=YELLOW, font=(FONT_NAME, 18)
)
instruction_label.grid(column=1, row=0)
instruction_label.config(padx=10, pady=20)


prompt = random.choice(prompt_data)["sentence"]
prompt_label = tk.Message(window,text=prompt,bg=YELLOW, font=(FONT_NAME, 14),justify='center')
prompt_label.grid(column=1, row=1)



entry_field = tk.Text(window, height = 5, width = 60) #multiline text field
entry_field.grid(column=1, row=2)
entry_field.focus()


#buttons
done_button = tk.Button(text="Done", highlightthickness=0, command=each_question)
done_button.grid(column=1, row=3)

next_button = tk.Button(text="Next",highlightthickness=0, command=next_question)
next_button.grid(column=2,row=3)

download_button = tk.Button(text="Download Story",highlightthickness=0, command=download_story,state=tk.DISABLED)
download_button.grid(column=0,row=3)


#labels and values to show results
gross_wpm_label = tk.Label(text="Gross WPM: ", bg=YELLOW, font=(FONT_NAME, 12))
gross_wpm_label.grid(column=0, row=4)
gross_wpm_value = tk.Label(text="0", bg=YELLOW, font=(FONT_NAME, 12))
gross_wpm_value.grid(column=1, row=4)


net_wpm_label = tk.Label(text="Net WPM: ", bg=YELLOW, font=(FONT_NAME, 12))
net_wpm_label.grid(column=0, row=5)
net_wpm_value = tk.Label(text="0", bg=YELLOW, font=(FONT_NAME, 12))
net_wpm_value.grid(column=1, row=5)


accuracy_label = tk.Label(text="Accuracy: ", bg=YELLOW, font=(FONT_NAME, 12))
accuracy_label.grid(column=0, row=6)
accuracy_value = tk.Label(text="0", bg=YELLOW, font=(FONT_NAME, 12))
accuracy_value.grid(column=1, row=6)


window.mainloop()

