# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloCalidad(http.Controller):
#     @http.route('/modulo_calidad/modulo_calidad', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_calidad/modulo_calidad/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_calidad.listing', {
#             'root': '/modulo_calidad/modulo_calidad',
#             'objects': http.request.env['modulo_calidad.modulo_calidad'].search([]),
#         })

#     @http.route('/modulo_calidad/modulo_calidad/objects/<model("modulo_calidad.modulo_calidad"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_calidad.object', {
#             'object': obj
#         })
