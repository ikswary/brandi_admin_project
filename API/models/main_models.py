import pymysql


class MainDao:
    def role(self, db, role_id):
        try:
            with db.cursor() as cursor:
                query = """
                SELECT id FROM roles
                WHERE id = %s
                """

                affected_row = cursor.execute(query, role_id)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')
                if affected_row == 0:
                    return Exception('DATA_DOES_NOT_EXIST')

                return cursor.fetchone()

        except Exception as e:
            raise e


    def sidebar_list(self, db, role_id):
        try:
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                SELECT id,name FROM sidebar
                WHERE role_id = %s
                """

                affected_row = cursor.execute(query, role_id)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')
                if affected_row == 0:
                    raise Exception('DATA_DOES_NOT_EXIST')

                return cursor.fetchall()

        except Exception as e:
            raise e


    def sidebar_detail_list(self, db, sidebar_id):
        try:
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                SELECT id,name FROM sidebar_detail
                WHERE sidebar_id = %s
                """

                affected_row = cursor.execute(query, sidebar_id)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')

                return cursor.fetchall()

        except Exception as e:
            raise e
