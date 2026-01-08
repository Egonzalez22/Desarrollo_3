# -*- coding: utf-8 -*-
{
    'name': "informes_inventario",

    'summary': """
        Agrega reporte para historico de ajustes de stock en
        Inventario/Informes/Informe de Ajustes de inventario
    """,

    'description': """
        Agrega reporte para historico de ajustes de stock en
        Inventario/Informes/Informe de Ajustes de inventario

         - Guarda el histórico con el nombre de referencia del ajuste de inventario cuando se procesan varias lineas
         - Permite seleccionar las referencias y especificar la categoría de productos a la hora de imprimir el reporte
        Tarea N° 23.951 -  se copia modulo de regimiento 8 a cima

    """,

    'author': "Interfaces S.A.",
    'website': "http://www.interfaces.com.py",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Stock',
    'version': '2024.05.27.01',

    # any module necessary for this one to work correctly
    'depends': ['base','stock', 'account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'report/informe_ajustes.xml',
        'views/views.xml',
        'views/templates.xml',
        'data/data.xml',
        'wizard/informe_ajuste_inventario.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
