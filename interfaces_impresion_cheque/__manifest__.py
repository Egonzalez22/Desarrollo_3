# -*- coding: utf-8 -*-
{
    'name': "Impresion de Cheques",

    'summary': """
         Formato de impresion de Cheques PY""",

    'description': """
        Impresion de cheques, con permisos para imprimir y contador de impresiones.
        Tarea N° 22.959:
            Se corrige formato de Cheque tipo a la vista
            Se corrige formato de Cheque tipo Diferido
            Se crea personalizaciones por banco
            Tarea N°23 127 - se corrige en cheque al portador segun indicaciones de la tarea
            Tarea N°39 694 - se corrige espacio en fechas para cheques diferidos

    """,

    'author': "Interfaces S.A.",
    'website': "http://www.interfaces.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Account',
    'version': '2024.06.05.01',

    # any module necessary for this one to work correctly
    'depends': ['base','account','interfaces_payment'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/data.xml',
        'views/account_payment.xml',
        'views/template_cheque.xml',
        'views/cheque_sudameris_ita_vista.xml',
        'views/cheque_vision_vista.xml',
        'views/cheque_diferido.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
