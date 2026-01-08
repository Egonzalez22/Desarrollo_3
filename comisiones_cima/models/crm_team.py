from odoo import api, fields, models, _
from odoo.exceptions import UserError


class CrmTeam(models.Model):
    _inherit = "crm.team"

    calcular_objetivos = fields.Boolean(string="Calcular Objetivos", default=True)
