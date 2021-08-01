#Mad lib GUI program(class based) using checkbox,radio buttons,text field and files(story.txt)

from tkinter import *

class Application(Frame):
    #we will instantiate Application object to hold all buttons,
    #since Application object is special type of Frame object"""
    def __init__(self,master):
        """initialize Frame"""
        #call superclass constructor
        #pass along Application object's master so it gets properly set as the master
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
       #create instruction label
       Label(self,text="Enter information for new story").grid(row=0,column=0,columnspan=2,sticky=W)

       #create label and text entry for name of person
       Label(self,text="Person: ").grid(row=1,column=0,sticky=W)
       self.person_ent=Entry(self)
       self.person_ent.grid(row=1,column=1,sticky=W)

       #create label and text entry for plural noun
       Label(self,text="Plural Noun:").grid(row=2,column=0,sticky=W)
       self.noun_ent=Entry(self)
       self.noun_ent.grid(row=2,column=1,sticky=W)

       #create a label and text entry for verb
       Label(self,text="Verb:").grid(row=3,column=0,sticky=W)
       self.verb_ent=Entry(self)
       self.verb_ent.grid(row=3,column=1,sticky=W)

       #create label for adjectives check button
       Label(self,text="Adjective(s):").grid(row=4,column=0,sticky=W)

       #create itchy check button
       self.is_itchy=BooleanVar()
       Checkbutton(self,text="itchy",variable=self.is_itchy).grid(row=4,column=1,sticky=W)
       
       #create joyous check button
       self.is_joyous=BooleanVar()
       Checkbutton(self,text="joyous",variable=self.is_joyous).grid(row=4,column=2,sticky=W)

       #create electric check button
       self.is_electric=BooleanVar()
       Checkbutton(self,text="electric",variable=self.is_electric).grid(row=4,column=3,sticky=W)

       #create label for body parts radio buttons
       Label(self,text="Body Part:").grid(row=5,column=0,sticky=W)

       #create label for single body part
       self.body_part=StringVar()
       self.body_part.set(None)

       #create body part radio buttons
       body_parts=["bellybutton","bigtoe","medulla oblongata"]
       column=1
       for part in body_parts:
           Radiobutton(self,text=part,variable=self.body_part,value=part).grid(row=5,column=column,sticky=W)
           column+=1

       #create submit button
       Button(self,text="Click for story",command=self.tell_story).grid(row=6,column=0,sticky=W)

       self.story_txt=Text(self,width=75,height=10,wrap=WORD)
       self.story_txt.grid(row=7,column=0,columnspan=4)

    def tell_story(self):
        '''fill text box with new story based on user input'''
        #get values from GUI
        person=self.person_ent.get()
        noun=self.noun_ent.get()
        verb=self.verb_ent.get()
        adjectives=""
        if self.is_itchy.get():
            adjectives+="itchy, "
        if self.is_joyous.get():
            adjectives+="joyous, "
        if self.is_electric.get():
            adjectives+="electric, "
        
        body_part=self.body_part.get()

        with open("Day027/Project/story.txt",mode="r") as f:
            data=f.read()
            data=data.replace("[person]",person)
            data=data.replace("[noun]",noun)
            data=data.replace("[adjectives]",adjectives)
            data=data.replace("[body_part]",body_part)
            data=data.replace("[verb]",verb)
        
        self.story_txt.delete(0.0,END)
        self.story_txt.insert(0.0,data)


root=Tk()
root.title("Mad Lib")
app=Application(root)
root.mainloop()


            
        



        









