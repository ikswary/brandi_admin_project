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

PRODUCT_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "seller_id": 1,
            "on_sale": 1,
            "on_list": 1,
            "first_category_id": 1,
            "second_category_id": 1,
            "manufacturer": "string",
            "manufacture_date": "date",
            "manufacture_country_id": 1,
            "name": "string",
            "description_short": "string",
            "images": [
                {
                    "url": "url"
                }
            ],
            "color_filter_id": 1,
            "style_filter_id": 1,
            "description_detail": "string",
            "option": [
                {
                    "color_id": 1,
                    "size_id": 1,
                    "stock": 10
                }
            ],
            "price": 100,
            "discount_rate": 10,
            "discount_price": 90,
            "discount_start": "str",
            "discount_end": "date",
            "min_sales_unit": 1,
            "max_sales_unit": 20,
            "tag": [
                {
                    "name": "string"
                }
            ]
        }
    ],
    "required": [
        "on_sale",
        "on_list",
        "first_category_id",
        "second_category_id",
        "manufacturer",
        "manufacture_date",
        "manufacture_country_id",
        "name",
        "images",
        "color_filter_id",
        "style_filter_id",
        "description_detail",
        "option",
        "price",
        "min_sales_unit",
        "max_sales_unit",
        "tag"
    ],
    "additionalProperties": True,
    "properties": {
        "seller_id": {
            "$id": "#/properties/seller_id",
            "type": ["integer", "null"],
            "title": "The seller_id schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                1
            ]
        },
        "on_sale": {
            "$id": "#/properties/on_sale",
            "type": "integer",
            "title": "The on_sale schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                1
            ]
        },
        "on_list": {
            "$id": "#/properties/on_list",
            "type": "integer",
            "title": "The on_list schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                1
            ]
        },
        "first_category_id": {
            "$id": "#/properties/first_category_id",
            "type": "integer",
            "title": "The first_category_id schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                1
            ]
        },
        "second_category_id": {
            "$id": "#/properties/second_category_id",
            "type": [
                "integer",
                "null"
            ],
            "title": "The second_category_id schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                1
            ]
        },
        "manufacturer": {
            "$id": "#/properties/manufacturer",
            "type": [
                "string",
                "null"
            ],
            "title": "The manufacturer schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "string"
            ]
        },
        "manufacture_date": {
            "$id": "#/properties/manufacture_date",
            "type": [
                "string",
                "null"
            ],
            "title": "The manufacture_date schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "date"
            ]
        },
        "manufacture_country_id": {
            "$id": "#/properties/manufacture_country_id",
            "type": [
                "integer",
                "null"
            ],
            "title": "The manufacture_country_id schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                1
            ]
        },
        "name": {
            "$id": "#/properties/name",
            "type": "string",
            "title": "The name schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "string"
            ]
        },
        "description_short": {
            "$id": "#/properties/description_short",
            "type": [
                "string",
                "null"
            ],
            "title": "The description_short schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "string"
            ]
        },
        "images": {
            "$id": "#/properties/images",
            "type": "array",
            "title": "The images schema",
            "description": "An explanation about the purpose of this instance.",
            "default": [],
            "examples": [
                [
                    {
                        "url": "url"
                    }
                ]
            ],
            "additionalItems": True,
            "items": {
                "anyOf": [
                    {
                        "$id": "#/properties/images/items/anyOf/0",
                        "type": "object",
                        "title": "The first anyOf schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": {},
                        "examples": [
                            {
                                "url": "url"
                            }
                        ],
                        "required": [
                            "url"
                        ],
                        "additionalProperties": True,
                        "properties": {
                            "url": {
                                "$id": "#/properties/images/items/anyOf/0/properties/url",
                                "type": "string",
                                "title": "The url schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "url"
                                ]
                            }
                        }
                    }
                ],
                "$id": "#/properties/images/items"
            }
        },
        "color_filter_id": {
            "$id": "#/properties/color_filter_id",
            "type": [
                "integer",
                "null"
            ],
            "title": "The color_filter_id schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                1
            ]
        },
        "style_filter_id": {
            "$id": "#/properties/style_filter_id",
            "type": [
                "integer",
                "null"
            ],
            "title": "The style_filter_id schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                1
            ]
        },
        "description_detail": {
            "$id": "#/properties/description_detail",
            "type": "string",
            "title": "The description_detail schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "string"
            ]
        },
        "option": {
            "$id": "#/properties/option",
            "type": "array",
            "title": "The option schema",
            "description": "An explanation about the purpose of this instance.",
            "default": [],
            "examples": [
                [
                    {
                        "color_id": 1,
                        "size_id": 1,
                        "stock": 10
                    }
                ]
            ],
            "additionalItems": True,
            "items": {
                "anyOf": [
                    {
                        "$id": "#/properties/option/items/anyOf/0",
                        "type": "object",
                        "title": "The first anyOf schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": {},
                        "examples": [
                            {
                                "color_id": 1,
                                "size_id": 1,
                                "stock": 10
                            }
                        ],
                        "required": [
                            "color_id",
                            "size_id",
                            "stock"
                        ],
                        "additionalProperties": True,
                        "properties": {
                            "color_id": {
                                "$id": "#/properties/option/items/anyOf/0/properties/color_id",
                                "type": [
                                    "integer",
                                    "null"
                                ],
                                "title": "The color_id schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": 0,
                                "examples": [
                                    1
                                ]
                            },
                            "size_id": {
                                "$id": "#/properties/option/items/anyOf/0/properties/size_id",
                                "type": [
                                    "integer",
                                    "null"
                                ],
                                "title": "The size_id schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": 0,
                                "examples": [
                                    1
                                ]
                            },
                            "stock": {
                                "$id": "#/properties/option/items/anyOf/0/properties/stock",
                                "type": [
                                    "integer",
                                    "null"
                                ],
                                "title": "The stock schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": 0,
                                "examples": [
                                    10
                                ]
                            }
                        }
                    }
                ],
                "$id": "#/properties/option/items"
            }
        },
        "price": {
            "$id": "#/properties/price",
            "type": "integer",
            "title": "The price schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                100
            ]
        },
        "discount_rate": {
            "$id": "#/properties/discount_rate",
            "type": [
                "integer",
                "null"
            ],
            "title": "The discount_rate schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                10
            ]
        },
        "discount_price": {
            "$id": "#/properties/discount_price",
            "type": [
                "integer",
                "null"
            ],
            "title": "The discount_price schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                90
            ]
        },
        "discount_start": {
            "$id": "#/properties/discount_start",
            "type": [
                "string",
                "null"
            ],
            "title": "The discount_start schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "str"
            ]
        },
        "discount_end": {
            "$id": "#/properties/discount_end",
            "type": [
                "string",
                "null"
            ],
            "title": "The discount_end schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "date"
            ]
        },
        "min_sales_unit": {
            "$id": "#/properties/min_sales_unit",
            "type": "integer",
            "title": "The min_sales_unit schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                1
            ]
        },
        "max_sales_unit": {
            "$id": "#/properties/max_sales_unit",
            "type": "integer",
            "title": "The max_sales_unit schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                20
            ]
        },
        "tag": {
            "$id": "#/properties/tag",
            "type": "array",
            "title": "The tag schema",
            "description": "An explanation about the purpose of this instance.",
            "default": [],
            "examples": [
                [
                    {
                        "name": "string"
                    }
                ]
            ],
            "additionalItems": True,
            "items": {
                "anyOf": [
                    {
                        "$id": "#/properties/tag/items/anyOf/0",
                        "type": "object",
                        "title": "The first anyOf schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": {},
                        "examples": [
                            {
                                "name": "string"
                            }
                        ],
                        "required": [
                            "name"
                        ],
                        "additionalProperties": True,
                        "properties": {
                            "name": {
                                "$id": "#/properties/tag/items/anyOf/0/properties/name",
                                "type": "string",
                                "title": "The name schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "string"
                                ]
                            }
                        }
                    }
                ],
                "$id": "#/properties/tag/items"
            }
        }
    }
}

