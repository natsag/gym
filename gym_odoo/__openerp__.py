# -*- coding: utf-8 -*-
{
    'name': "miGym_dev",

    'summary': """
        Administre su gimnasio con odoo.
        Versión de desarrollo.
        """,

    'description': """
        Aplicación para control de suscripciones en gimnasios
    """,

    'author': "SIISCAD",
    'website': "http://www.siiscad.com.mx",

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
        'views/miembros.xml',
        'views/suscripciones.xml',
        'views/opciones.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
