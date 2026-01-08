# -*- coding: utf-8 -*-

from odoo import models, fields, api

class itabo_rutas(models.Model):
    _name = 'itabo_rutas.itabo_rutas'
    _description = 'itabo_rutas.itabo_rutas'
    
    name = fields.Char(string="Nombre", required=True)
    zonas_ids = fields.Many2many('itabo_zonas.itabo_zonas', string='Zonas')
