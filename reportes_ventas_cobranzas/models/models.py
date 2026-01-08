# -*- coding: utf-8 -*-
from odoo import api, fields, models, exceptions
from datetime import datetime
import json
from odoo.tools import float_round
import itertools


class ReportesVentasCobranzas(models.TransientModel):
    _name = 'reportes_ventas_cobranzas.reporte'

    fecha = fields.Date(string="Fecha de inicio",required=True)
    fecha_fin = fields.Date(string="Fecha de fin",required=True)
    tipo_reporte = fields.Selection(
        [
            ('ventas_contado', 'Ventas al Contado'),
            # ('ventas_acumuladas', 'Ventas Acumuladas'),
            ('ventas_credito', 'Ventas a Crédito'),
            ('reporte_cobranzas', 'Reporte de Cobranzas'),
        ],
            string="Reporte")

    cobrador_id = fields.Many2one('hr.employee', string="Cobrador")
    usuario = fields.Many2one('res.users', string="Usuario")

    

    def button_generar(self):

        data = {
            'fecha': self.fecha,
            'fecha_fin': self.fecha_fin,
            'tipo_reporte': self.tipo_reporte,
            'cobrador_id': self.cobrador_id.id,
            'usuario': self.usuario.id,
        }
        if self.tipo_reporte == 'ventas_contado':
            return self.env.ref('reportes_ventas_cobranzas.ventas_contado_action').report_action(self, data=data)
        
        if self.tipo_reporte == 'ventas_credito':
            return self.env.ref('reportes_ventas_cobranzas.ventas_credito_action').report_action(self, data=data)

        # if self.tipo_reporte == 'ventas_acumuladas':
        #     return self.env.ref('reportes_ventas_cobranzas.ventas_acumuladas_action').report_action(self, data=data)

        if self.tipo_reporte == 'reporte_cobranzas':
            return self.env.ref('reportes_ventas_cobranzas.reporte_cobranzas_action').report_action(self, data=data)


