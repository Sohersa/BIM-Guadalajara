#-*- coding: utf-8 -*-
from odoo import http


class Courses(http.Controller):
    @http.route('/courses/course/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/courses/course/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('courses.listing', {
            'root': '/courses/courses',
            'objects': http.request.env['courses.courses'].search([]),
         })

    @http.route('/courses/course/objects/<model("courses.course"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('courses.object', {
            'object': obj
         })
