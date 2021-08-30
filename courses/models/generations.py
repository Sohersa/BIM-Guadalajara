#-*- coding: utf-8 -*-

from odoo import models, fields, api


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
    
