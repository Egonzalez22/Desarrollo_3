# -*- coding: utf-8 -*-
{
    'name': "itabo_orden_produccion",

    'summary': """
        Módulo para permitir la selección de depositos en la lista de materiales y desde orden de producción """,

    'description': """
        Módulo para permitir la selección de depositos en la lista de materiales y desde orden de producción.
    """,

    'author': "Interfaces S.A.",
    'website': "https://www.interfaces.com.py",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '2024.03.25.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mrp'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/mrp_productionForm.xml',
        'views/mrp_bom_form.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
