from flask import Flask
from flask_cors import CORS

from user.views import UserView


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(UserView.user_app)

    return app
