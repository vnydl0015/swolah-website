from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/preferences')
def preferences():
    return render_template('preferences.html')

@app.route('/process')
def process():
    return render_template('process.html')

@app.route('/instruction_page1')
def instruction_page1():
    return render_template('instruction_page1.html')


@app.route('/instruction_page2')
def instruction_page2():
    return render_template('instruction_page2.html')

if __name__ == '__main__':
    app.run(debug=True)
