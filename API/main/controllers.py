import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath("API"))
sys.path.extend([BASE_DIR])

import pymysql

from connections import get_db_connector

from flask import Blueprint, request, jsonify
from .models import sidebar_list, sidebar_detail_list, role

main_app = Blueprint("main_app", __name__)


@main_app.route('/category', methods=['GET'])
def category():
    """사이드바 예시 API

    Args:
        role_id : user의 권한 확인

    Returns:
        {data : sidebar_list}, http status code
    """

    db = None
    try:
        db = get_db_connector()
        if db is None:
            return jsonify(message="DATABASE_INIT_ERROR"), 500

        role_id = request.headers['role_id']

        if role(db, role_id) is None:
            return jsonify(message="DATA_DOES_NOT_EXIST"), 404

        data = sidebar_list(db, role_id)

        sidebar = [{
            "id": side_list.get('id'),
            "name": side_list.get('name'),
            "detail_data": [{"id": detail.get('id'),
                             "name": detail.get('name')}
                            for detail in sidebar_detail_list(db, side_list.get('id'))]
        } for side_list in data]

        return jsonify(data=sidebar), 200

    except pymysql.err.OperationalError:
        return jsonify(message="DATABASE_AUTHORIZATION_DENIED"), 500

    except pymysql.err.InternalError:
        return jsonify(message="DATABASE_DOES_NOT_EXIST"), 500

    except KeyError:
        return jsonify(message="KEY_ERROR"), 400

    except Exception as e:
        return jsonify(message={e}), 500

    finally:
        if db:
            db.close()
