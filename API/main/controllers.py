import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath("API"))
sys.path.extend([BASE_DIR])

import pymysql

from connections import get_db_connector

from flask import Blueprint, request, jsonify
from .models import sidebar_list, sidebar_detail_list

main_app = Blueprint("main_app",__name__)


@main_app.route('/category', methods=['GET'])
def category():
    db = get_db_connector()
    db.begin()
    role_id = request.headers.get('role_id')
    data = sidebar_list(db,role_id)
    sidebar = [ {
                "id":side_list.get('id'),
                "name":side_list.get('name'),
                "detail_data":[{"id":detail.get('id'),
                                "name":detail.get('name')}
                             for detail in sidebar_detail_list(db,side_list.get('id'))]
                }for side_list in data]
    db.close()
    return jsonify(sidebar), 200
