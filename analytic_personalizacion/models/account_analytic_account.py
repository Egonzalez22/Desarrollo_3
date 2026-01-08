from odoo import api, fields, models


class AccountAnalyticAccount(models.Model):
    _inherit = 'account.analytic.account'

    almacenable_en_apunte = fields.Boolean(string="Almacenable en Apunte Contable")
