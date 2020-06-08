SIGN_UP_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "account": "seller2",
            "password": "Dlcmzk135!",
            "seller_name": "손진현2",
            "seller_name_eng": "second",
            "manager_phone": "010-3151-7153",
            "cs_phone": "02-4592-7153",
            "seller_attribute_id": "1",
            "site_url": "http://tag.brandi.co.kr"
        }
    ],
    "required": [
        "account",
        "password",
        "seller_name",
        "seller_name_eng",
        "manager_phone",
        "cs_phone",
        "seller_attribute_id",
        "site_url"
    ],
    "additionalProperties": True,
    "properties": {
        "account": {
            "$id": "#/properties/account",
            "type": "string",
            "title": "The account schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "seller2"
            ],
            "pattern": "^[a-z0-9\\-_]{5,20}$"
        },
        "password": {
            "$id": "#/properties/password",
            "type": "string",
            "title": "The password schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "Dlcmzk135!"
            ],
            "pattern": "^(?=.*\\d{1,20})(?=.*[~`!@#$%\\^&*()-+=]{1,20})(?=.*[a-z]{1,20})(?=.*[A-Z]{1,20}).{8,20}$"
        },
        "seller_name": {
            "$id": "#/properties/seller_name",
            "type": "string",
            "title": "The seller_name schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "손진현2"
            ],
            "pattern": "^[가-힣a-zA-z0-9]{1,50}$"
        },
        "seller_name_eng": {
            "$id": "#/properties/seller_name_eng",
            "type": "string",
            "title": "The seller_name_eng schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "second"
            ],
            "pattern": "^[a-z]{1,100}$"
        },
        "manager_phone": {
            "$id": "#/properties/manager_phone",
            "type": "string",
            "title": "The manager_phone schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "010-3151-7153"
            ],
            "pattern": "^01(0|1|[6-9])-([0-9]{4})-([0-9]{4})$"
        },
        "cs_phone": {
            "$id": "#/properties/cs_phone",
            "type": "string",
            "title": "The cs_phone schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "02-4592-7153"
            ],
            "pattern": "^(0[1-6][0-4]?)-(?:\\d{3}|\\d{4})-\\d{4}$"
        },
        "seller_attribute_id": {
            "$id": "#/properties/seller_attribute_id",
            "type": "string",
            "title": "The seller_attribute_id schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "1"
            ],
            "pattern": "^[1-7]$"
        },
        "site_url": {
            "$id": "#/properties/site_url",
            "type": "string",
            "title": "The site_url schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "http://tag.brandi.co.kr"
            ],
            "pattern": "^(https?://)(([a-z0-9\\-]+)\\.)+[a-z0-9]{2,4}$"
        }
    }
}

SIGN_IN_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "account": "seller2",
            "password": "Dlcmzk135!"
        }
    ],
    "required": [
        "account",
        "password"
    ],
    "additionalProperties": True,
    "properties": {
        "account": {
            "$id": "#/properties/account",
            "type": "string",
            "title": "The account schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "seller2"
            ],
            "pattern": "^[a-z0-9\-_]{5,20}$"
        },
        "password": {
            "$id": "#/properties/password",
            "type": "string",
            "title": "The password schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "Dlcmzk135!"
            ],
            "pattern": "^(?=.*\d{1,20})(?=.*[~`!@#$%\^&*()-+=]{1,20})(?=.*[a-z]{1,20})(?=.*[A-Z]{1,20}).{8,20}$"
        }
    }
}
