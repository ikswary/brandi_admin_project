from models.user_models import (
    insert_users,
    insert_user_details,
    insert_managers,
    insert_user_managers,
    insert_user_status,
    get_user_status_history,
    get_detail,
    get_attribute,
    get_managers
)

MASTER_ROLE_ID = 1
SELLER_ROLE_ID = 2
BASIC_STATUS_ID = 1


def sign_up_service(db, data):
    try:
        user_id = insert_users(db, SELLER_ROLE_ID, data['account'])  # root user 레코드 생성
        insert_user_details(db, user_id=user_id, **data)  # user details 레코드 생성
        manager_id = insert_managers(db, data['manager_phone'])  # managers 레코드 생성
        insert_user_managers(db, user_id=user_id, manager_id=manager_id)  # user_managers 레코드 생성
        insert_user_status(db, user_id=user_id, modifier_id=user_id, status_id=BASIC_STATUS_ID)  # user의 상태를 입점 대기로 설정
    except Exception as e:
        raise e


def get_user_data_service(db, user_id, account, role_id):
    try:
        status_history = get_user_status_history(db, user_id)  # user_status의 변경 기록을 조회
        details = get_detail(db, user_id)  # user의 최신 details 레코드 조회
        attributes = get_attribute(db, details['seller_attribute_id'])  # user의 최신 details에서 속성 조회
        managers = get_managers(db, user_id) # user의 현재 담당자 조

        result = {
            'role': role_id,  # 셀러/마스터
            'base_info': {   # 기본 정보
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

        return result

    except Exception as e:
        raise e
