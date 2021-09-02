#-*- coding: utf-8 -*-

from odoo import models, fields, api


class courses(models.Model):
    _name = 'courses.courses'
    _description = 'Courses'
    
    name = fields.Char()
    notes = fields.Text()
    #Generations count computed field
    generations_count = fields.Integer(string="Cantidad de Generaciones", readonly="true")

    #Total counters for every course
    students_total = fields.Integer(string="Alumnos")
    in_course_total = fields.Integer(string="Cursando")
    pending_project_total = fields.Integer(string="Proyecto Pendiente")
    approved_total = fields.Integer(string="Aprovados")
    failed_total = fields.Integer(string="Reprobados")

    #photo for course
    photo = fields.Image(string="Foto", help="Foto de curso")

    #Relational field to generations model
    generations_ids = fields.One2many('courses.generations', 'course_id', string="Generaciones")