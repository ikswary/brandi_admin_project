import os, sys

BASE_DIR = os.path.dirname(os.path.abspath("API"))
sys.path.extend([BASE_DIR])

import pymysql

from flask import Blueprint, request, jsonify

from connections import get_db_connector
from decorator import login_required
from models.main_models import role
from models.product_models import (
    seller_list,
    first_category,
    get_attribute_group_id,
    second_category,
    country_data,
    option_color,
    option_size,
    color_filter,
    style_filter
)

product_app = Blueprint("product_app", __name__)


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

        if role_id == 1:
            seller_data = seller_list(db)

            sellers = [{
                "id": seller.get('user_id'),
                "image": seller.get('profile_image'),
                "name": seller.get('seller_name')} for seller in seller_data]

            return jsonify(data=sellers), 200
        elif role_id == 2:
            return jsonify(message="UNAUTHORIZED"), 401
        elif role(db, role_id) is None:
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

        if role_id == 1 :
            seller_id = request.args.get('seller_id')
            attribute_group_id = get_attribute_group_id(db, seller_id)['attribute_group_id']
        elif role_id == 2 :
            attribute_group_id = get_attribute_group_id(db, user_id)['attribute_group_id']
        elif role(db, role_id) is None:
            return jsonify(message="DATA_DOES_NOT_EXIST"), 404

        first_category_data = first_category(db, attribute_group_id)

        category_list = [{
            "id":category.get('id'),
            "name":category.get('name'),
            "second_category": [{
                "id":category_detail.get('id'),
                "name":category_detail.get('name')
            }for category_detail in second_category(db,category.get('id'))]
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

        countries = country_data(db)
        colors = option_color(db)
        sizes = option_size(db)
        color_filters = color_filter(db)
        style_filters = style_filter(db)

        information_data = [{
            "country":[{
                "id": country.get('id'),
                "name": country.get('name')}for country in countries],
            "option_color":[{
                "id": color.get('id'),
                "name": color.get('name')}for color in colors],
            "option_size": [{
                "id": size.get('id'),
                "name": size.get('name')}for size in sizes],
            "color_filter": [{
                "id": color_data.get('id'),
                "name": color_data.get('name'),
       		"name_eng": color_data.get('name_eng'),
       		"image_url": color_data.get('image_url')}for color_data in color_filters],
            "style_filter": [{
                "id": style_data.get('id') ,
                "name": style_data.get('name')}for style_data in style_filters]}]

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
