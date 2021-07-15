#Creating windows and labels with Tkinter
import tkinter

window=tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500,height=300)


#Label
my_label=tkinter.Label(text="I am a Label",font=("Arial",24,"bold"))
my_label.pack() #place it in screen and center it else you won't see label
# my_label.pack(side="left") #label is displayed to the left
# my_label.pack(side="bottom") #label displayed on bottom
# my_label.pack(expand=True) #will take up full height and width of available screen size
my_label["text"]="New text" #changing intiial text
# my_label.config(text="New text")  #another way to write

#Entry
# input=tkinter.Entry(width=10)
# input.pack()
# ans=input.get()

input=tkinter.Entry(width=10)  #create text field
input.pack()  

#event listener
def button_clicked():
    # print("Button got clicked!")
    # my_label["text"]="Button got clicked!"
    ans=input.get()       #type in text field and click button,text will be displayed in place of "New text"
    my_label["text"]=ans



#Button
button=tkinter.Button(text="Click here",command=button_clicked)
button.pack()


# while True:
#     listening
window.mainloop()