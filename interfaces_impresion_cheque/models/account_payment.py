from odoo import api, fields, models
from . import amount_to_text_spanish


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    print_count = fields.Integer(string='Contador de impresiones', copy=False)
    fecha_inicio_vencimiento = fields.Boolean(string='Fecha y Vencimiento igual', compute="_tipo_cheque")
    es_portador = fields.Boolean(string='Es cheque al portador', default=False, copy=False)

    @api.model
    def formatear_monto(self, monto, currency=False, lang=False):
        if not lang:
            lang_str = self._context.get('lang')
        else:
            lang_str = lang
        if not currency:
            currency_id = self.env.user.company_id.currency_id
        else:
            currency_id = currency
        lang_id = self.env['res.lang'].search([('code', '=', lang_str)])

        if lang_id and currency_id:
            fmt = "%.{0}f".format(currency_id.decimal_places)
            return lang_id.format(fmt, monto, grouping=True)
        else:
            return '{:.6f}'.format(monto)

    def amount_to_text(self, amount, currency):
        convert_amount_in_words = amount_to_text_spanish.to_word(amount)
        return convert_amount_in_words

    def _tipo_cheque(self):
        for i in self:
            if i.fecha_cheque == i.fecha_vencimiento_cheque:
                self.update({'fecha_inicio_vencimiento': True})
            else:
                self.update({'fecha_inicio_vencimiento': False})

    def print_cheque_vista(self):
        self.print_count += 1
        return self.env.ref('interfaces_impresion_cheque.cheque_vista_action').report_action(self)

    def print_cheque_diferido(self):
        self.print_count += 1
        return self.env.ref('interfaces_impresion_cheque.cheque_diferido_action').report_action(self)

    def permitir_reimpresion(self):
        self.print_count = 0

    def print_cheque_vista_itau_sudameris(self):
        self.print_count += 1
        return self.env.ref('interfaces_impresion_cheque.cheque_itau_sudameris_vista_action').report_action(self)
    

    def print_cheque_vista_vision(self):
        self.print_count += 1
        return self.env.ref('interfaces_impresion_cheque.cheque_vision_vista_action').report_action(self)

    def print_cheque_diferido_v2(self):
        self.print_count += 1
        return self.env.ref('interfaces_impresion_cheque.cheque_diferido_v2_action').report_action(self)
