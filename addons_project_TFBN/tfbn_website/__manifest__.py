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
{
    'name': "TFBN Website",

    'summary': """
        This module contains the website of the TFBN.""",

    'description': """
        The Website of the TFBN includes static pages, menu configuration items, and styling.
    """,

    'author': "Marc Lijour",
    'website': "https://www.linkedin.com/in/marclijour/",
    'license': "AGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 
				'website', 
				'theme_default',	# we need the plain bootstrap theme
				],

    # always loaded
    'data': [
        'views/template-homepage.xml',
        'views/template-layout_footer_copyright.xml',
        'views/template-footer_default.xml',
        'views/template-about-us.xml',
        'views/template-programs_and_services.xml',
        'views/template-membership.xml',
    ],

    "auto_install": False,
    "installable": True,
}

