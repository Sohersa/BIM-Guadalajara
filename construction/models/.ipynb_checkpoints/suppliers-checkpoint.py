from odoo import api, fields, models


class Supplier(models.Model):
    _name = 'construction.supplier'
    _description = 'Proveedores'

    code = fields.Char(string='Código')
    name = fields.Char(string='Nombre')
    description = fields.Char(string='Descripción')
    web_site = fields.Char(string='Sitio web')
    image = fields.Image( string="Imagen", help="Imagen del proveedor")
