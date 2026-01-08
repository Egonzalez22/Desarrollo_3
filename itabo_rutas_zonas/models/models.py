# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class itabo_rutas_zonas(models.Model):
#     _name = 'itabo_rutas_zonas.itabo_rutas_zonas'
#     _description = 'itabo_rutas_zonas.itabo_rutas_zonas'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
