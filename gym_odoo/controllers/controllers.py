# -*- coding: utf-8 -*-
from openerp import http

# class Gym(http.Controller):
#     @http.route('/gym/gym/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gym/gym/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gym.listing', {
#             'root': '/gym/gym',
#             'objects': http.request.env['gym.gym'].search([]),
#         })

#     @http.route('/gym/gym/objects/<model("gym.gym"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gym.object', {
#             'object': obj
#         })