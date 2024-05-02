#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_HBNB():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_cool(text):
    text = text.replace("_", " ")
    return f'C {text}'


@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text="is cool"):
    text = text.replace("_", " ")
    return f'Python {text}'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
