from odoo import api, fields, models, exceptions,_
from odoo.exceptions import UserError


class AccountMove(models.Model):
    _inherit = "account.move"

    vendedor = fields.Many2one('hr.employee', string="Vendedor")


    @api.onchange('partner_id')
    def vendedor_dato_account_move(self):
        for vendedor in self:
            vendedor.vendedor = vendedor.partner_id.vendedor_id


    def action_post(self):
        result = super(AccountMove, self).action_post()
        for this in self:
            if not this.vendedor:
                this.vendedor = this.partner_id.vendedor_id
            
            if this.move_type in ['in_invoice']:
                # Verificamos si el campo "ref" está en blanco
                if not this.ref:
                    raise exceptions.ValidationError('El campo "Numero de Factura" es requerido.')
                if not this.timbrado_id:
                    raise exceptions.ValidationError('El campo "Timbrado" es requerido.')

        return result

    @api.model
    def create(self, vals):
        record = super(AccountMove, self).create(vals)
        for c in record:
            if c.move_type == 'out_invoice':
                cliente = c.partner_id.vendedor_id
                if cliente:
                    c.vendedor = cliente.id
                
        return record