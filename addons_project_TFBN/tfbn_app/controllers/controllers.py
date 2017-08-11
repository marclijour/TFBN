# -*- coding: utf-8 -*-
#	The TFBN Application (tfbn_app) is an Odoo module that encapsulates the features required on top of the base community version.
#	Copyright (C) 2017 Marc Lijour
#   https://www.linkedin.com/in/marclijour
#   https://github.com/marclijour
#
#	This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.

from odoo import http

from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.http import request
from odoo.addons.auth_signup.models.res_users import SignupError
from odoo.addons.web.controllers.main import ensure_db, Home

import logging
_logger = logging.getLogger(__name__)

class MyAuthSignupHome(AuthSignupHome):

    # Override
    # Adding two required fields to the value dict, to be passed on to ResUser (Odoo base)
    # The rest is the same
    def do_signup(self, qcontext):
        """ Shared helper that creates a res.partner out of a token """
        values = { key: qcontext.get(key) for key in ('login', 'name', 'password', 
                                                      'company_name', 'function' # Added two fields
                                                     ) }
        assert values.values(), "The form was not properly filled in."      # TODO check AssertionError in web_auth_signup() --working?
        assert values.get('password') == qcontext.get('confirm_password'), "Passwords do not match; please retype them."
        supported_langs = [lang['code'] for lang in request.env['res.lang'].sudo().search_read([], ['code'])]
        if request.lang in supported_langs:
            values['lang'] = request.lang
        self._signup_with_values(qcontext.get('token'), values) # calls signup() on ResUsers, then authenticates or fails
        request.env.cr.commit()

    # TODO set commercial_company_name after user is registered (may need to access partner first)

    # TODO add a check box to signify acceptance of t&cs for the TFBN system 
    #           + prohibit registration in case box is not checked (e.g. gray out the signup button)

    # TODO make safer
    # - forbid registered users to register again (check login=email, and if exists then send to login instead + error msg) -check the try-catch in web_auth_signup()
    # - check the display of error messages inline (e.g. when passwords don't match) --this is done through assertions above

# class TfbnMembership(http.Controller):
#     @http.route('/tfbn_membership/tfbn_membership/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tfbn_membership/tfbn_membership/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tfbn_membership.listing', {
#             'root': '/tfbn_membership/tfbn_membership',
#             'objects': http.request.env['tfbn_membership.tfbn_membership'].search([]),
#         })

#     @http.route('/tfbn_membership/tfbn_membership/objects/<model("tfbn_membership.tfbn_membership"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tfbn_membership.object', {
#             'object': obj
#         })
