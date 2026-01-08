from odoo import api, fields, models
import ast
import json 

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    analytic_account_id = fields.Many2one('account.analytic.account', string="Cuenta analítica")

    @api.model_create_multi
    def create(self, vals):
        # Llama al método create del modelo padre
        records = super(AccountMoveLine, self).create(vals)
        for record in records:
            if record.analytic_distribution:
                contar = len(record.analytic_distribution)
                diccionario1 = record.analytic_distribution
                claves1 = diccionario1.keys()
                analitico = []
                for c in claves1:
                    cuenta = self.env['account.analytic.account'].search([('id','=',c)])
                    for cuenta in cuenta:
                        cod = cuenta.almacenable_en_apunte
                        if cod:
                            analitico.append(cuenta.id)
                

                print(f"analitico: ", analitico)    
                if len(analitico) == 1:
                    print(f"ENTRA: ")
                    cuentas = self.env['account.analytic.account'].search([('id','=',analitico)])

                    for cuenta in cuentas:
                        cod = cuenta.almacenable_en_apunte
                        if cod:
                            record.analytic_account_id = cuenta.id

        return records

    @api.model
    def actualizar_lineas(self):
        for record in self:
            if record.analytic_distribution:
                diccionario1 = record.analytic_distribution
                claves1 = diccionario1.keys()
                analitico = []
                for c in claves1:
                    filtro = self.env['account.analytic.account'].search([('id','=',c)])
                    for cuenta in filtro:
                        cod = cuenta.almacenable_en_apunte
                        if cod:
                            analitico.append(cuenta.id)

                if len(analitico) == 1:
                    cuentas = self.env['account.analytic.account'].search([('id','=',analitico)])

                    for cuenta in cuentas:
                        cod = cuenta.almacenable_en_apunte
                        if cod:
                            record.write({
                                'analytic_account_id' : cuenta.id
                            })

    

    @api.model
    def actualizar_analitico(self):
        for record in self:
            if record.move_id.journal_id.type == 'sale' and record.account_id.account_type in ('income','income_other','expense','expense_depreciation','expense_direct_cost'):
                if len(record.move_id.partner_id.category_id.ids) == 1:
                    consulta = self.env['account.analytic.distribution.model'].search([('partner_category_id','=',record.move_id.partner_id.category_id.id)])
                    record.write({
                            'analytic_distribution' : consulta.analytic_distribution
                        })
                else:
                    for cliente_categoria in record.move_id.partner_id.category_id.ids:
                        consulta = self.env['account.analytic.distribution.model'].search([('partner_category_id','=',cliente_categoria)])
                        if consulta:
                            record.write({
                                'analytic_distribution' : consulta.analytic_distribution
                            })
                    

                    
                


                        
    
