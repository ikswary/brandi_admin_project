from create_table.create_table_utils import init_database, import_aquery_to_list
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
print('MIGRATION COMPLETE')
