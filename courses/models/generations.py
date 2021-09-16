#-*- coding: utf-8 -*-

from odoo import models, fields, api


class Generation(models.Model):
    _name = "courses.generations"
    _description = "Generations"
    #_inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char()

    #Estado/fase de curso
    status = fields.Selection([('new', 'Nuevo'),
                               ('in_process', 'En curso'),
                               ('terminated', 'Finalizado'),
                               ('canceled', 'Cancelado')], default="new")

    #Counter fields for every student status
    students_count = fields.Integer(string="Alumnos", readonly="1") #computado
    in_course_count = fields.Integer(string="Cursando", readonly="1") #computado
    pending_project_total = fields.Integer(string="Proyecto Pendiente", readonly="1") #computado
    approved_count = fields.Integer(string="Aprobados", readonly="1") #computado
    failed_count = fields.Integer(string="Reprobados", readonly="1") #computado

    #Generation category
    category = fields.Selection([('public', 'Público'),
                                 ('c_company', 'Personalziado Empresa'),
                                 ('contracted', 'Contratado')], 'Categoría')

    #relational field to courses model
    course_id = fields.Many2one('courses.courses', string="Curso")

    #relational field to students model
    student_ids = fields.One2many('courses.students', 'generation_id')
    
    speaker = fields.Many2one('hr.employee', string="Ponente")

    #Course duration variables
    total_hours = fields.Float(string="Duración del Curso (Horas)") #computado
    total_days = fields.Float(string="Duración del Curso (Dias)") #computado
    total_weeks = fields.Float(string="Duración del Curso (Semanas)") #computado
    start_date = fields.Datetime(string="Fecha de Inicio") #calendario

    team_ids = fields.One2many('courses.student_teams', 'generation_id')

    notes = fields.Text()