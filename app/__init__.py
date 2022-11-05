from flask import Flask

from extension import db


def create_app(config_file='settings.py'):
    app = Flask(__name__)
    db.init_app(app)
    app.config.from_pyfile(config_file)
    return app
