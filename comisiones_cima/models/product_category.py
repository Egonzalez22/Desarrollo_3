# -*- coding: utf-8 -*-

from odoo import _, api, exceptions, fields, models



class ProductCategory(models.Model):
    _inherit = 'product.category'

    es_comisionable = fields.Boolean(string='Es comisionable', default=False)