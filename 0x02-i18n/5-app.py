#!/usr/bin/env python3
"""
A basic flask app
"""
from flask import Flask, g, render_template, request
from flask_babel import Babel
from typing import Dict, Union

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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


def get_user() -> Union[Dict, None]:
    """Returns a user dictionary if valid user
    """
    user = request.args.get('login_as')

    if user:
        try:
            return users.get(int(user))
        except Exception:
            return None
    return None


@app.before_request
def before_request() -> None:
    """Adds a user to the global session before any other function
    is executed
    """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """returns the best supported language
    """
    lang = request.args.get('locale')
    if lang and lang in app.config['LANGUAGES']:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """default home route
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
