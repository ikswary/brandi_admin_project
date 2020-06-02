import json

from flask import Blueprint, request, jsonify

from connections import get_db_connector, DataError
from user.models import sign_up_model, is_account_exists

user_app = Blueprint('user_app', __name__, url_prefix='/user')


@user_app.route('mock-up', methods=['POST'])
def test_sign_up():
    """회원가입 예시 API

    parameters
    ----------
    account, password, seller_name, seller_name_eng,
    cs_number, seller_attribute_id, site_url
        all required argument is string
    :returns:
        {message: STATUS_MESSAGE}, http status code
    """
    try:
        db = get_db_connector()
        db.begin()
        required_keys = ('account', 'password', 'seller_name', 'seller_name_eng',
                         'cs_number', 'seller_attribute_id', 'site_url')
        data = {}
        for key in required_keys:
            data[key] = request.json[key]

        if is_account_exists(db, data['account']):
            return jsonify({'message': 'ACCOUNT_DUPLICATED'}), 409

        sign_up_model(db, data)
        db.commit()

        return jsonify({'message': 'SIGN_IN_COMPLETE'}), 200

    except DataError:
        return jsonify({'message': 'DATA_ERROR'}), 400
    except KeyError:
        return jsonify({'message': 'KEY_ERROR'}), 400
    except AttributeError:
        return jsonify({'message': 'DATABASE_INIT_ERROR'}), 404
    finally:
        if db:
            db.close()
