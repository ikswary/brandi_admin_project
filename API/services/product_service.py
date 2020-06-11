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
            product_dao.insert_options(db, product_detail_id, color_id, size_id, stock)

    except Exception as e:
        raise e