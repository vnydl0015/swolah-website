from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

# Route for an additional page
@app.route('/about')
def about():
    return render_template('aboutus.html')


@app.route('/login')
def login():
    return render_template('login.html')
"""
@app.route('/login')
def about():
    return render_template('login.html')

@app.route('/swap')
def about():
    return render_template('swap.html')

@app.route('/help')
def about():
    return render_template('help.html')
"""
if __name__ == '__main__':
    app.run(debug=True)
