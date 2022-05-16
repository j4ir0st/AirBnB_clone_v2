#!/usr/bin/python3
"""
Write a script that starts a Flask web application
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """ Returns hello HBNB """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """ Returns hello HBNB """
    return 'HBNB'


@app.route('/c/<path:text>', strict_slashes=False)
def c_text(text):
    """ Returns hello HBNB """
    return 'C {}'.format(text.replace("_", " "))


@app.route('/python', strict_slashes=False, defaults={"text": "is cool"})
@app.route('/python/<path:text>', strict_slashes=False)
def python_text(text):
    """ Returns hello HBNB """
    return 'Python {}'.format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def n_isnumber(n):
    """ Returns hello HBNB """
    if (isinstance(n, int)):
        return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def n_template(n):
    """ Returns hello HBNB """
    if (isinstance(n, int)):
        return render_template('5-number.html', number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
