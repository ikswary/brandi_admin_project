import pymysql


class ProductDao:
    def seller_list(self, db):
        try:
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                SELECT user_id, profile_image, seller_name FROM seller_details
                INNER JOIN users on users.id=seller_details.user_id
                WHERE seller_details.enddate="9999-12-31 23:59:59" AND seller_details.profile_image is not  Null AND users.role_id=2
                """

                affected_row = cursor.execute(query)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')

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


    def insert_options(self, db, product_id, color_id, size_id, stock, code):
        try:
            with db.cursor() as cursor:
                query = """
                INSERT INTO options(product_id, color_id, size_id, stock, code)
                VALUES(%s, %s, %s, %s, %s)
                """

                affected_row = cursor.execute(query, (product_id, color_id, size_id, stock, code))
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')

                return None
        except Exception as e:
            raise e


    def find_product(self, db, code):
        try:
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                SELECT * FROM product_details INNER JOIN products
                ON product_details.product_id = products.id
                WHERE product_details.enddate="9999-12-31 23:59:59" AND products.code = %s
                """

                affected_row = cursor.execute(query, code)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')
                if affected_row == 0:
                    raise Exception('DATA_DOES_NOT_EXIST')

                return cursor.fetchone()
        except Exception as e:
            raise e


    def null_generator(self, query, data):
        if data:
            return query.replace('%s', "= " + str(data))
        else:
            return query.replace('%s', 'is NULL')


    def find_category(self, db, first_category_id, second_category_id):
        try:
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                query_1 = """
                SELECT * FROM first_categories LEFT JOIN second_categories
                ON first_categories.id = second_categories.first_category_id
                WHERE first_categories.id = %s AND"""

                query_2 = """ second_categories.id %s
                """

                query = query_1 + self.null_generator(query_2, second_category_id)

                affected_row = cursor.execute(query, first_category_id)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')
                if affected_row == 0:
                    raise Exception('DATA_DOES_NOT_EXIST')

                return cursor.fetchone()
        except Exception as e:
            raise e


    def find_country_data(self, db, country_id):
        try:
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                SELECT name FROM countries WHERE id = %s
                """

                affected_row = cursor.execute(query, country_id)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')
                if affected_row == 0:
                    raise Exception('DATA_DOES_NOT_EXIST')

                return cursor.fetchone()['name']
        except Exception as e:
            raise e


    def find_images(self, db, product_id):
        try:
            with db. cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                SELECT * FROM product_images INNER JOIN images
                ON product_images.image_id = images.id
                WHERE product_images.product_id = %s
                """

                affected_row = cursor.execute(query, product_id)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')
                if affected_row == 0:
                    raise Exception('DATA_DOES_NOT_EXIST')

                return cursor.fetchall()
        except Exception as e:
            raise e


    def find_first_image(self, db, product_id):
        try:
            with db. cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                SELECT * FROM product_images INNER JOIN images
                ON product_images.image_id = images.id
                WHERE product_images.product_id = %s
                AND list_order = 1
                """

                affected_row = cursor.execute(query, product_id)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')
                if affected_row == 0:
                    raise Exception('DATA_DOES_NOT_EXIST')

                return cursor.fetchone()['large_url']
        except Exception as e:
            raise e


    def find_options(self, db, product_id):
        try:
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                SELECT * FROM options INNER JOIN colors INNER JOIN sizes
                ON colors.id = options.color_id and sizes.id = options.size_id
                WHERE product_id = %s
                """

                affected_row = cursor.execute(query, product_id)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')
                if affected_row == 0:
                    raise Exception('DATA_DOES_NOT_EXIST')

                return cursor.fetchall()
        except Exception as e:
            raise e


    def find_product_tags(self, db, product_id):
        try:
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                SELECT * FROM product_tags INNER JOIN tags
                ON product_tags.tag_id = tags.id
                WHERE product_id = %s
                """

                affected_row = cursor.execute(query, product_id)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')
                if affected_row == 0:
                    raise Exception('DATA_DOES_NOT_EXIST')

                return cursor.fetchall()
        except Exception as e:
            raise e


    def change_product_date(self, db, enddate, product_id):
        try:
            with db.cursor() as cursor:
                query = """
                UPDATE product_details SET enddate = %s
                WHERE id = %s
                """

                affected_row = cursor.execute(query, (enddate, product_id))
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')
                if affected_row == 0:
                    raise Exception('DATA_DOES_NOT_EXIST')

                return None
        except Exception as e:
            raise e


    def find_product_date(self, db, product_id):
        try:
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                SELECT startdate FROM product_details
                WHERE id = %s
                """

                affected_row = cursor.execute(query, product_id)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')
                if affected_row == 0:
                    raise Exception('DATA_DOES_NOT_EXIST')

                return cursor.fetchone()['startdate']
        except Exception as e:
            raise e


    def find_option_code(self, db, code):
        try:
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                SELECT size_id, color_id FROM options
                WHERE code = %s
                """

                affected_row = cursor.execute(query, code)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')
                if affected_row == 0:
                    raise Exception('DATA_DOES_NOT_EXIST')

                return cursor.fetchone()
        except Exception as e:
            raise e


    def find_last_option_code(self, db):
        try:
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                SELECT code FROM options
                ORDER BY code
                """

                affected_row = cursor.execute(query)

                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')
                if affected_row == 0:
                    return 1

                return cursor.fetchall()[-1]['code']
        except Exception as e:
            raise e

    def get_id_from_seller_name(self, db, seller_name):
        try:
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                SELECT user_id FROM seller_details
                WHERE seller_name = %s
                """

                affected_row = cursor.execute(query, seller_name)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')
                if affected_row == 0:
                    return 0

                return cursor.fetchone()['user_id']
        except Exception as e:
            raise e

    def similar_seller_name(self, db, seller_name):
        try:
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                SELECT user_id, seller_name, profile_image FROM seller_details
                WHERE seller_name LIKE %s
                """

                affected_row = cursor.execute(query, "%" + seller_name + "%")
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')
                if affected_row == 0:
                    return Exception('DATA_DOES_NOT_EXIST')

                return cursor.fetchall()
        except Exception as e:
            raise e


    def find_product_history(self, db, code):
        try:
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                SELECT startdate, on_sale, on_list, price, discount_rate, discount_price, modifier_id FROM product_details INNER JOIN products
                ON product_details.product_id = products.id
                WHERE code = %s
                """

                affected_row = cursor.execute(query, code)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')
                if affected_row == 0:
                    return Exception('DATA_DOES_NOT_EXIST')

                return cursor.fetchall()
        except Exception as e:
            raise e


    def product_filter(self, filter_dict):
        try:
            filter_query = ""

            if filter_dict['start_period']:
                query = "AND products.create_at > %(start_period)s "
                filter_query = filter_query + query

            if filter_dict['end_period']:
                query = "AND products.create_at < %(end_period)s "
                filter_query = filter_query + query

            if filter_dict['user_id'] == 0:
                query = "AND products.user_id = 0 "
                filter_query = filter_query + query

            if filter_dict['user_id']:
                query = "AND products.user_id = %(user_id)s "
                filter_query = filter_query + query

            if filter_dict['product_name']:
                query= "AND name = %(product_name)s "
                filter_query = filter_query + query

            if filter_dict['product_id']:
                query= "AND product_id = %(product_id)s "
                filter_query = filter_query + query

            if filter_dict['code']:
                query= "AND code = %(code)s "
                filter_query = filter_query + query

            if filter_dict['seller_attribute']:
                query= "AND seller_attribute_id IN %(seller_attribute)s "
                filter_query = filter_query + query

            if filter_dict['on_sale']:
                query= "AND on_sale = %(on_sale)s "
                filter_query = filter_query + query

            if filter_dict['on_list']:
                query= "AND on_list = %(on_list)s "
                filter_query = filter_query + query

            if filter_dict['discount']:
                if filter_dict['discount'] == '1':
                    query = "AND discount_rate != 0 "
                if filter_dict['discount'] == '0':
                    query= "AND discount_rate = 0 "
                filter_query = filter_query + query

            return filter_query

        except Exception as e:
            raise e


    def pagination(self, filter_dict):
        try:
            pagination_query = "LIMIT %(limit)s "
            if filter_dict['offset']:
                query = "OFFSET %(offset)s "
                pagination_query = pagination_query + query

            return pagination_query

        except Exception as e:
            raise e


    def product_list(self, db, filter_dict):
        try:
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                SELECT product_details.id, product_id, products.create_at, name, code,
                products.user_id, seller_name, on_sale, on_list, price, discount_price,
                discount_rate, seller_attribute_id FROM product_details
                LEFT JOIN products ON products.id = product_details.product_id
                LEFT JOIN users ON products.user_id = users.id
                LEFT JOIN seller_details on users.id = seller_details.user_id
                AND seller_details.enddate = "9999-12-31 23:59:59"
                WHERE product_details.enddate = "9999-12-31 23:59:59"
                """

                filter_query = self.product_filter(filter_dict)

                order_query = """
                ORDER BY product_id DESC """

                pagination_query = self.pagination(filter_dict)

                query = query + filter_query + order_query + pagination_query

                affected_row = cursor.execute(query, filter_dict)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')

                return cursor.fetchall()
        except Exception as e:
            raise e

    def count_product_list(self, db, filter_dict):
        try:
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                SELECT COUNT(*) FROM product_details
                LEFT JOIN products ON products.id = product_details.product_id
                LEFT JOIN users ON products.user_id = users.id
                LEFT JOIN seller_details on users.id = seller_details.user_id
                AND seller_details.enddate = "9999-12-31 23:59:59"
                WHERE product_details.enddate = "9999-12-31 23:59:59"
                """

                filter_query = self.product_filter(filter_dict)

                query = query + filter_query

                affected_row = cursor.execute(query, filter_dict)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')

                return cursor.fetchone()['COUNT(*)']
        except Exception as e:
            raise e

    def find_seller_attribute(self, db, seller_attribute_id):
        try:
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                SELECT name FROM seller_attributes
                WHERE id = %s
                """

                affected_row = cursor.execute(query, seller_attribute_id)
                if affected_row == -1:
                    raise Exception('EXECUTE_FAILED')
                if affected_row == 0:
                    return Exception('DATA_DOES_NOT_EXIST')

                return cursor.fetchone()['name']
        except Exception as e:
            raise e


