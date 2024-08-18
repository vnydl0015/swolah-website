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

@app.route('/buy')
def buy():
    return render_template('buy.html')


@app.route('/account_page')
def account_page():
    return render_template('account_page.html')


@app.route('/eligibility')
def eligibility():
    return render_template('eligibility.html')


@app.route('/dropoff')
def dropoff():
    return render_template('dropoff.html')

if __name__ == '__main__':
    app.run(debug=True)
