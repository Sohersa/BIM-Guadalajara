#-*- coding: utf-8 -*-

from odoo import models, fields, api


class Student(models.Model):
    _name = "courses.students"
    _description = "Students"
#   _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(related='partner_id.name', string="Nombre", store="True", readonly="True")
    notes = fields.Text()

#   Partner fields related to student
    partner_id = fields.Many2one('res.partner', string="Contacto", required="True")
    partner_phone = fields.Char(related='partner_id.phone', string="Teléfono", store="True")
    partner_email = fields.Char(related='partner_id.email', string="Correo Electrónico", store="True")
    partner_country = fields.Many2one('res.country', related='partner_id.country_id', string="País", store="True")
    partner_company = fields.Many2one('res.partner', related='partner_id.parent_id', string="Empresa", store="True")
    partner_city = fields.Char(related='partner_id.city', string="Ciudad", store="True")
    partner_function = fields.Char(related='partner_id.function', string="Puesto de Trabajo", store="True")
    partner_title = fields.Many2one('res.partner.title', related='partner_id.title', string="Profesión", store="True")


    #student information
    origin = fields.Selection([
        ('company', 'Empresa'),
        ('individual', 'Individual')]
        , 'Origen')

    state = fields.Selection([
        ('in_course', 'Cursando'),
        ('pending_project', 'Proyecto Pendiente'),
        ('aprobado', 'Aprobado'),
        ('reprobado', 'Reprobado')]
        , 'Estado Académico')

    generation_id = fields.Many2one('courses.generations', string="Generación")
    group_id = fields.Many2one('courses.student_groups', string="Grupo")
    team_id = fields.Many2one('courses.student_teams', string="Equipo")
    assignments_ids = fields.Many2many('courses.assignments', 'Tareas', 'assignment_id', 'students_id', 'Tareas Asignadas')
    grade = fields.Float(string="Calificación")
    diploma = fields.Binary("Diploma")


class StudentGroup(models.Model):

    _name = "courses.student_groups"
    _description = "Student Groups"
#   _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Nombre", store="True")

    students_count = fields.Integer(string="Cantidad Alumnos", readonly="1")
    in_course_count = fields.Integer(string="Cursando", readonly="1")
    pending_project_total = fields.Integer(string="Proyecto Pendiente", readonly="1")
    approved_count = fields.Integer(string="Aprobados", readonly="1")
    failed_count = fields.Integer(string="Reprobados", readonly="1")

    partner_id = fields.Many2one('res.partner', string="Representante")

    generation_id = fields.Many2one('courses.generations', string="Curso")
    student_ids = fields.One2many('courses.students', 'group_id', string="Alumnos")
    
class StudentTeam(models.Model):
    _name = "courses.student_teams"
    _description = "Equipos de Alumnos"
    
    name = fields.Char(string="Nombre")
    team_members = fields.Integer(string="Cantidad de Integrantes") #computado
    team_grade = fields.Float(string="Promedio General")

    generation_id = fields.Many2one('courses.generations', string="Generación")
    student_ids = fields.One2many('courses.students', 'team_id', string="Integrantes")

    
    
    
    
    
    
    
    
    
    
    
    
    