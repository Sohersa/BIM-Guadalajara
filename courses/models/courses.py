#-*- coding: utf-8 -*-

from odoo import models, fields, api


class Courses(models.Model):
    _name = 'courses.courses'
    _description = 'Courses'
    #_inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char()
    notes = fields.Text()

    #Generations count computed field
    generations_count = fields.Integer(string="Cantidad de Generaciones", readonly="true")

    #Total counters for every course
    students_total = fields.Integer(string="Alumnos", readonly="1")
    in_course_total = fields.Integer(string="Cursando", readonly="1")
    pending_project_total = fields.Integer(string="Proyecto Pendiente", readonly="1")
    approved_total = fields.Integer(string="Aprovados", readonly="1")
    failed_total = fields.Integer(string="Reprobados", readonly="1")

    #photo for course
    photo = fields.Image(string="Foto", help="Foto de curso")

    #Relational field to generations model
    generations_ids = fields.One2many('courses.generations', 'course_id', string="Generaciones")