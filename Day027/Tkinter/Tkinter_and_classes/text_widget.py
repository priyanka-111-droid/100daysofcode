#demonstrating text and entry widgets,grid layout manager
#The longevity program reveals the secret to living to the ripe old age of 100 is user enters correct password in text entry and clicks Submit button.
#if password is correct,program displays key to longevity in text box.
#For testing:correct password is "secret"

from tkinter import *
class Application(Frame):
    def __init__(self,master):
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        '''create button,text and entry widgets'''
        #create instruction label
        self.inst_lbl=Label(self,text="Enter password for secret of longevity:")
        self.inst_lbl.grid(row=0,column=0,columnspan=2,sticky=W)
        #after specifying row and column and columnspan to establish which cell(or cells) a widget occupies,
        #we can move widget to quadrant of cell(or cells) using parameter sticky
        #sticky takes values N(north),S(south),E(east),W(west)


        #create password label
        self.passw_lbl=Label(self,text="Password: ")
        self.passw_lbl.grid(row=1,column=0,sticky=W)


        #create entry widget to accept password entered by user
        self.passw_ent=Entry(self)
        self.passw_ent.grid(row=1,column=1,sticky=W)

        #create submit button
        self.submit_bttn=Button(self,text="Submit",command=self.reveal)
        self.submit_bttn.grid(row=2,column=0,sticky=W)

        #create text widget(text box)
        #parameters are width,height,wrap
        self.secret_text=Text(self,width=35,height=5,wrap=WORD)
        self.secret_text.grid(row=3,column=0,columnspan=2,sticky=W)

        #inserting text with text-based widgets
    def reveal(self):
        '''display message based on password'''
        contents=self.passw_ent.get()
        if(contents=="secret"):
            message="Here's the secret to living to 100:live to 99 and then be very careful."
        else:
            message="That's not the correct password,so I can't share the secret with you."

        #first delete any text already in Text widget
        self.secret_text.delete(0.0,END)
        #delete text starting from row=0,column=0 up till end of text

        #now insert string to be displayed
        self.secret_text.insert(0.0,message)


#main
root=Tk()
root.title("Longevity")
root.minsize(width=300,height=150)
app=Application(root)
root.mainloop()




