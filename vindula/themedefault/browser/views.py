# -*- coding: utf-8 -*-
import requests
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from Products.Five import BrowserView
from five import grok
from vindula.myvindula.cache import *
from zope.component import getMultiAdapter
from zope.interface import Interface, implements

from vindula.themedefault.browser.interfaces import IThemeVindulaView


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
            return "columns large-12 medium-12"
        elif sl and sr:
            # In case we have both columns, content takes 50% of the whole
            # width and the rest 50% is spread between the columns
            return "columns large-6 medium-12"
        else:
            return "columns large-9 medium-9"



class ToolsView(grok.View):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('tools_viewlet')


    def render(self):
        return 'ok'


    def hasPermission(self, user, obj):

        def merge_permisson(user_roles,user,obj):
            def merge(list1,list2):
                for i in list2:
                    if not i in list1:
                        list1.append(i)
                return list1

            if obj:
                user_roles = merge(user_roles, user.getRolesInContext(obj))
                if obj.portal_type == "Layout":
                    for item in obj.values():
                        user_roles = merge_permisson(user_roles,user,item)
            return user_roles

        user_roles = merge_permisson([],user,obj)

        if obj.portal_type == 'LayoutLoad':
            user_roles = merge_permisson(user_roles,user,obj.getObj_layout())
            user_roles = merge_permisson(user_roles,user,obj.getObj_layout_B())
            user_roles = merge_permisson(user_roles,user,obj.getObj_layout_C())
            user_roles = merge_permisson(user_roles,user,obj.getObj_layout_topo())

        for i in ['editPortlet', 'Editor', 'Contributor', 'Reviewer','Manager']:
            if i in user_roles:
                return True

        return False


class LoadScssView(grok.View):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('load-scss')

    def render(self):
        return 'OK'

    def load(self):
        key = hashlib.md5('LoadScss').hexdigest()
        key = 'LoadScssView:load:%s' % key

        cached_data = get_redis_cache(key)

        if cached_data:
            result = cached_data
        else:
            uri = '/vindula-api/theme/load_scss/'
            result = ''

            url = self.context.portal_url() + uri

            scss = requests.get(url)
            result = scss.text.replace('/>',' id="new-theme" />')

            set_redis_cache(key, 'LoadScssView:load:keys', result)

        return result

class MacroLogoTopView(grok.View):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('vindula-macro-logotop')

    url = "/++resource++vindula.controlpanel/imagens/logo_topo.png"

    def render(self):
        return 'OK'

    def getOrgStrucContent(self):
        return {}

        # ctx = self.context.restrictedTraverse('OrgStruct_view')()
        # portal = self.context.portal_url.getPortalObject();
        # config_obj = portal['control-panel-objects']['ThemeConfig'];

        # D = {}
        # if ctx.portal_type != 'Plone Site':
        #     if ctx.activ_personalit:
        #         D['id'] = ctx.id
        #         if ctx.getLogoPortal():
        #             D['url'] = ctx.getLogoPortal().absolute_url()
        #         else:
        #             if config_obj.getLogoCabecalho():
        #                 D['url']  =  config_obj.getLogoCabecalho().absolute_url()
        #             else:
        #                 D['url']  = self.url
        # return D


class MacroFooterView(MacroLogoTopView):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('vindula-macro-footer')

    url = "/++resource++vindula.controlpanel/imagens/logo_rodape.png"

    def getObjectThemeConfig(self):
        portal = self.context.portal_url.getPortalObject()
        theme_config = None
        if 'control-panel-objects' in portal.keys():
            control = portal.get('control-panel-objects')
            if 'ThemeConfig' in control.keys():
                theme_config = control.get('ThemeConfig')
        return theme_config


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
            for item in result:
                D = {}
                obj = item.getObject()
                D['obj'] = obj
                D['subitens'] = obj.values()

                L.append(D)

        return L


class NewHomePageView(grok.View):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('new-home')

class SectionsMenuView(grok.View):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('sections-menu')

    def render(self):
        pass

    def getIsProfile(self):
        url_split = self.request.URL.split('/')
        for part in url_split:
            if 'myvindulalistuser' in part:
                return 'pessoas'
        return ''

class TextFooterView(grok.View):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('view_text_footer')


    def getTextFooter(self):
        portal = self.context.portal_url.getPortalObject()
        text = ''

        if 'control-panel-objects' in portal.keys():
            control = portal.get('control-panel-objects')
            if 'ThemeConfig' in control.keys():
                theme_config = control.get('ThemeConfig')
                text = theme_config.getText()

        return text


    def getOrgStru(self,ctx):
        portal = getToolByName(ctx, 'portal_url').getPortalObject()

        if ctx != portal and ctx.portal_type != 'OrganizationalStructure':
            try:
                return self.getOrgStru(ctx.aq_parent)
            except:
                pass

        elif ctx.portal_type == 'OrganizationalStructure':
            return ctx
            # if ctx.activ_personalit:
            #     return ctx
            # else:
            # try:return self.getOrgStru(ctx.aq_parent)
            # except:pass

        return ctx



class TopoBarraView(grok.View):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('topo_barra_view')

    def getTopoBarra(self):
        portal = self.context.portal_url.getPortalObject()
        html = ''
        if 'control-panel-objects' in portal.keys():
            control = portal.get('control-panel-objects')
            if 'ThemeConfig' in control.keys():
                theme_config = control.get('ThemeConfig')
                html = theme_config.getHTML_header()
        return html
