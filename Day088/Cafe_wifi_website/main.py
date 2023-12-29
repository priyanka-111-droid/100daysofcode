
from flask import Flask, jsonify, render_template, request, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
import random
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
    


#display all cafes.
@app.route("/")
def home():
    cafes = db.session.query(Cafe).all()
    return render_template("index.html",cafes=cafes)


## HTTP GET - get a random cafe(in case user is confused where to go)
@app.route("/random", methods=['GET'])
def get_random_cafe():
    with app.app_context():
        cafes = db.session.query(Cafe).all()
        random_cafe = random.choice(cafes)
    return render_template("get_random.html",random_cafe=random_cafe)


#not needed since home page displays all cafes.
# @app.route("/all")
# def get_all():
#     cafes = db.session.query(Cafe).all()
#     return jsonify(cafes=[cafe.to_dict() for cafe in cafes])



        

## HTTP POST -Add cafe
@app.route("/add", methods=['POST','GET'])
def add_a_cafe():
    if request.method == 'POST':
            name=request.form.get("name")
            map_url=request.form.get("map_url")
            img_url=request.form.get("img_url")
            loc=request.form.get("location")
            has_sockets=(request.form.get("has_sockets"))=='on'
            has_toilet=(request.form.get("has_toilet"))=='on'
            has_wifi=(request.form.get("has_wifi"))=='on'
            can_take_calls=bool(request.form.get("can_take_calls"))
            seats=request.form.get("seats")
            coffee_price=request.form.get("coffee_price")
            with app.app_context():
                new_cafe = Cafe(name=name,
                                map_url=map_url,
                                img_url=img_url,
                                location=loc,
                                has_sockets = has_sockets,
                                has_toilet=has_toilet,
                                has_wifi=has_wifi,
                                can_take_calls=can_take_calls,
                                seats=seats,
                                coffee_price=coffee_price)
                db.session.add(new_cafe)
                db.session.commit()
            return redirect(url_for('home'))
    # return jsonify(response={"success": "Successfully added the new cafe."})
    return render_template('add_cafe.html')





## HTTP Update Record - update coffee price.
@app.route("/update_price/<num>", methods=['POST','GET'])
def update_price(num):
    number = int(num)
    all_cafes = db.session.query(Cafe).all()
    if request.method=="POST":
        coffee_price = request.form.get('coffee_price')
        cafe_id = num
        cafe_to_update = Cafe.query.get(cafe_id)
        cafe_to_update.coffee_price = coffee_price
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('update.html', cafes=all_cafes, num=number)
    

# ## HTTP DELETE - Delete Record
@app.route("/delete/<num>")
def delete_cafe(num):
    cafe_id = num
    cafe_to_delete = Cafe.query.get(cafe_id)
    db.session.delete(cafe_to_delete)
    db.session.commit()
    return redirect(url_for('home'))
    
## Search Location to get all cafes in that location. Eg. Peckham.
@app.route("/search",methods=['GET','POST'])
def find_a_cafe():
    cafes = db.session.query(Cafe).all()
    if request.method=="POST":
        location = request.form.get('location')
        return render_template('search.html',location=location,cafes=cafes)
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)