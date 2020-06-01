import pymysql


def is_account_exists(db, account):
    with db.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute("""
        SELECT COUNT(*) count FROM users 
        WHERE account = %s
        """, account)

        return cursor.fetchone()['count']


def get_account_id(db, account):
    with db.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute("""
        SELECT id FROM users 
        WHERE account = %s
        """, account)
        return cursor.fetchone()['id']


def sign_up_model(db, data):
    SELLER_ROLE_ID = 2

    with db.cursor() as cursor:
        insert_user_query = """
            INSERT INTO users(role_id, account) 
            VALUES(%s, %s)
            """
        user_id = cursor.execute(insert_user_query, (SELLER_ROLE_ID, data['account']))
        insert_user_detail_query = """
            INSERT INTO seller_details(user_id, modifier_id, password, seller_name, 
            seller_name_eng, cs_number, seller_attribute_id, site_url) 
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
            """

        cursor.execute(insert_user_detail_query,
                       (user_id,
                        user_id,
                        data['password'],
                        data['seller_name'],
                        data['seller_name_eng'],
                        data['cs_number'],
                        data['seller_attribute_id'],
                        data['site_url'])
                       )
