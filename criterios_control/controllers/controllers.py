# -*- coding: utf-8 -*-
# from odoo import http


# class CriteriosControl(http.Controller):
#     @http.route('/criterios_control/criterios_control', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/criterios_control/criterios_control/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('criterios_control.listing', {
#             'root': '/criterios_control/criterios_control',
#             'objects': http.request.env['criterios_control.criterios_control'].search([]),
#         })

#     @http.route('/criterios_control/criterios_control/objects/<model("criterios_control.criterios_control"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('criterios_control.object', {
#             'object': obj
#         })
