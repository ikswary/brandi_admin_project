import os
import sys

import pymysql

BASE_DIR = os.path.dirname(os.path.abspath("API"))
sys.path.extend([BASE_DIR])

SELLER_ROLE_ID = 2


def is_account_exists(db, account):
    with db.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute("""
        SELECT COUNT(*) count FROM users
        WHERE account = %s
        """, account)

        return cursor.fetchone()['count']


def insert_users(db, account):
    with db.cursor() as cursor:
        insert_user_query = """
        INSERT INTO users(role_id, account)
        VALUES(%s, %s)
        """
        cursor.execute(insert_user_query, (SELLER_ROLE_ID, account))

        return cursor.lastrowid


def insert_user_details(db, **args):
    with db.cursor() as cursor:
        insert_user_detail_query = """
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
        cursor.execute(insert_user_detail_query, args)

        return cursor.lastrowid


def insert_managers(db, phone):
    with db.cursor() as cursor:
        insert_manager_query = """
        INSERT INTO managers(phone) VALUES(%s)
        """
        cursor.execute(insert_manager_query, phone)

        return cursor.lastrowid


def insert_user_managers(db, **args):
    with db.cursor() as cursor:
        insert_user_manager_query = """
        INSERT INTO user_managers(user_detail_id, manager_id)
        VALUES(%(user_detail_id)s, %(manager_id)s)
        """
        cursor.execute(insert_user_manager_query, args)
