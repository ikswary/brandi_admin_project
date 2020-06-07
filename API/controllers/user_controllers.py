import os, sys, re

BASE_DIR = os.path.dirname(os.path.abspath("API"))
sys.path.extend([BASE_DIR])

import pymysql
import bcrypt
import jwt
from datetime import datetime, timedelta
from flask import Blueprint, request, jsonify
from flask.views import MethodView

from my_settings import SERCRET, HASH_ALGORITHM
from connections import get_db_connector
from decorator import login_required
from models.user_models import (
    get_account_id,
    insert_users,
    insert_user_details,
    insert_managers,
    insert_user_managers,
    get_id_role_password_status_from_account,
    insert_user_status,
    get_user_status_history,
    get_user_current_detail_id,
    get_detail,
    get_attribute,
    get_managers
)

user_app = Blueprint('user_app', __name__)


class UserController(MethodView):
    MASTER_ROLE_ID = 1
    SELLER_ROLE_ID = 2
    BASIC_STATUS_ID = 1

    def post(self):
        """회원가입 API

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
            ProgramingError: SQL syntax가 잘못되었을 때 발생
            IntegrityError: Key의 무결성을 해쳤을 때 발생
            DataError: 컬럼 타입과 매칭되지 않는 값이 DB에 전달되었을 때 발생
            KeyError: 엔드포인트에서 요구하는 키값이 전달되지 않았을 때 발생
        """
        required_keys = ('account', 'password', 'seller_name', 'seller_name_eng',
                         'manager_phone', 'cs_phone', 'seller_attribute_id', 'site_url')
        validation_rules = {
            'account': lambda account: True if re.match(
                '^[a-z0-9\-_]{5,20}$', account) else False,
            'password': lambda password: True if re.match(
                '^(?=.*\d{1,20})(?=.*[~`!@#$%\^&*()-+=]{1,20})(?=.*[a-z]{1,20})(?=.*[A-Z]{1,20}).{8,20}$',
                password) else False,
            'seller_name': lambda seller_name: True if re.match(
                '^[가-힣a-zA-z0-9]{1,50}$', seller_name) else False,
            'seller_name_eng': lambda seller_name_eng: True if re.match(
                '^[a-z]{1,100}$', seller_name_eng) else False,
            'manager_phone': lambda manager_phone: True if re.match(
                '^01(0|1|[6-9])-([0-9]{4})-([0-9]{4})$', manager_phone) else False,
            'cs_phone': lambda cs_number: True if re.match(
                '^(0[1-6][0-4]?)-(?:\d{3}|\d{4})-\d{4}$', cs_number) else False,
            'site_url': lambda site_url: True if re.match(
                '^(https?://)(([a-z0-9\-]+)\.)+[a-z0-9]{2,4}$', site_url) else False,
        }
        db = None
        try:
            db = get_db_connector()
            if db is None:
                return jsonify(message="DATABASE_INIT_ERROR"), 500
            data = {}
            for key in required_keys:
                data[key] = request.json[key]
            for field, validator in validation_rules.items():
                if not validator(data[field]):
                    return jsonify(message=field.upper() + "_VALIDATION_ERROR"), 400

            user_id = get_account_id(db, data['account'])
            if user_id:
                return jsonify(message="ACCOUNT_DUPLICATED"), 409

            data['password'] = bcrypt.hashpw(data['password'].encode('utf-8'),
                                             bcrypt.gensalt()).decode('utf-8')

            db.begin()
            user_id = insert_users(db, self.SELLER_ROLE_ID, data['account'])
            user_detail_id = insert_user_details(db, user_id=user_id, **data)
            manager_id = insert_managers(db, data['manager_phone'])
            insert_user_managers(db, user_detail_id=user_detail_id, manager_id=manager_id)
            insert_user_status(db, user_id=user_id, modifier_id=user_id, status_id=self.BASIC_STATUS_ID)
            db.commit()

            return jsonify(message="SIGN_UP_COMPLETE"), 200

        except pymysql.err.InternalError:
            db.rollback()
            return jsonify(message="DATABASE_DOES_NOT_EXIST"), 500
        except pymysql.err.OperationalError:
            db.rollback()
            return jsonify(message="DATABASE_AUTHORIZATION_DENIED"), 500
        except pymysql.err.ProgrammingError:
            db.rollback()
            return jsonify(message="DATABASE_SYNTAX_ERROR"), 500
        except pymysql.err.IntegrityError:
            db.rollback()
            return jsonify(message="FOREIGN_KEY_CONSTRAINT_ERROR"), 500
        except pymysql.err.DataError:
            db.rollback()
            return jsonify(message="DATA_ERROR"), 400
        except KeyError:
            db.rollback()
            return jsonify(message="KEY_ERROR"), 400
        except Exception as e:
            db.rollback()
            return jsonify(message=f"{e}"), 500
        finally:
            if db:
                db.close()

    @login_required
    def get(self, **kwargs):
        try:
            """회원정보 수정 페이지의 값을 뿌려주는 API

                Args:
                    account: 계정명,
                    password: 비밀번호

                Returns:
                    {
                        message: STATUS_MESSAGE
                        token: JWT_TOKEN
                        },
                    http status code

                Exceptions:
                    InternalError: DATABASE가 존재하지 않을 때 발생
                    OperationalError: DATABASE 접속이 인가되지 않았을 때 발생
                    ProgramingError: SQL syntax가 잘못되었을 때 발생
                    IntegrityError: 컬럼의 무결성을 해쳤을 때 발생
                    DataError: 컬럼 타입과 매칭되지 않는 값이 DB에 전달되었을 때 발생
                    KeyError: 엔드포인트에서 요구하는 키값이 전달되지 않았을 때 발생
            """

            db = get_db_connector()
            if db is None:
                return jsonify(message="DATABASE_INIT_ERROR"), 500

            if kwargs['role_id'] == self.MASTER_ROLE_ID:
                user_id = get_account_id(db, kwargs['user_account'])
            elif kwargs['role_id'] == self.SELLER_ROLE_ID:
                user_id = kwargs['user_id']

            detail_id = get_user_current_detail_id(db, user_id)
            status_history = get_user_status_history(db, user_id)
            details = get_detail(db, detail_id)
            attributes = get_attribute(db, details['seller_attribute_id'])
            managers = get_managers(db, detail_id)

            return jsonify(details=details,
                           history=status_history,
                           attributes=attributes,
                           managers=managers), 200

        except pymysql.err.InternalError:
            db.rollback()
            return jsonify(message="DATABASE_DOES_NOT_EXIST"), 500
        except pymysql.err.OperationalError:
            db.rollback()
            return jsonify(message="DATABASE_AUTHORIZATION_DENIED"), 500
        except pymysql.err.ProgrammingError:
            db.rollback()
            return jsonify(message="DATABASE_SYNTAX_ERROR"), 500
        except pymysql.err.IntegrityError:
            db.rollback()
            return jsonify(message="FOREIGN_KEY_CONSTRAINT_ERROR"), 500
        except pymysql.err.DataError:
            db.rollback()
            return jsonify(message="DATA_ERROR"), 400
        except KeyError:
            db.rollback()
            return jsonify(message="KEY_ERROR"), 400
        except Exception as e:
            db.rollback()
            return jsonify(message=f"{e}"), 500
        finally:
            if db:
                db.close()


