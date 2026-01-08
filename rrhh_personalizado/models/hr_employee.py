from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
import datetime


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    @api.onchange('children_ids')
    def _get_underage_children_count(self, explicit_date=fields.date.today()):
        res = super(HrEmployee, self)._get_underage_children_count(explicit_date=fields.date.today())
        for this in self:
            underage_children_count = len([children for children in this.children_ids if children._get_age(explicit_date=explicit_date, return_age=True) < 18])
            this.underage_children_count = underage_children_count