#!/usr/bin/env python3
'''Force locale with URL parameter'''


from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    '''Check if the locale parameter is present in the
    request's query string'''
    if 'locale' in request.args:
        requested_locale = request.args['locale']
        # Check if the requested locale is supported
        if requested_locale in app.config['LANGUAGES']:
            return requested_locale

    # Resort to the previous default behavior
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    '''our router'''
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(debug=True)
