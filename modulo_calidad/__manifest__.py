# -*- coding: utf-8 -*-
{
    'name': "modulo_calidad",

    'summary': """
        
        Modulo Calidad
        
        """,

    'description': """
        Tarea N° 19335 - se agrego validacion de campos en modelo de punto del control de calidad (quality.point)}
        asi como un campo del modelo de criterios.parametros de tipo Many2many.

    """,

    'author': "Interfaces - Edgar Gonzalez",
    'website': "https://www.interfaces.com.py",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '2023.06.16.01',

    # any module necessary for this one to work correctly
    'depends': ['base', 'quality', 'quality_control'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/quality_point.xml',

    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
