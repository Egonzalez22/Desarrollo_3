from odoo import _, exceptions, fields, models,api, exceptions

class Qualitypoint(models.Model):
    _inherit = 'quality.point'

    criterio_parametro_id = fields.Many2many('criterios.parametros', string='Criterios')

    @api.onchange('product_ids')
    def _onchange_product_ids(self):
        domain = [('product_id', 'in', self.product_ids.ids)]
        return {'domain': {'criterio_parametro_id': domain}}
    
    
    