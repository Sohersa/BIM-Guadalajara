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
                                 ('c_company', 'Personalizado Empresa'),
                                 ('contracted', 'Contratado')], 'Categoría')

    #relational field to courses model
    course_id = fields.Many2one('courses.courses', string="Curso")

    #relational field to students model
    student_ids = fields.One2many('courses.students', 'generation_id')
    team_ids = fields.One2many('courses.student_teams', 'generation_id')

    speaker = fields.Many2one('hr.employee', string="Ponente")

    session_ids = fields.One2many('courses.generations.sessions', 'generation_id', string="Sesiones")
    session_count = fields.Integer(compute="get_session_count")

    assignment_ids = fields.One2many('courses.generations.assignments', 'generation_id', string="Tareas")
    assignment_count = fields.Integer(compute="get_assignment_count")
    #Course duration variables
    total_hours = fields.Float(string="Duración del Curso (Horas)") #computado
    total_days = fields.Float(string="Duración del Curso (Dias)") #computado
    total_weeks = fields.Float(string="Duración del Curso (Semanas)") #computado
    start_date = fields.Datetime(string="Fecha de Inicio") #calendario

    notes = fields.Text()

    def start_course(self):
        self.status = 'in_process'

    #------------SESSION-SMART-BUTTON-METHODS------------
    @api.depends('session_ids')
    def get_session_count(self):
        count = 0
        for record in self:
            for line in record.session_ids:
                count += 1
            record['session_count'] = count

    def action_view_sessions(self):
        return {
            'name': "Sesiones",
            'domain': ['generation_id', '=', self.id],
            'view_type': 'form',
            'res_model': 'courses.generations.sessions',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act.window',
        }

    #------------ASSIGNMENT-SMART-BUTTON-METHODS------------
    @api.depends('assignment_ids')
    def get_assignment_count(self):
        count = 0
        for record in self:
            for line in record.assignment_ids:
                count += 1
            record['assignment_count'] = count

    def action_view_assignments(self):
        return {
            'name': "Tareas",
            'domain': ['generation_id', '=', self.id],
            'view_type': 'form',
            'res_model': 'courses.generations.assignments',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act.window',
        }

class Session(models.Model):
    _name = "courses.generations.sessions"
    _description = "Sesiones"

    name = fields.Char(string="Nombre")
    generation_id = fields.Many2one('courses.generations', string="Generación")



class Assignment(models.Model):
    _name = "courses.generations.assignments"
    _description = "Tareas"

    name = fields.Char(string="Nombre")
    grade = fields.Float(string="Calificación")

    due_date = fields.Datetime("Fecha de Entrega")
    #student_ids = fields.Many2many('courses.students', 'Alumnos', 'students_id', 'assignment_id', 'Alumnos Asignados')
    generation_id = fields.Many2one('courses.generations', string="Generación")

