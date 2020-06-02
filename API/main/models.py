import pymysql


def sidebar_list(db, role_id):
    try:
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("""
                SELECT id,name FROM sidebar WHERE role_id = %s
                        """, role_id)
        result = cursor.fetchall()
    finally:
        cursor.close()
    return result


def sidebar_detail_list(db, sidebar_id):
    try:
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("""
                SELECT id,name FROM sidebar_detail WHERE sidebar_id = %s
        """, sidebar_id)
        result = cursor.fetchall()
    finally:
        cursor.close()
    return result
