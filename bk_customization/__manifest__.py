# -*- coding: utf-8 -*-
{
    'name': 'BKB Customization',
    'version': '1.0',
    'category': 'Manufacturing/Manufacturing',
    'summary': 'Custom fields for boiler manufacturing specifications',
    'description': """
BKB Customization
=================
This module adds custom fields to product.template for boiler manufacturing company:

- SPECIFICATION
- MODEL NO.
- SIZE
- SCH.
- CLASS
- LONG
- RANGE
- REF. NO.
- MAKE
- PRESS.
- TEMP.
- HEAD
- FLOW
- HP
- KW
- RPM

These fields are displayed in a dedicated "BKB Specs" section in the product form view.
    """,
    'author': 'BKB Boiler Manufacturing',
    'website': '',
    'depends': ['product', 'purchase'],
    'data': [
        'views/product_template_views.xml',
        'views/purchase_view.xml',
        'views/mrp_views.xml',
        'views/mrp_report.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}
