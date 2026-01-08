# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _, Command


# Lista de materiales
class MrpBom(models.Model):
    _inherit = 'mrp.bom.line'

    location_id = fields.Many2one('stock.location', "Desde", store=True)


    
# Lista de Subproductos
class MrpBom(models.Model):
    _inherit = 'mrp.bom.byproduct'

    location_dest_id = fields.Many2one('stock.location', "A", store=True)
