import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath("API"))
sys.path.extend([BASE_DIR])

from my_settings import MYSQL_CONFIGS

DB_NAME = MYSQL_CONFIGS['database']


def init_database(db):
    cursor = db.cursor()
    db.begin()
    cursor.execute("DROP DATABASE " + DB_NAME)
    cursor.execute("CREATE DATABASE " + DB_NAME + " character set utf8mb4 collate utf8mb4_general_ci")
    cursor.execute("use " + DB_NAME)
    db.commit()
    cursor.close()


def import_aquery_to_list(file):
    # Aquery에서 export된 파일에서 쓸모없는 부분들을 지워 list로 리턴

    file.readline()
    aquery_string = file.read()
    aquery_string = aquery_string.replace('-- roles Table Create SQL', '')
    aquery_string = aquery_string.replace('\n', '')
    aquery_string = ' '.join(aquery_string.split())
    aquery_string = aquery_string.replace('`is_deleted` TINYINT', '`is_deleted` TINYINT DEFAULT 0 ')
    aquery_string = aquery_string.replace('`on_sale` TINYINT', '`on_sale` TINYINT DEFAULT 1 ')
    aquery_string = aquery_string.replace('`on_list` TINYINT', '`on_list` TINYINT DEFAULT 1 ')

    return aquery_string.split(';')[:-1]
