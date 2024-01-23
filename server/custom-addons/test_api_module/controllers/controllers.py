# -*- coding: utf-8 -*-
# from odoo import http


# class TestApiModule(http.Controller):
#     @http.route('/test_api_module/test_api_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_api_module/test_api_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_api_module.listing', {
#             'root': '/test_api_module/test_api_module',
#             'objects': http.request.env['test_api_module.test_api_module'].search([]),
#         })

#     @http.route('/test_api_module/test_api_module/objects/<model("test_api_module.test_api_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_api_module.object', {
#             'object': obj
#         })

