import pymysql

def seller_list(db):
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("""
            SELECT user_id, profile_image, seller_name FROM seller_details
            JOIN users on users.id=seller_details.user_id
            WHERE seller_details.enddate="9999-12-31 23:59:59" AND seller_details.profile_image is not  Null AND users.role_id=2
            """)

            return cursor.fetchall()
    except Exception as e:
        raise e
