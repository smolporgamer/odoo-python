# -*- coding: utf-8 -*-
{
    'name': "Animals App",
    'version': "0.0.0",
    'summary': """ An Animals App """,
    'description': """ Animals App only """,
    'author': "Digital Transformation Team - Emmanuel Louis V. Gonzaga",
    'category': "Animals",
    'website': "www.cfbtools.app",
    'maintainer': "Emmanuel Louis V. Gonzaga",
    'sequence': 1,
    'depends': ['base', 'base_setup'],
    'data': [
        "views/animals_menus.xml",
    ],
    'assets': {
        'web.assets_backend': [
            'animals/static/src/components/*/*.js',
            'animals/static/src/components/*/*.xml',
        ],
    },
    'application': True,
    'auto_install': True,
    'installable': True,
    'license': "LGPL-3"
}
