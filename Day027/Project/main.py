#Miles to km converter
from tkinter import *

window=Tk()
window.title("Miles to Km Converter")
window.minsize(width=400, height=120)


#Entry
input=Entry(width=10)  #create text field
input.place(x=150,y=30)


#Label for miles
label1=Label(text="Miles",font=("Arial",12))
label1.place(x=250,y=30)

#Label for is equal to
label2=Label(text="is equal to",font=("Arial",12))
label2.place(x=50,y=60)


#Label for answer
label3=Label(text="",font=("Arial",12))
label3.place(x=170,y=60)

def button_clicked():
    ans=float(input.get())    
    km=(ans * 1.609344)
    label3["text"]=round(km,2)
#Button
button=Button(text="Calculate",command=button_clicked,font=("Arial",12))
button.place(x=154,y=100)

#Label for Km
label4=Label(text="Km",font=("Arial",12))
label4.place(x=250,y=60)


window.mainloop()
