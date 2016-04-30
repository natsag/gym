# -*- coding: utf-8 -*-
{
    'name': "gym",

    'summary': """
	Modulo de gestión de membresias de gimnasio.        
	""",

    'description': """
        Te permite llevar el control de los miembros del gimnasio de una manera sencilla y mínima
    """,

    'author': "SIISCAD",
    'website': "http://siiscad.com.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
	'views/miembros.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
