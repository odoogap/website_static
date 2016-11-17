# -*- coding: utf-8 -*-
{
    'name': 'Static Website Publishing',
    'version': '1.0',
    'author': 'OdooGap.com',
    'summary': 'Static Website Publishing for Odoo',
    'description': """
Static Website Publishing
=========================
Static Website Publishing Engine for Odoo


    """,
    'website': 'http://www.odoogap.com',
    'depends': ['website'],
    'category': 'Website',
    'demo': [
    ],
    'data': [
        'views/website_static.xml',
        'res_config.xml',
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
