# -*- coding: utf-8 -*-
# from odoo import http


# class WebsiteFirenor(http.Controller):
#     @http.route('/website_firenor/website_firenor', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_firenor/website_firenor/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_firenor.listing', {
#             'root': '/website_firenor/website_firenor',
#             'objects': http.request.env['website_firenor.website_firenor'].search([]),
#         })

#     @http.route('/website_firenor/website_firenor/objects/<model("website_firenor.website_firenor"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_firenor.object', {
#             'object': obj
#         })

