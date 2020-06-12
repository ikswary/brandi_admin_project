import os, sys

BASE_DIR = os.path.dirname(os.path.abspath("API"))
sys.path.extend([BASE_DIR])

import pymysql
import math
from jsonschema import validate, ValidationError
from datetime import datetime, timedelta
from flask import Blueprint, request, jsonify

from jsonschemas import PRODUCT_SCHEMA, CHANGE_PRODUCT_SCHEMA
from connections import get_db_connector
from decorator import login_required
from models.main_models import MainDao
from models.product_models import ProductDao
from services.product_service import product_save_service, product_data_service

product_app = Blueprint("product_app", __name__)
main_dao = MainDao()
product_dao = ProductDao()

MASTER_ROLE_ID = 1
SELLER_ROLE_ID = 2


@product_app.route('/seller', methods=['GET'])
@login_required
def seller(**kwargs):
    """셀러 리스트 불러오는 API

        Args:
            role_id : user의 권한 확인

        Returns:
            {data : sellers}, http status code

        Exceptions:
            InternalError: DATABASE가 존재하지 않을 때 발생
            OperationalError: DATABASE 접속이 인가되지 않았을 때 발생
            ProgramingError: SQL syntax가 잘못되었을 때 발생
            IntegrityError: Key의 무결성을 해쳤을 때 발생
            DataError: 컬럼 타입과 매칭되지 않는 값이 DB에 전달되었을 때 발생
            KeyError: 엔드포인트에서 요구하는 키값이 전달되지 않았을 때 발생
    """
    db = None
    try:
        db = get_db_connector()
        if db is None:
            return jsonify(message="DATABASE_INIT_ERROR"), 500
        role_id = kwargs['role_id']

        if role_id == MASTER_ROLE_ID:
            seller_data = product_dao.seller_list(db)

            sellers = [{
                "id": seller.get('user_id'),
                "image": seller.get('profile_image'),
                "name": seller.get('seller_name')} for seller in seller_data]

            return jsonify(data=sellers), 200
        elif role_id == SELLER_ROLE_ID:
            return jsonify(message="UNAUTHORIZED"), 401
        elif main_dao.role(db, role_id) is None:
            return jsonify(message="DATA_DOES_NOT_EXIST"), 404

    except pymysql.err.InternalError:
        return jsonify(message="DATABASE_DOES_NOT_EXIST"), 500
    except pymysql.err.OperationalError:
        return jsonify(message="DATABASE_AUTHORIZATION_DENIED"), 500
    except pymysql.err.ProgrammingError:
        return jsonify(message="DATABASE_SYNTAX_ERROR"), 500
    except pymysql.err.IntegrityError:
        return jsonify(message="FOREIGN_KEY_CONSTRAINT_ERROR"), 500
    except pymysql.err.DataError:
        return jsonify(message="DATA_ERROR"), 400
    except KeyError:
        return jsonify(message="KEY_ERROR"), 400
    except Exception as e:
        return jsonify(message=f"{e}"), 500
    finally:
        if db:
            db.close()


