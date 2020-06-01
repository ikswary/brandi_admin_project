from flask import Flask
from flask_cors import CORS

from user.controllers import user_app


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(user_app)

    return app
