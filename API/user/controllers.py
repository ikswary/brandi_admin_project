import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath("API"))
sys.path.extend([BASE_DIR])

import pymysql
from flask import Blueprint, request, jsonify

from connections import get_db_connector
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

    Exceptions:
        InternalError: DATABASE가 존재하지 않을 때 발생
        OperationalError: DATABASE 접속이 인가되지 않았을 때 발생
        DataError: 컬럼 타입과 매칭되지 않는 값이 DB에 전달되었을 때 발생
        KeyError: 엔드포인트에서 요구하는 키값이 전달되지 않았을 때 발생
    """
    db = None
    try:
        db = get_db_connector()
        if db is None:
            return jsonify(message="DATABASE_INIT_ERROR"), 500

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

    except pymysql.err.InternalError:
        return jsonify(message="DATABASE_DOES_NOT_EXIST"), 500
    except pymysql.err.OperationalError:
        return jsonify(message="DATABASE_AUTHORIZATION_DENIED"), 500
    except pymysql.err.DataError:
        db.rollback()
        return jsonify(message="DATA_ERROR"), 400
    except KeyError:
        return jsonify(message="KEY_ERROR"), 400
    except Exception as e:
        return jsonify(message=f"{e}"), 500
    finally:
        if db:
            db.close()
