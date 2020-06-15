import os, sys

BASE_DIR = os.path.dirname(os.path.abspath("API"))
sys.path.extend([BASE_DIR])

import pymysql
import math
from jsonschema import validate, ValidationError
from datetime import datetime, timedelta
from flask import Blueprint, request, jsonify

from jsonschemas import PRODUCT_SCHEMA, CHANGE_PRODUCT_SCHEMA, PRODUCT_FILTER_SCHEMA, PRODUCT_STATUS_SCHEMA
from connections import get_db_connector
from decorator import login_required
from models.user_models import UserDao
from models.main_models import MainDao
from models.product_models import ProductDao
from services.product_service import product_save_service, product_data_service, product_change_service

product_app = Blueprint("product_app", __name__)
user_dao = UserDao()
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

        # 마스터 권한 전용이므로 셀러인 경우 요청 drop
        if role_id == SELLER_ROLE_ID:
            return jsonify(message="UNAUTHORIZED"), 401
        # 권한 정보가 없는 경우 에러
        if main_dao.role(db, role_id) is None:
            return jsonify(message="DATA_DOES_NOT_EXIST"), 404

        if role_id == MASTER_ROLE_ID:
            seller_data = product_dao.seller_list(db)

            sellers = [{
                "id": seller.get('user_id'),
                "image": seller.get('profile_image'),
                "name": seller.get('seller_name')} for seller in seller_data]

            return jsonify(data=sellers), 200

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

        product_code=request.args.get('code')
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
        Args:
            "product_code": 상품코드,
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
                        "code": 옵션 상품 코드,
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
                        "name": 상품 태그
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
        validate(request.json, CHANGE_PRODUCT_SCHEMA)
        data = request.json

        db = get_db_connector()
        if db is None:
            return jsonify(message="DATABASE_INIT_ERROR"), 500

        data['modifier_id'] = kwargs['user_id']
        product_code = data['product_code']

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
        product_change_service(db, previous_product_detail_id, data, tag_data, image_data, option_data)
        db.commit()
        return (''), 200

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


