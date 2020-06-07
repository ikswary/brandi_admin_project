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
        "discount_rate",
        "discount_price",
        "discount_start",
        "discount_end",
        "min_sales_unit",
        "max_sales_unit",
        "tag"
    ],
    "additionalProperties": True,
    "properties": {
        "seller_id": {
            "$id": "#/properties/seller_id",
            "type": "integer",
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
