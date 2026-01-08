# -*- coding: utf-8 -*-
{
    'name': "picking_personalizacion",

    'summary': """
        picking_personalizacion
    """,

    'description': """
       Tarea N° 22.925 -  Se crea reporte de orden de trabajo.
                Se agrega campo nuevo y nuevos datos en reporte de orden de reparto.
       Tarea N° 22.930 - se agrega campo de vendedor a varias vistas segun pedido de la tarea
                       - se agrega dentro de la funcion de action_post para que asigne el vendedor una vez que se carga desde ventas
                       
       Tarea N° 23.093  - Se crea funcion para que tome el cambio de ubicacion destino para que se aplique 
                        a las lineas 
        Tarea N° 23.094 - cambios en reporte de reparto
        Tarea N° 23.095 - se crea reporte de orden de carga en modulo 
        Tarea N° 22.924 -  se agrega campo en stock.picking de equipo de venta
        - Se agrega campo de 'es_vendedor' en hr.employee
        Tarea N°22.995 - se hereda funcion de create de account.move para agregar vendedor 
                       - se crea campo nuevo en contactos   
                       - se crea funcion para accion planificada 
        Tarea N°23537 - se agrega funcion de control de numero factura y numero de timbrado
        Tarea N°23768 - se crea campos segun indicaciones de la tarea
        Tarea N°23.771 - se realizan cambios en reporte de orden resumen segun indicacion de la tarea
        Tarea N°23.770 -  se agrega un campo en el reporte de pedido de compras segun indicacion en la tarea
        Tarea N°23.960 -  se procede a mostrar campos calculados en las vistas del picking
        Tarea N° 24.315 - se agrega control de estado para mostrar monto y numeor de factura dentro de picking
                        - se corrige error en montos de facturas que mostraba mal dentro de agrupacion de albaranes
                        - se agrega nuevos controles los cuales se definieron en la tarea
        Tarea N°23.772  - se agrga columna nueva en reporte y una funcion que verifique la cantidad de paquetes y unidades para 
                        la parte de carga
                        - modificacion en funcion que remplaza ultimos numeros decimales de la cantidad pedida del producto
        Tarea N°32.370 -Se procede a agregar campo de vendedor en el informe de ventas
    """,

    'author': "Interfaces - Edgar Gonzalez",
    'website': "https://www.interfaces.com.py",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '2024.05.30.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock_picking_batch', 'sales_team', 'sale', 'hr', 'stock','interfaces_tools',
                'purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'report/orden_reparto.xml',
        'views/crm_team.xml',
        'views/account_move.xml',
        'views/sale_order.xml',
        'views/res_partner.xml',
        'views/stock_picking_batch.xml',
        'report/orden_reparto_resumen.xml',
        'report/reporte_lotes.xml',
        'views/stock_picking.xml',
        'views/hr_employee.xml',
        'report/pedido_compras.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
