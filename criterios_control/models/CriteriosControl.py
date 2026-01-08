from odoo import _, exceptions, fields, models

class CriteriosControl(models.Model):
    _name = 'criterios.control'
    _description = 'Criterios de Control'

    name = fields.Char(string='Nombre', required=True)
    uom_control = fields.Char(string='Unidad de Medida')
