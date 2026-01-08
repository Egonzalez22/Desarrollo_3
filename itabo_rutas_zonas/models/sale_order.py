# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrders(models.Model):
    _inherit = 'sale.order'
       
    zona_ids = fields.Many2one('itabo_zonas.itabo_zonas', string='Zona', compute='_compute_zona_ids', store=True)
    ruta_ids = fields.Many2many('itabo_rutas.itabo_rutas', string='Ruta', compute='_compute_ruta_ids', store=True)

    @api.depends('partner_id.zonas_ids', 'partner_id.zonas_ids.rutas_ids')
    def _compute_zona_ids(self):
        for order in self:
            order.zona_ids = order.partner_id.zonas_ids
    
    @api.depends('zona_ids.rutas_ids')
    def _compute_ruta_ids(self):
        for order in self:
            order.ruta_ids = order.zona_ids.rutas_ids
