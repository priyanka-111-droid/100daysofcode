#(using classes)Create tkinter window with three buttons that don't do anything when you click them.
from tkinter import *

#Creating new class Application based on Frame
class Application(Frame):
    '''GUI application with three buttons'''
    #Instead of instantiating Frame object,we will instantiate Application to hold all buttons.
    #This works as Application object is special type of Frame object.
    def __init__(self,master):
        '''initialize the frame'''
        #calling superclass constructor
        #passing Application object's master so it gets properly set as the master
        super(Application,self).__init__(master)
        self.grid()
        #Invoke Application object's create_widgets() method
        self.create_widgets()
    
    def create_widgets(self):
        '''create three buttons that do nothing'''
        #create first button
        self.bttn1=Button(self,text="I do nothing!")
        self.bttn1.grid()

        #create second button
        self.bttn2=Button(self)
        self.bttn2.grid()
        self.bttn2.configure(text="Me too!")

        #create third button
        self.bttn3=Button(self)
        self.bttn3.grid()
        self.bttn3["text"]="Same here!"

        # bttn1,bttn2,bttn3 are attributes of an Application object
        # we use self as the master for buttons so that Application object is their master


#main

#create a root window
root=Tk()
root.title("Lazy Buttons")
root.minsize(width=300,height=85)
#instantiate an Application object with root window as its master
app=Application(root)
#this creates Application object with root window as its master
#Application object's constructor invokes object's create_widgets() method
#The method creates three buttons,with Application object as their master.

#invoke root window's event loop 
root.mainloop()

