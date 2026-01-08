# -*- coding: utf-8 -*-
import json
from datetime import datetime

from odoo import models, fields, api


class WizardInformeAjusteInventario(models.TransientModel):
    _name = 'inventario.wizard'

    # fecha_inicio = fields.Date(string='Fecha Inicio', required=True)
    # fecha_fin = fields.Date(string='Fecha Fin', required=True)
    nro_ajuste = fields.Char(string="Nro de ajuste", compute="genera_secuencia_inv")
    company_id = fields.Many2one('res.company', required=True, default=lambda self: self.env.company, string="Compañia")
    stock_history = fields.Many2many('informes_inventario.stock_history', required=True, string="Historico de ajuste")
    # product_categ_id = fields.Many2one('product.category', string="Categoria de Producto")
    product_categ_ids = fields.Many2many('product.category', string="Categorías de Producto")
    mostrar_dif_cero = fields.Boolean('Mostrar registros con diferencia cero', default=True)
    location_id = fields.Many2one('stock.location', string="Ubicacion")

    def genera_secuencia_inv(self):
        secuencia = self.env['ir.sequence'].search([('name', '=', 'secuencia_inventario')])
        self.nro_ajuste = secuencia.number_next_actual

    def print_report(self):
        data = {
            # 'fecha_inicio': self.fecha_inicio,
            # 'fecha_fin': self.fecha_fin,
            'company_id': self.company_id.id,
            'stock_histoy_id': self.stock_history,
            # 'stock_histoy_id':self.stock_history.id,
            # 'product_categ_id':self.product_categ_id.id,
            'product_categ_ids': self.product_categ_ids,
            'mostrar_dif_cero': self.mostrar_dif_cero,
            'ubicacion': self.location_id.id if self.location_id else False,
            # 'nro_ajuste': self.sudo().env['ir.sequence'].next_by_code('secuencia_inventario')
        }
        return self.env.ref('informes_inventario.informe_ajuste_inventario_action').report_action(self, data=data)


class ReportInformeIntn(models.AbstractModel):
    _name = 'report.informes_inventario.informe_ajuste_inventario'

    def _get_report_values(self, docids, data=None):
        # stock_history = self.env['informes_inventario.stock_history'].search([('id','=',data.get('stock_histoy_id'))])
        # histoy_lines = stock_history.line_ids
        aidis = data.get('stock_histoy_id').split('(')[-1].split(')')[0].split(',')
        aidis2 = []
        for ide in aidis:
            if ide:
                aidis2.append(int(ide.strip()))
        stock_history = self.env['informes_inventario.stock_history'].browse(aidis2)
        if len(stock_history) > 1:
            nro_ajuste = ','.join(stock_history.mapped('name'))
        else:
            nro_ajuste = ' '.join(stock_history.mapped('name'))
        histoy_lines = stock_history.mapped('line_ids')
        if not data.get('mostrar_dif_cero'):
            histoy_lines = histoy_lines.filtered(lambda x: x.inventory_diff_quantity > 0)
        listado_nombres = stock_history.mapped('name')
        listado_fechas = stock_history.mapped('date')
        # category = self.env['product.category'].browse(data.get('product_categ_id'))
        categ_ids = data.get('product_categ_ids').split('(')[-1].split(')')[0].split(',')
        categ_ids2 = []
        for categ in categ_ids:
            if categ:
                categ_ids2.append(int(categ.strip()))
        categories = self.env['product.category'].browse(categ_ids2)
        ubicacion = self.env['stock.location'].browse(data.get('ubicacion'))

        if categ_ids2:
            histoy_lines = histoy_lines.filtered(lambda x: x.product_id.categ_id.id in categ_ids2)

        # if data.get('product_categ_id'):
        #    histoy_lines = histoy_lines.filtered(lambda x: x.product_id.categ_id.id == data.get('product_categ_id'))

        if data.get('ubicacion'):
            histoy_lines = histoy_lines.filtered(lambda x: x.location_id.id == data.get('ubicacion'))

        productos = []
        new_history_lines = []
        for l in histoy_lines:
            if l.product_id.id not in productos:
                productos.append(l.product_id.id)

        for prod in productos:
            fil = histoy_lines.filtered(lambda x: x.product_id.id == prod)
            elemento = fil[0]
            quantity = 0
            inventory_quantity = 0
            for f in fil:
                quantity += f.quantity
                inventory_quantity += f.inventory_quantity
            elemento.quantity = quantity
            elemento.inventory_quantity = inventory_quantity
            if quantity < 0:
                elemento.inventory_diff_quantity = inventory_quantity + quantity
            else:
                elemento.inventory_diff_quantity = inventory_quantity - quantity
            new_history_lines.append(elemento)

        return {
            'company': self.env.company,
            'listado_nombres': listado_nombres,
            'listado_fechas': listado_fechas,
            'histoy_lines': new_history_lines,
            # 'f_category': category,
            'f_categories': categories,
            'currency': self.env.company.currency_id,
            'nro_ajuste': nro_ajuste,
            'f_ubicacion': ubicacion,
            'f_dif_cero': data.get('mostrar_dif_cero')
        }
