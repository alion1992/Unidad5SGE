# -*- coding: utf-8 -*-
# from odoo import http


# class Renta(http.Controller):
#     @http.route('/renta/renta', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/renta/renta/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('renta.listing', {
#             'root': '/renta/renta',
#             'objects': http.request.env['renta.renta'].search([]),
#         })

#     @http.route('/renta/renta/objects/<model("renta.renta"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('renta.object', {
#             'object': obj
#         })

