import os
import sys

ROOT_DIR = os.path.dirname(os.path.abspath("API"))
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
sys.path.extend([ROOT_DIR])
os.chdir(BASE_DIR)

from create_table_utils import init_database, import_aquery_to_list
from connections import get_db_connector

db = get_db_connector()
cursor = db.cursor()

init_database(db)

with open('aquery_exports/brandi_20200530_29_44.txt', 'r') as aquery_file:
    TABLE_QUERIES = import_aquery_to_list(aquery_file)

for query in TABLE_QUERIES:
    cursor.execute(query)

db.commit()
cursor.close()
db.close()
print('COMPLETE')
