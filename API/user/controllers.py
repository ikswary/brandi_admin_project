from flask import Blueprint, request

from connections import get_db_connector
from user.models import sign_up_model, is_account_exists

user_app = Blueprint('user_app', __name__, url_prefix='/user')


@user_app.route('mock-up', methods=['POST'])
def test_sign_up():
    try:
        db = get_db_connector()
        db.begin()
        required_keys = ['account', 'password', 'seller_name', 'seller_name_eng',
                         'cs_number', 'seller_attribute_id', 'site_url']
        data = {}
        for key in required_keys:
            data[key] = request.json[key]

        if is_account_exists(db, data['account']):
            return 'ACCOUNT_DUPLICATED', 400

        sign_up_model(db, data)
        db.commit()

        return '', 200

    except KeyError:
        return '', 400

    finally:
        db.close()
        # db 객체 None일 경우 핸들
        # 리스트형, 등록,    수정 예시 SET
