#!/usr/bin/env python3
"""
A flask app
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """A config class for the flask app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index():
    """default home route
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