@product_app.route('/category', methods=['GET'])
@login_required
def product_category(**kwargs):
    """상품 등록시 카테고리 정보 전달 API

        Args:
             user_id: 접속 아이디,
             seller_id : 셀러 아이디,
             attribute_group_id: 판매자 속성

        Returns:
             {data : category_list}, http status code

        Exceptions:
            InternalError: DATABASE가 존재하지 않을 때 발생
            OperationalError: DATABASE 접속이 인가되지 않았을 때 발생
            ProgramingError: SQL syntax가 잘못되었을 때 발생
            IntegrityError: Key의 무결성을 해쳤을 때 발생
            DataError: 컬럼 타입과 매칭되지 않는 값이 DB에 전달되었을 때 발생
            KeyError: 엔드포인트에서 요구하는 키값이 전달되지 않았을 때 발생
    """

    db = None
    try:
        db = get_db_connector()
        if db is None:
            return jsonify(message="DATABASE_INIT_ERROR"), 500

        user_id = kwargs['user_id']
        role_id = kwargs['role_id']

        if role_id == MASTER_ROLE_ID:
            seller_id = request.args.get('seller_id')
            attribute_group_id = product_dao.get_attribute_group_id(db, seller_id)
        elif role_id == SELLER_ROLE_ID :
            attribute_group_id = product_dao.get_attribute_group_id(db, user_id)
        elif main_dao.role(db, role_id) is None:
            return jsonify(message="DATA_DOES_NOT_EXIST"), 404

        first_category_data = product_dao.first_category(db, attribute_group_id)

        category_list = [{
            "id": category.get('id'),
            "name": category.get('name'),
            "second_category": [{
                "id":category_detail.get('id'),
                "name":category_detail.get('name')
            }for category_detail in product_dao.second_category(db,category.get('id'))]
        }for category in first_category_data]
        return jsonify(data=category_list), 200

    except pymysql.err.InternalError:
        return jsonify(message="DATABASE_DOES_NOT_EXIST"), 500
    except pymysql.err.OperationalError:
        return jsonify(message="DATABASE_AUTHORIZATION_DENIED"), 500
    except pymysql.err.ProgrammingError:
        return jsonify(message="DATABASE_SYNTAX_ERROR"), 500
    except pymysql.err.IntegrityError:
        return jsonify(message="FOREIGN_KEY_CONSTRAINT_ERROR"), 500
    except pymysql.err.DataError:
        return jsonify(message="DATA_ERROR"), 400
    except KeyError:
        return jsonify(message="KEY_ERROR"), 400
    except Exception as e:
        return jsonify(message=f"{e}"), 500
    finally:
        if db:
            db.close()


@product_app.route('/information', methods=['GET'])
@login_required
def product_information(**kwargs):
    """상품 등록시 옵션 및 필터 정보 전달 API

        Returns:
             {data : information_data}, http status code

        Exceptions:
            InternalError: DATABASE가 존재하지 않을 때 발생
            OperationalError: DATABASE 접속이 인가되지 않았을 때 발생
            ProgramingError: SQL syntax가 잘못되었을 때 발생
            IntegrityError: Key의 무결성을 해쳤을 때 발생
            DataError: 컬럼 타입과 매칭되지 않는 값이 DB에 전달되었을 때 발생
            KeyError: 엔드포인트에서 요구하는 키값이 전달되지 않았을 때 발생

    """

    db = None
    try:
        db = get_db_connector()
        if db is None:
            return jsonify(message="DATABASE_INIT_ERROR"), 500

        countries = product_dao.country_data(db)
        colors = product_dao.option_color(db)
        sizes = product_dao.option_size(db)
        color_filters = product_dao.color_filter(db)
        style_filters = product_dao.style_filter(db)

        information_data = [{
            "country": [{
                "id": country.get('id'),
                "name": country.get('name')} for country in countries],
            "option_color": [{
                "id": color.get('id'),
                "name": color.get('name')} for color in colors],
            "option_size": [{
                "id": size.get('id'),
                "name": size.get('name')} for size in sizes],
            "color_filter": [{
                "id": color_data.get('id'),
                "name": color_data.get('name'),
                "name_eng": color_data.get('name_eng'),
                "image_url": color_data.get('image_url')} for color_data in color_filters],
            "style_filter": [{
                "id": style_data.get('id'),
                "name": style_data.get('name')} for style_data in style_filters]}]

        return jsonify(data=information_data), 200

    except pymysql.err.InternalError:
        return jsonify(message="DATABASE_DOES_NOT_EXIST"), 500
    except pymysql.err.OperationalError:
        return jsonify(message="DATABASE_AUTHORIZATION_DENIED"), 500
    except pymysql.err.ProgrammingError:
        return jsonify(message="DATABASE_SYNTAX_ERROR"), 500
    except pymysql.err.IntegrityError:
        return jsonify(message="FOREIGN_KEY_CONSTRAINT_ERROR"), 500
    except pymysql.err.DataError:
        return jsonify(message="DATA_ERROR"), 400
    except KeyError:
        return jsonify(message="KEY_ERROR"), 400
    except Exception as e:
        return jsonify(message=f"{e}"), 500
    finally:
        if db:
            db.close()

