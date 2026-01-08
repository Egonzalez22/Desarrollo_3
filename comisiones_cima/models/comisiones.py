# -*- coding: utf-8 -*-

from odoo import api, exceptions, fields, models

COMISION_BASE = 5
COMISION_OBJ_1 = 2
COMISION_OBJ_2 = 1

class Comision(models.Model):
    _name = 'cima_comision'
    
    name = fields.Char(string='Nombre', store=True)
    company_id = fields.Many2one('res.company', string='Compañia', required=True, default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency', string='Moneda', required=True, related='company_id.currency_id')
    line_ids = fields.One2many('cima_comision_line', 'comision_id', string='Comisiones por vendedor')

    # Campos especificos de la comision
    fecha_inicio = fields.Date(string='Fecha de inicio')
    fecha_fin = fields.Date(string='Fecha de fin')
    
    fecha_inicio_cobros = fields.Date(string='Fecha de inicio Cobros')
    fecha_fin_cobros = fields.Date(string='Fecha de fin Cobros')

    vendedor_ids = fields.Many2many('hr.employee', string='Vendedores', domain=[('es_vendedor', '=', True)])

    total_venta = fields.Monetary(string='Total venta')
    total_cobrado = fields.Monetary(string='Total cobrado')
    total_comision = fields.Monetary(string='Total comisión')

    estado = fields.Selection([('borrador', 'Borrador'), ('confirmado', 'Confirmado')], string='Estado', default='borrador')

    def button_limpiar_comisiones(self):
        """
        Eliminamos todas las lineas de comisiones creadas, si está en estado borrador
        """
        # Solo se puede limpiar si está en estado borrador
        if self.estado != 'borrador':
            raise exceptions.ValidationError('Solo se puede limpiar si está en estado borrador')

        # Borramos las lineas de comisiones
        self.line_ids.unlink()

    def button_confirmar_comisiones(self):
        """
        Cambiamos el estado de la comision a confirmado
        """
        # Si no hay vendedores seleccionados, retornamos
        if not self.vendedor_ids:
            raise exceptions.ValidationError('Debe seleccionar al menos un vendedor')

        # Si no hay lineas de comisiones, retornamos
        if not self.line_ids:
            raise exceptions.ValidationError('No hay lineas de comisión para guardar1')

        # Cambiamos el estado a confirmado
        self.estado = 'confirmado'

    def button_procesar_comisiones(self):
        """
        Procesamos las comisiones de los vendedores
        """
        # Verificamos si el registro está guardado
        if not self.id:
            raise exceptions.ValidationError('Debe guardar la comisión antes de procesarla')

        # Si no hay vendedores seleccionados, retornamos
        if not self.vendedor_ids:
            raise exceptions.ValidationError('Debe seleccionar al menos un vendedor')

        # Creamos las lineas de comisiones
        self.crear_lineas_comision()
        # Calculamos las comisiones
        self.calcular_comision_normal()
    
    def crear_lineas_comision(self):
        """
        Creamos una linea de comision por cada vendedor y categoria.
        Un grupo de comision tiene asignado vendedores y a su vez lineas de comisiones con objetivos diferentes por categoria.
        """

        # Obtenemos todas las categorias comisionables
        categorias = self.env['product.category'].search([('es_comisionable', '=', True)])

        for record in self:
            # Borramos las lineas de comisiones anteriores para poder crear las nuevas
            domain_delete_lines = [('comision_id', '=', record.id)]
            self.env['cima_comision_line'].search(domain_delete_lines).unlink()

            for vendedor in record.vendedor_ids:
                grupo_comision = self.env['grupo_comision'].search([('vendedor_ids', 'in', vendedor.id)])
                
                # Si no hay grupo de comision retornamos
                if not grupo_comision:
                    continue
                    
                # Si hay mas de un grupo de comisiones para el vendedor, se lanzará un error
                if len(grupo_comision) > 1:
                    raise exceptions.ValidationError(f'El vendedor {vendedor.name} tiene más de un grupo de comisiones asignado')

                # Si no hay lineas de comisiones para el grupo de comisiones del vendedor, retornamos
                if not grupo_comision.line_ids:
                    raise exceptions.ValidationError(f'El grupo {grupo_comision.name} no tiene reglas de comisiones asignadas')

                for category in categorias:

                    # Obtenemos el grupo de comision de la category
                    grupo_comision_linea = self.env['grupo_comision_line'].search([('category_id', '=', category.id), ('grupo_id', '=', grupo_comision.id)])

                    # Creamos la linea de comision
                    vals = {
                        'comision_id': record.id,
                        'fecha_inicio': record.fecha_inicio,
                        'fecha_fin': record.fecha_fin,
                        'fecha_inicio_cobros': record.fecha_inicio_cobros,
                        'fecha_fin_cobros': record.fecha_fin_cobros,
                        'vendedor_id': vendedor.id,
                        'category_id': category.id,
                        'grupo_comision_id': grupo_comision.id,
                        'grupo_comision_line_id': grupo_comision_linea.id,
                        'objetivo_1': grupo_comision_linea.objetivo_1,
                        'objetivo_2': grupo_comision_linea.objetivo_2,
                        'comision_base': grupo_comision_linea.comision_base,
                    }
                    linea = self.env['cima_comision_line'].create(vals)
                    linea.asociar_documentos()
                    linea.calcular_totales_linea()

            # Calcular totales
            record.total_venta = sum(record.line_ids.mapped('total_venta'))
            record.total_cobrado = sum(record.line_ids.mapped('total_cobrado'))

    def calcular_comision_normal(self):
        """
        Calculamos la comisión de cada linea de comision
        """
        for record in self:
            # Obtenemos las lineas por cada vendedor
            vendedores = self.env['hr.employee'].search([('es_vendedor', '=', True)])
            for vendedor in vendedores:
                
                # Obtenemos todas las lineas de comisiones del vendedor
                comision_line_domain = [
                    ('vendedor_id', '=', vendedor.id), 
                    ('comision_id', '=', record.id)
                ]
                lineas = self.env['cima_comision_line'].search(comision_line_domain)
                total_cobrados = sum(lineas.mapped('total_cobrado'))

                # Obtenemos la comisiones tercerizadas y restamos el total_cobrado
                comision_line_domain += [('grupo_comision_line_id.es_tercerizado', '=', True)]
                tercerizadas = self.env['cima_comision_line'].search(comision_line_domain)
                total_cobrados -= sum(tercerizadas.mapped('total_cobrado'))
                
                # Verificamos si se activo el objetivo 1 por la categoria de activacion
                objetivo_1_activado = False
                objetivo_2_activado = False

                for linea in lineas:
                    # Si el total cobrado es igual o mayor al objetivo del grupo
                    if total_cobrados >= linea.grupo_comision_id.meta_objetivo_1:

                        # Si la linea tiene una categoria activadora y es superior al objetivo 1, se habilita la bandera de activador
                        if linea.grupo_comision_line_id.es_activador and linea.total_cobrado >= linea.objetivo_1:
                            objetivo_1_activado = True

                    # Si el total cobrado es igual o mayor al objetivo del grupo
                    if total_cobrados >= linea.grupo_comision_id.meta_objetivo_2:

                        # Si la linea tiene una categoria activadora y es superior al objetivo 2, se habilita la bandera de activador
                        if linea.grupo_comision_line_id.es_activador and linea.total_cobrado >= linea.objetivo_2:
                            objetivo_2_activado = True

                for linea in lineas:

                    # Comision base
                    linea.total_comision_base = (linea.total_cobrado * linea.comision_base) / 100

                    # Objetivo 1
                    if linea.total_cobrado >= linea.objetivo_1 or objetivo_1_activado:
                        if not linea.grupo_comision_line_id.es_tercerizado:
                            linea.objetivo_1_premio = (linea.total_cobrado * COMISION_OBJ_1) / 100
                        else:
                            linea.objetivo_1_premio = 0
                        
                    # Objetivo 2
                    if linea.total_cobrado >= linea.objetivo_2 or objetivo_2_activado:
                        if not linea.grupo_comision_line_id.es_tercerizado:
                            linea.objetivo_2_premio = (linea.total_cobrado * COMISION_OBJ_2) / 100
                        else:
                            linea.objetivo_2_premio = 0

                    # Total comision
                    linea.total_comision = linea.total_comision_base + linea.objetivo_1_premio + linea.objetivo_2_premio

            # Obtenemos el total de la comision
            record.total_comision = sum(record.line_ids.mapped('total_comision'))

class ComisionLine(models.Model):
    _name = 'cima_comision_line'
    
    company_id = fields.Many2one('res.company', string='Compañia', required=True, default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency', string='Moneda', required=True, related='company_id.currency_id')
    comision_id = fields.Many2one('cima_comision', string='Comisión')

    # Campos especificos de la comision
    fecha_inicio = fields.Date(string='Fecha de inicio')
    fecha_fin = fields.Date(string='Fecha de fin')
    
    fecha_inicio_cobros = fields.Date(string='Fecha de inicio Cobros')
    fecha_fin_cobros = fields.Date(string='Fecha de fin Cobros')

    vendedor_id = fields.Many2one('hr.employee', string='Vendedor')

    # Grupos de comisiones
    category_id = fields.Many2one('product.category', string='Categoría')
    grupo_comision_id = fields.Many2one('grupo_comision', string='Grupo de comisión')
    grupo_comision_line_id = fields.Many2one('grupo_comision_line', string='Grupo de comisión')

    # Para auditoria se guarda relación con los documentos
    factura_ids = fields.Many2many('account.move', 'facturas_rango',  string='Rango de Facturas')
    factura_pagos_ids = fields.Many2many('account.move', 'facturas_pago_rango',  string='Facturas por Rango de Pagos')
    
    payment_ids = fields.Many2many('account.payment', string='Pagos')

    # Se guarda como historico porque podrían variar en la relacion
    comision_base = fields.Float(string='Comisión Base', digits=(16, 2))
    objetivo_1 = fields.Monetary(string='Objetivo 1')
    objetivo_2 = fields.Monetary(string='Objetivo 2')

    # Total de comisiones
    objetivo_1_premio = fields.Monetary(string='Premio 1')
    objetivo_2_premio = fields.Monetary(string='Premio 2')
    total_comision_base = fields.Monetary(string='Comisión Base')

    total_venta = fields.Monetary(string='Total venta')
    total_cobrado = fields.Monetary(string='Total cobrado')
    total_comision = fields.Monetary(string='Total comisión')

    # Campos para visualizacion
    category_name = fields.Char(string='Categoría', related='category_id.name', store=True)
    premio_1_logrado = fields.Boolean(string='Premio 1 logrado', compute='_compute_premio_1_logrado')
    premio_2_logrado = fields.Boolean(string='Premio 2 logrado', compute='_compute_premio_2_logrado')

    diferencia_objetivo_1 = fields.Monetary(string='Diferencia objetivo 1', compute='_compute_diferencia_objetivo_1')
    diferencia_objetivo_2 = fields.Monetary(string='Diferencia objetivo 2', compute='_compute_diferencia_objetivo_2')
    porcentaje_objetivo_1 = fields.Float(string='Objetivo 1 %', compute='_compute_porcentaje_objetivo_1')
    porcentaje_objetivo_2 = fields.Float(string='Objetivo 2 %', compute='_compute_porcentaje_objetivo_2')

    @api.depends('total_cobrado', 'objetivo_1')
    @api.onchange('total_cobrado', 'objetivo_1')
    def _compute_premio_1_logrado(self):
        """
        Calculamos si se logró el premio 1
        """
        for rec in self:
            if rec.total_cobrado >= rec.objetivo_1:
                rec.premio_1_logrado = True
            else:
                rec.premio_1_logrado = False
    
    @api.depends('total_cobrado', 'objetivo_2')
    @api.onchange('total_cobrado', 'objetivo_2')
    def _compute_premio_2_logrado(self):
        """
        Calculamos si se logró el premio 2
        """
        for rec in self:
            if rec.total_cobrado >= rec.objetivo_2:
                rec.premio_2_logrado = True
            else:
                rec.premio_2_logrado = False

    @api.depends('total_venta', 'objetivo_1')
    @api.onchange('total_venta', 'objetivo_1')
    def _compute_diferencia_objetivo_1(self):
        """
        Calculamos la diferencia del objetivo 1
        """
        for rec in self:
            rec.diferencia_objetivo_1 = rec.objetivo_1 - rec.total_venta

    @api.depends('total_venta', 'objetivo_2')
    @api.onchange('total_venta', 'objetivo_2')
    def _compute_diferencia_objetivo_2(self):
        """
        Calculamos la diferencia del objetivo 2
        """
        for rec in self:
            rec.diferencia_objetivo_2 = rec.objetivo_2 - rec.total_venta
    
    @api.depends('total_venta', 'objetivo_1')
    @api.onchange('total_venta', 'objetivo_1')
    def _compute_porcentaje_objetivo_1(self):
        """
        Calculamos el porcentaje del objetivo 1
        """
        for rec in self:
            if rec.total_venta > 0 and rec.objetivo_1 > 0:
                rec.porcentaje_objetivo_1 = rec.total_venta / rec.objetivo_1 * 100
            else:
                rec.porcentaje_objetivo_1 = 0
    
    @api.depends('total_venta', 'objetivo_2')
    @api.onchange('total_venta', 'objetivo_2')
    def _compute_porcentaje_objetivo_2(self):
        """
        Calculamos el porcentaje del objetivo 2
        """
        for rec in self:
            if rec.total_venta > 0 and rec.objetivo_2 > 0:
                rec.porcentaje_objetivo_2 = rec.total_venta / rec.objetivo_2 * 100
            else:
                rec.porcentaje_objetivo_2 = 0

    @api.depends('objetivo_1', 'objetivo_2', 'total_venta', 'total_cobrado')
    @api.onchange('objetivo_1', 'objetivo_2', 'total_venta', 'total_cobrado')
    def calcular_comision(self):
        """
        Calculamos la comision en base a los totales
        """
        for rec in self:
            rec.comision_id.calcular_comision_normal()

    def asociar_documentos(self):
        """
        Obtenemos todas las facturas y pagos en estado posted del vendedor y que tengan productos con la categoria seleccionada
        """
        self.asociar_facturas()
        self.asociar_pagos()
    
    def asociar_facturas(self):
        """
        Se obtienen todas las facturas en el rango de fechas seleccionado, que tengan productos con la categoria seleccionada
        """
        domain_invoices_without_payment = [
            ('invoice_date', '>=', self.fecha_inicio),
            ('invoice_date', '<=', self.fecha_fin),
            ('product_id.categ_id', '=', self.category_id.id),
            ('move_id.vendedor', '=', self.vendedor_id.id),
            ('move_id.move_type', '=', 'out_invoice'),
            ('move_id.state', '=', 'posted'),
            ('move_id.payment_state', 'in', ['not_paid', 'paid', 'in_payment', 'partial']),
        ]
        move_lines = self.env['account.move.line'].sudo().search(domain_invoices_without_payment)
        self.factura_ids = move_lines.move_id

    def asociar_pagos(self):
        """
        Se obtienen todos las facturas en el rango de fechas seleccionado, se separa del método de obtener facturas
        porque las facturas asociadas puede ser de otro rango de fechas
        """
        domain_payments = [
            ('date', '>=', self.fecha_inicio_cobros),
            ('date', '<=', self.fecha_fin_cobros),
            ('state', '=', 'posted'),
            ('payment_type', '=', 'inbound'),
        ]
        payments = self.env['account.payment'].sudo().search(domain_payments)

        # Obtenemos las facturas asociadas a los pagos, que tengan el vendedor seleccionado
        domain_invoices = [
            ('move_id', 'in', payments.reconciled_invoice_ids.ids),
            ('product_id.categ_id', '=', self.category_id.id),
            ('move_id.vendedor', '=', self.vendedor_id.id),
            ('move_id.move_type', '=', 'out_invoice'),
            ('move_id.state', '=', 'posted'),
            ('move_id.payment_state', 'in', ['not_paid', 'paid', 'in_payment', 'partial']),
        ]
        move_lines = self.env['account.move.line'].sudo().search(domain_invoices)

        self.factura_pagos_ids = move_lines.move_id
        
    def calcular_totales_linea(self):
        """
        Calcular los totales por facturas y pagos
        """
        self.calcular_total_vendido()
        self.calcular_total_cobrado()
    
    def calcular_total_vendido(self):
        for rec in self:
            total_venta = 0

            # Recorremos por cada linea de factura para obtener el total del producto asociado a la categoria
            for factura in rec.factura_ids:
                for linea in factura.invoice_line_ids:
                    if linea.product_id.categ_id.id == rec.category_id.id:
                        total_venta += linea.price_subtotal

            rec.total_venta = total_venta

    def calcular_total_cobrado(self):
        for rec in self:
            total_cobrado = 0

            # Recorremos por las facturas de los pagos asociados
            for factura in rec.factura_pagos_ids:
                pagado_parcialmente = factura.amount_residual > 0

                # Si la factura no está completamente pagada, se hace un prorrateo del monto sin IVA
                if pagado_parcialmente:
                    monto_pagado = (factura.amount_total_signed - factura.amount_residual) / 11
                    porcentaje_prorrateo = (monto_pagado * 100) / (factura.amount_total_signed / 11)

                # Recorremos por cada linea de factura para obtener el total del producto asociado a la categoria
                for linea in factura.invoice_line_ids:
                    if linea.product_id.categ_id.id == rec.category_id.id:
                        if pagado_parcialmente:
                            total_cobrado += (linea.price_subtotal * porcentaje_prorrateo) / 100
                        else:
                            total_cobrado += linea.price_subtotal

            rec.total_cobrado = total_cobrado

        
