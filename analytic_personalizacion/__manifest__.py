# -*- coding: utf-8 -*-
{
    'name': "analytic_personalizacion",

    'summary': """
        Campos personalizados en Account.analytic
    """,

    'description': """
        Tarea N° 21.653 - se crearon campos nuevos segun indicaciones de la tarea - 
        función de almacenar cuenta analítica en apunte contable
        Se actualiza funcion que controla y almacena la cuenta analitica
        Tarea N° 23.836 - se crea funcion que se llama desde una accion planificada, 
        segun indicaciones de la tarea
    """,

    'author': "Interfaces S.A. -  Edgar Gonzalez",
    'website': "https://www.interfaces.com.py",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '2024.03.15.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/account_analytic_account.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
