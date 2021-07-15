# Layout managers in Tkinter are
# pack(),place(),grid()
# place():need exact coordinates
# grid():relative to other components
#So while using grid(),start with widget at top left,define as 0,0 and then move on to other widgets.
# Also don't mix grid() and pack() together in same master window

import tkinter

window=tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500,height=300)
#to add padding
window.config(padx=20,pady=20)


#Label
my_label=tkinter.Label(text="I am a Label",font=("Arial",24,"bold"))
my_label["text"]="New text" #changing intiial text

# my_label.place(x=0,y=0)
my_label.grid(column=0,row=0)

#add padding to each individual widget
my_label.config(padx=50,pady=50)


#event listener
def button_clicked():
    # print("Button got clicked!")
    # my_label["text"]="Button got clicked!"
    ans=input.get()       #type in text field and click button,text will be displayed in place of "New text"
    my_label["text"]=ans



#Button
button=tkinter.Button(text="Click here",command=button_clicked)
# button.pack()
button.grid(column=1,row=1)

#Entry
input=tkinter.Entry(width=10)  #create text field
# input.pack()  
input.grid(column=2,row=2)


# while True:
#     listening
window.mainloop()