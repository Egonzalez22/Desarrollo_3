# -*- coding: utf-8 -*-
{
    'name': "rrhh_personalizado",

    'summary': """
        Recibo de salario formato ministerio de trabajo
        """,

    'description': """
        Tarea N° 20.722 - se agrega reporte de recibo de salario en formato del ministerio
                        - se modifican las reglas para cada columna del reporte
        Tarea N° 23.762 - se procede a quitar el titulo del reporte.
        Tarea N° 32.235 - se modifica funcion que calcula la bonificacion familiar, se pone menor a 18 años
        Tarea N° 23.620 - Se personaliza funcion de calculo de salario real en el informe de ips rei
                        - Se deja sin efecto el pedido del cliente, se comenta parte del codigo desarrollado.    

    """,

    'author': "Interfaces S.A. - Edgar Gonzalez",
    'website': "https://www.interfaces.com.py",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '2024.05.30.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'rrhh_payroll', 'rrhh_liquidacion', 'reportes_ministerio_trabajo_py', 'ips_rei_hr_payslip'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/hr_payroll.xml',
        'report/hr_payroll.xml',
        # 'report/notificacion_vacacion_comunicacion.xml',
        # 'report/notificacion_vacacion_recibo.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
