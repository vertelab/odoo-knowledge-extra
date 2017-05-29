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

from cStringIO import StringIO
from openerp import models, fields, api, _
from openerp import SUPERUSER_ID
from openerp import http
from openerp.http import request
#from openerp.http import request
import werkzeug.urls
import logging
_logger = logging.getLogger(__name__)


class WebsiteDocument(http.Controller):

    @http.route(['/attachment/<model("ir.attachment"):attachment>/<string:file_name>'], type='http', auth="public", website=True)
    def get_attachment(self, attachment=None, file_name=None, **post):
        if attachment:
            return http.send_file(StringIO(attachment.datas.decode('base64')), filename=attachment.datas_fname.replace(' ', '_'), mimetype=attachment.mimetype, mtime=attachment.write_date, as_attachment=True)

