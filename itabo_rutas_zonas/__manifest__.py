# -*- coding: utf-8 -*-
{
    'name': "itabo_rutas_zonas",

    'summary': """
        Se agrega módulo de rutas y zonas""",

    'description': """
        Se agrega en clientes y presupuesto de ventas.
        tarea N°23.934 -  Se pasa modulo creado para itabo a cima
    """,

    'author': "Interfaces S.A.",
    'website': "http://www.interfaces.com.py",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '2024.02.26.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/zonas.xml',
        'views/rutas.xml',
        'views/res_partner.xml',
        'views/sale_order.xml',
        'views/sale_order_tree.xml',
        'views/stock_picking.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