@user_app.route('sign-in', methods=['POST'])
def sign_in():
    """로그인 API

        Args:
            account: 계정명,
            password: 비밀번호

        Returns:
            {
                message: STATUS_MESSAGE
                token: JWT_TOKEN
                },
            http status code

        Exceptions:
            InternalError: DATABASE가 존재하지 않을 때 발생
            OperationalError: DATABASE 접속이 인가되지 않았을 때 발생
            ProgramingError: SQL syntax가 잘못되었을 때 발생
            IntegrityError: Key의 무결성을 해쳤을 때 발생
            DataError: 컬럼 타입과 매칭되지 않는 값이 DB에 전달되었을 때 발생
            KeyError: 엔드포인트에서 요구하는 키값이 전달되지 않았을 때 발생
        """
    required_keys = ('account', 'password')

    db = None
    try:
        db = get_db_connector()
        if db is None:
            return jsonify(message="DATABASE_INIT_ERROR"), 500
        data = {}
        for key in required_keys:
            data[key] = request.json[key]

        result = get_id_role_password_status_from_account(db, data['account'])
        if not result:
            return jsonify(message="ACCOUNT_DOES_NOT_EXIST"), 404
        if not bcrypt.checkpw(data['password'].encode('utf-8'), result['password'].encode('utf-8')):
            return jsonify(message="PASSWORD_MISMATCH"), 403
        if (result['role_id'] == UserController.SELLER_ROLE_ID
                and result['status_id'] == UserController.BASIC_STATUS_ID):
            return jsonify(message="NOT_AUTHORIZED_USER"), 403

        token = jwt.encode(
            {
                'role_id': result['role_id'],
                'user_id': result['id'],
                'exp': datetime.utcnow() + timedelta(hours=1)
            },
            SERCRET,
            HASH_ALGORITHM
        )
        return jsonify(message="SIGN_IN_COMPLETE", token=token), 200

    except pymysql.err.InternalError:
        return jsonify(message="DATABASE_DOES_NOT_EXIST"), 500
    except pymysql.err.OperationalError:
        return jsonify(message="DATABASE_AUTHORIZATION_DENIED"), 500
    except pymysql.err.ProgrammingError:
        return jsonify(message="DATABASE_SYNTAX_ERROR"), 500
    except pymysql.err.IntegrityError:
        return jsonify(message="FOREIGN_KEY_CONSTRAINT_ERROR"), 500
    except pymysql.err.DataError:
        return jsonify(message="DATA_ERROR"), 400
    except KeyError:
        return jsonify(message="KEY_ERROR"), 400
    except Exception as e:
        return jsonify(message=f"{e}"), 500
    finally:
        if db:
            db.close()


user_app.add_url_rule('', view_func=UserController.as_view(name='user_seller'), methods=['GET', 'POST'])
user_app.add_url_rule('/<string:user_account>', view_func=UserController.as_view(name='user_master'), methods=['GET'])
