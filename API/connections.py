import pymysql
from pymysql.err import DataError

from my_settings import MYSQL_CONFIGS


def get_db_connector():
    connector = pymysql.connect(**MYSQL_CONFIGS)
    return connector


def get_cursor(db):
    cursor = db.cursor()
    cursor.execute("SET AUTOCOMMIT = FALSE;")
    return cursor


def get_dict_cursor(db):
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SET AUTOCOMMIT = FALSE;")
    return cursor
