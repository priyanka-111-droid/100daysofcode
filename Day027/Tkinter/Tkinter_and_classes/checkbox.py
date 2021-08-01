#Using check buttons(select any number of choices from a group)
#Create a Movie chooser program
#users can choose their preferred movie type(comedy,drame or romance)
#All selections are displayed in text box.

from tkinter import *
class Application(Frame):
    def __init__(self,master):
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        #create description label
        Label(self,
        text="Choose your favourite movie types"
        ).grid(row=0,column=0,sticky=W)

        #create instruction label
        Label(self,
        text="Select all that apply: "
        ).grid(row=1,column=0,sticky=W)

        #CREATE CHECK BUTTONS
        #Every check button needs special object associated with it that 
        #automatically reflects check button's status
        #special object must be instance of BooleanVar class from tkinter module

        #before creating comedy check button,let us instantiate BooleanVar object
        #and asign it to new object attribute,likes_comedy
        self.likes_comedy=BooleanVar()

        #create comedy check button itself
        Checkbutton(self,
        text="Comedy",
        variable=self.likes_comedy,
        command=self.update_text
        ).grid(row=2,column=0,sticky=W)

        #create drama check button
        self.likes_drama=BooleanVar()
        Checkbutton(self,
        text="Drama",
        variable=self.likes_drama,
        command=self.update_text
        ).grid(row=3,column=0,sticky=W)

        #create romance check button
        self.likes_romance=BooleanVar()
        Checkbutton(self,
        text="Romance",
        variable=self.likes_romance,
        command=self.update_text
        ).grid(row=4,column=0,sticky=W)

        #create text box to display results
        self.results_text=Text(self,width=40,height=5,wrap=WORD)
        self.results_text.grid(row=5,column=0,columnspan=3)

    def update_text(self):
        '''update text widget,display user's favourite movie types'''
        likes=""

        if(self.likes_comedy.get()):
            likes+="You like comedy movies.\n"
        if(self.likes_drama.get()):
            likes+="You like dramatic movies.\n"
        if(self.likes_romance.get()):
            likes+="You like romantic movies.\n"

        self.results_text.delete(0.0,END)
        self.results_text.insert(0.0,likes)

        

#main
root=Tk()
root.title("Movie chooser")
app=Application(root)
root.mainloop()

