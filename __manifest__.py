# -*- coding: utf-8 -*-
{
    'name': "viewtractor",

    'summary': """
       Herencia de template del Home del Sitio Web""",

    'description': """
       Con este módulo, importamos la página inicial (home) de una página mediante
       una herencia de template (views/homeview.xml).
    """,

    'author': "rexuswolf",
    'website': "github.com/rexuswolf",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Importación',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    'depends': ['website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/home.xml',
        'views/newpage.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}