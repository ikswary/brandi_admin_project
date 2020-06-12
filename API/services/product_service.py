import math
from models.product_models import ProductDao

product_dao = ProductDao()


def product_save_service(db, data, seller_id, user_id, code, tag_data, image_data, option_data):
    try:
        product_id = product_dao.insert_product(db, seller_id, code)
        data['product_id'] = product_id
        data['modifier_id'] = user_id
        product_detail_id = product_dao.insert_product_details(db, data)

        # 리스트로 들어온 tag_name을 이용하여 tag_id (tag가 db에 존재하는지) 찾기
        for tag in tag_data:
            tag_id = product_dao.find_tag_id(db, tag['name'])
            # tag가 db에 존재하지 않으면tag 추가하고 product_tag에도 추가
            if tag_id is None:
                tag_id = product_dao.insert_tag(db, tag['name'])
                product_dao.insert_product_tag(db, product_detail_id, tag_id)
            # tag가 db에 존재하면 tag_id 이용하여 product_tag에 추가
            elif tag_id:
                tag_id = tag_id['id']
                product_dao.insert_product_tag(db, product_detail_id, tag_id)

        # 리스트로 들어온 image_data를 이용하여 image를 db에 추가 후 product에 연결
        for order in range(len(image_data)):
            large_url = image_data[order]['url']
            medium_url = image_data[order]['url']
            small_url = image_data[order]['url']
            list_order = order+1
            image_id = product_dao.insert_image(db, large_url, medium_url, small_url)
            product_dao.insert_product_images(db, product_detail_id, image_id, list_order)

        # 리스트로 들어온 option_data 추가
        for option in option_data:
            color_id = option['color_id']
            size_id = option['size_id']
            stock = option['stock']
            if product_dao.find_last_option_code(db) == 1:
                code_number = "1"
            if product_dao.find_last_option_code(db) != 1:
                code_number = str(int(product_dao.find_last_option_code(db)[2:])+1)
            code = "SP"+code_number.zfill(18)
            product_dao.insert_options(db, product_detail_id, color_id, size_id, stock, code)

    except Exception as e:
        raise e


def product_data_service(db, product_code, data, category_data, images_data, options_data, tags_data):
    try:
        return {
                 "product_code": product_code,
                 "on_sale": data['on_sale'],
                 "on_list": data['on_list'],
                 "first_category": {
                     "id": category_data['id'],
                     "name": category_data['name']
                                     },
                 "second_category": {
                     "id": category_data['second_categories.id'],
                     "name": category_data['second_categories.name']
                                     },
                     "manufacturer": data['manufacturer'],
                 "manufacturer_date": data['manufacture_date'],
                 "manufacture_country": {
                     "id": data['manufacture_country_id'],
                     "name": product_dao.find_country_data(db, data['manufacture_country_id']) if data['manufacture_country_id'] else None
                                         },
                 "name": data['name'],
                 "description_short": data['description_short'],
                 "images":[{
                     "url": image['large_url'],
                     "order": image['list_order']
                             } for image in images_data],
                 "color_filter": data['color_filter_id'],
                 "style_filter": data['style_filter_id'],
                 "description_detail": data['description_detail'],
                 "option": [{
                     "code": option['code'],
                     "color_id": option['color_id'],
                     "color_name": option['name'],
                     "size_id": option['size_id'],
                     "size_name": option['sizes.name'],
                     "stock": option['stock']
                             } for option in options_data],
                 "price": data['price'],
                 "discount_rate": data['discount_rate'],
                 "discount_price": data['discount_price'],
                 "discounted_price" : math.trunc(data['price']*(data['discount_rate']/100)),
                 "discount_start": data['discount_start'],
                 "discount_end": data['discount_end'],
                 "min_sales_unit": data['min_sales_unit'],
                 "max_sales_unit": data['max_sales_unit'],
                 "tag":[{
                         "name": tag['name']
                         } for tag in tags_data]
                             }
    except Exception as e:
        raise e

def product_change_service(db, previous_product_detail_id, data, tag_data, image_data, option_data):
    try:
        product_detail_id = product_dao.insert_product_details(db, data)

        # 이전 product_detail의 enddate 날짜 변경
        previous_enddate = product_dao.find_product_date(db,product_detail_id)
        product_dao.change_product_date(db, previous_enddate, previous_product_detail_id)

        # 리스트로 들어온 tag_name을 이용하여 tag_id (tag가 db에 존재하는지) 찾기
        for tag in tag_data:
            tag_id = product_dao.find_tag_id(db, tag['name'])
            # tag가 db에 존재하지 않으면tag 추가하고 product_tag에도 추가
            if tag_id is None:
                tag_id = product_dao.insert_tag(db, tag['name'])
                product_dao.insert_product_tag(db, product_detail_id, tag_id)
            # tag가 db에 존재하면 tag_id 이용하여 product_tag에 추가
            elif tag_id:
                tag_id = tag_id['id']
                product_dao.insert_product_tag(db, product_detail_id, tag_id)

        # 리스트로 들어온 image_data를 이용하여 image를 db에 추가 후 product에 연결
        for order in range(len(image_data)):
            large_url = image_data[order]['url']
            medium_url = image_data[order]['url']
            small_url = image_data[order]['url']
            list_order = order+1
            image_id = product_dao.insert_image(db, large_url, medium_url, small_url)
            product_dao.insert_product_images(db, product_detail_id, image_id, list_order)

        # 리스트로 들어온 option_data 추가
        for option in option_data:
            if option['code']:
                color_id = option['color_id']
                size_id = option['size_id']
                stock = option['stock']
                code = option['code']
                product_dao.insert_options(db, product_detail_id, color_id, size_id, stock, code)
            if option['code'] is None:
                color_id = option['color_id']
                size_id = option['size_id']
                stock = option['stock']
                if product_dao.find_last_option_code(db) == 1:
                    code_number = "1"
                if product_dao.find_last_option_code(db) != 1:
                    code_number = str(int(product_dao.find_last_option_code(db)[2:])+1)
                code = "SP"+code_number.zfill(18)
                product_dao.insert_options(db, product_detail_id, color_id, size_id, stock, code)

    except Exception as e:
        raise e
