# -*- coding: utf-8 -*-
# from odoo import http


# class AnalyticPersonalizacion(http.Controller):
#     @http.route('/analytic_personalizacion/analytic_personalizacion', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/analytic_personalizacion/analytic_personalizacion/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('analytic_personalizacion.listing', {
#             'root': '/analytic_personalizacion/analytic_personalizacion',
#             'objects': http.request.env['analytic_personalizacion.analytic_personalizacion'].search([]),
#         })

#     @http.route('/analytic_personalizacion/analytic_personalizacion/objects/<model("analytic_personalizacion.analytic_personalizacion"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('analytic_personalizacion.object', {
#             'object': obj
#         })
