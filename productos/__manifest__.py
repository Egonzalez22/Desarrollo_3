# -*- coding: utf-8 -*-
{
    'name': "productos_custom",

    'summary': """
        Modulo para personalizar datos relacionados a productos
        """,

    'description': """
        1 - Creación de tabla Marcas (ID, Name, Active)
        2 - En Productos, agregar campo Marca (Many2Many)
    """,

    'author': "Interfaces",
    'website': "https://www.interfaces.com.py",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '2023.06.08.01',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/product_marca.xml',
        'views/product_template.xml',
    ],
}
