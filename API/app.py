from flask import Flask
from flask_cors import CORS

from user.controllers import user_app
from main.controllers import main_app

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['JSON_SORT_KEYS'] = False
    app.register_blueprint(user_app)
    app.register_blueprint(main_app,url_prefix="/main")
    return app
