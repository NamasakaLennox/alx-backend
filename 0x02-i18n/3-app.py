#!/usr/bin/env python3
"""
A basic flask app
"""
from flask import Flask, render_template, request
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


@babel.localeselector
def get_locale() -> str:
    """returns the best supported language
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """default home route
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
