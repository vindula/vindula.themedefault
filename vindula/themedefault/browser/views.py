# -*- coding: utf-8 -*-
from five import grok
from Acquisition import aq_inner
from zope.component import getMultiAdapter
from zope.interface import Interface
from zope.interface import implements
from Products.Five import BrowserView

from vindula.themedefault.browser.interfaces import IThemeVindulaView

import requests

class ThemeVindulaView(BrowserView):
    implements(IThemeVindulaView)

    # Utility methods
    def getColumnsClass(self, view=None):
        context = aq_inner(self.context)
        plone_view = getMultiAdapter((context, self.request), name=u'plone')
        sl = plone_view.have_portlets('plone.leftcolumn', view=view);
        sr = plone_view.have_portlets('plone.rightcolumn', view=view);
        portal_state = getMultiAdapter((context, self.request), name=u'plone_portal_state')

        if not sl and not sr:
            # we don't have columns, thus conten takes the whole width
            return "columns large-12"
        elif sl and sr:
            # In case we have both columns, content takes 50% of the whole
            # width and the rest 50% is spread between the columns
            return "columns large-6"
        else:
            return "columns large-9"

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

class ManageTopicFooterView(grok.View):
    grok.name('vindula_topicfooter_view')
    grok.require('zope2.View')
    grok.context(Interface)

    def render(self):
        return "OK"

    def update(self):
        portal = self.context.portal_url.getPortalObject()
        p_catalog = portal.portal_catalog
        context = self.context
        L = []

        query = {}
        query['portal_type'] = ['FooterTopic']
        query['sort_order'] = 'descending'
        query['sort_on'] = 'getObjPositionInParent'
        # query['review_state'] = ['published', 'external','internal']

        result = p_catalog(**query)
        if result:
            # import pdb; pdb.set_trace()
            for item in result:
                D = {}
                obj = item.getObject()
                D['obj'] = obj
                D['subitens'] = obj.values()

                L.append(D)

        return L