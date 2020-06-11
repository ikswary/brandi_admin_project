import pymysql


class UserDao:
    def get_id_from_account(self, db, account):
        try:
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                SELECT id FROM users
                WHERE account = %s AND is_deleted = 0
                """

                affected_row = cursor.execute(query, account)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')

                if cursor.rowcount:
                    return cursor.fetchone()['id']

                return None

        except Exception as e:
            raise e

    def get_account_from_id(self, db, user_id):
        try:
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                SELECT account FROM users
                WHERE id = %s AND is_deleted = 0
                """
                affected_row = cursor.execute(query, user_id)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')
                if cursor.rowcount:
                    return cursor.fetchone()['account']

                return None

        except Exception as e:
            raise e

    def insert_users(self, db, role_id, account):
        try:
            with db.cursor() as cursor:
                query = """
                INSERT INTO users(role_id, account)
                VALUES(%s, %s)
                """

                affected_row = cursor.execute(query, (role_id, account))
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')

                return cursor.lastrowid
        except Exception as e:
            raise e

    def insert_user_details_first(self, db, **kwargs):
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

                affected_row = cursor.execute(query, kwargs)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')

                return cursor.lastrowid
        except Exception as e:
            raise e

    def insert_managers_first(self, db, phone):
        try:
            with db.cursor() as cursor:
                query = """
                INSERT INTO managers(phone) VALUES(%s)
                """

                affected_row = cursor.execute(query, phone)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')

                return cursor.lastrowid

        except Exception as e:
            raise e

    def insert_user_managers_first(self, db, **kwargs):
        try:
            with db.cursor() as cursor:
                query = """
                INSERT INTO user_managers(user_id, manager_id)
                VALUES(%(user_id)s, %(manager_id)s)
                """

                affected_row = cursor.execute(query, kwargs)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')

        except Exception as e:
            raise e

    def insert_user_status(self, db, **kwargs):
        try:
            with db.cursor() as cursor:
                query = """
                INSERT INTO user_status(user_id, modifier_id, status_id)
                VALUES(%(user_id)s, %(modifier_id)s, %(status_id)s)
                """

                affected_row = cursor.execute(query, kwargs)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')

        except Exception as e:
            raise e

    def get_id_role_password_status_from_account(self, db, account):
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

                affected_row = cursor.execute(query, account)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')
                if cursor.rowcount:
                    return cursor.fetchone()

                return None

        except Exception as e:
            raise e

    def get_user_status_history_as_master(self, db, user_id):
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

                affected_row = cursor.execute(query, user_id)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')
                if cursor.rowcount:
                    return cursor.fetchall()

                raise Exception('QUERY_RETURNED_NOTHING')

        except Exception as e:
            raise e

    def get_user_status_history_as_seller(self, db, user_id):
        try:
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                SELECT us.startdate, status.name
                FROM user_status AS us
                JOIN statuses AS status
                ON us.status_id = status.id
                WHERE us.user_id = %s AND enddate = 99991231235959
                """

                affected_row = cursor.execute(query, user_id)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')
                if cursor.rowcount:
                    return cursor.fetchall()

                raise Exception('QUERY_RETURNED_NOTHING')

        except Exception as e:
            raise e

    def get_attribute(self, db, seller_attributes_id):
        try:
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                SELECT id, name FROM seller_attributes
                WHERE attribute_group_id = (SELECT attribute_group_id 
                FROM seller_attributes 
                WHERE id = %s)
                """

                affected_row = cursor.execute(query, seller_attributes_id)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')
                if cursor.rowcount:
                    return cursor.fetchall()

                raise Exception('QUERY_RETURNED_NOTHING')

        except Exception as e:
            raise e

    def get_managers(self, db, user_id):
        try:
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                SELECT managers.name, managers.phone, managers.email 
                FROM user_managers AS um
                JOIN managers ON um.manager_id = managers.id
                WHERE um.user_id = %s AND um.is_deleted = 0
                """

                affected_row = cursor.execute(query, user_id)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')
                if cursor.rowcount:
                    return cursor.fetchall()

                raise Exception('QUERY_RETURNED_NOTHING')

        except Exception as e:
            raise e

    def get_user_detail(self, db, user_id):
        try:
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                SELECT 
                password,
                seller_attribute_id,
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
                TIME_FORMAT(weekday_start_time, '%%H:%%i') AS weekday_start_time,
                TIME_FORMAT(weekday_end_time, '%%H:%%i') AS weekday_end_time,
                TIME_FORMAT(weekend_start_time, '%%H:%%i') AS weekend_start_time,
                TIME_FORMAT(weekend_end_time, '%%H:%%i') AS weekend_end_time,
                bank,
                bank_account_name,
                bank_account_number,
                height,
                top_size,
                bottom_size,
                foot_size,
                feed
                FROM seller_details
                WHERE user_id = %s AND enddate = 99991231235959
                """

                affected_row = cursor.execute(query, user_id)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')
                if cursor.rowcount:
                    return cursor.fetchone()

                raise Exception('QUERY_MACTHING_RECORD_DOES_NOT_EXIST')

        except Exception as e:
            raise e

    def update_detail(self, db, user_id, enddate):
        try:
            with db.cursor() as cursor:
                query = """
                UPDATE seller_details SET enddate = %s
                WHERE user_id = %s AND enddate = 99991231235959
                """

                affected_row = cursor.execute(query, (enddate, user_id))
                if affected_row == -1:
                    raise Exception('UPDATE_FAILED')

        except Exception as e:
            raise e

    def insert_user_details(self, db, details):
        try:
            with db.cursor() as cursor:
                query = """
                INSERT INTO seller_details(
                startdate,
                user_id,
                modifier_id,
                password,
                seller_attribute_id,
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
                )
                VALUES(
                %(startdate)s,
                %(user_id)s,
                %(modifier_id)s,
                %(password)s,
                %(seller_attribute_id)s,
                %(seller_name)s,
                %(seller_name_eng)s,
                %(cs_phone)s,
                %(site_url)s,
                %(profile_image)s,
                %(introduction_short)s,
                %(introduction_detail)s,
                %(background_image)s,
                %(zip_code)s,
                %(address)s,
                %(address_detail)s,
                %(weekday_start_time)s,
                %(weekday_end_time)s,
                %(weekend_start_time)s,
                %(weekend_end_time)s,
                %(bank)s,
                %(bank_account_name)s,
                %(bank_account_number)s,
                %(height)s,
                %(top_size)s,
                %(bottom_size)s,
                %(foot_size)s,
                %(feed)s
                )
                """

                affected_row = cursor.execute(query, details)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')

                return cursor.lastrowid
        except Exception as e:
            raise e

    def update_manager(self, db, user_id):
        try:
            with db.cursor() as cursor:
                query = """
                UPDATE user_managers SET is_deleted = 1
                WHERE user_id = %s AND is_deleted = 0
                """

                affected_row = cursor.execute(query, user_id)
                if affected_row == -1:
                    raise Exception('UPDATE_FAILED')

        except Exception as e:
            raise e

    def insert_managers(self, db, manager):
        try:
            with db.cursor() as cursor:
                query = """
                INSERT INTO managers(name, phone, email ) 
                VALUES(%(name)s, %(phone)s, %(email)s)
                """

                affected_row = cursor.execute(query, manager)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')

                return cursor.lastrowid

        except Exception as e:
            raise e

    def insert_user_managers(self, db, **kwargs):
        try:
            with db.cursor() as cursor:
                query = """
                INSERT INTO user_managers(user_id, manager_id, list_order)
                VALUES(%(user_id)s, %(manager_id)s, %(list_order)s)
                """

                affected_row = cursor.execute(query, kwargs)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')

        except Exception as e:
            raise e

    def get_seller_list(self, db, **kwargs):
        try:
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                SELECT 
                    user.id,
                    user.account,
                    user.create_at as created_at,
                    detail.seller_name as name,
                    detail.seller_name_eng as name_eng,
                    detail.site_url,
                    manager.name as manager_name,
                    manager.phone as manager_phone,
                    manager.email as manager_email,
                    status.name as seller_status,
                    attr.name as seller_attribute,
                    (SELECT COUNT(*) FROM users AS user
                    INNER JOIN products AS product
                    ON product.user_id = user.id AND product.is_deleted = 0) AS product_amount
                FROM users AS user
                INNER JOIN seller_details AS detail
                ON detail.user_id = user.id AND detail.enddate = 99991231235959
                INNER JOIN user_managers AS um
                ON um.user_id = user.id AND um.is_deleted = 0 AND um.list_order = 1
                INNER JOIN managers AS manager
                ON um.manager_id = manager.id
                INNER JOIN user_status AS us
                ON user.id = us.user_id AND us.enddate = 99991231235959
                INNER JOIN statuses AS status
                ON us.status_id = status.id
                INNER JOIN seller_attributes AS attr
                ON attr.id = detail.seller_attribute_id 
                WHERE user.role_id = 2
                ORDER BY id DESC
                LIMIT %(limit)s OFFSET %(offset)s
                """

                affected_row = cursor.execute(query, kwargs)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')
                if cursor.rowcount:
                    return affected_row, cursor.fetchall()

                return []

        except Exception as e:
            raise e


    def activate_user(self, db, user_id):
        try:
            with db.cursor() as cursor:
                query = """
                UPDATE users SET is_activated = 1
                WHERE id = %s
                """

                affected_row = cursor.execute(query, user_id)
                if affected_row == -1:
                    raise Exception('UPDATE_FAILED')

        except Exception as e:
            raise e