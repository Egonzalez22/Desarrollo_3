# -*- coding: utf-8 -*-
from odoo import fields, models, _


class StockInventoryAdjustmentName(models.TransientModel):
    _inherit = 'stock.inventory.adjustment.name'

    def action_apply(self):
        # informes_inventario/wizard/stock_inventory_adjustment_name.py
        # action create on inventory header
        StockHistory = self.env['informes_inventario.stock_history']
        StockHistoryLine = self.env['informes_inventario.stock_history_line']

        stock_line = StockHistory.create({
            "name":self.inventory_adjustment_name,
            "company_id": self.env.company.id,
            "date": fields.Date.today()
        })

        for line in self.quant_ids:
            StockHistoryLine.create({
                "history_id": stock_line.id,
                "product_id": line.product_id.id,
                "quantity": line.quantity,
                "inventory_quantity": line.inventory_quantity,
                "inventory_diff_quantity": line.inventory_diff_quantity,
                "user_id": line.user_id.id,
                "location_id": line.location_id.id if line.location_id else False
            })

        res = super(StockInventoryAdjustmentName, self).action_apply()
        return res
