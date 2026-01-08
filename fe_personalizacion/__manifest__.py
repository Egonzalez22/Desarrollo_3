# -*- coding: utf-8 -*-
{
    'name': "Facturación Electrónica Personalizacion",

    'summary': """
        Personalización de facturación electrónica para Cima
    """,

    'description': """
        - Se agrega campo para descripción corta del producto, en producto y lineas de factura
        - Se sobreescribe la forma de representar el monto unitario en letras para facturas USD
        - Se agrega información del lote en las lineas de facturas
        - 23959: Se quita filtro de contacto en nota de remision
    """,

    'author': "Interfaces S.A., Gustavo Bazan",
    'website': "https://www.interfaces.com.py",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '2024.03.13.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'sifen', 'facturacion_electronica_py', 'product', 'picking_personalizacion', 'notas_remision_account_stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/kude_factura.xml',
        'views/account_move_line.xml',
        'views/product_template.xml',
        'views/notas_remision.xml'
    ],
}