USER_DATA_MODIFY_MASTER = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "base_info": {
                "profile_image": "string",
                "seller_attribute_id": 1,
                "seller_name": "하이모디",
                "seller_name_eng": "himodi"
            },
            "detail_info": {
                "background_image": "string",
                "introduction_short": "string",
                "introduction_detail": "string",
                "site_url": "http://tag.brandi.co.kr",
                "managers": [
                    {
                        "name": "손진현",
                        "phone": "010-3151-7153",
                        "email": "ikswary@naver.com"
                    }
                ],
                "cs_phone": "02-4592-7153",
                "zip_code": "string",
                "address": "string",
                "address_detail": "string",
                "weekday_start_time": "string",
                "weekday_end_time": "string",
                "weekend_start_time": "string",
                "weekend_end_time": "string",
                "bank": "string",
                "bank_account_name": "string",
                "bank_account_number": "string"
            },
            "model_size": {
                "height": 180,
                "top_size": 100,
                "bottom_size": 28,
                "foot_size": 280
            }
        }
    ],
    "required": [
        "base_info",
        "detail_info"
    ],
    "additionalProperties": True,
    "properties": {
        "base_info": {
            "$id": "#/properties/base_info",
            "type": "object",
            "title": "The base_info schema",
            "description": "An explanation about the purpose of this instance.",
            "default": {},
            "examples": [
                {
                    "profile_image": "string",
                    "seller_attribute_id": 1,
                    "seller_name": "하이모디",
                    "seller_name_eng": "himodi"
                }
            ],
            "required": [
                "profile_image",
                "seller_attribute_id",
                "seller_name",
                "seller_name_eng"
            ],
            "additionalProperties": True,
            "properties": {
                "profile_image": {
                    "$id": "#/properties/base_info/properties/profile_image",
                    "type": "string",
                    "title": "The profile_image schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "string"
                    ]
                },
                "seller_attribute_id": {
                    "$id": "#/properties/base_info/properties/seller_attribute_id",
                    "type": "integer",
                    "title": "The seller_attribute_id schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": 0,
                    "examples": [
                        1
                    ]
                },
                "seller_name": {
                    "$id": "#/properties/base_info/properties/seller_name",
                    "type": "string",
                    "title": "The seller_name schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "하이모디"
                    ],
                    "pattern": "^[가-힣a-zA-z0-9]{1,50}$"
                },
                "seller_name_eng": {
                    "$id": "#/properties/base_info/properties/seller_name_eng",
                    "type": "string",
                    "title": "The seller_name_eng schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "himodi"
                    ],
                    "pattern": "^[a-z]{1,100}$"
                }
            }
        },
        "detail_info": {
            "$id": "#/properties/detail_info",
            "type": "object",
            "title": "The detail_info schema",
            "description": "An explanation about the purpose of this instance.",
            "default": {},
            "examples": [
                {
                    "background_image": "string",
                    "introduction_short": "string",
                    "introduction_detail": "string",
                    "site_url": "http://tag.brandi.co.kr",
                    "managers": [
                        {
                            "name": "손진현",
                            "phone": "010-3151-7153",
                            "email": "ikswary@naver.com"
                        }
                    ],
                    "cs_phone": "02-4592-7153",
                    "zip_code": "string",
                    "address": "string",
                    "address_detail": "string",
                    "weekday_start_time": "string",
                    "weekday_end_time": "string",
                    "weekend_start_time": "string",
                    "weekend_end_time": "string",
                    "bank": "string",
                    "bank_account_name": "string",
                    "bank_account_number": "string"
                }
            ],
            "required": [
                "introduction_short",
                "site_url",
                "managers",
                "cs_phone",
                "zip_code",
                "address",
                "address_detail",
                "weekday_start_time",
                "weekday_end_time",
                "bank",
                "bank_account_name",
                "bank_account_number"
            ],
            "additionalProperties": True,
            "properties": {
                "background_image": {
                    "$id": "#/properties/detail_info/properties/background_image",
                    "type": "string",
                    "title": "The background_image schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "string"
                    ]
                },
                "introduction_short": {
                    "$id": "#/properties/detail_info/properties/introduction_short",
                    "type": "string",
                    "title": "The introduction_short schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "string"
                    ]
                },
                "site_url": {
                    "$id": "#/properties/detail_info/properties/site_url",
                    "type": "string",
                    "title": "The site_url schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "http://tag.brandi.co.kr"
                    ],
                    "pattern": "^(https?://)(([a-z0-9\\-]+)\\.)+[a-z0-9]{2,4}$"
                },
                "managers": {
                    "$id": "#/properties/detail_info/properties/managers",
                    "type": "array",
                    "title": "The managers schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": [],
                    "examples": [
                        [
                            {
                                "name": "손진현",
                                "phone": "010-3151-7153",
                                "email": "ikswary@naver.com"
                            }
                        ]
                    ],
                    "additionalItems": True,
                    "items": {
                        "anyOf": [
                            {
                                "$id": "#/properties/detail_info/properties/managers/items/anyOf/0",
                                "type": "object",
                                "title": "The first anyOf schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": {},
                                "examples": [
                                    {
                                        "name": "손진현",
                                        "phone": "010-3151-7153",
                                        "email": "ikswary@naver.com"
                                    }
                                ],
                                "required": [
                                    "name",
                                    "phone",
                                    "email"
                                ],
                                "additionalProperties": True,
                                "properties": {
                                    "name": {
                                        "$id": "#/properties/detail_info/properties/managers/items/anyOf/0/properties/name",
                                        "type": "string",
                                        "title": "The name schema",
                                        "description": "An explanation about the purpose of this instance.",
                                        "default": "",
                                        "examples": [
                                            "손진현"
                                        ],
                                        "pattern": "^[가-힣a-zA-z0-9]{1,50}$"
                                    },
                                    "phone": {
                                        "$id": "#/properties/detail_info/properties/managers/items/anyOf/0/properties/phone",
                                        "type": "string",
                                        "title": "The phone schema",
                                        "description": "An explanation about the purpose of this instance.",
                                        "default": "",
                                        "examples": [
                                            "010-3151-7153"
                                        ],
                                        "pattern": "^01(0|1|[6-9])-([0-9]{4})-([0-9]{4})$"
                                    },
                                    "email": {
                                        "$id": "#/properties/detail_info/properties/managers/items/anyOf/0/properties/email",
                                        "type": "string",
                                        "title": "The email schema",
                                        "description": "An explanation about the purpose of this instance.",
                                        "default": "",
                                        "examples": [
                                            "ikswary@naver.com"
                                        ],
                                        "pattern": "^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$"
                                    }
                                }
                            }
                        ],
                        "$id": "#/properties/detail_info/properties/managers/items"
                    }
                },
                "cs_phone": {
                    "$id": "#/properties/detail_info/properties/cs_phone",
                    "type": "string",
                    "title": "The cs_phone schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "02-4592-7153"
                    ],
                    "pattern": "^(0[1-6][0-4]?)-([0-9]{3,4})-([0-9]{4})$"
                },
                "zip_code": {
                    "$id": "#/properties/detail_info/properties/zip_code",
                    "type": "string",
                    "title": "The zip_code schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "string"
                    ],
                    "pattern": "^[0-9]{5}$"
                },
                "address": {
                    "$id": "#/properties/detail_info/properties/address",
                    "type": "string",
                    "title": "The address schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "string"
                    ]
                },
                "address_detail": {
                    "$id": "#/properties/detail_info/properties/address_detail",
                    "type": "string",
                    "title": "The address_detail schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "string"
                    ]
                },
                "weekday_start_time": {
                    "$id": "#/properties/detail_info/properties/weekday_start_time",
                    "type": "string",
                    "title": "The weekday_start_time schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "string"
                    ],
                    "pattern": "^(0|1[0-9])|(2[0-3]):[0-5][0-9]$"
                },
                "weekday_end_time": {
                    "$id": "#/properties/detail_info/properties/weekday_end_time",
                    "type": "string",
                    "title": "The weekday_end_time schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "string"
                    ],
                    "pattern": "^(0|1[0-9])|(2[0-3]):[0-5][0-9]$"
                },
                "bank": {
                    "$id": "#/properties/detail_info/properties/bank",
                    "type": "string",
                    "title": "The bank schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "string"
                    ]
                },
                "bank_account_name": {
                    "$id": "#/properties/detail_info/properties/bank_account_name",
                    "type": "string",
                    "title": "The bank_account_name schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "string"
                    ]
                },
                "bank_account_number": {
                    "$id": "#/properties/detail_info/properties/bank_account_number",
                    "type": "string",
                    "title": "The bank_account_number schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "string"
                    ]
                }
            }
        },
        "model_size": {
            "$id": "#/properties/model_size",
            "type": "object",
            "title": "The model_size schema",
            "description": "An explanation about the purpose of this instance.",
            "default": {},
            "examples": [
                {
                    "height": 180,
                    "top_size": 100,
                    "bottom_size": 28,
                    "foot_size": 280
                }
            ],
            "required": [
                "height",
                "top_size",
                "bottom_size",
                "foot_size"
            ],
            "additionalProperties": True,
            "properties": {
                "height": {
                    "$id": "#/properties/model_size/properties/height",
                    "type": "integer",
                    "title": "The height schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": 0,
                    "examples": [
                        180
                    ]
                },
                "top_size": {
                    "$id": "#/properties/model_size/properties/top_size",
                    "type": "integer",
                    "title": "The top_size schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": 0,
                    "examples": [
                        100
                    ]
                },
                "bottom_size": {
                    "$id": "#/properties/model_size/properties/bottom_size",
                    "type": "integer",
                    "title": "The bottom_size schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": 0,
                    "examples": [
                        28
                    ]
                },
                "foot_size": {
                    "$id": "#/properties/model_size/properties/foot_size",
                    "type": "integer",
                    "title": "The foot_size schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": 0,
                    "examples": [
                        280
                    ]
                }
            }
        }
    }
}