# @product_app.route('/', methods=['POST'])
# @login_required
# def save_product(**kwargs):

@product_app.route('', methods=['POST'])
@login_required
def save_product(**kwargs):
    """ 상품등록 API

        Args:
           "seller_id": 판매자 id,
           "on_sale": 판매여부,
           "on_list": 진열여부,
           "first_category_id": 1차 카테고리,
           "second_category_id": 2차 카테고리,
           "manufacturer": 제조사,
           "manufacture_date": 제조일자,
           "manufacture_country_id": 원산지 id,
           "name": 상품명,
           "description_short": 한줄 상품 설명,
           "images": {
                        "url": 이미지 url
                     }
           "color_filter_id": 색상필터(썸네일 이미지),
           "style_filter_id": 스타일필터,
           "description_detail": 상세 상품 정보,
           "option": {
                        "color_id": 옵션 색상 id,
                        "size_id": 옵션 size id,
                        "stock": 재고 수량
                     }
          "price": 판매가,
          "discount_rate": 할인율,
          "discount_price": 할인판매가,
          "discount_start": 할인기간 시작일,
          "discount_end": 할인기간 종료일,
          "min_sales_unit": 최소판매수량,
          "max_sales_unit": 최대판매수량,
          "tag" : {
                    "name": 상품 태
                  }

        Returns:
            {message: ''}, http status code

        Exceptions:
            InternalError: DATABASE가 존재하지 않을 때 발생
            OperationalError: DATABASE 접속이 인가되지 않았을 때 발생
            ProgramingError: SQL syntax가 잘못되었을 때 발생
            IntegrityError: Key의 무결성을 해쳤을 때 발생
            DataError: 컬럼 타입과 매칭되지 않는 값이 DB에 전달되었을 때 발생
            KeyError: 엔드포인트에서 요구하는 키값이 전달되지 않았을 때 발생
            ValidationError : 엔드포인트에서 요구하는 키값이 전달되지 않았을 때 발생
    """

    db = None
    try:
        validate(request.json, PRODUCT_SCHEMA)
        data = request.json

        db = get_db_connector()
        if db is None:
            return jsonify(message="DATABASE_INIT_ERROR"), 500

        user_id = kwargs['user_id']
        role_id = kwargs['role_id']

        product_number = str(product_dao.count_product(db) + 1)
        code = "SB"+product_number.zfill(18)

        # 권한이 Master인 경우 seller_id는 data에서 들어온 seller_id
        if role_id == MASTER_ROLE_ID:
            seller_id = data['seller_id']
        # 권한이 Seller인 경우 seller_id는user_id
        elif role_id == SELLER_ROLE_ID:
            seller_id = user_id
        elif main_dao.role(db, role_id) is None:
            return jsonify(message="DATA_DOES_NOT_EXIST"), 404

        tag_data = data['tag']
        image_data = data['images']
        option_data = data['option']

        # 이미지가 5개를 넘어서 들어오는 경우
        if len(image_data) >= 6:
            return jsonify(message = "DATA_ERROR"), 400

        # 옵션 중복 값 확인
        option_duplicate_check=[]
        # (color_id,size_id)쌍으로 중복 체크
        for option in option_data:
            if ((option['color_id'],option['size_id'])) in option_duplicate_check:
                return jsonify(message = "DATA_ERROR"), 400
            else:
                option_duplicate_check.append((option['color_id'],option['size_id']))

        # required가 아닌 항목이 Null값으로도 들어오지 않은 경우 처리
        if 'description_short' not in data:
            data['descriotion_short'] = None
        if 'discount_rate' not in data:
            data['discount_rate'] = None
        if 'discount_price' not in data:
            data['discount_price'] = None
        if 'discount_start' not in data:
            data['discount_start'] = None
        if 'discount_end' not in data:
            data['discount_end'] = None

        # 상품 정보 고시 에러확인
        manufacture_list = [data['manufacture_country_id'], data['manufacturer'], data['manufacture_date']]
        # 직접 입력인 경우 None이 존재하면 안됨
        if manufacture_list.count(None) == 1 or manufacture_list.count(None) == 2:
            return jsonify(message = "DATA_ERROR"), 400

        # 아래에서 data 입력위해 불필요한 list_data 삭제
        rm_data = ['images','option','tag']
        for rm in rm_data:
            del data[rm]

        price = data['price']
        discount_rate = data['discount_rate']
        discount_price = data['discount_price']

        # 할인율이 없는데 할인가가 있는 경우 에러 return
        if discount_rate is None and discount_price is not None:
            return jsonify(message = "DATA_ERROR"), 400
        # 할인율이 음수인 경우 에러 return
        elif discount_rate < 0:
            return jsonify(message = "DATA_ERROR"), 400
        # 할인율이 100%가 넘는 경우 에러 return
        elif discount_rate >= 100:
            return jsonify(message = "DATA_ERROR"), 400
        # 할인율이 있고 할인가가 없는 경우 할인가 계산
        elif discount_rate is not None and discount_price is None:
            discount_data = math.floor(price*((100-discount_rate)/100)/10)*10
            data['discount_price'] = int(discount_data)

        db.begin()
        product_save_service(db, data, seller_id, user_id, code, tag_data, image_data, option_data)
        db.commit()

        return (''),200

    except pymysql.err.InternalError:
        db.rollback()
        return jsonify(message="DATABASE_DOES_NOT_EXIST"), 500
    except pymysql.err.OperationalError:
        db.rollback()
        return jsonify(message="DATABASE_AUTHORIZATION_DENIED"), 500
    except pymysql.err.ProgrammingError:
        db.rollback()
        return jsonify(message="DATABASE_SYNTAX_ERROR"), 500
    except pymysql.err.IntegrityError:
        db.rollback()
        return jsonify(message="FOREIGN_KEY_CONSTRAINT_ERROR"), 500
    except pymysql.err.DataError:
        db.rollback()
        return jsonify(message="DATA_ERROR"), 400
    except KeyError:
        db.rollback()
        return jsonify(message=f"KEY_ERROR"), 400
    except ValidationError as e:
        error_path = str(e.path)[8:-3]
        return jsonify(message=f"{error_path.upper()}_VALIDATION_ERROR"), 400
    except Exception as e:
        db.rollback()
        return jsonify(message=f"{e}"), 500
    finally:
        if db:
            db.close()


