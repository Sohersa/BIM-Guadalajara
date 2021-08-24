#-*- coding: utf-8 -*-

from odoo import models, fields, api

class students(models.Model):
    
    _name = "courses.students"
    _description = "Students"
        
    name = fields.Char()
    
    partner_id = fields.Many2one('res.partner', string="Contacto")