USER_DATA_MODIFY_SELLER = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "base_info": {
                "profile_image": "string"
            },
            "detail_info": {
                "background_image": "string",
                "introduction_short": "string",
                "introduction_detail": "string",
                "site_url": "http://tag.brandi.co.kr",
                "managers": [
                    {
                        "name": "손진현",
                        "phone": "010-3151-7153",
                        "email": "ikswary@naver.com"
                    }
                ],
                "cs_phone": "02-4592-7153",
                "zip_code": "string",
                "address": "string",
                "address_detail": "string",
                "weekday_start_time": "string",
                "weekday_end_time": "string",
                "weekend_start_time": "string",
                "weekend_end_time": "string",
                "bank": "string",
                "bank_account_name": "string",
                "bank_account_number": "string"
            },
            "model_size": {
                "height": 180,
                "top_size": 100,
                "bottom_size": 28,
                "foot_size": 280
            }
        }
    ],
    "required": [
        "base_info",
        "detail_info"
    ],
    "additionalProperties": True,
    "properties": {
        "base_info": {
            "$id": "#/properties/base_info",
            "type": "object",
            "title": "The base_info schema",
            "description": "An explanation about the purpose of this instance.",
            "default": {},
            "examples": [
                {
                    "profile_image": "string"
                }
            ],
            "required": [
                "profile_image"
            ],
            "additionalProperties": True,
            "properties": {
                "profile_image": {
                    "$id": "#/properties/base_info/properties/profile_image",
                    "type": "string",
                    "title": "The profile_image schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "string"
                    ]
                }
            }
        },
        "detail_info": {
            "$id": "#/properties/detail_info",
            "type": "object",
            "title": "The detail_info schema",
            "description": "An explanation about the purpose of this instance.",
            "default": {},
            "examples": [
                {
                    "background_image": "string",
                    "introduction_short": "string",
                    "introduction_detail": "string",
                    "site_url": "http://tag.brandi.co.kr",
                    "managers": [
                        {
                            "name": "손진현",
                            "phone": "010-3151-7153",
                            "email": "ikswary@naver.com"
                        }
                    ],
                    "cs_phone": "02-4592-7153",
                    "zip_code": "string",
                    "address": "string",
                    "address_detail": "string",
                    "weekday_start_time": "string",
                    "weekday_end_time": "string",
                    "weekend_start_time": "string",
                    "weekend_end_time": "string",
                    "bank": "string",
                    "bank_account_name": "string",
                    "bank_account_number": "string"
                }
            ],
            "required": [
                "introduction_short",
                "site_url",
                "managers",
                "cs_phone",
                "zip_code",
                "address",
                "address_detail",
                "weekday_start_time",
                "weekday_end_time",
                "bank",
                "bank_account_name",
                "bank_account_number"
            ],
            "additionalProperties": True,
            "properties": {
                "background_image": {
                    "$id": "#/properties/detail_info/properties/background_image",
                    "type": "string",
                    "title": "The background_image schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "string"
                    ]
                },
                "introduction_short": {
                    "$id": "#/properties/detail_info/properties/introduction_short",
                    "type": "string",
                    "title": "The introduction_short schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "string"
                    ]
                },
                "site_url": {
                    "$id": "#/properties/detail_info/properties/site_url",
                    "type": "string",
                    "title": "The site_url schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "http://tag.brandi.co.kr"
                    ],
                    "pattern": "^(https?://)(([a-z0-9\\-]+)\\.)+[a-z0-9]{2,4}$"
                },
                "managers": {
                    "$id": "#/properties/detail_info/properties/managers",
                    "type": "array",
                    "title": "The managers schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": [],
                    "examples": [
                        [
                            {
                                "name": "손진현",
                                "phone": "010-3151-7153",
                                "email": "ikswary@naver.com"
                            }
                        ]
                    ],
                    "additionalItems": True,
                    "items": {
                        "anyOf": [
                            {
                                "$id": "#/properties/detail_info/properties/managers/items/anyOf/0",
                                "type": "object",
                                "title": "The first anyOf schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": {},
                                "examples": [
                                    {
                                        "name": "손진현",
                                        "phone": "010-3151-7153",
                                        "email": "ikswary@naver.com"
                                    }
                                ],
                                "required": [
                                    "name",
                                    "phone",
                                    "email"
                                ],
                                "additionalProperties": True,
                                "properties": {
                                    "name": {
                                        "$id": "#/properties/detail_info/properties/managers/items/anyOf/0/properties/name",
                                        "type": "string",
                                        "title": "The name schema",
                                        "description": "An explanation about the purpose of this instance.",
                                        "default": "",
                                        "examples": [
                                            "손진현"
                                        ],
                                        "pattern": "^[가-힣a-zA-z0-9]{1,50}$"
                                    },
                                    "phone": {
                                        "$id": "#/properties/detail_info/properties/managers/items/anyOf/0/properties/phone",
                                        "type": "string",
                                        "title": "The phone schema",
                                        "description": "An explanation about the purpose of this instance.",
                                        "default": "",
                                        "examples": [
                                            "010-3151-7153"
                                        ],
                                        "pattern": "^01(0|1|[6-9])-([0-9]{4})-([0-9]{4})$"
                                    },
                                    "email": {
                                        "$id": "#/properties/detail_info/properties/managers/items/anyOf/0/properties/email",
                                        "type": "string",
                                        "title": "The email schema",
                                        "description": "An explanation about the purpose of this instance.",
                                        "default": "",
                                        "examples": [
                                            "ikswary@naver.com"
                                        ],
                                        "pattern": "^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$"
                                    }
                                }
                            }
                        ],
                        "$id": "#/properties/detail_info/properties/managers/items"
                    }
                },
                "cs_phone": {
                    "$id": "#/properties/detail_info/properties/cs_phone",
                    "type": "string",
                    "title": "The cs_phone schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "02-4592-7153"
                    ],
                    "pattern": "^(0[1-6][0-4]?)-([0-9]{3,4})-([0-9]{4})$"
                },
                "zip_code": {
                    "$id": "#/properties/detail_info/properties/zip_code",
                    "type": "string",
                    "title": "The zip_code schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "string"
                    ],
                    "pattern": "^[0-9]{5}$"
                },
                "address": {
                    "$id": "#/properties/detail_info/properties/address",
                    "type": "string",
                    "title": "The address schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "string"
                    ]
                },
                "address_detail": {
                    "$id": "#/properties/detail_info/properties/address_detail",
                    "type": "string",
                    "title": "The address_detail schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "string"
                    ]
                },
                "weekday_start_time": {
                    "$id": "#/properties/detail_info/properties/weekday_start_time",
                    "type": "string",
                    "title": "The weekday_start_time schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "string"
                    ],
                    "pattern": "^(0|1[0-9])|(2[0-3]):[0-5][0-9]$"
                },
                "weekday_end_time": {
                    "$id": "#/properties/detail_info/properties/weekday_end_time",
                    "type": "string",
                    "title": "The weekday_end_time schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "string"
                    ],
                    "pattern": "^(0|1[0-9])|(2[0-3]):[0-5][0-9]$"
                },
                "bank": {
                    "$id": "#/properties/detail_info/properties/bank",
                    "type": "string",
                    "title": "The bank schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "string"
                    ]
                },
                "bank_account_name": {
                    "$id": "#/properties/detail_info/properties/bank_account_name",
                    "type": "string",
                    "title": "The bank_account_name schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "string"
                    ]
                },
                "bank_account_number": {
                    "$id": "#/properties/detail_info/properties/bank_account_number",
                    "type": "string",
                    "title": "The bank_account_number schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "string"
                    ]
                }
            }
        },
        "model_size": {
            "$id": "#/properties/model_size",
            "type": "object",
            "title": "The model_size schema",
            "description": "An explanation about the purpose of this instance.",
            "default": {},
            "examples": [
                {
                    "height": 180,
                    "top_size": 100,
                    "bottom_size": 28,
                    "foot_size": 280
                }
            ],
            "required": [
                "height",
                "top_size",
                "bottom_size",
                "foot_size"
            ],
            "additionalProperties": True,
            "properties": {
                "height": {
                    "$id": "#/properties/model_size/properties/height",
                    "type": "integer",
                    "title": "The height schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": 0,
                    "examples": [
                        180
                    ]
                },
                "top_size": {
                    "$id": "#/properties/model_size/properties/top_size",
                    "type": "integer",
                    "title": "The top_size schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": 0,
                    "examples": [
                        100
                    ]
                },
                "bottom_size": {
                    "$id": "#/properties/model_size/properties/bottom_size",
                    "type": "integer",
                    "title": "The bottom_size schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": 0,
                    "examples": [
                        28
                    ]
                },
                "foot_size": {
                    "$id": "#/properties/model_size/properties/foot_size",
                    "type": "integer",
                    "title": "The foot_size schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": 0,
                    "examples": [
                        280
                    ]
                }
            }
        }
    }
}

