from odoo import _, exceptions, fields, models, api

class CriteriosParametros(models.Model):
    _name = 'criterios.parametros'
    _description = 'Criterios y Parametros'

    criterio_control_id =  fields.Many2one('criterios.control', string='Criterio',required=True)
    # uom_control_id = fields.Many2one('uom.category', string='Unidad de Medida')
    uom_control = fields.Char(string='Unidad de Medida')
    valor_min = fields.Float(string='Valor Minimo')
    valor_max = fields.Float(string='Valor Máximo')
    name = fields.Char()
    product_id =  fields.Many2one('product.product', string='Producto')

    
    @api.model
    def create(self, vals):
        if vals.get('criterio_control_id') and vals.get('uom_control_id'):
            criterio_control = self.env['criterios.control'].browse(vals['criterio_control_id'])
            vals['name'] = f"{criterio_control.name}"
        return super(CriteriosParametros, self).create(vals)

    @api.onchange('criterio_control_id')
    def dato_unidad(self):
        for record in self:
           record.uom_control =  record.criterio_control_id.uom_control