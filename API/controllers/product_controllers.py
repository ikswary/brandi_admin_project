import os, sys

BASE_DIR = os.path.dirname(os.path.abspath("API"))
sys.path.extend([BASE_DIR])

import pymysql

from flask import Blueprint, request, jsonify

from connections import get_db_connector
from decorator import login_required
from models.product_models import seller_list
from models.main_models import role

product_app = Blueprint("product_app", __name__)


@product_app.route('seller', methods=['GET'])
@login_required
def seller(**kwargs):
    """셀러 리스트 불러오는 API


    """
    db = None
    try:
        db = get_db_connector()
        if db is None:
            return jsonify(message="DATABASE_INIT_ERROR"), 500
        role_id = kwargs['role_id']

        if role_id == 1:
            seller_data = seller_list(db)

            sellers = [{
                "id": seller.get('user_id'),
                "image": seller.get('profile_image'),
                "name": seller.get('seller_name')} for seller in seller_data]

            return jsonify(data=sellers), 200
        elif role_id == 2:
            return jsonify(message="UNAUTHORIZED"), 401
        elif role(db, role_id) is None:
            return jsonify(message="DATA_DOES_NOT_EXIST"), 404

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
    except Exception as e:
        return jsonify(message=f"{e}"), 500
    finally:
        if db:
            db.close()
