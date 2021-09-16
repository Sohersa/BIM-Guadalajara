# -*- coding: utf-8 -*-
{
    'name': "courses",

    'summary': """
        Intern course administration system""",

    'description': """
        Course administration system made for intern company purposes. It manage courses,
        students, generations, sessions, assignments and student teams. The module is conected to
        employees and calendar modules for session management 
    """,

    'author': "Sohersa",
    'website': "https://www.sohersabim.com",

    'category': 'Tools',
    'version': '0.1',

    'depends': ['base', 'hr', 'calendar'],

    'data': [
        'security/ir.model.access.csv',
        'views/courses.xml',
        'views/generations.xml',
        'views/students.xml',
        'views/templates.xml',
    ],

    'demo': [
        #'demo/demo.xml',
    ],
}
