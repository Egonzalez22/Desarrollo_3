from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = "sale.order"
        
    vendedor_id = fields.Many2one('hr.employee', string="Vendedor")

    @api.onchange('partner_id')
    def vendedor_dato_ventas(self):
        for vendedor in self:
            vendedor.vendedor_id = vendedor.partner_id.vendedor_id

    def action_confirm(self):
        result = super(SaleOrder, self).action_confirm()
        for this in self:
            if this.partner_id.vendedor_id:
                this.vendedor_id = this.partner_id.vendedor_id

        return result
