from odoo import _, exceptions, fields, models


class ProductMarca(models.Model):
    _name = 'product.marca'
    _description = 'Marcas del producto'

    company_id = fields.Many2one('res.company', string='Compañia', required=True, default=lambda self: self.env.company)
    code = fields.Char(string='Código', required=True)
    name = fields.Char(string='Nombre', required=True)
    active = fields.Boolean(string='Habilitado', default=True)

    _sql_constraints = [
        ('code_unique', 'unique(code)', 'El código debe ser único'),
    ]

    # No se puede eliminar una marca si tiene productos asociados
    def unlink(self):
        for marca in self:
            productos = self.env['product.template'].search([('marcas_ids', '=', marca.id)])
            if productos:
                raise exceptions.ValidationError(
                    _(f'No se puede eliminar la marca {marca.name} porque tiene productos asociados')
                )

        return super(ProductMarca, self).unlink()
