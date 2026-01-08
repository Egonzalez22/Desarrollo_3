# -*- coding: utf-8 -*-

from odoo import models, fields, api


class itabo_zonas(models.Model):
    _name = 'itabo_zonas.itabo_zonas'
    _description = 'itabo_zonas.itabo_zonas'

    name = fields.Char(string="Nombre", required=True)
    rutas_ids = fields.One2many('itabo_rutas.itabo_rutas', 'zonas_ids', string='Rutas')

