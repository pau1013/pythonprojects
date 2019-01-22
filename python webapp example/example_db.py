from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
gender_opt = ['Male', 'Female']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password123@localhost:5000/example_database'
db = SQLAlchemy(app)

class Database(db.Model):
    __tablename__ = 'data'  # database name
    id = db.Column(db.Integer, primary_key=True)  # will add an unique ID to each item on database
    name = db.Column(db.String)
    gender = db.Column(db.String)
    age = db.Column(db.Integer)
    email = db.Column(db.String)

    def __init__(self, name, gender, age, email):
        self.name = name
        self.gender = gender
        self.age = age
        self.email = email


def add_to_db(name, gender, age, email):
    # Add new items to the database
    data = Database(name, gender, age, email)
    db.session.add(data)  # add new data to db
    db.session.commit()  # save/commit changes

def get_db_data():
    name, gender, age, email = [], [], [], []
    items = len(db.session.query(Database).all())
    for i in range(items):
        data = db.session.query(Database).get(i+1)
        name.append(data.name)
        gender.append(data.gender)
        age.append(data.age)
        email.append(data.email)
    return name, gender, age, email

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        return render_template('index.html', gender_opt=gender_opt)
    else:
        return render_template('index.html', gender_opt=gender_opt)

@app.route('/all-data', methods=['POST', 'GET'])
def submited_new_page():
    if request.method == 'POST':
        name = request.form['name'].title()
        gender = request.form['gender']
        age = request.form['age']
        email = request.form['email']
        add_to_db(name, gender, age, email)
        name, gender, age, email = get_db_data()
        return render_template('data.html', name=name, gender=gender, age=age, email=email)
    else:
        name, gender, age, email = get_db_data()
        return render_template('data.html', name=name, gender=gender, age=age, email=email)

if __name__ == '__main__':
    # app.debug = True
    app.run(port=5005)
