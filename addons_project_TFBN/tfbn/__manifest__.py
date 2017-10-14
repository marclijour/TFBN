# -*- coding: utf-8 -*-
#	The TFBN Application (tfbn) is an Odoo module that encapsulates the features required on top of the base community version.
#   This version is compatible with Odoo version 11.0.
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

{
    'name': "TFBN Application",

    'summary': """
        Encapsulates the features and enhancements to Odoo Community (base) required by TFBN
    """,

    'description': """
        This application includes a website, a membership management system (users can register and pay online, while the system invoice them and keeps track of their status), and members-only features such as a private forum.
    """,

    'author': "Marc Lijour",
    'website': "https://www.linkedin.com/in/marclijour/",
    'license': "AGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Specific Industry Applications',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'l10n_ca',      # base Odoo and Canadian context (incl. accounting)
                'website',              # the website builder
                'website_embed',        # paid module to add third-party boostrap snippets
                'auth_signup',          # allows user to self-register
                'membership',           # to manage memberships
##                'website_crm',          # adds contact form, and pulls in crm, website_form, website_partner
#                'website_sale',        # pulls in 'sale', 'website', 'payment', etc
#                'payment_paypal',      # pulls in 'payment'
#                'website_event',       # pulls in 'event', 'website'
#                'account_accountant',  # Accounting & Finance: bank sync, P&L reports, etc
#                'website_forum',       # member-only forum
                               ],


    # always loaded
    'data': [
        # 'security/ir.model.access.csv', TODO later
        'views/set_config_parameters.xml',  # programmatically set config parameters (company, data, favicon, config, etc)
        'views/signup_member.xml',          # tailors the auth_signup form HTML for TFBN needs
        'views/extended-res_partner_form.xml',    # to display the information from the members panel in Odoo
    ],
    
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}

