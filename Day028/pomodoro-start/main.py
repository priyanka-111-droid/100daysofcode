from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps=0
timer=None 
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    # to stop timer
    window.after_cancel(timer)
    #timer_text 00:00
    canvas.itemconfig(timer_text,text="00:00")
    #label1 "Timer"
    label1.config(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,45))
    #reset checkmarks
    check_marks.config(text="")

    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    reps+=1

    # if 8th rep
    if(reps%8==0):
        label1.config(text="Long break",fg=RED)
        count_down(long_break_sec)
    elif(reps%2==0):
    #if 2nd/4th/6th rep
        label1.config(text="Short break",fg=PINK)
        count_down(short_break_sec)
    # For 1st/3rd/5th/7th rep
    else:
        label1.config(text="Work",fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if(count_sec<10):
        count_sec=f"0{count_sec}"

    #to change canvas element to count down up to 0
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")

    
    if(count>0):
        global timer 
        #wait for 1000ms
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()

        #dealing with checkmarks
        marks=""
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            marks+="✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro timer")
window.config(padx=100,pady=50,bg=YELLOW)



#setting label Timer at top
#fg is foreground color,bg is background color
label1=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,45))
label1.grid(column=1,row=0)


#setting tomato background
#highlightthickness is to remove borders
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="Day028/pomodoro-start/tomato.png")
#using tomato image
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


#Buttons
start_button=Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)
start_button.config(padx=10,pady=3)
reset_button=Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)
reset_button.config(padx=10,pady=3)


#checkmark
check_marks=Label(text="",fg=GREEN,bg=YELLOW)
check_marks.grid(column=1,row=3)

window.mainloop()