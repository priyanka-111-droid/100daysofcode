from flask import Flask

app=Flask(__name__)


def make_bold(original_function):
    def wrapper_func():
        return "<b>" + original_function() + "</b>"

    return wrapper_func


def make_emphasis(original_function):
    def wrapper_func():
        return "<em>" + original_function() + "</em>"
    return wrapper_func

def make_underlined(original_function):
    def wrapper_func():
        return "<u>" + original_function() + "</u>"
    return wrapper_func


@app.route('/')
@make_bold
@make_emphasis
@make_underlined 
def hello_world():
    return 'Have a nice day!'
    



if __name__ == "__main__":
    app.run(debug=True)  