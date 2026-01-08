from odoo import api, fields, models, _


class Respartner(models.Model):
    _inherit = "res.partner"
        
    vendedor_id = fields.Many2one('hr.employee', string="Vendedor")
    no_comisionable = fields.Boolean(string="Cliente no comisionable")

    @api.onchange('team_id')
    def vendedor_dato(self):
        for vendedor in self:
            vendedor.vendedor_id = vendedor.team_id.vendedor



    @api.model
    def agregar_vendedor(self): 
        for record in self:
            if not record.no_comisionable and record.team_id:
                if record.team_id.vendedor:
                    record.write({
                                'vendedor_id' : record.team_id.vendedor
                            })
