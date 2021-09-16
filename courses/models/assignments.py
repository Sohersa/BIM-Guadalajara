#-*- coding: utf-8 -*-

from odoo import models, fields, api

class Assignment(models.Model):
    
    _name = "courses.assignments"
    _description = "Tareas"
    
    name = fields.Char(string="Nombre")
    grade = fields.Float(string="Calificación")
    
    due_date = fields.Datetime("Fecha de Entrega")
    
    student_ids = fields.Many2many('courses.students', 'Alumnos', 'students_id', 'assignment_id', 'Alumnos Asignados')