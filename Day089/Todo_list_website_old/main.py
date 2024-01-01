from flask import Flask,render_template, request, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'




##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Todo TABLE Configuration
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    content = db.Column(db.String(250), nullable=False)
    complete = db.Column(db.String(250), nullable=False)
    



@app.route('/')
def home():
    todos = db.session.query(Todo).all()
    return render_template('index.html',todos=todos)




@app.route('/add',methods=['GET','POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        complete = request.form['complete']

        with app.app_context():
            new_todo = Todo(title=title,
                            content=content,
                            complete=complete)
            db.session.add(new_todo)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')




@app.route('/edit/<num>', methods=['GET', 'POST'])
def edit(num):
    todo_id = num
    todo_to_update= Todo.query.get(todo_id)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        complete = request.form['complete']
        todo_to_update.title = title 
        todo_to_update.content = content
        todo_to_update.complete = complete
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', todo_to_update = todo_to_update)
        

# ## HTTP DELETE - Delete Record
@app.route("/delete/<num>")
def delete(num):
    todo_id = num
    todo_to_delete = Todo.query.get(todo_id)
    db.session.delete(todo_to_delete)
    db.session.commit()
    return redirect(url_for('home'))
    



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)