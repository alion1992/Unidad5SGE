# -*- coding: utf-8 -*-
{
    'name': "Clientes Renta",

    'summary': "Este módulo va a conseguir calcular el salario neto de una persona.",

    'description': """
Long description of module's purpose
    """,

    'author': "Francisco Alía",
    'website': "www.company.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

