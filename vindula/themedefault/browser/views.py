# -*- coding: utf-8 -*-
from five import grok
from zope.interface import Interface

import requests

class LoadScssView(grok.View):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('load-scss')

    def render(self):
        return 'OK'

    def load(self):
        uri = '/vindula-api/theme/load_scss/'
        result = ''

        # import pdb;pdb.set_trace()
        url = self.context.portal_url() + uri
        scss = requests.get(url)
        result = scss.text.replace('/>',' id="new-theme" />')



        return result