@product_app.route('/history', methods=['GET'])
@login_required
def history(**kwargs):
    """상품 수정의 수정 이력 API

        Args:
             code : 상품 코드

        Returns:
             {data : history_list}, http status code

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

        product_code=request.args.get('code')

        role_id = kwargs['role_id']

        # 마스터 권한 전용이므로 마스터가 아닌 경우 요청 drop
        if role_id == SELLER_ROLE_ID:
            return jsonify(message="UNAUTHORIZED"), 401
        # 권한 정보를 찾을 수 없을 때
        if main_dao.role(db, role_id) is None:
            return jsonify(message="DATA_DOES_NOT_EXIST"), 404

        if role_id == MASTER_ROLE_ID:
            history_data = product_dao.find_product_history(db, product_code)
            history_list =[ {
                "modified_data" : history['startdate'],
                "on_sale": history['on_sale'],
                "on_list": history['on_list'],
                "price": history['price'],
                "discount_price": history['discount_price'] if history['discount_price'] else history['price'],
                "discount_rate": history['discount_rate'] if history['discount_rate'] else 0,
                "modifier": user_dao.get_account_from_id(db, history['modifier_id']),
                "group": "브랜디" }
                    for history in history_data]

            return jsonify(data=history_list), 200

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


@product_app.route('/list', methods=['GET'])
@login_required
def product_list(**kwargs):
    """상품관리 리스트 및 필터

        Header:
            Authorizaion: jwt

         Query Strings: 필터링 옵션
            start_period: 조회 시작 기간
            end_period: 조회 마지막 기간
            seller_name: 셀러 한글 이름
            seller_attribute: 셀러 구분
            product_name: 상품명
            product_id: 상품번호
            code: 상품코드
            on_sale : 판매여부
            on_list: 진열여부
            discount: 할인여부

        Returns:
            {data = product_list}, http status code

        Exceptions:
            InternalError: DATABASE가 존재하지 않을 때 발생
            OperationalError: DATABASE 접속이 인가되지 않았을 때 발생
            ProgramingError: SQL syntax가 잘못되었을 때 발생
            IntegrityError: 컬럼의 무결성을 해쳤을 때 발생
            DataError: 컬럼 타입과 매칭되지 않는 값이 DB에 전달되었을 때 발생
            KeyError: 엔드포인트에서 요구하는 키값이 전달되지 않았을 때 발생
            ValidationError : 엔드포인트에서 요구하는 키값이 전달되지 않았을 때 발생
    """

    db = None
    try:
        # filter의 validation 확인
        validate(request.args, PRODUCT_FILTER_SCHEMA)

        role_id = kwargs['role_id']
        user_id = kwargs['user_id']

        # pagination 조건 생성
        filter_dict = {}
        filter_dict['limit'] = request.args.get('limit', 10, int)
        filter_dict['offset'] = request.args.get('offset', 0, int)

        # 권한이 마스터인 경우의  필터 조건 생성
        if role_id == MASTER_ROLE_ID:
            filter_list = ['start_period', 'end_period', 'seller_name', 'user_id', 'product_name', 'product_id', 'code', 'on_sale', 'on_list', 'discount']

            for filter_key in filter_list:
                filter_dict[filter_key] = request.args.get(filter_key, None)

            # seller_attribute_id 값 리스트로 저장 / 잘못된 필터 데이터가 들어오면 에러 return
            seller_attribute_check_list = ['1','2','3','4','5','6','7']
            seller_attributes = tuple(request.args.getlist('seller_attribute', None))
            for seller_attribute in seller_attributes:
                if seller_attribute not in seller_attribute_check_list:
                    return jsonify(message = "DATA_ERROR"), 400
            filter_dict['seller_attribute'] = seller_attributes

            # seller_name을 user_id로 변환
            if filter_dict['seller_name']:
                filter_dict['user_id'] = product_dao.get_id_from_seller_name(db, filter_dict['seller_name'])

            # Select로 검색하는 값이 한번에 여러개 들어온 경우 에러 return
            select_check_list = [filter_dict['product_name'], filter_dict['product_id'], filter_dict['code']]
            if select_check_list.count(None) == 0 or select_check_list.count(None) == 1:
                return jsonify(message = "DATA_ERROR"), 400

        # 권한이 셀러인 경우의 필터 조건 생성
        if role_id == SELLER_ROLE_ID:
            filter_list = ['start_period', 'end_period', 'product_name', 'product_id', 'code', 'on_sale', 'on_list', 'discount']
            for filter_key in filter_list:
                filter_dict[filter_key] = request.args.get('filter_key', None)

            # 셀러권한인 경우 셀러 아이디를 필터에 추가
            filter_dict['user_id'] = user_id

            # Select로 검색하는 값이 한번에 여러개 들어온 경우 에러 return
            select_check_list = [filter_dict['product_name'], filter_dict['product_id'], filter_dict['code']]
            if select_check_list.count(None) == 0 or select_check_list.count(None) == 1:
                return jsonify(message = "DATA_ERROR"), 400

        db = get_db_connector()

        if db is None:
            return jsonify(message="DATABASE_INIT_ERROR"), 500

        if main_dao.role(db, role_id) is None:
            return jsonify(message="DATA_DOES_NOT_EXIST"), 404

        products_data = product_dao.product_list(db, filter_dict)[0]
        quantity =  product_dao.product_list(db, filter_dict)[1]

        product_list = {
            "quantity": quantity,
            "product" : [{
            "created_at": product['create_at'],
            "image": product_dao.find_first_image(db, product['id']),
            "product_name": product['name'],
            "product_code": product['code'],
            "product_id" : product['product_id'],
            "seller_attribute": product_dao.find_seller_attribute(db, product['seller_attribute_id']),
            "seller_name": product['seller_name'],
            "price": product['price'],
            "discount_price": product['discount_price'] if product['discount_price'] else product['price'],
            "discount_rate": product['discount_rate'],
            "on_sale": product['on_sale'],
            "on_list": product['on_list'],
    	    "discount": 1 if product['discount_rate'] else 0
                }   for product in products_data]}

        return jsonify(data = product_list), 200

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
    except ValidationError as e:
         error_path = str(e.path)[8:-3]
         return jsonify(message=f"{error_path.upper()}_VALIDATION_ERROR"), 400
    except Exception as e:
        return jsonify(message=f"{e}"), 500
    finally:
        if db:
            db.close()


@product_app.route('/status', methods=['PUT'])
@login_required
def change_product_status(**kwargs):
    """상품 상태 변경 API

        Args:
            code : 상품 코드
            on_sale: 판매여부
            on_list: 진열여부

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
        validate(request.json, PRODUCT_STATUS_SCHEMA)
        # 상품 코드를 이용하여 이전의 데이터 및 정보  불러오기
        product_code=request.json['product_code']

        db = get_db_connector()

        previous_product_detail_id = product_dao.find_product(db, product_code)['id']
        previous_data = product_dao.find_product(db, product_code)
        product_detail_id = previous_data['id']

        images_data = product_dao.find_images(db, product_detail_id)
        options_data = product_dao.find_options(db, product_detail_id)
        tags_data = product_dao.find_product_tags(db, product_detail_id)

        # 변경 값 받아와서 이전 값에서 변경하기
        on_sale = request.json.get('on_sale', None)
        on_list = request.json.get('on_list', None)

        if on_sale is not None:
            if not (on_sale == 1 or on_sale == 0) :
                return jsonify(message = "DATA_ERROR"), 400
            previous_data['on_sale'] = on_sale

        if on_list is not None:
            if not (on_list == 1 or on_list == 0):
                return jsonify(message = "DATA_ERROR"), 400
            previous_data['on_list'] = on_list

        db.begin()
        # 변경된 데이터 삽입 후 삽입 된 번호 return
        product_detail_id = product_dao.insert_product_details(db, previous_data)

        # 이전 product_detail의 enddate 날짜 변경
        previous_enddate = product_dao.find_product_date(db,product_detail_id)
        product_dao.change_product_date(db, previous_enddate, previous_product_detail_id)

        # 리스트로 들어온 태그 데이터 삽입
        for tag in tags_data:
            tag_id = product_dao.find_tag_id(db, tag['name'])['id']
            product_dao.insert_product_tag(db, product_detail_id, tag_id)

        # 리스트로 들어온 imgae_data 삽입
        for image in images_data:
            large_url = image['large_url']
            medium_url = image['medium_url']
            small_url = image['small_url']
            list_order = image['list_order']
            image_id = product_dao.insert_image(db, large_url, medium_url, small_url)
            product_dao.insert_product_images(db, product_detail_id, image_id, list_order)

        # 리스트로 들어온 option_data 추가
        for option in options_data:
            color_id = option['color_id']
            size_id = option['size_id']
            stock = option['stock']
            code = option['code']
            product_dao.insert_options(db, product_detail_id, color_id, size_id, stock, code)

        db.commit()
        return (''), 200

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


@product_app.route('/seller-name', methods=['GET'])
@login_required
def find_seller_name(**kwargs):
    """
    Args:
        seller_name : 셀러 한글 이름

    Returns:
        {data : seller_list}, http status code

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
        role_id = kwargs['role_id']
        seller_name = request.args['seller_name']

        db = get_db_connector()
        if db is None:
            return jsonify(message="DATABASE_INIT_ERROR"), 500

        # 마스터 권한 전용이므로 셀러인 경우 요청 drop
        if role_id == SELLER_ROLE_ID:
            return jsonify(message="UNAUTHORIZED"), 401
        # 권한 정보가 없는 경우 에러
        if main_dao.role(db, role_id) is None:
            return jsonify(message="DATA_DOES_NOT_EXIST"), 404

        if role_id == MASTER_ROLE_ID:
            seller_data = product_dao.similar_seller_name(db, seller_name)

            print(seller_data)
            seller_list = [{ "id" : seller['user_id'],
                  "name": seller['seller_name'],
                  "image": seller['profile_image']
                }for seller in seller_data]

            print(seller_list)

            return jsonify(data=seller_list), 200

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

