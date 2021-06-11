# Turtle Graphics:

Let's say that someone has already created a blueprint for a turtle with a paintbrush and you can use it to draw on the screen,use it in different colours.
This blueprint for a turtle is in Turtle graphics module,preloaded when you download python,so no need to install anything extra.

    #import module
    import turtle
    #get Turtle class from module
    turtle.Turtle
    #save class into an object and activate construction of object
    turtle_object=turtle.Turtle()

Can also do this:

    #from module import Turtle class directly
    from turtle import Turtle
    #turtle_object is new object created from Turtle class
    turtle_object=Turtle()

# Exercises:
Use turtle [documentation](https://docs.python.org/3/library/turtle.html) for all references 

## 1.Creating Turtle screen object:

Screen is a window where turtle will show up.

* from turtle module,import Turtle class and Screen class
* create turtle object
* create a turtle screen object
* Tap into height attribute of screen object and print that value.
* now try to use screensize() method to set new coordinates for height and width of window and print it.
* your turtle object will look like an arrow by default.
* use exitonclick() method to make sure window doesn't disappear till you click on it.

Hints:

1.https://docs.python.org/3/library/turtle.html#turtle.screensize

2.https://docs.python.org/3/library/turtle.html#turtle.exitonclick

Solution:[16-1.py](https://github.com/priyanka-111-droid/100daysofcode/blob/main/Day016/exercises/turtle/16-1.py)

## 2.Change i)shape of object to turtle and ii)change colour of turtle from black to any colour iii)move it forward by 100 units

Hints:

1.https://docs.python.org/3/library/turtle.html#turtle.shape

2.https://docs.python.org/3/library/turtle.html#turtle.color

3.See colours available [here](https://cs111.wellesley.edu/labs/lab01/colors)

4.https://docs.python.org/3/library/turtle.html#turtle.forward


Solution:[16-2.py](https://github.com/priyanka-111-droid/100daysofcode/blob/main/Day016/exercises/turtle/16-2.py)











