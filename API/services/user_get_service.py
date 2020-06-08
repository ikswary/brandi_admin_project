from models.user_models import (
    get_user_status_history,
    get_user_current_detail_id,
    get_detail,
    get_attribute,
    get_managers
)


def user_get(db, user_id, account, role_id):
    try:
        detail_id = get_user_current_detail_id(db, user_id)
        status_history = get_user_status_history(db, user_id)
        details = get_detail(db, detail_id)
        attributes = get_attribute(db, details['seller_attribute_id'])
        managers = get_managers(db, detail_id)

        result = {
            'role': role_id,
            'base_info': {
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
            'detail_info': {
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
            'model_size': {
                "height": details['height'],
                "top_size": details['top_size'],
                "bottom_size": details['bottom_size'],
                "foot_size": details['foot_size']
            }
        }

        return result

    except Exception as e:
        raise e