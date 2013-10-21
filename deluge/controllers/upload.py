import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from deluge.lib.base import BaseController, render

log = logging.getLogger(__name__)

class UploadController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/upload.mako')
        # or, return a string
        return '<h3>Hello, World!</h3>'

    def foobar(self):
        return 'Foobar %s' % str(request.params.get('id', None))

    def file(self):
        return request.POST['test'].filename
