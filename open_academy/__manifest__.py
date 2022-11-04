# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Serhii",
    'website': "http://localhost",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customizations',
    'version': '1.0.4',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/open_academy_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'wizards/filling_sessions_views.xml',
        'data/courses_data.xml',
        'views/courses_views.xml',
        'views/sessions_views.xml',
        'data/res_partner_category_data.xml',
        'views/res_partner_views.xml',
        'reports/sessions_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
     #   'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'sequence': -100,
}
