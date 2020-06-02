import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath("API"))
sys.path.extend([BASE_DIR])

from flask import Blueprint, request, jsonify

from connections import get_db_connector, DataError
from .models import sign_up, is_account_exists

user_app = Blueprint('user_app', __name__)


@user_app.route('mock-up', methods=['POST'])
def test_sign_up():
    """회원가입 예시 API

    Args:
        account: 계정명
        password: 비밀번호
        seller_name: 셀러명
        seller_name_eng: 셀러명(영문)
        cs_number: 고객센터 전화번호
        seller_attribute_id: 셀러 속성 id
        site_url: 셀러 사이트 url

    Returns:
        {message: STATUS_MESSAGE}, http status code
    """
    try:
        db = get_db_connector()
        if db:
            db.begin()
            required_keys = ('account', 'password', 'seller_name', 'seller_name_eng',
                             'cs_number', 'seller_attribute_id', 'site_url')
            data = {}
            for key in required_keys:
                data[key] = request.json[key]

            if is_account_exists(db, data['account']):
                return jsonify(message="ACCOUNT_DUPLICATED"), 409

            sign_up(db, data)
            db.commit()

            return jsonify(message="SIGN_IN_COMPLETE"), 200

        return jsonify(message="DATABASE_INIT_ERROR"), 404

    except DataError:
        db.rollback()
        return jsonify(message="DATA_ERROR"), 400
    except KeyError:
        return jsonify(message="KEY_ERROR"), 400
    except AttributeError:
        return jsonify(message="DATABASE_INIT_ERROR"), 404
    finally:
        if db:
            db.close()