CHANGE_PRODUCT_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "product_code": "SB00000000000541630",
            "on_sale": 1,
            "on_list": 1,
            "first_category_id": 22,
            "second_category_id": 1,
            "manufacturer": "제조사",
            "manufacturer_date": "date",
            "manufacture_country_id": 1,
            "name": "간지나는 스킨로션_2",
            "description_short": "string",
            "images": [
                {
                    "url": "url"
                }
            ],
            "color_filter_id": 2,
            "style_filter_id": 2,
            "description_detail": "상세 상품 정보",
            "option": [
                {
                    "code": 2,
                    "color_id": 1,
                    "size_id": 1,
                    "stock": 1
                }
            ],
            "price": 20000,
            "discount_rate": 12,
            "discount_price": 17600,
            "discount_start": "2020-06-02 14:37",
            "discount_end": "2020-06-26 14:37",
            "min_sales_unit": 1,
            "max_sales_unit": 20,
            "tag": [
                {
                    "name": "간지"
                }
            ]
        }
    ],
    "required": [
        "product_code",
        "on_sale",
        "on_list",
        "first_category_id",
        "second_category_id",
        "manufacturer",
        "manufacture_date",
        "manufacture_country_id",
        "name",
        "images",
        "color_filter_id",
        "style_filter_id",
        "description_detail",
        "option",
        "price",
        "min_sales_unit",
        "max_sales_unit",
        "tag"
    ],
    "additionalProperties": True,
    "properties": {
        "product_code": {
            "$id": "#/properties/product_code",
            "type": "string",
            "title": "The product_code schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "SB00000000000541630"
            ]
        },
        "on_sale": {
            "$id": "#/properties/on_sale",
            "type": "integer",
            "title": "The on_sale schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                1
            ]
        },
        "on_list": {
            "$id": "#/properties/on_list",
            "type": "integer",
            "title": "The on_list schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                1
            ]
        },
        "first_category_id": {
            "$id": "#/properties/first_category_id",
            "type": "integer",
            "title": "The first_category_id schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                22
            ]
        },
        "second_category_id": {
            "$id": "#/properties/second_category_id",
            "type": [
                "integer",
                "null"
            ],
            "title": "The second_category_id schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                1
            ]
        },
        "manufacturer": {
            "$id": "#/properties/manufacturer",
            "type": [
                "string",
                "null"
            ],
            "title": "The manufacturer schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "제조사"
            ]
        },
        "manufacture_date": {
            "$id": "#/properties/manufacturer_date",
            "type": [
                "string",
                "null"
            ],
            "title": "The manufacture_date schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "date"
            ]
        },
        "manufacture_country_id": {
            "$id": "#/properties/manufacture_country_id",
            "type": [
                "integer",
                "null"
            ],
            "title": "The manufacture_country_id schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                1
            ]
        },
        "name": {
            "$id": "#/properties/name",
            "type": "string",
            "title": "The name schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "간지나는 스킨로션_2"
            ]
        },
        "description_short": {
            "$id": "#/properties/description_short",
            "type": [
                "string",
                "null"
            ],
            "title": "The description_short schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "string"
            ]
        },
        "images": {
            "$id": "#/properties/images",
            "type": "array",
            "title": "The images schema",
            "description": "An explanation about the purpose of this instance.",
            "default": [],
            "examples": [
                [
                    {
                        "url": "url"
                    }
                ]
            ],
            "additionalItems": True,
            "items": {
                "anyOf": [
                    {
                        "$id": "#/properties/images/items/anyOf/0",
                        "type": "object",
                        "title": "The first anyOf schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": {},
                        "examples": [
                            {
                                "url": "url"
                            }
                        ],
                        "required": [
                            "url"
                        ],
                        "additionalProperties": True,
                        "properties": {
                            "url": {
                                "$id": "#/properties/images/items/anyOf/0/properties/url",
                                "type": "string",
                                "title": "The url schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "url"
                                ]
                            }
                        }
                    }
                ],
                "$id": "#/properties/images/items"
            }
        },
        "color_filter_id": {
            "$id": "#/properties/color_filter_id",
            "type": [
                "integer",
                "null"
            ],
            "title": "The color_filter_id schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                2
            ]
        },
        "style_filter_id": {
            "$id": "#/properties/style_filter_id",
            "type": [
                "integer",
                "null"
            ],
            "title": "The style_filter_id schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                2
            ]
        },
        "description_detail": {
            "$id": "#/properties/description_detail",
            "type": "string",
            "title": "The description_detail schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "상세 상품 정보"
            ]
        },
        "option": {
            "$id": "#/properties/option",
            "type": "array",
            "title": "The option schema",
            "description": "An explanation about the purpose of this instance.",
            "default": [],
            "examples": [
                [
                    {
                        "code": 2,
                        "color_id": 1,
                        "size_id": 1,
                        "stock": 1
                    }
                ]
            ],
            "additionalItems": True,
            "items": {
                "anyOf": [
                    {
                        "$id": "#/properties/option/items/anyOf/0",
                        "type": "object",
                        "title": "The first anyOf schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": {},
                        "examples": [
                            {
                                "code": 2,
                                "color_id": 1,
                                "size_id": 1,
                                "stock": 1
                            }
                        ],
                        "required": [
                            "code",
                            "color_id",
                            "size_id",
                            "stock"
                        ],
                        "additionalProperties": True,
                        "properties": {
                            "code": {
                                "$id": "#/properties/option/items/anyOf/0/properties/id",
                                "type": [
                                    "integer",
                                    "null"
                                ],
                                "title": "The id schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    2
                                ]
                            },
                            "color_id": {
                                "$id": "#/properties/option/items/anyOf/0/properties/color_id",
                                "type": "integer",
                                "title": "The color_id schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": 0,
                                "examples": [
                                    1
                                ]
                            },
                            "size_id": {
                                "$id": "#/properties/option/items/anyOf/0/properties/size_id",
                                "type": "integer",
                                "title": "The size_id schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": 0,
                                "examples": [
                                    1
                                ]
                            },
                            "stock": {
                                "$id": "#/properties/option/items/anyOf/0/properties/stock",
                                "type": [
                                    "integer",
                                    "null"
                                ],
                                "title": "The stock schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": 0,
                                "examples": [
                                    1
                                ]
                            }
                        }
                    }
                ],
                "$id": "#/properties/option/items"
            }
        },
        "price": {
            "$id": "#/properties/price",
            "type": "integer",
            "title": "The price schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                20000
            ]
        },
        "discount_rate": {
            "$id": "#/properties/discount_rate",
            "type": [
                "integer",
                "null"
            ],
            "title": "The discount_rate schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                12
            ]
        },
        "discount_price": {
            "$id": "#/properties/discount_price",
            "type": [
                "integer",
                "null"
            ],
            "title": "The discount_price schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                17600
            ]
        },
        "discount_start": {
            "$id": "#/properties/discount_start",
            "type": [
                "string",
                "null"
            ],
            "title": "The discount_start schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "2020-06-02 14:37"
            ]
        },
        "discount_end": {
            "$id": "#/properties/discount_end",
            "type": [
                "string",
                "null"
            ],
            "title": "The discount_end schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "2020-06-26 14:37"
            ]
        },
        "min_sales_unit": {
            "$id": "#/properties/min_sales_unit",
            "type": "integer",
            "title": "The min_sales_unit schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                1
            ]
        },
        "max_sales_unit": {
            "$id": "#/properties/max_sales_unit",
            "type": "integer",
            "title": "The max_sales_unit schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                20
            ]
        },
        "tag": {
            "$id": "#/properties/tag",
            "type": "array",
            "title": "The tag schema",
            "description": "An explanation about the purpose of this instance.",
            "default": [],
            "examples": [
                [
                    {
                        "name": "간지"
                    }
                ]
            ],
            "additionalItems": True,
            "items": {
                "anyOf": [
                    {
                        "$id": "#/properties/tag/items/anyOf/0",
                        "type": "object",
                        "title": "The first anyOf schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": {},
                        "examples": [
                            {
                                "name": "간지"
                            }
                        ],
                        "required": [
                            "name"
                        ],
                        "additionalProperties": True,
                        "properties": {
                            "name": {
                                "$id": "#/properties/tag/items/anyOf/0/properties/name",
                                "type": "string",
                                "title": "The name schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "간지"
                                ]
                            }
                        }
                    }
                ],
                "$id": "#/properties/tag/items"
            }
        }
    }
}

