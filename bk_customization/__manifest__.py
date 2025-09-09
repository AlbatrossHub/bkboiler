# -*- coding: utf-8 -*-
{
    'name': 'BKB Customization',
    'version': '18.0.1.0.0',
    'category': 'Manufacturing',
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
    'depends': ['product'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_template_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}
