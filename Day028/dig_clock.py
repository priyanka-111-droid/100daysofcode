# Creating a digital GUI clock

from tkinter import *
import time
FONT = ("Courier",68,"bold")
BGCOLOR = "#f2e750"
FGCOLOR= "#363529"


window=Tk()
window.title("Digital Clock")
window.minsize(width=410,height=110)
label=Label(window,font=FONT,bg=BGCOLOR,fg=FGCOLOR)
label.grid(row=0,column=1)
def digital_clock():
    time_live=time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200,digital_clock)

digital_clock()


window.mainloop()