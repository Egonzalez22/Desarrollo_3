# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    marcas_ids = fields.Many2many('product.marca', string='Marcas')