@product_app.route('', methods=['GET'])
@login_required
def get_product_information(**kwargs):
    """ 상품 수정시 기본 정보 보내주는 API

        URL params:
            <string:product_code>: 상품 코드

        Args:
             product_code : 상품 코드,

        Returns:
             {data : product_data}, http status code

        Exceptions:
            InternalError: DATABASE가 존재하지 않을 때 발생
            OperationalError: DATABASE 접속이 인가되지 않았을 때 발생
            ProgramingError: SQL syntax가 잘못되었을 때 발생
            IntegrityError: Key의 무결성을 해쳤을 때 발생
            DataError: 컬럼 타입과 매칭되지 않는 값이 DB에 전달되었을 때 발생
            KeyError: 엔드포인트에서 요구하는 키값이 전달되지 않았을 때 발생

    """
    db = None
    try:
        db = get_db_connector()
        if db is None:
            return jsonify(message="DATABASE_INIT_ERROR"), 500

        product_code=request.args.get('product_code')
        data = product_dao.find_product(db, product_code)

        first_category_id = data['first_category_id']
        second_category_id = data['second_category_id']
        product_detail_id = data['id']

        category_data = product_dao.find_category(db, first_category_id, second_category_id)
        images_data = product_dao.find_images(db, product_detail_id)
        options_data = product_dao.find_options(db, product_detail_id)
        tags_data = product_dao.find_product_tags(db, product_detail_id)

        product_data = product_data_service(db, product_code, data, category_data, images_data, options_data, tags_data)
        return jsonify(data=product_data), 200

    except pymysql.err.InternalError:
        return jsonify(message="DATABASE_DOES_NOT_EXIST"), 500
    except pymysql.err.OperationalError:
        return jsonify(message="DATABASE_AUTHORIZATION_DENIED"), 500
    except pymysql.err.ProgrammingError:
        return jsonify(message="DATABASE_SYNTAX_ERROR"), 500
    except pymysql.err.IntegrityError:
        return jsonify(message="FOREIGN_KEY_CONSTRAINT_ERROR"), 500
    except pymysql.err.DataError:
        return jsonify(message="DATA_ERROR"), 400
    except KeyError:
        return jsonify(message="KEY_ERROR"), 400
    except Exception as e:
        return jsonify(message=f"{e}"), 500
    finally:
        if db:
            db.close()


