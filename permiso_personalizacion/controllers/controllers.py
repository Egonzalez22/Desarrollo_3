# -*- coding: utf-8 -*-
# from odoo import http


# class PermisoPersonalizacion(http.Controller):
#     @http.route('/permiso_personalizacion/permiso_personalizacion', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/permiso_personalizacion/permiso_personalizacion/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('permiso_personalizacion.listing', {
#             'root': '/permiso_personalizacion/permiso_personalizacion',
#             'objects': http.request.env['permiso_personalizacion.permiso_personalizacion'].search([]),
#         })

#     @http.route('/permiso_personalizacion/permiso_personalizacion/objects/<model("permiso_personalizacion.permiso_personalizacion"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('permiso_personalizacion.object', {
#             'object': obj
#         })
