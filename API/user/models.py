import os
import sys

import pymysql

BASE_DIR = os.path.dirname(os.path.abspath("API"))
sys.path.extend([BASE_DIR])

SELLER_ROLE_ID = 2


def is_account_exists(db, account):
    try:
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("""
        SELECT COUNT(*) count FROM users
        WHERE account = %s
        """, account)

        return cursor.fetchone()['count']

    finally:
        if cursor:
            cursor.close()


def get_account_id(db, account):
    try:
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("""
        SELECT id FROM users
        WHERE account = %s
        """, account)

        return cursor.fetchone()['id']

    finally:
        if cursor:
            cursor.close()


def sign_up(db, data):
    try:
        cursor = db.cursor()
        insert_user_query = """
            INSERT INTO users(role_id, account)
            VALUES(%s, %s)
            """
        cursor.execute(insert_user_query, (SELLER_ROLE_ID, data['account']))
        user_id = get_account_id(db, data['account'])

        insert_user_detail_query = """
            INSERT INTO seller_details(
            user_id,
            modifier_id,
            password,
            seller_name,
            seller_name_eng,
            cs_number,
            seller_attribute_id, site_url
            )
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
            """
        cursor.execute(insert_user_detail_query,
                       (user_id,
                        user_id,
                        data['password'],
                        data['seller_name'],
                        data['seller_name_eng'],
                        data['cs_number'],
                        data['seller_attribute_id'],
                        data['site_url'])
                       )

    except pymysql.err.DataError:
        raise pymysql.err.DataError
    finally:
        if cursor:
            cursor.close()
