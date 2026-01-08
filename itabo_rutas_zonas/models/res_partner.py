# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _, Command


class ResPartner(models.Model):
    _inherit = 'res.partner'

    zonas_ids=fields.Many2one('itabo_zonas.itabo_zonas',string='Zona de Ruta')