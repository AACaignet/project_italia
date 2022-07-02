# -*- coding: utf-8 -*-
# from odoo import http


# class ProvaMagazzino(http.Controller):
#     @http.route('/prova_magazzino/prova_magazzino', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/prova_magazzino/prova_magazzino/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('prova_magazzino.listing', {
#             'root': '/prova_magazzino/prova_magazzino',
#             'objects': http.request.env['prova_magazzino.prova_magazzino'].search([]),
#         })

#     @http.route('/prova_magazzino/prova_magazzino/objects/<model("prova_magazzino.prova_magazzino"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('prova_magazzino.object', {
#             'object': obj
#         })
