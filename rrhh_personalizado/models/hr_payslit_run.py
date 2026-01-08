
from odoo import models, fields, api
import datetime



class PartnerXlsx(models.AbstractModel):
    _inherit = 'report.ips_rei_hr_payslip.xlsx_report'


    # def get_salario_real(self, payslips_employee):
    #     salario_real = 0
    #     total_patronal = 0
    #     s_imponible = self.get_salario_imponible(payslips_employee)

    #     for patronal in payslips_employee.line_ids:
    #         if patronal.code == 'IPS':
    #             total_patronal += patronal.total

    #     if total_patronal:
    #         salario_real = s_imponible-total_patronal
    #     else:
    #         salario_real = self.get_salario_imponible(payslips_employee)   
            
        
    #     return salario_real
