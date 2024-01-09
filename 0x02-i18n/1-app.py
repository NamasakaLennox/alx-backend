#!/usr/bin/env python3
"""
A basic flask app
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """A config class for the flask app
    Defines the class attributes
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Instantiate the application object
app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@app.route('/', strict_slashes=False)
def index() -> str:
    """default home route
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
