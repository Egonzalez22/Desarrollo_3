# -*- coding: utf-8 -*-
# from odoo import http


# class ItaboRutasZonas(http.Controller):
#     @http.route('/itabo_rutas_zonas/itabo_rutas_zonas', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/itabo_rutas_zonas/itabo_rutas_zonas/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('itabo_rutas_zonas.listing', {
#             'root': '/itabo_rutas_zonas/itabo_rutas_zonas',
#             'objects': http.request.env['itabo_rutas_zonas.itabo_rutas_zonas'].search([]),
#         })

#     @http.route('/itabo_rutas_zonas/itabo_rutas_zonas/objects/<model("itabo_rutas_zonas.itabo_rutas_zonas"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('itabo_rutas_zonas.object', {
#             'object': obj
#         })
