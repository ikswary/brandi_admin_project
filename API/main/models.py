import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath("API"))
sys.path.extend([BASE_DIR])

from connections import get_dict_cursor

def sidebar_list(db, role_id):
    try:
        cursor = get_dict_cursor(db)
        cursor.execute("""
        SELECT id,name FROM sidebar
        WHERE role_id = %s
        """, role_id)

        return cursor.fetchall()

    finally:
        cursor.close()

def sidebar_detail_list(db, sidebar_id):
    try:
        cursor = get_dict_cursor(db)
        cursor.execute("""
        SELECT id,name FROM sidebar_detail
        WHERE sidebar_id = %s
        """, sidebar_id)

        return cursor.fetchall()

    finally:
        cursor.close()
