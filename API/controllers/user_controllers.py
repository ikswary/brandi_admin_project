import os, sys, re

BASE_DIR = os.path.dirname(os.path.abspath("API"))
sys.path.extend([BASE_DIR])

import pymysql
import bcrypt
import jwt
from jsonschema import validate, ValidationError
from datetime import datetime, timedelta
from flask import Blueprint, request, jsonify
from flask.views import MethodView

from my_settings import SERCRET, HASH_ALGORITHM
from connections import get_db_connector
from decorator import login_required
from jsonschemas import (
    SIGN_UP_SCHEMA,
    SIGN_IN_SCHEMA,
    USER_DATA_MODIFY_MASTER,
    USER_DATA_MODIFY_SELLER
)
from models.user_models import UserDao
from services.user_service import (
    get_user_data_service,
    sign_up_service,
    user_data_formatter,
    user_data_deformatter,
    user_update_service
)

user_app = Blueprint('user_app', __name__)
user_dao = UserDao()


class User(MethodView):
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
            ValidationError : 엔드포인트에서 요구하는 키값이 전달되지 않았을 때 발생
        """

        db = None
        try:
            validate(request.json, SIGN_UP_SCHEMA)
            data = request.json

            db = get_db_connector()
            if db is None:
                return jsonify(message="DATABASE_INIT_ERROR"), 500

            user_id = user_dao.get_id_from_account(db, data['account'])
            if user_id:
                return jsonify(message="ACCOUNT_DUPLICATED"), 409

            data['password'] = bcrypt.hashpw(data['password'].encode('utf-8'),
                                             bcrypt.gensalt()).decode('utf-8')

            db.begin()
            sign_up_service(db, data)
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
        except ValidationError as e:
            error_path = str(e.path)[8:-3]
            return jsonify(message=f"{error_path.upper()}_VALIDATION_ERROR"), 400
        except Exception as e:
            db.rollback()
            return jsonify(message=f"{e}"), 500
        finally:
            if db:
                db.close()

    @login_required
    def get(self, **kwargs):
        """회원정보 수정 페이지의 값을 뿌려주는 API

            Header:
                Authorizaion: jwt

            URL params:
                <string:user_account>: 마스터권한일 경우 대상


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
        try:
            db = get_db_connector()
            if db is None:
                return jsonify(message="DATABASE_INIT_ERROR"), 500

            # master 권한일 경우 urlparameter에서 대상 account를 가져오고 account에 해당하는 user_id를 가져온다
            if kwargs['role_id'] == self.MASTER_ROLE_ID:
                user_account = kwargs.get('user_account', '')
                user_id = user_dao.get_id_from_account(db, user_account)
            # seller 권한일 경우 token에서 user_id를 가져오고 id에 해당하는 account를 가져온다
            elif kwargs['role_id'] == self.SELLER_ROLE_ID:
                user_id = kwargs['user_id']
                user_account = user_dao.get_account_from_id(db, user_id)
            # get_id_from_account, get_account_from_id중 하나라도 제대로 동작하지 않았을 경우 400
            if user_account is None or user_id is None:
                return jsonify(message="INVALID_REQUEST"), 400

            result = get_user_data_service(db, user_id, user_account, kwargs['role_id'])

            return jsonify(user_data_formatter(*result)), 200

        except pymysql.err.INVALID_REQUESTternalError:
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
    def put(self, **kwargs):
        """회원정보 수정 페이지에서 입력받은 값으로 회원정보를 수정하는 API

            Header:
                Authorizaion: jwt

            Args:
                profile_image: 프로필 이미지(url),
                seller_attribute: 셀러 속성 id,
                seller_name: 셀러 이름,
                seller_name_eng: 셀러 영어 이름,
                seller_account: 셀러 계정,
                "background_image": 배경 이미지(url),
                "introduction_short": 셀러 한줄 소개,
                "introduction_detail": 셀러 상세 소개,
                "site_url": 홈페이지,
                "manager": {
                                "name: 담당자 이름,
                                "phone": 담당자 전화번호,
                                "email": 담당자 이메일
                            }
                "cs_phone": 고객센터 전화번호,
                "zip_code": 우편번호,
                "address": 주소,
                "address_detail": 상세 주소,
                "weekday_start_time": 고객센터 운영시작시간(주중),
                "weekday_end_time": 고객센터 운영종료시간(주중),
                "weekend_start_time": 고객센터 운영시작시간(주말),
                "weekend_end_time": 고객센터 운영시작시간(주말),
                "bank": 정산은행,
                "bank_account_name": 예금주,
                "bank_account_number": 계좌번호
                "height": 모델 키,
                "top_size": 모델 상의 사이즈,
                "bottom_size": 모델 하의 사이즈,
                "foot_size": 모델 발 사이즈

            Returns:
                {message: STATUS_MESSAGE}, http status code

            Exceptions:
                InternalError: DATABASE가 존재하지 않을 때 발생
                OperationalError: DATABASE 접속이 인가되지 않았을 때 발생
                ProgramingError: SQL syntax가 잘못되었을 때 발생
                IntegrityError: 컬럼의 무결성을 해쳤을 때 발생
                DataError: 컬럼 타입과 매칭되지 않는 값이 DB에 전달되었을 때 발생
                KeyError: 엔드포인트에서 요구하는 키값이 전달되지 않았을 때 발생
        """

        try:
            db = get_db_connector()
            if db is None:
                return jsonify(message="DATABASE_INIT_ERROR"), 500

            # master 권한일 경우에 대한 validation 및 urlparameter에서 가져온 account에 해당하는 user_id를 조회
            if kwargs['role_id'] == self.MASTER_ROLE_ID:
                validate(request.json, USER_DATA_MODIFY_MASTER)
                user_id = user_dao.get_id_from_account(db, kwargs['user_account'])
                modifier_id = kwargs['user_id']
            # seller 권한일 경우에 대한 validation 및 token에서 user_id를 조회
            elif kwargs['role_id'] == self.SELLER_ROLE_ID:
                validate(request.json, USER_DATA_MODIFY_SELLER)
                user_id = kwargs['user_id']
                modifier_id = user_id
            # user_id가 존재하지 않을 경우 유효하지 않은 동작으로 400 출력
            if user_id is None:
                return jsonify(message="INVALID_REQUEST"), 400

            # request로 전달받은 json을 테이블별로 정렬
            details, managers = user_data_deformatter(**request.json)
            db.begin()
            user_update_service(db, user_id, modifier_id, details, managers)
            db.commit()

            return jsonify(''), 200

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
            ValidationError : 엔드포인트에서 요구하는 키값이 전달되지 않았을 때 발생
        """

    db = None
    try:
        db = get_db_connector()

        validate(request.json, SIGN_IN_SCHEMA)
        data = request.json

        if db is None:
            return jsonify(message="DATABASE_INIT_ERROR"), 500

        result = user_dao.get_id_role_password_status_from_account(db, data['account'])
        if not result:
            return jsonify(message="ACCOUNT_DOES_NOT_EXIST"), 404
        if not bcrypt.checkpw(data['password'].encode('utf-8'), result['password'].encode('utf-8')):
            return jsonify(message="PASSWORD_MISMATCH"), 403
        if (result['role_id'] == User.SELLER_ROLE_ID
                and result['status_id'] == User.BASIC_STATUS_ID):
            return jsonify(message="NOT_AUTHORIZED_USER"), 403

        # jwt 작성
        token = jwt.encode(
            {
                'role_id': result['role_id'],
                'user_id': result['id'],
                'exp': datetime.utcnow() + timedelta(hours=12)
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
    except ValidationError as e:
        error_path = str(e.path)[8:-3]
        return jsonify(message=f"{error_path.upper()}_VALIDATION_ERROR"), 400
    except Exception as e:
        return jsonify(message=f"{e}"), 500
    finally:
        if db:
            db.close()


user_app.add_url_rule('', view_func=User.as_view(name='user_seller'), methods=['GET', 'POST', 'PUT'])
user_app.add_url_rule('/<string:user_account>', view_func=User.as_view(name='user_master'), methods=['GET', 'PUT'])
