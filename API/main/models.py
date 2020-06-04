import pymysql

def role(db, role_id):
    try:
        cursor = db.cursor()
        cursor.execute("""
        SELECT id FROM roles
        WHERE id = %s
        """, role_id)

        return cursor.fetchone()

    finally:
        cursor.close()


def sidebar_list(db, role_id):
    try:
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("""
        SELECT id,name FROM sidebar
        WHERE role_id = %s
        """, role_id)

        return cursor.fetchall()

    finally:
        cursor.close()


def sidebar_detail_list(db, sidebar_id):
    try:
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("""
        SELECT id,name FROM sidebar_detail
        WHERE sidebar_id = %s
        """, sidebar_id)

        return cursor.fetchall()

    finally:
        cursor.close()
