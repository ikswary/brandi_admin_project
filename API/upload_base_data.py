import csv

from connections import get_db_connector

csv_list = [
    'actions', 'attribute_group', 'color_filters', 'colors', 'countries', 'first_categories',
    'roles', 'second_categories', 'seller_attributes', 'seller_statuses', 'sidebar',
    'sidebar_detail', 'sizes', 'status_actions', 'style_filters'
]

db = get_db_connector()
db.begin()
cursor = db.cursor()

for table_name in csv_list:
    csv_url = 'csv/' + table_name + '.csv'
    with open(csv_url) as csv_file:
        reader = csv.reader(csv_file)
        records = [x for x in reader]
        columns = records.pop(0)
        values = ('%s,' * len(columns))[:-1]

        query = f"""INSERT INTO {table_name}({','.join(columns)}) VALUES({values})"""
        cursor.executemany(query, records)

db.commit()
cursor.close()
db.close()
print("UPLOAD COMPLETE")