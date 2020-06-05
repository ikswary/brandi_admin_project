import os
import sys

import pymysql

BASE_DIR = os.path.dirname(os.path.abspath("API"))
sys.path.extend([BASE_DIR])

SELLER_ROLE_ID = 2


def is_account_exists(db, account):
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
            SELECT COUNT(*) count FROM users
            WHERE account = %s
            """
            cursor.execute(query, account)

            return cursor.fetchone()['count']
    except Exception as e:
        raise e


def insert_users(db, account):
    try:
        with db.cursor() as cursor:
            query = """
            INSERT INTO users(role_id, account)
            VALUES(%s, %s)
            """
            cursor.execute(query, (SELLER_ROLE_ID, account))

            return cursor.lastrowid
    except Exception as e:
        raise e


def insert_user_details(db, **args):
    try:
        with db.cursor() as cursor:
            query = """
            INSERT INTO seller_details(
            user_id,
            modifier_id,
            password,
            seller_name,
            seller_name_eng,
            cs_phone,
            seller_attribute_id,
            site_url
            )
            VALUES(%(user_id)s,
             %(user_id)s, 
             %(password)s, 
             %(seller_name)s, 
             %(seller_name_eng)s, 
             %(cs_phone)s, 
             %(seller_attribute_id)s, 
             %(site_url)s
             )
            """
            cursor.execute(query, args)

            return cursor.lastrowid
    except Exception as e:
        raise e


def insert_managers(db, phone):
    try:
        with db.cursor() as cursor:
            query = """
            INSERT INTO managers(phone) VALUES(%s)
            """
            cursor.execute(query, phone)

            return cursor.lastrowid
    except Exception as e:
        raise e


def insert_user_managers(db, **args):
    try:
        with db.cursor() as cursor:
            query = """
            INSERT INTO user_managers(user_detail_id, manager_id)
            VALUES(%(user_detail_id)s, %(manager_id)s)
            """
            cursor.execute(query, args)
    except Exception as e:
        raise e


def get_id_password_from_account(db, account):
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
            SELECT details.password from users 
            join seller_details as details 
            on details.user_id = users.id where account = %s
            """
            cursor.execute(query, account)
            result = cursor.fetchone()
            result['user_id'] = cursor.lastrowid
            return result

    except Exception as e:
        raise e
