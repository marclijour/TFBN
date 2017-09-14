# -*- coding: utf-8 -*-
#   The TFBN Application (tfbn) is an Odoo module that encapsulates the features required on top of the base community version.
#   Copyright (C) 2017 Marc Lijour
#   https://www.linkedin.com/in/marclijour
#   https://github.com/marclijour
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
        _logger.info(qcontext.get('policy'))
        assert qcontext.get('policy') != 'checked', "You need to accept the terms and conditions to become a member."
        assert values.values(), "The form was not properly filled in."
        assert values.get('password') == qcontext.get('confirm_password'), "Passwords do not match; please retype them."
        supported_langs = [lang['code'] for lang in request.env['res.lang'].sudo().search_read([], ['code'])]
        if request.lang in supported_langs:
            values['lang'] = request.lang
        self._signup_with_values(qcontext.get('token'), values) # calls signup() on ResUsers, then authenticates or fails
        request.env.cr.commit()



