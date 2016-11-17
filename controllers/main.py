import werkzeug.wsgi
# -*- coding: utf-8 -*-
import os
from openerp.addons.website.controllers.main import Website
from openerp import http
from openerp.http import request
from .. import res_config

app = werkzeug.wsgi.SharedDataMiddleware(http.root.dispatch, {'/staticweb':res_config.WWW__ROOT},
                                         cache_timeout=http.STATIC_CACHE)

http.root.dispatch = http.DisableCacheMiddleware(app)


class Website(Website):
 
    @http.route('/', type='http', auth="public", website=True)
    def index(self, **kw):
        return http.local_redirect('/staticweb/index.html', query=request.params, keep_hash=True)

