from odoo import api, fields, models

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    
    @api.onchange('product_id', 'product_qty')
    def _onchange_product_id(self):
        if self.product_id and self.move_raw_ids:
            bom_line_domain = [('bom_id', '=', self.bom_id.id)]
            byproduct_domain = [('bom_id', '=', self.bom_id.id)]
            bom_lines = self.env['mrp.bom.line'].sudo().search(bom_line_domain)
            byproducts = self.env['mrp.bom.byproduct'].sudo().search(byproduct_domain)

            for move in self.move_raw_ids:
                bom_line = bom_lines.filtered(lambda x: x.product_id == move.product_id)
                if bom_line:
                    move.location_id = bom_line.location_id.id
                else:
                    move.location_id = None
                    
            for movep in self.move_byproduct_ids:
                byproduct = byproducts.filtered(lambda x: x.product_id == movep.product_id)
                if byproduct:
                    movep.location_dest_id = byproduct.location_dest_id.id
                else:
                    movep.location_dest_id = None
                
class StockMove(models.Model):
    _inherit = 'stock.move'

    bom_line_id = fields.Many2one('mrp.bom.line', string="Línea de Lista de Materiales")