import os, sys

BASE_DIR = os.path.dirname(os.path.abspath("API"))
sys.path.extend([BASE_DIR])

import pymysql

from flask import Blueprint, request, jsonify

from connections import get_db_connector
from decorator import login_required
from models.main_models import MainDao

main_app = Blueprint("main_app", __name__)
main_dao = MainDao()

@main_app.route('/category', methods=['GET'])
@login_required
def category(**kwargs):
    """사이드바 예시 API
    API 작성:
        최진아

    Args:
        role_id : user의 권한 확인

    Returns:
        {data : sidebar_list}, http status code

    Exceptions:
        InternalError: DATABASE가 존재하지 않을 때 발생
        OperationalError: DATABASE 접속이 인가되지 않았을 때 발생
        ProgramingError: SQL syntax가 잘못되었을 때 발생
        IntegrityError: Key의 무결성을 해쳤을 때 발생
        DataError: 컬럼 타입과 매칭되지 않는 값이 DB에 전달되었을 때 발생
        KeyError: 엔드포인트에서 요구하는 키값이 전달되지 않았을 때 발생
    """

    db = None
    try:
        db = get_db_connector()
        if db is None:
            return jsonify(message="DATABASE_INIT_ERROR"), 500
        role_id = kwargs['role_id']

        if main_dao.role(db, role_id) is None:
            return jsonify(message="DATA_DOES_NOT_EXIST"), 404

        data = main_dao.sidebar_list(db, role_id)

        sidebar = [{
            "id": side_list.get('id'),
            "name": side_list.get('name'),
            "detail_data": [{"id": detail.get('id'),
                             "name": detail.get('name')}
                            for detail in main_dao.sidebar_detail_list(db, side_list.get('id'))]
        } for side_list in data]

        return jsonify(data=sidebar), 200

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
