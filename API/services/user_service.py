from datetime import datetime
from copy import deepcopy
from jsonschema import validate, ValidationError

from exceptions import UserNotExistError, WrongActionError
from models.user_models import UserDao
from jsonschemas import USER_STATUS_UPDATE_SCHEMA, FILTER_SCHEMA

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
                                    status_id=BASIC_STATUS_ID, start_date=datetime.now())  # user의 상태를 입점 대기로 설정
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
            "seller_name_eng": details['seller_name_eng'],
            "seller_account": account,
        },
        'detail_info': {  # 상세 정보
            "background_image": details['background_image'],
            "introduction_short": details['introduction_short'],
            "introduction_detail": details['introduction_detail'],
            "site_url": details['site_url'],
            "managers": managers,
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


def filter_query_generator(filter_options):
    filter_keys = (
        'id',
        'account',
        'seller_name_eng',
        'seller_name',
        'manager_name',
        'seller_status',
        'manager_phone',
        'manager_email',
        'seller_attribute',
        'view',
        'page'
    )

    filters = dict()
    for key in filter_keys:
        filters[key] = filter_options.get(key, None)

    query = ''
    if filters['id']:
        query = query + f" AND user.id = '{filters['id']}'"
    if filters['account']:
        query = query + f" AND user.account LIKE '%%{filters['account']}%%'"
    if filters['seller_name_eng']:
        query = query + f" AND detail.seller_name_eng LIKE '%%{filters['seller_name_eng']}%%'"
    if filters['seller_name']:
        query = query + f" AND detail.seller_name LIKE '%%{filters['seller_name']}%%'"
    if filters['manager_name']:
        query = query + f" AND manager.name LIKE '%%{filters['manager_name']}%%'"
    if filters['seller_status']:
        query = query + f" AND status.name = '{filters['seller_status']}'"
    if filters['manager_phone']:
        query = query + f" AND manager.phone LIKE '%%{filters['manager_phone']}%%'"
    if filters['manager_email']:
        query = query + f" AND manager.email LIKE '%%{filters['manager_email']}%%'"
    if filters['seller_attribute']:
        query = query + f" AND attr.name LIKE '%%{filters['seller_attribute']}%%'"

    return query


def filter_validation_service(filter_options):
    try:
        validate(filter_options, FILTER_SCHEMA)

    except Exception as e:
        raise e


def get_seller_list_service(db, filter_options):
    try:
        # query string으로 전달받은 필터 조건들을 query문으로 변환
        filter_query = filter_query_generator(filter_options)
        limit = int(filter_options['view'])
        offset = limit * (int(filter_options['page']) - 1)

        # user_list에서 필요한 list와 쿼리 match 갯수를 리턴받는다
        rows = user_dao.get_users_count(db, filter_query)
        lists = user_dao.get_seller_list(db, filter_query, limit, offset)
        # action 버튼을 seller_status_id로 GROUP_CONCAT한 값을 리턴받는다
        actions = user_dao.get_actions_list(db)
        # 리턴받은 액션버튼을 {id,name} 딕셔너리화 시켜 actions_list에 담는다
        actions_list = []
        for action in actions:
            id_list = action['id'].split(',')
            action_list = action['actions'].split(',')
            reformat = [{
                "id": int(id_list[i]),
                "name": action_list[i]
            } for i in range(len(id_list))]

            actions_list.append(reformat)

        if lists:
            # 위에서 받아온 seller_list에 actions를 update한다
            for user_list in lists:
                user_list['actions'] = actions_list[user_list['seller_status_id'] - 1]

        if rows % limit == 0:
            list_pages = rows // limit
        elif rows % limit > 0:
            list_pages = (rows // limit) + 1

        result = {
            "page": list_pages,
            "record": rows,
            "list": lists
        }

        return result

    except Exception as e:
        raise e


def user_status_update_service(db, user_id, modifier_id, action):
    # 액션버튼이 눌림에 따라 바뀌는 셀러 상태의 맵핑
    action_status_mapping = {
        1: 2,  # 입점 승인 -> 입점 상태
        2: 5,  # 입점 거절 -> 퇴점 상태
        3: 3,  # 휴점 신청 -> 휴점 상태
        4: 2,  # 휴점 해제 -> 입점 상태
        5: 4,  # 퇴점 신청 처리 -> 퇴점 대기 상태
        6: 5,  # 퇴점 확정 처리 -> 퇴점 상태
        7: 2  # 퇴점 철회 처리 -> 입점 상태
    }
    try:
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        user_dao.update_user_status(db, user_id, current_time)
        user_dao.insert_user_status(db,
                                    user_id=user_id,
                                    modifier_id=modifier_id,
                                    status_id=action_status_mapping[action],
                                    start_date=current_time)

        # 입점 거절 또는 퇴점 확정 처리 일 경우
        if action in (2, 6):
            user_dao.soft_delete_user(db, user_id)

    except Exception as e:
        raise e


def user_status_update_validate_service(db, action, user_id):
    try:
        validation_object = {
            "user_id": user_id,
            "action": int(action)
        }
        validate(validation_object, USER_STATUS_UPDATE_SCHEMA)

        # user의 id값으로 user의 status id를 조회한다
        status_id = user_dao.get_user_status_id(db, user_id)
        # 위 조회값이 없으면 ERROR를 raise한다
        if status_id == 5 or status_id is None:
            raise UserNotExistError

        # user의 status에서 적용 가능한 버튼을 조회한다
        right_actions = user_dao.get_actions_id(db, status_id)
        right_action_list = [action[0] for action in right_actions]
        # 입력받은 action값이 조회한 list에 존재하지 않다면 올바르지 않은 입력
        if not validation_object['action'] in right_action_list:
            raise WrongActionError

    except Exception as e:
        raise e
