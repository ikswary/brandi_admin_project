import pymysql


class ProductDao:
    def seller_list(self, db):
        try:
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                SELECT user_id, profile_image, seller_name FROM seller_details
                JOIN users on users.id=seller_details.user_id
                WHERE seller_details.enddate="9999-12-31 23:59:59" AND seller_details.profile_image is not  Null AND users.role_id=2
                """

                affected_row = cursor.execute(query)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')
                if affected_row == 0:
                    raise Exception('DATA_DOES_NOT_EXIST')

                return cursor.fetchall()
        except Exception as e:
            raise e


    def first_category(self, db, attribute_group_id):
        try:
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                SELECT id, name FROM first_categories
                WHERE attribute_group_id = %s
                """

                affected_row = cursor.execute(query, attribute_group_id)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')
                if affected_row == 0:
                    raise Exception('DATA_DOES_NOT_EXIST')

                return cursor.fetchall()

        except Exception as e:
            raise e


    def second_category(self, db, first_category_id):
        try:
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                SELECT id, name FROM second_categories
                WHERE first_category_id = %s
                """

                affected_row = cursor.execute(query, first_category_id)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')

                return cursor.fetchall()

        except Exception as e:
            raise e


    def get_attribute_group_id(self, db, user_id):
        try:
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                SELECT attribute_group_id FROM seller_attributes
                JOIN seller_details
                ON seller_details.seller_attribute_id = seller_attributes.id
                WHERE user_id = %s
                """

                affected_row = cursor.execute(query, user_id)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')
                if affected_row == 0:
                    raise Exception('DATA_DOES_NOT_EXIST')

                return cursor.fetchone()['attribute_group_id']

        except Exception as e:
            raise e


    def country_data(self, db):
        try:
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                SELECT id, name FROM countries
                """

                affected_row = cursor.execute(query)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')
                if affected_row == 0:
                    raise Exception('DATA_DOES_NOT_EXIST')

                return cursor.fetchall()

        except Exception as e:
            raise e


    def option_color(self, db):
        try:
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                SELECT id, name FROM colors
                """

                affected_row = cursor.execute(query)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')
                if affected_row == 0:
                    raise Exception('DATA_DOES_NOT_EXIST')

                return cursor.fetchall()

        except Exception as e:
            raise e


    def option_size(self, db):
        try:
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                SELECT id, name FROM sizes
                """

                affected_row = cursor.execute(query)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')
                if affected_row == 0:
                    raise Exception('DATA_DOES_NOT_EXIST')

                return cursor.fetchall()

        except Exception as e:
            raise e


    def color_filter(self, db):
        try:
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                SELECT id, name, name_eng, image_url FROM color_filters
                """

                affected_row = cursor.execute(query)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')
                if affected_row == 0:
                    raise Exception('DATA_DOES_NOT_EXIST')

                return cursor.fetchall()

        except Exception as e:
            raise e


    def style_filter(self, db):
        try:
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                SELECT id, name FROM style_filters
                """

                affected_row = cursor.execute(query)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')
                if affected_row == 0:
                    raise Exception('DATA_DOES_NOT_EXIST')

                return cursor.fetchall()

        except Exception as e:
            raise e


    def count_product(self, db):
        try:
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                SELECT COUNT(*) FROM products;
                """

                affected_row = cursor.execute(query)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')
                if affected_row == 0:
                    raise Exception('DATA_DOES_NOT_EXIST')

                return cursor.fetchone()['COUNT(*)']

        except Exception as e:
            raise e


    def insert_product(self, db, user_id, code):
        try:
            with db.cursor() as cursor:
                query = """
                INSERT INTO products(user_id, code)
                VALUES(%s, %s)
                """
                affected_row = cursor.execute(query, (user_id, code))
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')

                return cursor.lastrowid
        except Exception as e:
            raise e


    def insert_product_details(self, db, kwargs):
        try:
            with db.cursor() as cursor:
                query = """
                INSERT INTO product_details(
                product_id,
                first_category_id,
                second_category_id,
                manufacture_country_id,
                style_filter_id,
                color_filter_id,
                modifier_id,
                on_sale,
                on_list,
                manufacturer,
                manufacture_date,
                name,
                description_short,
                description_detail,
                min_sales_unit,
                max_sales_unit,
                price,
                discount_rate,
                discount_price,
                discount_start,
                discount_end
                )
                VALUES(%(product_id)s,
                %(first_category_id)s,
                %(second_category_id)s,
                %(manufacture_country_id)s,
                %(style_filter_id)s,
                %(color_filter_id)s,
                %(modifier_id)s,
                %(on_sale)s,
                %(on_list)s,
                %(manufacturer)s,
                %(manufacture_date)s,
                %(name)s,
                %(description_short)s,
                %(description_detail)s,
                %(min_sales_unit)s,
                %(max_sales_unit)s,
                %(price)s,
                %(discount_rate)s,
                %(discount_price)s,
                %(discount_start)s,
                %(discount_end)s
                )
                """

                affected_row = cursor.execute(query, kwargs)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')

                return cursor.lastrowid
        except Exception as e:
            raise e

    def find_tag_id(self, db, tag_name):
        try:
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                SELECT id FROM tags
                WHERE name = %s
                """

                affected_row = cursor.execute(query, tag_name)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')

                return cursor.fetchone()
        except Exception as e:
            raise e

    def insert_tag(self, db, tag_name):
        try:
            with db.cursor() as cursor:
                query = """
                INSERT INTO tags(name)
                VALUES(%s)
                """

                affected_row = cursor.execute(query, tag_name)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')

                return cursor.lastrowid
        except Exception as e:
            raise e


    def insert_product_tag(self, db, product_id, tag_id):
        try:
            with db.cursor() as cursor:
                query = """
                INSERT INTO product_tags(product_id, tag_id)
                VALUES(%s, %s)
                """

                affected_row = cursor.execute(query, (product_id, tag_id))
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')

                return None

        except Exception as e:
            raise e


    def insert_image(self, db, large_url, medium_url, small_url):
        try:
            with db.cursor() as cursor:
                query = """
                INSERT INTO images(large_url, medium_url, small_url)
                VALUES(%s, %s, %s)
                """

                affected_row = cursor.execute(query, (large_url, medium_url, small_url))
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')

                return cursor.lastrowid

        except Exception as e:
            raise e


    def insert_product_images(self, db, product_id, image_id, list_order):
        try:
            with db.cursor() as cursor:
                query = """
                INSERT INTO product_images(product_id, image_id, list_order)
                VALUES(%s, %s, %s)
                """

                affected_row = cursor.execute(query, (product_id, image_id, list_order))
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')

                return None
        except Exception as e:
            raise e


    def insert_options(self, db, product_id, color_id, size_id, stock):
        try:
            with db.cursor() as cursor:
                query = """
                INSERT INTO options(product_id, color_id, size_id, stock)
                VALUES(%s, %s, %s, %s)
                """

                affected_row = cursor.execute(query, (product_id, color_id, size_id, stock))
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')

                return None
        except Exception as e:
            raise e
