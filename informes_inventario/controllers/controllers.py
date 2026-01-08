# -*- coding: utf-8 -*-
# from odoo import http


# class InformesInventario(http.Controller):
#     @http.route('/informes_inventario/informes_inventario', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/informes_inventario/informes_inventario/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('informes_inventario.listing', {
#             'root': '/informes_inventario/informes_inventario',
#             'objects': http.request.env['informes_inventario.informes_inventario'].search([]),
#         })

#     @http.route('/informes_inventario/informes_inventario/objects/<model("informes_inventario.informes_inventario"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('informes_inventario.object', {
#             'object': obj
#         })
