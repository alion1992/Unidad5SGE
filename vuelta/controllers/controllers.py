# -*- coding: utf-8 -*-
# from odoo import http


# class Vuelta(http.Controller):
#     @http.route('/vuelta/vuelta', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vuelta/vuelta/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('vuelta.listing', {
#             'root': '/vuelta/vuelta',
#             'objects': http.request.env['vuelta.vuelta'].search([]),
#         })

#     @http.route('/vuelta/vuelta/objects/<model("vuelta.vuelta"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vuelta.object', {
#             'object': obj
#         })

