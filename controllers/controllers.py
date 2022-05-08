# -*- coding: utf-8 -*-
# from odoo import http


# class OpenCinema(http.Controller):
#     @http.route('/open_cinema/open_cinema/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/open_cinema/open_cinema/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('open_cinema.listing', {
#             'root': '/open_cinema/open_cinema',
#             'objects': http.request.env['open_cinema.open_cinema'].search([]),
#         })

#     @http.route('/open_cinema/open_cinema/objects/<model("open_cinema.open_cinema"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('open_cinema.object', {
#             'object': obj
#         })
