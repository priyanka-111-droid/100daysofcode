from flask import Flask


#this is a special attribute built in python
# A module's __name__ is set equal to '__main__' when read from standard input,script or from interactive prompt
#__main__ is basically the file that is currently being run
app=Flask(__name__)
print(__name__) 


#This syntax(starting with @) is called PYTHON DECORATOR
#This gives additional functionality to existing function
#When user navigates to url with just /,they just want to see home page.
#In this case,the decorator will trigger the function hello_world() only when user wants to access home page,denoted by /
@app.route('/')
def hello_world():
    return 'Hello, World!'



#This decorator will trigger function say_bye() in case user decides to access url /bye
@app.route("/bye")
def say_bye():
    return "Bye"



#FIRST WAY TO RUN FLASK APPLICATIONS:
#for windows powershell,
# set FLASK_APP=intro_flask.py
# $env:FLASK_APP = "intro_flask.py"
# flask run


#SECOND(MORE CONVENIENT) WAY TO RUN FLASK APPLICATIONS:
if __name__ == "__main__":
    app.run()  

    #just like when we went to terminal and typed flask run
    #But now we don't have to set environment variables and stop the code,
    #We can use standard run controls. 


