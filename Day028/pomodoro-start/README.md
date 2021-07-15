# Tkinter,Dynamic typing,Pomodoro GUI application

# Pomodoro technique of efficiently working

* 25min work (1st rep)

* 5min break(2nd rep)

* 25min work (3rd rep)

* 5min break(4th rep)

* 25min work (5th rep)

* 5min break(6th rep)

* 25min work(7th rep)

* 20min break(8th rep)

Get colour options [here](https://colorhunt.co/).Define colors to be used,font to be used,working minutes(25 min),short break minutes(5min) and long break(20 min) as constants in the beginning.

## UI setup

1.Using Canvas widget and adding Images to Tkinter(tomato image)

2.Add title label(Timer),start and reset buttons and checkmark to finish UI(USer Interface) setup.

## Countdown mechanism

1.GUI programs are event driven,they need to keep listening if something happened which is done by window.mainloop().

2.Use window.after(),see [here](http://tcl.tk/man/tcl8.6/TclCmd/after.htm)

3.Create function count_down that helps us count down from 5 seconds to 0 and is displayed on the screen.

## Timer mechanism 

1.Create function start_timer() that starts countdown ONLY  when start button is pressed.

2.Use keyword argument command along with start_button(in the UI setup) to start_timer.

3.Now we need to format it so that it can work for 5 minutes not 5 seconds.

## Countdown mechanism

1.Import math module and use math.floor to get minutes of the countdown and store in count_min.

2.Use modulo to get remaining seconds left and store in count_sec

3.Now use f string to display time in minutes and seconds.

4.Now we need to make countdown start from 5:00 not 5:0.Hence we have to learn dynamic typing.

5.Dynamic typing means in python,we are able to change variable's datatype by changing content in variable.

        a=3

        a="Hello"

Hence python is strongly typed(you can't do int operations on a string) but even though python knows what type variable is or what type function expects,we can change variable dynamically.

6.In above program,we are using dynamic typing to see if count_sec is 0 and if it is,we do count_sec="00".Hence we can use f string to display.

7.For below 10 seconds, for example,it shows "0:9" instead of "0:09".So we need to fix this issue too.

8.Define global variable reps to count down appropriate number of seconds.When you run the program,it has to switch between counting down work time and break time.(Test with setting WORK_MIN as 1 min instead of 25 min).Hint :(use %)

9.Now finally,to improve user UI,for working time,label should display "Work" in green at top,"Short break" in pink and "Long break" in red colour instead of  just printing "Timer" all the time.

10.For every 2 reps,we have done 1 work session,so add a check to checkmark label just when break starts.

Eg.4 reps means 2 work sessions and 2 breaks.

## Timer Reset

This removes checkmarks,reset text in timer,stop timer and change title back to original text "Timer".Also set global reps back to 0.


