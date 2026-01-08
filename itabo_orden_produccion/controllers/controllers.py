# -*- coding: utf-8 -*-
# from odoo import http


# class ItaboOrdenProduccion(http.Controller):
#     @http.route('/itabo_orden_produccion/itabo_orden_produccion', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/itabo_orden_produccion/itabo_orden_produccion/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('itabo_orden_produccion.listing', {
#             'root': '/itabo_orden_produccion/itabo_orden_produccion',
#             'objects': http.request.env['itabo_orden_produccion.itabo_orden_produccion'].search([]),
#         })

#     @http.route('/itabo_orden_produccion/itabo_orden_produccion/objects/<model("itabo_orden_produccion.itabo_orden_produccion"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('itabo_orden_produccion.object', {
#             'object': obj
#         })
