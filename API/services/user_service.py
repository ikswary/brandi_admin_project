from datetime import datetime
from copy import deepcopy

from models.user_models import UserDao

MASTER_ROLE_ID = 1
SELLER_ROLE_ID = 2
BASIC_STATUS_ID = 1

user_dao = UserDao()


def sign_up_service(db, data):
    try:
        user_id = user_dao.insert_users(db, SELLER_ROLE_ID, data['account'])  # root user 레코드 생성
        user_dao.insert_user_details_first(db, user_id=user_id, **data)  # user details 레코드 생성
        manager_id = user_dao.insert_managers_first(db, data['manager_phone'])  # managers 레코드 생성
        user_dao.insert_user_managers_first(db, user_id=user_id, manager_id=manager_id)  # user_managers 레코드 생성
        user_dao.insert_user_status(db, user_id=user_id, modifier_id=user_id,
                                    status_id=BASIC_STATUS_ID)  # user의 상태를 입점 대기로 설정
    except Exception as e:
        raise e


def get_user_data_service(db, user_id, account, role_id):
    try:
        if role_id == MASTER_ROLE_ID:
            status_history = user_dao.get_user_status_history_as_master(db, user_id)  # user_status의 변경 기록을 조회
        elif role_id == SELLER_ROLE_ID:
            status_history = user_dao.get_user_status_history_as_seller(db, user_id)
        details = user_dao.get_user_detail(db, user_id)  # user의 최신 details 레코드 조회
        attributes = user_dao.get_attribute(db, details['seller_attribute_id'])  # user의 최신 details에서 속성 조회
        managers = user_dao.get_managers(db, user_id)  # user의 현재 담당자 조회

        return role_id, account, details, managers, attributes, status_history

    except Exception as e:
        raise e


def user_data_formatter(role_id, account, details, managers, attributes, status_history):
    return {
        'role': role_id,  # 셀러/마스터
        'base_info': {  # 기본 정보
            "profile_image": details['profile_image'],
            "seller_status": status_history[-1]['name'],
            "seller_attributes": {
                "list": attributes,
                "selected": details['seller_attribute_id']
            },
            "seller_name": details['seller_name'],
            "seller_name_eng": details['seller_name'],
            "seller_account": account,
        },
        'detail_info': {  # 상세 정보
            "background_image": details['background_image'],
            "introduction_short": details['introduction_short'],
            "introduction_detail": details['introduction_detail'],
            "site_url": details['site_url'],
            "manages": managers,
            "cs_phone": details['cs_phone'],
            "zip_code": details['zip_code'],
            "address": details['address'],
            "address_detail": details['address_detail'],
            "weekday_start_time": details['weekday_start_time'],
            "weekday_end_time": details['weekday_end_time'],
            "weekend_start_time": details['weekend_start_time'],
            "weekend_end_time": details['weekend_end_time'],
            "bank": details['bank'],
            "bank_account_name": details['bank_account_name'],
            "bank_account_number": details['bank_account_number'],
            "seller_status_history": status_history
        },
        'model_size': {  # 모델 사이즈
            "height": details['height'],
            "top_size": details['top_size'],
            "bottom_size": details['bottom_size'],
            "foot_size": details['foot_size']
        },
        'feed': details['feed']
    }


def user_data_deformatter(base_info, detail_info, model_size):
    try:
        detail_info.update(base_info)
        detail_info.update(model_size)
        managers = detail_info.pop('managers')

        return detail_info, managers

    except Exception as e:
        raise e


def user_update_service(db, user_id, modifier_id, details, managers):
    try:
        # user detail modify와 manager modify를 호출
        user_detail_modify_service(db, user_id, modifier_id, details)
        user_manager_modify_service(db, user_id, managers)
        # 한번이라도 정보를 수정한 셀러는 activate 상태로 만들어준다
        user_dao.activate_user(db, user_id)


    except Exception as e:
        raise e


def user_detail_modify_service(db, user_id, modifier_id, details):
    try:
        # detail 현재 레코드와 request로 전달받은 부분을 합치고
        # 바뀐부분이 있는지 check후 update
        last_detail = user_dao.get_user_detail(db, user_id)
        current_detail = deepcopy(last_detail)
        current_detail.update(details)

        # 현재 request에서 전달받은 detail과 DB의 detail이 다르면 update 수행
        if current_detail != last_detail:
            current_time = datetime.now().strftime("%Y%m%d%H%M%S")
            current_detail['user_id'] = user_id
            current_detail['modifier_id'] = modifier_id
            current_detail['startdate'] = current_time
            user_dao.update_detail(db, user_id, current_time)
            user_dao.insert_user_details(db, current_detail)

    except Exception as e:
        raise e


def user_manager_modify_service(db, user_id, managers):
    try:
        order = 1

        # 현재 user의 manager는 소프트 딜리트 하고
        # 전달받은 manager를 모두 Update
        user_dao.update_manager(db, user_id)
        for manager in managers:
            manager_id = user_dao.insert_managers(db, manager)
            user_dao.insert_user_managers(db, user_id=user_id, manager_id=manager_id, list_order=order)
            order += 1
    except Exception as e:
        raise e


def get_seller_list_service(db, limit, offset):
    try:
        # user_list에서 필요한 list와 쿼리 match 갯수를 리턴받는다
        rows, lists = user_dao.get_seller_list()


    except Exception as e:
        raise e

