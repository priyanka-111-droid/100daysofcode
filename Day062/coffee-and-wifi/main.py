from flask import Flask, render_template,redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import (StringField,SelectField,SubmitField)
from wtforms.validators import InputRequired, URL
# Import writer class from csv module
from csv import writer
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[InputRequired()])
    cafe_location = StringField('Cafe location', validators=[InputRequired(),URL()])
    opening_time = StringField('Opening Time:', validators=[InputRequired()])
    closing_time = StringField('Closing Time', validators=[InputRequired()])
    coffee_rating = SelectField('Coffee rating',
                                choices=[('☕️','☕️'), ('☕️☕️','☕️☕️'), ('☕️☕️☕️','☕️☕️☕️'), ('☕️☕️☕️☕️','☕️☕️☕️☕️'), ('☕️☕️☕️☕️☕️','☕️☕️☕️☕️☕️')],
                                 validators=[InputRequired()])
    wifi_rating = SelectField('Wifi Rating', 
                              choices=[('✘','✘'),('💪','💪'), ('💪💪','💪💪'), ('💪💪💪','💪💪💪'), ('💪💪💪💪','💪💪💪💪'), ('💪💪💪💪💪','💪💪💪💪💪')],
                              validators=[InputRequired()])
    power_availability = SelectField('Power Availability', 
                                     choices=[('✘','✘'),('🔌','🔌'), ('🔌🔌','🔌🔌'), ('🔌🔌🔌','🔌🔌🔌'), ('🔌🔌🔌🔌','🔌🔌🔌🔌'), ('🔌🔌🔌🔌🔌','🔌🔌🔌🔌🔌')],
                                     validators=[InputRequired()])

    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',methods=["GET","POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe_data = [
            form.cafe.data,
            form.cafe_location.data,
            form.opening_time.data,
            form.closing_time.data,
            form.coffee_rating.data,
            form.wifi_rating.data,
            form.power_availability.data,
            ]
        with open(r'C:\Users\Admin\AppData\Roaming\SPB_Data\100daysofcode\Day062\coffee-and-wifi\cafe-data.csv',"a",newline='',encoding='utf-8') as f_object:

            # Pass this file object to csv.writer()
            # and get a writer object
            writer_object = writer(f_object)
        
            # Pass the list as an argument into
            # the writerow()
            writer_object.writerow(cafe_data)
        
            # Close the file object
            f_object.close()
            
        return redirect(url_for('cafes'))     
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)
    



@app.route('/cafes')
def cafes():
    # had to specify absolute path and encoding otherwise error
    with open(r'C:\Users\Admin\AppData\Roaming\SPB_Data\100daysofcode\Day062\coffee-and-wifi\cafe-data.csv', newline='',encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
