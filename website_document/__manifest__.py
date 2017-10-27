# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015- Vertel AB (<http://www.vertel.se>).
#
#    This progrupdateam is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Website Document',
    'category': 'knowledge',
    'website': 'https://www.vertel.se',
    'summary': 'Controller for download attachments',
    'version': '1.0',
    'description': """

Use this url:

/attachment/<model("ir.attachment"):attachment>/<string:file_name>

Attachement are Odoo-attachment
Filename are used only for display purposes.

""",
    'author': 'Vertel AB',
    'depends': [
        'website',
        'document',
    ],
    'data': [ ],
    'qweb': [],
    'installable': True,
}
