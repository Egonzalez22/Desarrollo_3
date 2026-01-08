from odoo import api, fields, models, exceptions

class AccountPayment(models.Model):
    _inherit = "account.payment"

    cobrador_id = fields.Many2one('hr.employee', string="Cobrador")
    usuario = fields.Many2one('res.users', string="Usuario")


    @api.model
    def create(self, vals_list):
        record = super(AccountPayment, self).create(vals_list)
        cobrador_id = vals_list.get('cobrador_id', False)
        tipo_pago = vals_list.get('tipo_pago', False)
        if cobrador_id:
            self.cobrador_id = cobrador_id
        
        if tipo_pago:
            self.tipo_pago = tipo_pago

        for c in record:
            usuario_n = self.env.user  
            c.usuario = usuario_n.id
            
        return record