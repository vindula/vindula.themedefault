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



class MacroLogoTopView(grok.View):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('vindula-macro-logotop')

    url = "/++resource++vindula.controlpanel/imagens/logo_topo.png"

    def render(self):
        return 'OK'

    def getOrgStrucContent(self):
        ctx = self.context.restrictedTraverse('OrgStruct_view')()
        portal = self.context.portal_url.getPortalObject();
        config_obj = portal['control-panel-objects']['ThemeConfig'];

        D = {}
        if ctx.portal_type != 'Plone Site':
            if ctx.activ_personalit:
                D['id'] = ctx.id
                if ctx.getLogoPortal():
                    D['url'] = ctx.getLogoPortal().absolute_url()
                else:
                    if config_obj.getLogoCabecalho():
                        D['url']  =  config_obj.getLogoCabecalho().absolute_url()
                    else:
                        D['url']  = self.url
        return D


class MacroFooterView(MacroLogoTopView):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('vindula-macro-footer')

    url = "/++resource++vindula.controlpanel/imagens/logo_rodape.png"

