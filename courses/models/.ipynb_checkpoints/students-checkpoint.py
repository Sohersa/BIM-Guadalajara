#-*- coding: utf-8 -*-

from odoo import models, fields, api

class students(models.Model):
    
    _name = "courses.students"
    _description = "Students"
        
    #Partner fields related to student
    partner_id = fields.Many2one('res.partner', string="Contacto", store="True")
    name = fields.Char(related='partner_id.name', string="Nombre", store="True")
    partner_phone = fields.Char(related='partner_id.phone', string="Teléfono", widget="phone", store="True")
    partner_email = fields.Char(related='partner_id.email', string="Correo Electrónico", widget="email", store="True")        
    partner_country = fields.Many2one('res.country', related='partner_id.country_id', string="País", store="True")
    partner_city = fields.Many2one('res.city', related='partner_id.city_id', string="Ciudad", store="True")
    partner_company = fields.Many2one('res.partner', related='partner_id.perent_id', string="Empresa", store="True")
    partner_function = fields.Char(related='partner_id.function', string="Puesto de Trabajo", store="True")
    partner_title = fields.Many2one('res.partner', related='partner_id.title', string="Profesión", store="True")
    
#     origin = fields.Selection([
#         ('company', 'Empresa'),
#         ('individual', 'Individual'),
#         'Origen'
#     ])
    
    generation_id = fields.Many2one(related='courses.generations', string="Generación")
    
    diploma = fields.Binary("Suba su Archivo")