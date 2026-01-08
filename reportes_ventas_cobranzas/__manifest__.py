# -*- coding: utf-8 -*-
{
    'name': "reportes_ventas_cobranzas",

    'summary': """
        Reporte de Ventas y Cobranzas
    """,

    'description': """
        Reporte de Ventas y Cobranzas.
        Tarea N° 23.602  se trae reporte cobranza compra venta de lockers
                    - se agrega campos nuevos y filtros nuevos, se ajusta el reporte a segun notas dejada en la tarea.
                    - se quita resumen por tipo de pago del reporte y se modifica totales
                    - se agrega datos de cobrador y usuario en reporte y reducir tamaño de letra
        Tarea N° 23.163  -  se agregan campos nuevos en account.payment segun indicacion de la tarea    
        Tarea N° 26.065 - Se procedio a modificar condicion en reporte de cobranzas
     

    """,

    'author': "Interfaces S.A.",
    'website': "http://www.interfaces.com.py",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '2024.05.06.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/accountpayment.xml',
        'views/account_payment_register.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
