
from odoo import fields, models, _


class StockInventoryAdjustmentName(models.TransientModel):
    _inherit = 'stock.inventory.adjustment.name'

    def _default_inventory_adjustment_name(self):
        return self.sudo().env['ir.sequence'].next_by_code('secuencia_inventario')

    inventory_adjustment_name = fields.Char(default=_default_inventory_adjustment_name)

