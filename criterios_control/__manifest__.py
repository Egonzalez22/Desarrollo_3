# -*- coding: utf-8 -*-
{
    'name': "criterios_control",

    'summary': """
        Modulo para crear ABM de nuevo modelo creado para el modulo de Calidad.
        """,

    'description': """
        Tarea N° 19.322  -  Se crea ABM para el modelo de criterios.control, segun lo solicitado en la tarea
        Tarea N° 19.323 -  Se crea ABM para el modelo de criterios.parametros, segun lo solicitado en la tarea
        se modifico el nombre para el acceso al abm en el menu

    """,

    'author': "Interfaces - Edgar Gonzalez",
    'website': "https://www.interfaces.com.py",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '2023.11.16.01',

    # any module necessary for this one to work correctly
    'depends': ['base', 'quality', 'quality_control'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/criterio_control.xml',
        'views/criterio_parametros.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
