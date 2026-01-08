import math

from odoo import _, api, exceptions, fields, models
import re

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    fe_description = fields.Char(string="Descripción")

    # Cuando se cambia el producto en la linea de factura, se actualiza la descripcion
    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            # Si el producto tiene descripcion, la usamos
            if self.product_id.fe_description:
                self.fe_description = self.product_id.fe_description
            else:
                self.fe_description = self.obtener_nombre_linea_kude()

    def getdDesProSer(self):
        # fe_personalizacion/models/account_move_line.py
        # Si por algun motivo no se obtiene la descripcion customizada, generamos una descripcion
        name =  self.fe_description
        if not name:
            name = self.obtener_nombre_linea_kude()
        return name

    def obtener_nombre_linea_kude(self):
        name = self.obtener_nombre_linea()

        # Si hay nota de remision y producto
        if self.move_id.nota_remision_id and self.product_id:
            # Obtenemos la linea de la factura que coincide con la linea de la remision
            remision_line = self.move_id.nota_remision_id.line_ids.filtered(
                lambda x: x.product_id.default_code == self.product_id.default_code
            )

            if remision_line:
                # Si hay mas de una linea de la factura que coincide con la linea de la remision, tomamos la primera
                if len(remision_line) > 1:
                    remision_line = remision_line[0]

                if remision_line.lot_id:
                    name = f"{name} \n\n Lote: {remision_line.lot_id.name}"

                    if remision_line.lot_id.expiration_date:
                        expiracion = remision_line.lot_id.expiration_date.strftime('%d/%m/%Y')
                        name = f"{name} \n\n Vencimiento: {expiracion}"

        return name

    def obtener_nombre_linea(self):
        """
        Retornamos directamente el nombre del producto porque se esta concatenando con varios datos
        """

        name = ""

        if self.fe_description:
            name = self.fe_description
        elif self.product_id:
            name = self.product_id.name
        else:
            name = self.name[:120]

        return name
