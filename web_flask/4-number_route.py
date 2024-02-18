#!/usr/bin/python3
'''
a script that starts a Flask web application
'''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    '''
    Hello HBNB!
    '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''
    HBNB
    '''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    '''
    display “C ”, followed by the value of the text variable
    (replace underscore _ symbols with a space )
    '''
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonisfun(text='is cool'):
    '''
    display “Python ”, followed by the value of the text variable
    (replace underscore _ symbols with a space )
    '''
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    '''
    display “n is a number” only if n is an integer
    '''
    return f'{n} is a number'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
