from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField,TextAreaField, IntegerField, BooleanField,
                     RadioField,SubmitField)
from wtforms.validators import InputRequired, Length,Email
from flask_bootstrap import Bootstrap4


app = Flask(__name__)
app.secret_key = "secret"
bootstrap = Bootstrap4(app)



class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(),Email("Type @ or ."),
                                             Length(min=8)])
    password = PasswordField('Password', validators=[InputRequired(),
                                             Length(min=8)])
    submit = SubmitField('Submit')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login",methods=["GET","POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit(): #if form validated on submission
        if(login_form.email.data=="admin@email.com" and login_form.password.data=="12345678"):
            return render_template("success.html")
        else:
            return render_template("denied.html")
    
    return render_template('login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)
