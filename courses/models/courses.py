#-*- coding: utf-8 -*-

from odoo import models, fields, api


class courses(models.Model):
    _name = 'courses.course'
    _description = 'Courses'
    
    name = fields.Char()
    
    #Generations count computed field
    generations_count = fields.Integer(string="Generaciones", readonly="true")
    
    #Total counters for every course
    students_total = fields.Integer(string="Alumnos")
    in_course_total = fields.Integer(string="Cursando")
    pending_project_total = fields.Integer(string="Proyecto Pendiente")
    approved_total = fields.Integer(string="Aprovados")
    failed_total = fields.Integer(string="Reprobados")
    
    #Relational field to generations model
    generations_ids = fields.One2many('courses.generation', 'course_id', required="true", string="Generaciones")
    
    
class generations(models.Model):
    _name = "courses.generation"
    _description = "Generations"
    
    name = fields.Char()
    
    #Counter fields for every student status
    students_count = fields.Integer(string="Alumnos")
    in_course_count = fields.Integer(string="Cursando")
    pending_project_total = fields.Integer(string="Proyecto Pendiente")
    approved_count = fields.Integer(string="Aprobado")
    failed_count = fields.Integer(string="Reprobado")
    
    #Generation category
#     category = fields.Selection([('public', 'Público'), 
#                                  ('c_company', 'Personalziado Empresa'),
#                                  ('contracted', 'Contratado'),
#                                  'Categoría'
#                                 ])
    
    #relational field to courses model
    course_id = fields.Many2one('courses.courses', string="Curso")
    
    #relational field to students model
    student_ids = fields.One2many('courses.student', 'generation_id', string="Alumnos")
    
class students(models.Model):
    _name = "courses.student"
    _description = "Students"
        
    #Partner fields related to student
    partner_id = fields.Many2one('res.partner', string="Contacto")
    name = fields.Char(related='partner_id.name', string="Nombre", store="True")
    partner_phone = fields.Char(related='partner_id.phone', string="Teléfono", widget="phone", store="True")
    partner_email = fields.Char(related='partner_id.email', string="Correo Electrónico", widget="email", store="True")        
    partner_country = fields.Many2one('res.country', related='partner_id.country_id', string="País", store="True")
    partner_company = fields.Many2one('res.partner', related='partner_id.parent_id', string="Empresa", store="True")
    partner_city = fields.Char(related='partner_id.city', string="Ciudad", store="True")
    partner_function = fields.Char(related='partner_id.function', string="Puesto de Trabajo", store="True")
    partner_title = fields.Many2one('res.partner', related='partner_id.title', string="Profesión", store="True")
    
#     origin = fields.Selection([
#         ('company', 'Empresa'),
#         ('individual', 'Individual'),
#         'Origen'
#     ])
    
    generation_id = fields.Many2one('courses.generation', string="Generación")
    
    diploma = fields.Binary("Suba su Archivo")