class ReportCobranzas(models.AbstractModel):
    _name = 'report.reportes_ventas_cobranzas.reporte_cobranzas'

    def _get_report_values(self, docids, data=None):

        usuario = data.get('usuario')
        cobrador = data.get('cobrador_id')
        cobrador_name = self.env['hr.employee'].search([('id','=',cobrador)]).name
        usuario_name = self.env['res.users'].search([('id','=',usuario)]).name

        consulta =self.env['account.payment'].search([
                ('payment_type', '=', 'inbound'),
                ('date', '>=', data.get('fecha')),
                ('date', '<=', data.get('fecha_fin')),
                ('currency_id', '=', 'PYG'),
                ('state', '=', 'posted'),('cobrador_id', '=', data.get('cobrador_id'))
            ])
        
        



        pagos_gs = self.env['account.payment'].search([
                ('payment_type', '=', 'inbound'),
                ('date', '>=', data.get('fecha')),
                ('date', '<=', data.get('fecha_fin')),
                ('currency_id', '=', 'PYG'),
                ('state', '=', 'posted')
            ])
            
      

        pagos_us = self.env['account.payment'].search([
            ('payment_type', '=', 'inbound'),
            ('date', '>=', data.get('fecha')),
            ('date', '<=', data.get('fecha_fin')),
            ('currency_id', '=', 'USD'),
            ('state', '=', 'posted')
        ])
        
    
        pagos = self.env['account.payment'].search([
            ('payment_type', '=', 'inbound'),
            ('date', '>=', data.get('fecha')),
            ('date', '<=', data.get('fecha_fin')),
            ('state', '=', 'posted')
        ])    

        if cobrador and usuario:
            pagos_gs = self.env['account.payment'].search([
                ('payment_type', '=', 'inbound'),
                ('date', '>=', data.get('fecha')),
                ('date', '<=', data.get('fecha_fin')),
                ('currency_id', '=', 'PYG'),
                ('state', '=', 'posted'),('cobrador_id', '=', cobrador),
                ('usuario', '=', usuario)
            ])
            
        

            pagos_us = self.env['account.payment'].search([
                ('payment_type', '=', 'inbound'),
                ('date', '>=', data.get('fecha')),
                ('date', '<=', data.get('fecha_fin')),
                ('currency_id', '=', 'USD'),
                ('state', '=', 'posted'),('cobrador_id', '=', cobrador),
                ('usuario', '=', usuario)
            ])
            
        
            pagos = self.env['account.payment'].search([
                ('payment_type', '=', 'inbound'),
                ('date', '>=', data.get('fecha')),
                ('date', '<=', data.get('fecha_fin')),
                ('state', '=', 'posted'),('cobrador_id', '=', cobrador),
                ('usuario', '=', usuario)
            ])

        if cobrador and not usuario:
            pagos_gs = self.env['account.payment'].search([
                ('payment_type', '=', 'inbound'),
                ('date', '>=', data.get('fecha')),
                ('date', '<=', data.get('fecha_fin')),
                ('currency_id', '=', 'PYG'),
                ('state', '=', 'posted'),('cobrador_id', '=', cobrador)
            ])
            
        

            pagos_us = self.env['account.payment'].search([
                ('payment_type', '=', 'inbound'),
                ('date', '>=', data.get('fecha')),
                ('date', '<=', data.get('fecha_fin')),
                ('currency_id', '=', 'USD'),
                ('state', '=', 'posted'),('cobrador_id', '=', cobrador)
            ])
            
        
            pagos = self.env['account.payment'].search([
                ('payment_type', '=', 'inbound'),
                ('date', '>=', data.get('fecha')),
                ('date', '<=', data.get('fecha_fin')),
                ('state', '=', 'posted'),('cobrador_id', '=', cobrador)
            ])
        
        if usuario and not cobrador:
            pagos_gs = self.env['account.payment'].search([
                ('payment_type', '=', 'inbound'),
                ('date', '>=', data.get('fecha')),
                ('date', '<=', data.get('fecha_fin')),
                ('currency_id', '=', 'PYG'),
                ('state', '=', 'posted'),
                ('usuario', '=', usuario)
            ])
            
        

            pagos_us = self.env['account.payment'].search([
                ('payment_type', '=', 'inbound'),
                ('date', '>=', data.get('fecha')),
                ('date', '<=', data.get('fecha_fin')),
                ('currency_id', '=', 'USD'),
                ('state', '=', 'posted'),
                ('usuario', '=', usuario)
            ])
            
        
            pagos = self.env['account.payment'].search([
                ('payment_type', '=', 'inbound'),
                ('date', '>=', data.get('fecha')),
                ('date', '<=', data.get('fecha_fin')),
                ('state', '=', 'posted'),
                ('usuario', '=', usuario)
            ])

        
        pagos_ordenados = pagos.sorted('journal_id')
        grupos_pagos = itertools.groupby(pagos_ordenados, key=lambda pago: pago.journal_id)

        pagos_agrupados = []
        for journal_id, group in grupos_pagos:
            total_monto_diario = sum(pago.amount for pago in group)
            nombre_diario = self.env['account.journal'].browse(journal_id.id).name
            
            pagos_agrupados.append({
                'journal_id': nombre_diario,
                'pagos': list(group),
                'total_monto_diario': total_monto_diario,

            })
        
       
                    
        return {
                'fecha': data.get('fecha'),
                'fecha_fin': data.get('fecha_fin'),
                'pagos_gs': pagos_gs,
                'pagos_us': pagos_us,
                'pagos': pagos,
                'company': self.env.user.company_id,
                'pagos_agrupados':pagos_agrupados,
                'cobrador_name':cobrador_name,
                'usuario_name':usuario_name
                }


class ReportVentasContado(models.AbstractModel):
    _name = 'report.reportes_ventas_cobranzas.ventas_contado'

    def _get_report_values(self, docids, data=None):
        list_facts_contado = []  # listado de facturas de ventas al contado

        # se buscan todas las facturas al contado
        facturas = self.env['account.move'].search(
            [('company_id', '=', self.env.user.company_id.id), 
             ('invoice_date_due', '=', data.get('fecha')), 
             ('move_type', '=', 'out_invoice'), 
             ('state', 'in', ['posted']),
             ('invoice_date', '>=', data.get('fecha')),
             ('invoice_date', '<=', data.get('fecha_fin'))])
        
        for f in facturas:
            # invoice_payment = json.loads(f.invoice_payments_widget)  # lista de pagos conciliados a la factura
            if isinstance(f.invoice_payments_widget, dict):
                invoice_payment = f.invoice_payments_widget
            else:
                invoice_payment = json.loads(f.invoice_payments_widget)  # lista de pagos conciliados a la factura
            if invoice_payment: 
                detalle = invoice_payment['content']  # en content se encuentran los detalles del pago 
                for dt in detalle:
                    # buscamos en account.payment el pago relacionado a la factura
                    payment = self.env['account.payment'].search([('id', '=', dt['account_payment_id'])])
                    if payment:
                        list_facts_contado.append([f, payment])  # se agrega la instancia de factura y pago
                    else:
                        list_facts_contado.append([f, 'x'])  # se agrega una bandera x para denotar que no hay pago
            else:
                list_facts_contado.append([f, 'x'])  # se agrega una bandera x para denotar que no hay pago


        return {
                'fecha': data.get('fecha'),
                'facturas': list_facts_contado,
                'company': self.env.user.company_id
                }