@product_app.route('', methods=['PUT'])
@login_required
def change_product_information(**kwargs):
    """

    """

    db = None
    try:
        validate(request.json, CHANGE_PRODUCT_SCHEMA)
        data = request.json

        db = get_db_connector()
        if db is None:
            return jsonify(message="DATABASE_INIT_ERROR"), 500

        data['modifier_id'] = kwargs['user_id']
        product_code = data['product_code']

        # print(data)
        # 상품 코드를 이용하여 product_id를 구하고 data에 key,value 추가
        product_id = product_dao.find_product(db, product_code)['product_id']
        previous_product_detail_id = product_dao.find_product(db, product_code)['id']

        data['product_id'] = product_id

        tag_data = data['tag']
        image_data = data['images']
        option_data = data['option']

        # 이미지가 5개를 넘어서 들어오는 경우
        if len(image_data) >= 6:
            return jsonify(message = "DATA_ERROR"), 400

        # 옵션 중복 값 확인
        option_duplicate_check=[]
        # (color_id,size_id)쌍으로 중복 체크
        for option in option_data:
            if ((option['color_id'],option['size_id'])) in option_duplicate_check:
                return jsonify(message = "DATA_ERROR"), 400
            else:
                option_duplicate_check.append((option['color_id'],option['size_id']))

        # 기존의 옵션 코드에 저장된 내용과 현재 옵션값으로 받아온 정보가 다른 경우 체크
        for option in option_data:
            if option['code']:
                option_details=product_dao.find_option_code(db, option['code'])
                if (option_details['size_id'],option_details['color_id']) !=  (option['size_id'],option['color_id']):
                    return jsonify(message = "DATA_ERROR"), 400

        # required가 아닌 항목이 Null값으로도 들어오지 않은 경우 처리
        if 'description_short' not in data:
            data['descriotion_short'] = None
        if 'discount_rate' not in data:
            data['discount_rate'] = None
        if 'discount_price' not in data:
            data['discount_price'] = None
        if 'discount_start' not in data:
            data['discount_start'] = None
        if 'discount_end' not in data:
            data['discount_end'] = None

        # 상품 정보 고시 에러확인
        manufacture_list = [data['manufacture_country_id'], data['manufacturer'], data['manufacture_date']]
        # 직접 입력인 경우 None이 존재하면 안됨
        if manufacture_list.count(None) == 1 or manufacture_list.count(None) == 2:
            return jsonify(message = "DATA_ERROR"), 400

        # 아래에서 data 입력위해 불필요한 list_data 삭제
        rm_data = ['images','option','tag']
        for rm in rm_data:
            del data[rm]

        price = data['price']
        discount_rate = data['discount_rate']
        discount_price = data['discount_price']

        # 할인율이 없는데 할인가가 있는 경우 에러 return
        if discount_rate is None and discount_price is not None:
            return jsonify(message = "DATA_ERROR"), 400
        # 할인율이 음수인 경우 에러 return
        elif discount_rate < 0:
            return jsonify(message = "DATA_ERROR"), 400
        # 할인율이 100%가 넘는 경우 에러 return
        elif discount_rate >= 100:
            return jsonify(message = "DATA_ERROR"), 400
        # 할인율이 있고 할인가가 없는 경우 할인가 계산
        elif discount_rate is not None and discount_price is None:
            discount_data = math.floor(price*((100-discount_rate)/100)/10)*10
            data['discount_price'] = int(discount_data)

        db.begin()
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
                code = option['code']
                code_number = str(product_dao.count_options(db) + 1)
                code = "SP"+code_number.zfill(18)
                product_dao.insert_options(db, product_detail_id, color_id, size_id, stock, code)
        db.commit()
        return jsonify(''), 200

    finally:
        if db:
            db.close()

