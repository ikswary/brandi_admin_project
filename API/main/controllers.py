import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath("API"))
sys.path.extend([BASE_DIR])

from connections import get_db_connector, ProgrammingError

from flask import Blueprint, request, jsonify
from .models import sidebar_list, sidebar_detail_list

main_app = Blueprint("main_app", __name__)


@main_app.route('/category', methods=['GET'])
def category():
    """사이드바 예시 API

    Args:
        role_id : user의 권한 확인

    Returns:
        {data : sidebar_list}, http status code
    """
    try:
        db = get_db_connector()
        role_id = request.headers.get('role_id')

        data = sidebar_list(db, role_id)

        sidebar = [{
            "id": side_list.get('id'),
            "name": side_list.get('name'),
            "detail_data": [{"id": detail.get('id'),
                            "name": detail.get('name')}
                            for detail in sidebar_detail_list(db, side_list.get('id'))]
        } for side_list in data]

        return jsonify(data=sidebar), 200

    except ProgrammingError:
        return jsonify(message="MISSING_AUTHORIZATION_TOKEN"), 400

    except AttributeError:
        return jsonify(message="DATABASE_INIT_ERROR"), 404

    finally:
        if db:
            db.close()
