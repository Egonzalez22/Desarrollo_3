# -*- coding: utf-8 -*-
# from odoo import http


# class PickingPersonalizacion(http.Controller):
#     @http.route('/picking_personalizacion/picking_personalizacion', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/picking_personalizacion/picking_personalizacion/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('picking_personalizacion.listing', {
#             'root': '/picking_personalizacion/picking_personalizacion',
#             'objects': http.request.env['picking_personalizacion.picking_personalizacion'].search([]),
#         })

#     @http.route('/picking_personalizacion/picking_personalizacion/objects/<model("picking_personalizacion.picking_personalizacion"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('picking_personalizacion.object', {
#             'object': obj
#         })
