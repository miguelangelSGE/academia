# -*- coding: utf-8 -*-
{
    'name': "academia",

    'summary': """
        Módulo para la gestión de cursos de formación en la empresa""",

    'description': """
        Módulo para la gestión de cursos de formación en la empresa
    """,

    'author': "Chirinia Models",
    'website': "www.chiriniamodels.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.7',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'academia.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}