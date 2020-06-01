from flask import Blueprint, request


user_app = Blueprint('user_app', __name__, url_prefix='/user')


@user_app.route('', methods=['GET'])
def hello_world(*kwargs):
    print(request.headers['Authorization'])
    print(request.json)
    return '', 200


@user_app.route('', methods=['POST'])
def test_post(*kwargs):
    print(request.headers['Authorization'])
    print(request.json)
    return '', 200
