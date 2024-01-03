import tkinter as tk

class TextEditor:
    def __init__(self):

        #editor window
        self.root = tk.Tk()
        self.root.title("Write your story here:")
        self.text_area = tk.Text(self.root, wrap=tk.WORD)
        self.text_area.pack(expand=tk.YES, fill=tk.BOTH)

        
        self.timer = None
        self.root.bind('<Any-KeyPress>', self.reset_timer) #bind any key press so if user presses any key,timer resets
        self.root.bind('<Any-ButtonPress>', self.reset_timer)#bind any button so if user presses button, timer resets.


        self.reset_timer() #start initial timer
        self.root.mainloop() #keeps looping till event(user typing)


    def user_is_inactive(self):
        '''
        If user is inactive for more than 10 seconds, delete all text he has typed so far.
        '''
        self.text_area.delete(1.0, tk.END)  # Delete all text when the user is inactive

    def reset_timer(self, event=None): 
        '''
        Actual logic to start timer and then if 10 seconds of inactivity, set new timer and call user_is_inactive method.
        Root windows have a method called `after` which can be used to schedule a function to be called after a given period of time. 
        If that function itself calls after you've set up an automatically recurring event.
        '''
        if self.timer is not None: #check if existing timer
            self.root.after_cancel(self.timer) #if existing timer is there, cancel that timer. Only 1 timer must be there.
        self.timer = self.root.after(10000, self.user_is_inactive) #after 10 sec(10000 millisec) of inactivity, set new timer and call user_is_inactive method.



if __name__ == "__main__":
    text_editor = TextEditor()
    

