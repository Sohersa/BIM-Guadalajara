# -*- coding: utf-8 -*-
from odoo import models,fields,api

from ..utils import vars

statics = vars.Vars

class Unit(models.Model):
    _name = 'construction.unit'
    _description = 'Unidades'

    code = fields.Char(string='Código')
    name = fields.Char(string='Nombre')
    magnitude = fields.Selection( statics.magnitude, string='Magnitud',  default='longitud', help="Seleccionar una unidad")

#tipo de enfoque de cliente
class Client_approach_type(models.Model): 
    _name = 'construction.client_approach_type'
    _description = 'Clientes'

    name = fields.Char(string='Tipo de enfoque cliente')
    code = fields.Char(string='Código')
    description = fields.Char(string='Descripción')

class Project_type(models.Model):
    _name = 'construction.project_type'
    _description = 'Tipos de proyectos'

    name = fields.Char(string='Tipo de proyecto')
    code = fields.Char(string='Código')
    description = fields.Char(string='Descripción')

class Contract_type(models.Model):
    _name = 'construction.contract_type'
    _description = 'Tipos de contratos'

    name = fields.Char(string='Tipo de contrato')
    code = fields.Char(string='Código')
    description = fields.Char(string='Descripción')

