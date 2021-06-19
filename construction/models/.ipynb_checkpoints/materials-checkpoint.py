from odoo import api, fields, models

from ..utils import vars

statics = vars.Vars

class Material(models.Model):
    _name = 'construction.material'
    _description = 'Materiales para construcción'

    code = fields.Char(string='Código')
    name = fields.Char(string='Nombre')
    description = fields.Char(string='Descripción')
    m_unit = fields.Many2one( 'construction.unit', string='Unidad', ondelete='set null', index=True, copy=False)
    performance = fields.Float( digits=(6,2), string='Rendimiento')
    cost = fields.Float( digits=(6,4), string='Precio')
    coin = fields.Selection( statics.coins, string="Moneda", default='0', help="Seleccionar una moneda")
    image = fields.Image( string="Imagen", help="Imagen del material")
    web_site = fields.Char(string='Sitio web')

    supplier = fields.Many2one('construction.supplier', ondelete="set null", string="Proveedor", index=True)
    basic_id = fields.Many2one('construction.basic', string='Concepto/Básico',  ondelete='cascade', index=True, copy=False)

class Concept_material_lines(models.Model):
    _name = 'construction.concept_material_lines'
    _description = 'concepto material'

    quantity = fields.Float( string='Cantidad', default='1' )
    m_import = fields.Float( digits=(6,4), string='Importe', compute='_get_subtotal', store=True)

    concept_id = fields.Many2one('construction.concept', string='Concepto',  ondelete='cascade', index=True, copy=False)
    material_id = fields.Many2one('construction.material', string='Material',  ondelete='cascade', index=True, copy=False)
    material_cost = fields.Float( related='material_id.cost', string='Costo')
    material_unit = fields.Many2one( related='material_id.m_unit', string='Unidad')

    @api.depends('quantity','material_cost')
    def _get_subtotal(self):
        for rec in self:
            rec['m_import'] = rec.quantity * rec.material_cost

class Basic_material_lines(models.Model):
    _name = 'construction.basic_material_lines'
    _description = 'básico material'

    quantity = fields.Float( string='Cantidad', default='1' )
    m_import = fields.Float( digits=(6,4), string='Importe', compute='_get_subtotal', store=True)

    basic_id = fields.Many2one('construction.basic', string='Básico',  ondelete='cascade', index=True, copy=False)
    material_id = fields.Many2one('construction.material', string='Material',  ondelete='cascade', index=True, copy=False)
    material_cost = fields.Float( related='material_id.cost', string='Costo')
    material_unit = fields.Many2one( related='material_id.m_unit', string='Unidad')

    @api.depends('quantity','material_cost')
    def _get_subtotal(self):
        for rec in self:
            rec['m_import'] = rec.quantity * rec.material_cost