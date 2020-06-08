import pymysql


def get_id_from_account(db, account):
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
            SELECT id FROM users
            WHERE account = %s AND is_deleted = 0
            """
            cursor.execute(query, account)
            if cursor.rowcount:
                return cursor.fetchone()['id']

            return None

    except Exception as e:
        raise e


def get_account_from_id(db, user_id):
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
            SELECT account FROM users
            WHERE id = %s AND is_deleted = 0
            """
            cursor.execute(query, user_id)
            if cursor.rowcount:
                return cursor.fetchone()['account']

            return None

    except Exception as e:
        raise e


def insert_users(db, role_id, account):
    try:
        with db.cursor() as cursor:
            query = """
            INSERT INTO users(role_id, account)
            VALUES(%s, %s)
            """
            cursor.execute(query, (role_id, account))

            return cursor.lastrowid
    except Exception as e:
        raise e


def insert_user_details(db, **kwargs):
    try:
        with db.cursor() as cursor:
            query = """
            INSERT INTO seller_details(
            user_id,
            modifier_id,
            password,
            seller_name,
            seller_name_eng,
            cs_phone,
            seller_attribute_id,
            site_url
            )
            VALUES(%(user_id)s,
             %(user_id)s,
             %(password)s,
             %(seller_name)s,
             %(seller_name_eng)s,
             %(cs_phone)s,
             %(seller_attribute_id)s,
             %(site_url)s
             )
            """
            cursor.execute(query, kwargs)

            return cursor.lastrowid
    except Exception as e:
        raise e


def insert_managers(db, phone):
    try:
        with db.cursor() as cursor:
            query = """
            INSERT INTO managers(phone) VALUES(%s)
            """
            cursor.execute(query, phone)

            return cursor.lastrowid
    except Exception as e:
        raise e


def insert_user_managers(db, **kwargs):
    try:
        with db.cursor() as cursor:
            query = """
            INSERT INTO user_managers(user_detail_id, manager_id)
            VALUES(%(user_detail_id)s, %(manager_id)s)
            """
            cursor.execute(query, kwargs)
    except Exception as e:
        raise e


def insert_user_status(db, **kwargs):
    try:
        with db.cursor() as cursor:
            query = """
            INSERT INTO user_status(user_id, modifier_id, status_id)
            VALUES(%(user_id)s, %(modifier_id)s, %(status_id)s)
            """
            cursor.execute(query, kwargs)
    except Exception as e:
        raise e


def get_id_role_password_status_from_account(db, account):
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
            SELECT users.id, users.role_id, details.password, status.status_id AS status_id
            FROM users
            JOIN seller_details AS details
            ON (details.user_id = users.id
            AND details.enddate = 99991231235959)
            JOIN user_status AS status
            ON (status.user_id = users.id
            AND details.enddate = 99991231235959)
            WHERE users.account = %s AND users.is_deleted = 0
            """
            cursor.execute(query, account)
            if cursor.rowcount:
                return cursor.fetchone()

            return None

    except Exception as e:
        raise e


def get_user_status_history(db, user_id):
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
            SELECT us.startdate, status.name, user.account
            FROM user_status AS us
            JOIN statuses AS status
            ON us.status_id = status.id
            JOIN users AS user
            ON us.modifier_id = user.id
            WHERE us.user_id = %s AND enddate = 99991231235959
            """
            cursor.execute(query, user_id)
            if cursor.rowcount:
                return cursor.fetchall()

            return None

    except Exception as e:
        raise e


def get_user_current_detail_id(db, user_id):
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
            SELECT id FROM seller_details
            WHERE enddate = 99991231235959 AND user_id = %s
            """
            cursor.execute(query, user_id)
            if cursor.rowcount:
                return cursor.fetchone()['id']

            return None

    except Exception as e:
        raise e


def get_detail(db, detail_id):
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
            SELECT seller_attribute_id,
            seller_name,
            seller_name_eng,
            cs_phone,
            site_url,
            profile_image,
            introduction_short,
            introduction_detail,
            background_image,
            zip_code,
            address,
            address_detail,
            weekday_start_time,
            weekday_end_time,
            weekend_start_time,
            weekend_end_time,
            bank,
            bank_account_name,
            bank_account_number,
            height,
            top_size,
            bottom_size,
            foot_size,
            feed
            FROM seller_details
            WHERE id = %s
            """
            cursor.execute(query, detail_id)
            if cursor.rowcount:
                return cursor.fetchone()

            return None

    except Exception as e:
        raise e


def get_attribute(db, seller_attributes_id):
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
            SELECT id, name FROM seller_attributes
            WHERE attribute_group_id = (SELECT attribute_group_id 
            FROM brandi_admin.seller_attributes 
            WHERE id = %s)
            """
            cursor.execute(query, seller_attributes_id)
            if cursor.rowcount:
                return cursor.fetchall()

            return None

    except Exception as e:
        raise e


def get_managers(db, detail_id):
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
            SELECT managers.name, managers.phone, managers.email 
            FROM user_managers AS um
            JOIN managers ON um.manager_id = managers.id
            WHERE um.user_detail_id = %s AND um.is_deleted = 0
            """
            cursor.execute(query, detail_id)
            if cursor.rowcount:
                return cursor.fetchall()

            return None

    except Exception as e:
        raise e
