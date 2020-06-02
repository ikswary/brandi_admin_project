import pymysql
from pymysql.err import DataError, ProgrammingError

from my_settings import MYSQL_CONFIGS


def get_db_connector():
    connector = pymysql.connect(**MYSQL_CONFIGS)

    return connector


def get_cursor(db):
    return db.cursor()


def get_dict_cursor(db):
    return db.cursor(pymysql.cursors.DictCursor)
