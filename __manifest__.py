# -*- coding: utf-8 -*-
{
    'name': "opencinema",

    'summary': """
        Módulo para la gestión de películas
        """,

    'description': """
        Este módulo permite gestionar los datos de películas ...
    """,

    'author': "Jorge Vilariño Cagiao",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    'application': True, 

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/opencinema.xml',
        'views/views.xml',
        'views/reports.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
