from odoo import api, fields, models, _

from odoo.exceptions import UserError, ValidationError

class StockPicking(models.Model):
    _inherit = "stock.picking"

    equipo_venta = fields.Many2one('crm.team', string="Equipo de venta")  
    sale_id = fields.Many2one('sale.order')  
    numero_factura = fields.Char(compute="_compute_invoice_related")
    monto_factura = fields.Monetary(compute="_compute_invoice_monto")
    numero_factura_sale = fields.Char(string="Nro de factura", compute="_compute_invoice_related", store = True)
    monto_factura_sale = fields.Monetary(string="Monto de factura", compute="_compute_invoice_monto", store = True)

    @api.onchange('location_dest_id')  
    def _compute_locations_dest_id(self): 
        print(f"busqueda3")
        for move_line in self:
            for c in move_line.move_line_ids:
                # print(f"busqueda3: {c.location_dest_id}")
                c.location_dest_id = move_line.location_dest_id  
                # print(f"busqueda1: {c.location_dest_id}")


    def _equipo_venta(self):
        for c in self.sale_id:
            self.equipo_venta = c.team_id


    
    def action_confirm(self):
        self._check_company()
        self.mapped('package_level_ids').filtered(lambda pl: pl.state == 'draft' and not pl.move_ids)._generate_moves()
        # call `_action_confirm` on every draft move
        self.move_ids.filtered(lambda move: move.state == 'draft')._action_confirm()

        # run scheduler for moves forecasted to not have enough in stock
        self.move_ids.filtered(lambda move: move.state not in ('draft', 'cancel', 'done'))._trigger_scheduler()
        self._equipo_venta()
        return True


    @api.depends('sale_id')
    def _compute_invoice_related(self):
        # for record in self:
        #     if record.sale_id.invoice_ids:
        #         x = []

        #         for c in record.sale_id.invoice_ids:
        #             if c.move_type == 'out_invoice' and c.state == 'posted' and c.payment_state != 'reversed':
        #                 if not len(x) == 1: 
        #                     x.append(c.payment_reference)
        #             else:
        #                 if not len(x) == 1: 
        #                     x.append('')
        #         record.numero_factura =  x[0]
        #         record.numero_factura_sale = record.numero_factura

        #     else:
        #         record.numero_factura = False
        #         record.numero_factura_sale = False
        ids_set =set()
        for record in self:
            if record.sale_id.invoice_ids:
                if len(record.sale_id.invoice_ids) > 1:
                    #primero controlamos si los ids tienen el mismo estado
                    for c in record.sale_id.invoice_ids:
                        if c.amount_total:
                            if c.move_type == 'out_invoice' and c.state == 'posted' and c.payment_state != 'reversed':
                                if not c.id in ids_set:
                                    ids_set.add(c.id)
                    #si tienen el mismo estado se agrega a ids_set para luego obtener el max id y eso mostrar como dato
                    if ids_set:
                        max_id =  max(ids_set) 
                        max_invoice = self.env['account.move'].browse(max_id)
                        record.numero_factura = max_invoice.payment_reference
                        record.numero_factura_sale = record.numero_factura
                    else:
                        record.numero_factura = 0
                        record.numero_factura_sale = record.numero_factura
                else:
                    for c in record.sale_id.invoice_ids:
                        print("ids_in factura: ", c.id)
                        if c.move_type == 'out_invoice' and c.state == 'posted' and c.payment_state != 'reversed':
                            if c.payment_reference:
                                record.numero_factura = c.payment_reference
                                record.numero_factura_sale = record.numero_factura
                            else:
                                record.numero_factura = 0
                                record.numero_factura_sale = record.numero_factura
                        else:
                            record.numero_factura = 0
                            record.numero_factura_sale = record.numero_factura

            else:
                record.numero_factura = False
                record.numero_factura_sale = False



    @api.depends('sale_id')
    def _compute_invoice_monto(self):
        ids_set =set()
        for record in self:
            if record.sale_id.invoice_ids:
                if len(record.sale_id.invoice_ids) > 1:
                    #primero controlamos si los ids tienen el mismo estado
                    for c in record.sale_id.invoice_ids:
                        if c.amount_total:
                            if c.move_type == 'out_invoice' and c.state == 'posted' and c.payment_state != 'reversed':
                                if not c.id in ids_set:
                                    ids_set.add(c.id)
                    #si tienen el mismo estado se agrega a ids_set para luego obtener el max id y eso mostrar como dato
                    if ids_set:
                        max_id =  max(ids_set) 
                        max_invoice = self.env['account.move'].browse(max_id)
                        record.monto_factura = max_invoice.amount_total
                        record.monto_factura_sale = record.monto_factura
                    else:
                        record.monto_factura = 0
                        record.monto_factura_sale = record.monto_factura
                else:
                    for c in record.sale_id.invoice_ids:
                        print("ids_in: ", c.id)
                        if c.move_type == 'out_invoice' and c.state == 'posted' and c.payment_state != 'reversed':
                            if c.amount_total:
                                record.monto_factura = c.amount_total
                                record.monto_factura_sale = record.monto_factura
                            else:
                                record.monto_factura = 0
                                record.monto_factura_sale = record.monto_factura
                        else:
                            record.monto_factura = 0
                            record.monto_factura_sale = record.monto_factura

            else:
                record.monto_factura = False
                record.monto_factura_sale = False
            
            