USER_STATUS_UPDATE_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "user_id": 1,
            "action": 1
        }
    ],
    "required": [
        "user_id",
        "action"
    ],
    "additionalProperties": True,
    "properties": {
        "user_id": {
            "$id": "#/properties/user_id",
            "type": "integer",
            "title": "The user_id schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                1
            ],
            "pattern": "^[1-7]$"
        },
        "action": {
            "$id": "#/properties/action",
            "type": "integer",
            "title": "The action schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                1
            ]
        }
    }
}

FILTER_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "id": 1,
            "account": "wecode123",
            "seller_name_eng": "sjh",
            "seller_name": "위코드",
            "manager_name": "와썹맨",
            "seller_status": "입점",
            "manager_phone": "010-1234-5678",
            "manager_email": "email",
            "seller_attribute": "뷰티",
            "view": 10,
            "page": 5
        }
    ],
    "required": [
        "view",
        "page"
    ],
    "additionalProperties": True,
    "properties": {
        "id": {
            "$id": "#/properties/id",
            "type": "string",
            "title": "The id schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                1
            ]
        },
        "account": {
            "$id": "#/properties/account",
            "type": "string",
            "title": "The account schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "wecode123"
            ]
        },
        "seller_name_eng": {
            "$id": "#/properties/seller_name_eng",
            "type": "string",
            "title": "The seller_name_eng schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "sjh"
            ]
        },
        "seller_name": {
            "$id": "#/properties/seller_name",
            "type": "string",
            "title": "The seller_name schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "위코드"
            ]
        },
        "manager_name": {
            "$id": "#/properties/manager_name",
            "type": "string",
            "title": "The manager_name schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "와썹맨"
            ]
        },
        "seller_status": {
            "$id": "#/properties/seller_status",
            "type": "string",
            "title": "The seller_status schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "입점"
            ],
            "pattern": "^(입점대기|입점|휴점|퇴점대기|퇴점)$"
        },
        "manager_phone": {
            "$id": "#/properties/manager_phone",
            "type": "string",
            "title": "The manager_phone schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "010-1234-5678"
            ]
        },
        "manager_email": {
            "$id": "#/properties/manager_email",
            "type": "string",
            "title": "The manager_email schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "email"
            ]
        },
        "seller_attribute": {
            "$id": "#/properties/seller_attribute",
            "type": "string",
            "title": "The seller_attribute schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "뷰티"
            ],
            "pattern": "^(쇼핑몰|마켓|로드샵|디자이너브랜드|제너럴브랜드|내셔널브랜드|뷰티)$"
        },
        "view": {
            "$id": "#/properties/view",
            "type": "string",
            "title": "The view schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                10
            ],
            "pattern": "^(10|20|50|100|150)$"
        },
        "page": {
            "$id": "#/properties/page",
            "type": "string",
            "title": "The page schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                5
            ]
        }
    }
}

