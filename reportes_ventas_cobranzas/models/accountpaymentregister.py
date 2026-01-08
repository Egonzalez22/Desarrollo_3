from odoo import api, fields, models, exceptions

class AccountPaymentRegister(models.TransientModel):
    _inherit = "account.payment.register"

    cobrador_id = fields.Many2one('hr.employee', string="Cobrador")
    usuario = fields.Many2one('res.users', string="Usuario")

    def _create_payment_vals_from_wizard(self, batch_result):
        payment_vals = super(AccountPaymentRegister, self)._create_payment_vals_from_wizard(batch_result)
        payment_vals.update({
            'cobrador_id': self.cobrador_id.id,
            'tipo_pago':self.tipo_pago
        })

        return payment_vals


    def _create_payment_vals_from_batch(self, batch_result):
        payment_vals = super(AccountPaymentRegister, self)._create_payment_vals_from_batch(batch_result)
        payment_vals.update({
            'cobrador_id': self.cobrador_id.id,
            'tipo_pago':self.tipo_pago
        })


        return payment_vals


    @api.model
    def create(self, vals):
        record = super(AccountPaymentRegister, self).create(vals)
        for c in record:
            usuario_n = self.env.user  
            c.usuario = usuario_n.id
            
        return record
