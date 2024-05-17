# -*- coding: utf-8 -*-

{
    'name': 'CRM Social Media',
    'version': '1.0',
    'sequence': 10,
    "author": "Adnielys Abday",
    'contributors': [
        'Adnielys Abday Rojas Tadeo <adnielys.rojas89@gmail.com>',
    ],
    'description': """
    """,
    'depends': ['crm', 'website'],
    "data": [
          'views/res_partner_view.xml',
          'views/website_customer_views.xml'
    ],

    'assets': {
        'web.assets_backend': [


        ]
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
