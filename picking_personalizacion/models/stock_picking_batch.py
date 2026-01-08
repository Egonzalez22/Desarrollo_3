from odoo import api, fields, models, _


class StockPickingBatch(models.Model):
    _inherit = "stock.picking.batch"

    repartidor = fields.Many2one('hr.employee', string="Repartidor")
    location_id = fields.Many2one('stock.location', string="Ubicacion origen")
    location_dest_id = fields.Many2one('stock.location', string="Ubicacion destino",
                                       compute='_compute_locations_dest_id',
                                       store=True, )
    total_factura = fields.Float(string="Total Factura", compute='_compute_total_factura')
    total = fields.Float(string="Total Factura", compute='_compute_total_factura', store=True)
    
    @api.onchange('location_dest_id')
    def _compute_locations_dest_id(self):
        for batch in self:
            for move_line in batch.move_line_ids:
                move_line.ensure_one()
                if batch.location_dest_id: move_line.location_dest_id = batch.location_dest_id.id


    def _compute_total_factura(self):

        for batch in self:
            factura_monto = []
            calculo = 0
            for picking in batch.picking_ids:
                factura_num = picking.numero_factura
                if factura_num not in factura_monto:
                    factura_monto.append(factura_num)
                    calculo += picking.monto_factura
            
            batch.total_factura = calculo
            batch.total = calculo
