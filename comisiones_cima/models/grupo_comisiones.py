# -*- coding: utf-8 -*-

from odoo import api, exceptions, fields, models

COMISION_BASE = 5

class GrupoComision(models.Model):
    _name = 'grupo_comision'

    name = fields.Char(string='Nombre', store=True)
    company_id = fields.Many2one('res.company', string='Compañia', required=True, default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency', string='Moneda', required=True, related='company_id.currency_id')
    line_ids = fields.One2many('grupo_comision_line', 'grupo_id', string='Detalle de comisiones por categoría')
    vendedor_ids = fields.Many2many('hr.employee', string='Vendedores', domain=[('es_vendedor', '=', True)])
    meta_objetivo_1 = fields.Monetary(string='Meta objetivo 1')
    meta_objetivo_2 = fields.Monetary(string='Meta objetivo 2')

    def generar_lineas(self):
        """
        Obtenemos todas las categorías comisionables y creamos las lineas del grupo de comision
        """

        # Verificamos si ya existen lineas
        if self.line_ids:
            raise exceptions.UserError('Ya existen lineas en este grupo de comisión. Debe borrarlas antes de generar nuevas lineas.')

        # Obtenemos todas las categorías comisionables
        categorias = self.env['product.category'].search([('es_comisionable', '=', True)])

        # Creamos las lineas
        for categoria in categorias:
            self.env['grupo_comision_line'].create(
                {
                    'grupo_id': self.id,
                    'category_id': categoria.id,
                    'comision_base': COMISION_BASE,
                }
            )


class GrupoComisionLine(models.Model):
    _name = 'grupo_comision_line'

    grupo_id = fields.Many2one('grupo_comision', string='Grupo de comisión')
    company_id = fields.Many2one('res.company', string='Compañia', required=True, default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency', string='Moneda', required=True, related='company_id.currency_id')

    category_id = fields.Many2one('product.category', string='Categoría', required=True, domain=[('es_comisionable', '=', True)])
    objetivo_1 = fields.Monetary(string='Objetivo 1')
    objetivo_2 = fields.Monetary(string='Objetivo 2')
    comision_base = fields.Float(string='Comisión Base', digits=(16, 2))
    es_activador = fields.Boolean(string='Producto activador', default=False)
    es_tercerizado = fields.Boolean(string='Producto tercerizado', default=False)

    @api.onchange('objetivo_1', 'objetivo_2')
    def actualizar_objetivos_meta(self):
        """
        Actualizamos los objetivos del grupo de comisiones cuando cambian las lineas
        """
        for record in self:
            # Obtenemos la suma de todas las lineas
            record.grupo_id.meta_objetivo_1 = sum(record.grupo_id.line_ids.mapped('objetivo_1'))
            record.grupo_id.meta_objetivo_2 = sum(record.grupo_id.line_ids.mapped('objetivo_2'))
