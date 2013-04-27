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


class ManageLinksUserView(grok.View):
    grok.name('vindula-linkuser')
    grok.require('zope2.View')
    grok.context(Interface)

    def render(self):
        return "OK"

    def update(self):
        portal = self.context.portal_url.getPortalObject()
        workflow = portal['portal_workflow']

        membership = self.context.portal_membership
        groups = self.context.portal_groups

        user_login = membership.getAuthenticatedMember()
        user_groups = [i.id for i in groups.getGroupsByUserId(user_login.id) if i]

        L = []
        if 'control-panel-objects' in portal.keys():
            control = portal['control-panel-objects']
            if 'link-user-folder' in control.keys():
                folder_links = control['link-user-folder']
                links = folder_links.objectValues()
                for link in links:
                    checa = False
                    if workflow.getInfoFor(link, 'review_state') == 'published':
                       checa = True
                    else:
                        if 'Manager' in user_login.getRoles():
                            checa = True
                        else:
                            for roles in link.get_local_roles():
                                if user_login.id in roles:
                                    checa = True
                                else:
                                    for group in user_groups:
                                        if group in roles:
                                            checa = True
                                            break

                    if checa:
                        D ={}
                        D['url'] = link.getRemoteUrl()
                        D['id'] = link.id
                        try:
                            if link.getInternal_link():
                                D['url'] = link.getInternal_link().absolute_url()
                        except:
                            pass
                        D['title'] = link.Title()
                        L.append(D)

        return L