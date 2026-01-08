from odoo import fields, api, models, exceptions, _
import pytz


class HrEmployeeBase(models.AbstractModel):
    _inherit = 'hr.employee.base'

    es_vendedor =  fields.Boolean(string='Es vendedor', default=False)
