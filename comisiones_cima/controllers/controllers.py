# -*- coding: utf-8 -*-
# from odoo import http


# class ComisionesCima(http.Controller):
#     @http.route('/comisiones_cima/comisiones_cima', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/comisiones_cima/comisiones_cima/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('comisiones_cima.listing', {
#             'root': '/comisiones_cima/comisiones_cima',
#             'objects': http.request.env['comisiones_cima.comisiones_cima'].search([]),
#         })

#     @http.route('/comisiones_cima/comisiones_cima/objects/<model("comisiones_cima.comisiones_cima"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('comisiones_cima.object', {
#             'object': obj
#         })
