# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockHistory(models.Model):
    _name = 'informes_inventario.stock_history'
    _description = 'Cabecera para stock quant'

    name = fields.Char(string='Nombre')
    line_ids = fields.One2many('informes_inventario.stock_history_line', 'history_id', string='Line Ids')
    date = fields.Date('Fecha')
    company_id = fields.Many2one('res.company', string='Compañía')


class StockHistoryLine(models.Model):
    _name = 'informes_inventario.stock_history_line'
    _description = 'Cabecera para stock quant'

    name = fields.Char(string='Nombre')
    history_id = fields.Many2one('informes_inventario.stock_history', string='Historico de Inventairo')
    product_id = fields.Many2one('product.product')
    quantity = fields.Float("Cantidad a mano")
    inventory_quantity = fields.Float("Cantidad contada")
    inventory_diff_quantity = fields.Float("Diferencia")
    user_id = fields.Many2one('res.users')
    invetory_value = fields.Float("Valor unitario")
    location_id = fields.Many2one('stock.location', string="Ubicacion")

    def create(self, vals):
        res = super(StockHistoryLine, self).create(vals)
        res.invetory_value = res.product_id.standard_price
        return res


