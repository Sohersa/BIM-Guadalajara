#-*- coding: utf-8 -*-

from odoo import models, fields, api


class student_group(models.Model):
    _name = "courses.students.groups"
    _description = "Student Groups"

    name = fields.Char(string="Nombre", store="True")
    cant_students = fields.Integer(string="Alumnos")

    partner_id = fields.Many2one('res.partner', string="Representante")
    generation_id = fields.Many2one('courses.generations', string="Curso")
    student_ids = fields.One2many('courses.students', 'group_id', string="Alumnos")
