import json
import math

from odoo import _, api, exceptions, fields, models
from odoo.exceptions import AccessError, RedirectWarning, UserError, ValidationError

from .amount_to_text import to_word


class AccountMove(models.Model):
    _inherit = 'account.move'


    def amount_to_text(self, amount, currency=False):
        # fe_personalizacion/amount_to_text.py
        # Personalizamos la forma de escribir el monto en letras en USD
        convert_amount_in_words = to_word(amount)
        return convert_amount_in_words