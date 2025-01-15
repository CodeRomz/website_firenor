# -*- coding: utf-8 -*-
{
    'name': "Firenor Theme",
    'summary': "",
    'description': """
The Firenor Theme brings a modern, clean, and professional design to Odoo 17, crafted specifically for businesses adhering to quality management standards. 
With a custom color palette, including signature colors like #c4122f and #47a5ae, and thoughtfully structured SCSS variables, this theme ensures consistency and brand alignment across your Odoo environment.
Built to seamlessly integrate with FIRENOR's documentation style.
"""
    ,

    'author': "Romualdo Jr",
    'website': "https://github.com/CodeRomz/website_firenor.git",
    'category': 'Theme/Firenor',
    'version': '17.0.1.0.0',
    'license': 'LGPL-3',
    'depends': ['website', 'website_slides'],

    # always loaded
    'data': [
    ],
    'assets': {
        'web.assets_backend': [
            'website_firenor/static/src/scss/firenor_style_backend.scss',
        ],
        'web.assets_frontend': [
            'website_firenor/static/src/scss/firenor_style_frontend.scss',
        ]
    },
}