class ReportVentasCredito(models.AbstractModel):
    _name = 'report.reportes_ventas_cobranzas.ventas_credito'

    def _get_report_values(self, docids, data=None):
        facturas = self.env['account.move'].search(
            [('company_id', '=', self.env.user.company_id.id), 
             ('invoice_date_due', '!=', data.get('fecha')), 
             ('move_type', '=', 'out_invoice'), 
             ('state', 'in', ['posted']),
             ('invoice_date', '>=', data.get('fecha')),
             ('invoice_date', '<=', data.get('fecha_fin'))])

        rate = 0
        for factura in facturas:
            if factura.currency_id.name == 'USD':
                rate = factura.currency_id._get_conversion_rate(factura.currency_id, self.env.user.company_id.currency_id, self.env.user.company_id, factura.invoice_date)

        return {
                'fecha': data.get('fecha'),
                'facturas': facturas,
                'company': self.env.user.company_id,
                'rate_usd' : round(rate, 0)
                }


class ReportVentasAcumuladas(models.AbstractModel):
    _name = 'report.reportes_ventas_cobranzas.ventas_acumuladas'

    def _get_report_values(self, docids, data=None):
        inicio_mes = data.get('fecha')[:-2] + str('01')
        data_facturas = []
        facturas = self.env['account.move'].search(
            [('company_id', '=', self.env.user.company_id.id), 
             ('move_type', '=', 'out_invoice'), 
             ('state', 'in', ['posted']),
             ('invoice_date', '>=', data.get('fecha')),
             ('invoice_date', '<=', data.get('fecha_fin'))
             ])

        acumuladas = self.env['account.move'].search(
            [('company_id', '=', self.env.user.company_id.id), 
             ('move_type', '=', 'out_invoice'), 
             ('state', 'in', ['posted']),
             ('invoice_date', '>=', inicio_mes),
             ('invoice_date', '<=', data.get('fecha_fin'))
             ])

        total_base10 = 0
        total_iva10 = 0
        total_base5 = 0
        total_iva5 = 0
        total_exentas = 0
        total_facturas = 0

        acumulado_total = 0
        acumulado_base10 = 0
        acumulado_iva10 = 0
        acumulado_base5 = 0
        acumulado_iva5 = 0
        acumulado_exentas = 0

        for a in acumuladas.sorted(key=lambda x: x.name):
            base10 = 0
            base5 = 0
            exentas = 0
            iva10 = 0
            iva5 = 0

            if a.state != 'cancel':
                acumulado_total += abs(a.amount_total_signed)

            for t in a.filtered(lambda x: x.state != 'cancel').invoice_line_ids:
                if t.tax_ids and t.tax_ids[0].amount == 10:
                    base10 += t.price_total / 1.1
                    iva10 += t.price_total / 11
                if t.tax_ids and t.tax_ids[0].amount == 5:
                    base5 += t.price_total / 1.05
                    iva5 += t.price_total / 21
                if (t.tax_ids and t.tax_ids[0].amount == 0) or not t.tax_ids:
                    exentas += t.price_total

            # obtener valor de cotizacion
            coti = a.line_ids[0].credit / abs(a.line_ids[0].amount_currency)
            coti = float_round(coti, precision_digits=2, rounding_method='HALF-UP')

            # CONVERTIR TODO A GS
            if a.currency_id != self.env.company.currency_id:
                base10 = a.currency_id._convert(
                    round(base10,2), self.env.company.currency_id, self.env.company, a.invoice_date, cotizacion=coti)
                iva10 = a.currency_id._convert(
                    round(iva10,2), self.env.company.currency_id, self.env.company, a.invoice_date, cotizacion=coti)
                base5 = a.currency_id._convert(
                    round(base5,2), self.env.company.currency_id, self.env.company, a.invoice_date, cotizacion=coti)
                iva5 = a.currency_id._convert(
                    round(iva5,2), self.env.company.currency_id, self.env.company, a.invoice_date, cotizacion=coti)
                exentas = a.currency_id._convert(
                    round(exentas,2), self.env.company.currency_id, self.env.company, a.invoice_date, cotizacion=coti)
                

            # if a.currency_id.name == "USD":
            #     base10 = base10*a.cotizacion
            #     iva10 = iva10*a.cotizacion
            #     base5 = base5*a.cotizacion
            #     iva5 = iva5*a.cotizacion
            #     exentas = exentas*a.cotizacion

            base10 = int(round(base10, 0))
            iva10 = int(round(iva10, 0))
            base5 = int(round(base5, 0))
            iva5 = int(round(iva5, 0))
            exentas = int(round(exentas, 0))

            acumulado_base10 += base10
            acumulado_iva10 += iva10
            acumulado_base5 += base5
            acumulado_iva5 += iva5
            acumulado_exentas += exentas

        for i in facturas.sorted(key=lambda x: x.name):
            base10 = 0
            base5 = 0
            exentas = 0
            iva10 = 0
            iva5 = 0
            # i.amount_untaxed_signed
            # i.amount_tax_signed
            # i.amount_total_signed

            if i.state != 'cancel':
                total_facturas += abs(i.amount_total_signed)

            for t in i.filtered(lambda x: x.state != 'cancel').invoice_line_ids:
                if t.tax_ids and t.tax_ids[0].amount == 10:
                    base10 += t.price_total / 1.1
                    iva10 += t.price_total / 11
                if t.tax_ids and t.tax_ids[0].amount == 5:
                    base5 += t.price_total / 1.05
                    iva5 += t.price_total / 21
                if (t.tax_ids and t.tax_ids[0].amount == 0) or not t.tax_ids:
                    exentas += t.price_total
            
            # obtener valor de cotizacion
            coti = i.line_ids[0].credit / abs(i.line_ids[0].amount_currency)
            coti = float_round(coti, precision_digits=2, rounding_method='HALF-UP')

            # CONVERTIR TODO A GS
            if i.currency_id != self.env.company.currency_id:
                base10 = i.currency_id._convert(
                    round(base10,2), self.env.company.currency_id, self.env.company, i.invoice_date, cotizacion=coti)
                iva10 = i.currency_id._convert(
                    round(iva10,2), self.env.company.currency_id, self.env.company, i.invoice_date, cotizacion=coti)
                base5 = i.currency_id._convert(
                    round(base5,2), self.env.company.currency_id, self.env.company, i.invoice_date, cotizacion=coti)
                iva5 = i.currency_id._convert(
                    round(iva5,2), self.env.company.currency_id, self.env.company, i.invoice_date, cotizacion=coti)
                exentas = i.currency_id._convert(
                    round(exentas,2), self.env.company.currency_id, self.env.company, i.invoice_date, cotizacion=coti)

            # if i.currency_id.name == "USD":
            #     base10 = base10*i.cotizacion
            #     iva10 = iva10*i.cotizacion
            #     base5 = base5*i.cotizacion
            #     iva5 = iva5*i.cotizacion
            #     exentas = exentas*i.cotizacion

            base10 = int(round(base10, 0))
            iva10 = int(round(iva10, 0))
            base5 = int(round(base5, 0))
            iva5 = int(round(iva5, 0))
            exentas = int(round(exentas, 0))

            total_base10 += base10
            total_iva10 += iva10
            total_base5 += base5
            total_iva5 += iva5
            total_exentas += exentas

            data_facturas.append({
                'numero': i.name,
                'fecha': i.invoice_date,
                'razon_social': i.partner_id.name,
                'ruc': i.partner_id.vat,
                'base10': base10,
                'iva10':iva10,
                'base5': base5,
                'iva5':iva5,
                'exentas':exentas
            })

        return {
                'fecha': data.get('fecha'),
                'facturas': data_facturas,
                'total_base10': total_base10,
                'total_iva10': total_iva10,
                'total_base5': total_base5,
                'total_iva5': total_iva5,
                'total_exentas': total_exentas,
                'total_facturas': int(round(total_facturas,0)),
                'acumulado_total': int(round(acumulado_total,0)),
                'acumulado_base10': acumulado_base10,
                'acumulado_iva10': acumulado_iva10,
                'acumulado_base5': acumulado_base5,
                'acumulado_iva5': acumulado_iva5,
                'acumulado_exentas': acumulado_exentas,
                'company': self.env.user.company_id,
                }
