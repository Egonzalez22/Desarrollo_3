from odoo import api, fields, models, _


class SaleReport(models.Model):
    _inherit = "sale.report"

    vendedor_id = fields.Many2one('hr.employee', string="Vendedor")

    def _select_sale(self):
        res = super(SaleReport, self)._select_sale()

        res += ", s.vendedor_id AS vendedor_id"

        return res


    def _from_sale(self):
        res = super(SaleReport, self)._from_sale()

        res += "INNER JOIN hr_employee hr on hr.id = s.vendedor_id"

        return res
    

    def _group_by_sale(self):
        res = super(SaleReport, self)._group_by_sale()

        res += ", s.vendedor_id"

        return res