PRODUCT_FILTER_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "start_period": "2020-06-12",
            "end_period": "2020-07-02",
            "user_id": 1,
            "product_name": "상품",
            "product_id": "1",
            "code": "SB000000000000000009",
            "on_sale": "1",
            "on_list": "1",
            "discount": "1",
            "limit": "10",
            "offset": "0"
        }
    ],
    "required": [],
    "additionalProperties": True,
    "properties": {
        "start_period": {
            "$id": "#/properties/start_period",
            "type": ["string","null"],
            "title": "The start_period schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "2020-06-12"
            ]
        },
        "end_period": {
            "$id": "#/properties/end_period",
            "type": ["string","null"],
            "title": "The end_period schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "2020-07-02"
            ]
        },
        "user_id": {
            "$id": "#/properties/seller_name",
            "type": ["integer","null"],
            "title": "The seller_name schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                1
            ]
        },
        "product_name": {
            "$id": "#/properties/product_name",
            "type": ["string","null"],
            "title": "The product_name schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "상품"
            ]
        },
        "product_id": {
            "$id": "#/properties/product_id",
            "type": ["string", "null"],
            "title": "The product_id schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "1"
            ]
        },
        "code": {
            "$id": "#/properties/code",
            "type": ["string","null"],
            "title": "The code schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "SB000000000000000009"
            ]
        },
        "on_sale": {
            "$id": "#/properties/on_sale",
            "type": ["string","null"],
            "title": "The on_sale schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "1"
            ],
            "pattern": "^(0|1)$"
        },
        "on_list": {
            "$id": "#/properties/on_list",
            "type": ["string", "null"],
            "title": "The on_list schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "1"
            ],
            "pattern": "^(0|1)$"
        },
        "discount": {
            "$id": "#/properties/discount",
            "type": ["string", "null"],
            "title": "The discount schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "1"
            ],
            "pattern": "^(0|1)$"
        },
        "limit": {
            "$id": "#/properties/limit",
            "type": ["string", "null"],
            "title": "The limit schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "10"
            ],
            "pattern": "^(10|20|50)$"
        },
        "offset": {
            "$id": "#/properties/offset",
            "type": ["string", "null"],
            "title": "The offset schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "0"
            ]
        }
    }
}


PRODUCT_STATUS_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "product_code": "SB00000034534524",
            "on_sale": 0,
            "on_list": 1
        }
    ],
    "required": [
        "product_code",
        "on_sale",
        "on_list"
    ],
    "additionalProperties": True,
    "properties": {
        "product_code": {
            "$id": "#/properties/product_code",
            "type": "string",
            "title": "The product_code schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "SB00000034534524"
            ]
        },
        "on_sale": {
            "$id": "#/properties/on_sale",
            "type": [
                "integer",
                "null"
            ],
            "title": "The on_sale schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                0
            ],
            "pattern": "^(0|1)$"
        },
        "on_list": {
            "$id": "#/properties/on_list",
            "type": [
                "integer",
                "null"
            ],
            "title": "The on_list schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                1
            ]
        }
    }
}
