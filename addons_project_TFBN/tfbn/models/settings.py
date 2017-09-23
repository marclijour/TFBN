# -*- coding: utf-8 -*-
#	The TFBN Application (tfbn) is an Odoo module that encapsulates the features required on top of the base community version.
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


from odoo import models, fields, api

import os

import logging
_logger = logging.getLogger(__name__)

# To set the company record with TFBN data
class ResCompany(models.Model):
    _inherit = "res.company"

	# from https://www.odoo.com/fr_FR/forum/aide-1/question/how-to-override-your-company-data-through-a-custom-module-in-v8-87510
    # see alternatively https://github.com/netjunky-hub/company_setup/blob/master/company_setup/views/res_company_view.xml
    @api.model
    def set_tfbn_company_data(self):
        _logger.info("> Setting TFBN company data...")
        module_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        img_path = os.path.join(module_dir, 'static/description/icon.png')
        with open(img_path) as img:
            logo = img.read().encode('base64')

        # Look-ups for known address field contents
        id_ontario  = self.env['res.country.state'].search([('name', '=', 'Ontario')]).id
        id_canada = self.env['res.country'].search([('name', '=', 'Canada')]).id

        # Saving the record to the database
        self.browse(1).write({
            'name': u"Toronto French Business Network (TFBN)",
            'rml_header1': u"Driven by its members, for its members",
            'logo': logo,
			'email': u"contact@tfbn.ca", # TODO change this as required
			'website': u"https://www.tfbn.ca",
            'city': u"Toronto",
			'state_id': id_ontario,
            'country_id': id_canada,
            'currency_id': self.env.ref('base.CAD').id, # note: currency_id is also taken care by the l10n_ca module, which sets currency to CAD

        })
        _logger.info("> ... done.")


# To set the company record with TFBN data
class ResWebsiteSettings(models.Model):
    _inherit = "website"

    @api.model
    def set_website_settings(self):
        _logger.info("> Setting Website Configuration")
        module_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        img_path = os.path.join(module_dir, 'static/src/img/favicon-32x32.png')
        with open(img_path) as img:
            favicon = img.read().encode('base64')

        self.browse(1).write({
            'name': u"TFBN Website",
            'favicon': favicon,
        })
        _logger.info("> ... done.")
        # TODO Google Analytics key


# To enable users to register on their own through the auth_signup module
# Use a transient model (aka 'wizard') to set base.config.parameters, ending up in ir.config_parameter
# more info:
# https://www.odoo.com/forum/help-1/question/how-to-change-settings-on-module-installation-72694
# https://www.odoo.com/forum/help-1/question/how-to-save-and-update-custom-settings-in-odoo-transientmodel-93908
# https://github.com/tinyerp/erppeek/issues/85
class ResBaseConfigSettings(models.TransientModel):
    _name = "my.config.settings"   # that's prototype inheritance (vs. class inheritance if omitted)
                                   # see https://www.odoo.com/documentation/10.0/howtos/backend.html#inheritance
    _inherit = "base.config.settings"

    @api.model 
    def set_signup_parameters(self):
        _logger.info("> Settings sign-up parameters")

        settings = self.env['base.config.settings'].create({
            'auth_signup_uninvited': True,
            'auth_signup_reset_password': True,
        })
        settings.execute()
        _logger.info("> ... done.")

#class ResUser(models.Model)
#    _inherit = "res.users"


