import pymysql

def role(db, role_id):
    try:
        with db.cursor() as cursor:
            cursor.execute("""
            SELECT id FROM roles
            WHERE id = %s
            """, role_id)

            return cursor.fetchone()
    except Exception as e:
        raise e


def sidebar_list(db, role_id):
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("""
            SELECT id,name FROM sidebar
            WHERE role_id = %s
            """, role_id)

            return cursor.fetchall()
    except Exception as e:
        raise e


def sidebar_detail_list(db, sidebar_id):
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("""
            SELECT id,name FROM sidebar_detail
            WHERE sidebar_id = %s
            """, sidebar_id)

            return cursor.fetchall()
    except Exception as e:
        raise e
