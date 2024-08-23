# -*- coding: utf-8 -*-
{
    'name': "Firenor Theme",
    'summary': "A dynamic and visually captivating theme tailored for professional quality management systems.",
    'description': """
The Firenor Theme brings a modern, clean, and professional design to Odoo 17, crafted specifically for businesses adhering to quality management standards. 
With a custom color palette, including signature colors like #c4122f and #47a5ae, and thoughtfully structured SCSS variables, this theme ensures consistency and brand alignment across your Odoo environment.
Built to seamlessly integrate with FIRENOR's documentation style, the Firenor Theme is ideal for companies prioritizing both aesthetics and functionality in their Odoo interface.
"""
    ,

    'author': "Romualdo Jr",
    'website': "https://github.com/CodeRomz/website_firenor.git",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website/Theme',
    'version': '17.0.0.0.0',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    'assets': {
        # 'web._assets_primary_variables': [
        #     ('prepend', 'website_firenor/static/src/scss/primary_variables.scss'),
        # ],
        'web.assets_backend': [
            'website_firenor/static/src/scss/primary_variables.scss',
        ],
        'web.assets_frontend': [
            'website_firenor/static/src/scss/primary_variables.scss',
        ],
        'website.assets_editor': [
            'website_firenor/static/src/scss/primary_variables.scss',
        ],
    },
}
