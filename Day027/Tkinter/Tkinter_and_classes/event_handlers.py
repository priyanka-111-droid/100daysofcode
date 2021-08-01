#Here,let us write event handlers and bind them to events
#Create a Tkinter program that has a button and the button's event handler updates number of times button is clicked.
from tkinter import *

class Application(Frame):
    def __init__(self,master):
        super(Application,self).__init__(master)
        self.grid()
        self.bttn_clicks=0
        self.create_widget()
    def create_widget(self):
        '''create button that displays number of clicks'''
        self.bttn=Button(self)
        self.bttn["text"]="Total clicks:0"
        #here we bind an event(clicking of Button widget) to an event handler(update_count() method)
        self.bttn["command"]=self.update_count
        self.bttn.grid()
    
    def update_count(self):
        '''increase click count and display new total'''
        self.bttn_clicks+=1
        self.bttn["text"]="Total Clicks: "+str(self.bttn_clicks)


#main
root=Tk()
root.title("Click the button")
root.minsize(width=300,height=85)
app=Application(root)
root.mainloop()

    