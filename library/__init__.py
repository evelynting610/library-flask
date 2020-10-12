from flask import Flask, jsonify

from library.extensions import db, migrate, ma
from library.errors import APIError
from library.models import *
from library.commands import seed, drop_db


def create_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    # Load the file specified by the APP_CONFIG_FILE environment variable
    app.config.from_envvar('APP_CONFIG_FILE')

    from library.views import api_bp
    # Register the API Blueprint
    app.register_blueprint(api_bp)
    register_commands(app)
    register_extensions(app)
    register_error_handlers(app)
    return app


def register_commands(app):
    app.cli.add_command(seed)
    app.cli.add_command(drop_db)


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)


def register_error_handlers(app):
    def handle_api_error(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    app.errorhandler(APIError)(handle_api_error)
