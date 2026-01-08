# -*- coding: utf-8 -*-
{
    'name': "comisiones_cima",

    'summary': """
        Comisiones para CIMA
    """,

    'description': """
        WIP Comisiones para CIMA
    """,

    'author': "Interfaces S.A., Gustavo Bazan",
    'website': "https://www.interfaces.com.py",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '2024.02.29.02',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'hr', 'picking_personalizacion', 'crm'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/comisiones.xml',
        'views/comisiones_detalles.xml',
        'views/grupos_comisiones.xml',
        'views/product_category.xml',
        'views/crm_team.xml',
    ],
}
