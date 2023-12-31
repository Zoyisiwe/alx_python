"""A script that starts a new Flask application with a 2 texts and a number, and a even and odd number"""

from flask import Flask, escape, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    return "C " + escape(text.replace('_', ' '))

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text):
    return "Python " + escape(text.replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    return f"{n} is a number"

@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    return render_template('5-number.html', number=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_number_odd_or_even(n):
    odd_or_even = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', number=n, odd_even=odd_or_even)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
