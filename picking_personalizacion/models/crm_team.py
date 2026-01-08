from odoo import api, fields, models, _
from odoo.exceptions import UserError


class CrmTeam(models.Model):
    _inherit = "crm.team"

    vendedor = fields.Many2one('hr.employee', string="Vendedor")
