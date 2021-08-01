#Using radio buttons(select only one option)
#Create a Movie chooser program
#users can choose their preferred movie type(comedy,drame or romance)
#The selection is displayed in text box.


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
        text="Select one: "
        ).grid(row=1,column=0,sticky=W)

        #create variable for single,favourite type of movie
        #since only one radio button is selected at a time,
        #a group of radio buttons share one special object that
        #reflects which of radio buttons is selected. 
        self.favourite=StringVar()
        self.favourite.set(None)

        #create comedy radio button
        Radiobutton(self,
        text="Comedy",
        variable=self.favourite,
        value="comedy",
        command=self.update_text
        ).grid(row=2,column=0,sticky=W)

         #create drama radio button
        Radiobutton(self,
        text="Drama",
        variable=self.favourite,
        value="drama",
        command=self.update_text
        ).grid(row=3,column=0,sticky=W)

        #create romance radio button
        Radiobutton(self,
        text="Romance",
        variable=self.favourite,
        value="romance",
        command=self.update_text
        ).grid(row=4,column=0,sticky=W)

         #create text box to display results
        self.results_text=Text(self,width=40,height=5,wrap=WORD)
        self.results_text.grid(row=5,column=0,columnspan=3)

    def update_text(self):
        message="Your favourite type of movie is "
        message+=self.favourite.get()

        self.results_text.delete(0.0,END)
        self.results_text.insert(0.0,message)



#main
root=Tk()
root.title("Movie chooser")
app=Application(root)
root.mainloop()

