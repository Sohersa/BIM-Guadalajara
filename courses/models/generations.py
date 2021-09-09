#-*- coding: utf-8 -*-

from odoo import models, fields, api


class generations(models.Model):
    _name = "courses.generations"
    _description = "Generations"
    #_inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char()
    #notes = fields.Text()

    #Counter fields for every student status
    students_count = fields.Integer(string="Alumnos", readonly="1")
    in_course_count = fields.Integer(string="Cursando", readonly="1")
    pending_project_total = fields.Integer(string="Proyecto Pendiente", readonly="1")
    approved_count = fields.Integer(string="Aprobados", readonly="1")
    failed_count = fields.Integer(string="Reprobados", readonly="1")
    
    #Generation category
    category = fields.Selection([('public', 'Público'), 
                                 ('c_company', 'Personalziado Empresa'),
                                 ('contracted', 'Contratado')], 'Categoría')
    
    #relational field to courses model
    course_id = fields.Many2one('courses.courses', string="Curso")
    
    #relational field to students model
    student_ids = fields.One2many('courses.students', 'generation_id', nolabel="1")

