THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:

    #init function called during new object creation
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        #window is property of class so self
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20,bg=THEME_COLOR)

        self.score_label=Label(text="Score:0",fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)


        self.canvas = Canvas(width=300, height=300,bg="white")
        self.question_text=self.canvas.create_text(150,150,width=280,text="Some question text",fill=THEME_COLOR,font=("Arial",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)


        wrong_image = PhotoImage(file="Day034/quizzler-app/images/true.png")
        self.wrong_button = Button(image=wrong_image, highlightthickness=0,command=self.wrong_pressed)
        self.wrong_button.grid(row=2, column=0)
       

        correct_image = PhotoImage(file="Day034/quizzler-app/images/false.png")
        self.correct_button = Button(image=correct_image, highlightthickness=0,command=self.correct_pressed)
        self.correct_button.grid(row=2, column=1)


        self.get_next_question()

        #to constantly check if user clicked anything
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if(self.quiz.still_has_questions()):
            self.score_label.config(text=f"Score:{self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You have reached end of quiz!")
            #disable buttons at end of all questions
            self.wrong_button.config(state="disabled")
            self.correct_button.config(state="disabled")


    def wrong_pressed(self):
        is_wrong=self.quiz.check_answer("False")
        self.give_feedback(is_wrong)

    def correct_pressed(self):
        is_correct=self.quiz.check_answer("True")
        self.give_feedback(is_correct)
    
    def give_feedback(self,is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")


        self.window.after(1000,self.get_next_question)





