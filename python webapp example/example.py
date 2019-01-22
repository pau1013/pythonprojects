from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)
gender_opt = ['Male', 'Female']

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        return render_template('index.html', gender_opt=gender_opt)
    else:
        return render_template('index.html', gender_opt=gender_opt)

@app.route('/submited', methods=['POST'])
def submited():
    if request.method == 'POST':
        name = request.form['name'].title()
        gender = request.form['gender']
        age = request.form['age']
        email = request.form['email']
        return render_template('index.html', gender_opt=gender_opt, name=name, gender=gender, age=age, email=email)
    return render_template('index.html')

@app.route('/submit-new-page', methods=['POST'])
def submit_new_page():
    if request.method == 'POST':
        name = request.form['name'].title()
        gender = request.form['gender']
        age = request.form['age']
        email = request.form['email']
        return render_template('data.html', name=name, gender=gender, age=age, email=email)
    return render_template('index.html')

if __name__ == '__main__':
    # app.debug = True
    app.run()
