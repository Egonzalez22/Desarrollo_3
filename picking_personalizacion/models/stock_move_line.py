from odoo import api, fields, models, _


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"


    
    def _get_packing_product(self, product_id, cantidad):
        prod = product_id.packaging_ids
        control = prod.qty

        # Reemplazar la coma con un punto y eliminar otros caracteres no deseados
        cantidad = int((cantidad).replace(',00',''))

        try:
            cantidad = float(cantidad)
        except ValueError:
            return None


        if cantidad > control:
            paquetes_completos = int(cantidad / control)
            # Calcular las unidades adicionales después de los paquetes completos
            unidades_extra = cantidad % control
            if unidades_extra:
                return str(paquetes_completos) + ' Paquetes de '+ str(prod.qty) + ' + ' + str(unidades_extra) + ' unidades'
            else:
                return str(paquetes_completos) + ' Paquetes de '+ str(prod.qty) 
            
        if cantidad == control:
            return '1 Paquetes de '+ str(prod.qty) 

        if cantidad < control:
            return str(cantidad) + ' unidades'

