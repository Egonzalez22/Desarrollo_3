# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'
       
    zona_ids = fields.Many2one('itabo_zonas.itabo_zonas', string='Zona', compute='_compute_zona_ids', store=True)
    ruta_ids = fields.Many2many('itabo_rutas.itabo_rutas', string='Ruta', compute='_compute_ruta_ids', store=True)
    sale_id = fields.Many2one('sale.order', string='Sale Order')

    @api.depends('sale_id.zona_ids')
    def _compute_zona_ids(self):
        for picking in self:
            if picking.sale_id:
                picking.zona_ids = picking.sale_id.zona_ids
            else:
                picking.zona_ids = False

    @api.depends('zona_ids')
    def _compute_ruta_ids(self):
        for picking in self:
            if picking.zona_ids:
                picking.ruta_ids = picking.zona_ids.rutas_ids.ids
            else:
                picking.ruta_ids = False
