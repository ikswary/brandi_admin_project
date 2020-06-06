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


def first_category(db, attribute_group_id):
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("""
            SELECT id, name FROM first_categories
            WHERE attribute_group_id = %s
            """, attribute_group_id)

            return cursor.fetchall()
    except Exception as e:
        raise e


def second_category(db, first_category_id):
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("""
            SELECT id, name FROM second_categories
            WHERE first_category_id = %s
            """, first_category_id)

            return cursor.fetchall()
    except Exception as e:
        raise e


def get_attribute_group_id(db, user_id):
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("""
            SELECT attribute_group_id FROM seller_attributes
            JOIN seller_details
            ON seller_details.seller_attribute_id = seller_attributes.id
            WHERE user_id = %s
            """, user_id)

            return cursor.fetchone()
    except Exception as e:
        raise e
