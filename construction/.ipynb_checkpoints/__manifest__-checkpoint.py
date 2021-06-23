# -*- coding: utf-8 -*-
{
    'name': "Construction",

    'summary': """
        This constructuion app is used to manage the resourses involved in a construction project (clients, machinery, materials, projects and more)""",

    'description': """
        This constructuion app is used to manage the resourses involved in a construction project (clients, machinery, materials, projects and more)
    """,

    'author': "Grupo Sohersa",
    'website': "http://www.sohersabim.com",
    'images': [
        'static/description/icon.png',
        'static/src/img/icon.png'
    ],
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services/construction',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base'
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/workforce_views.xml',
        'views/projects_views.xml',
        'views/catalogs_views.xml',
        'views/clients_views.xml',
        'views/materials_views.xml',
        'views/machinery_views.xml',
        'views/suppliers_views.xml',
        'views/bim_views.xml',
        'views/assets.xml'
    ],
    
    'qweb': [
        'static/src/xml/*.xml'
    ],
    
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    
    'installable': True,
    'auto_install': False,
    'application': True,
}
