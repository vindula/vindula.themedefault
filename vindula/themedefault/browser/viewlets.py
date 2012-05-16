# -*- coding: utf-8 -*-
from five import grok
from zope.interface import Interface
from plone.app.layout.viewlets.interfaces import IPortalHeader, IAboveContent, IPortalFooter
from Products.CMFCore.utils import getToolByName
from zope.app.component.hooks import getSite


from Products.CMFPlone import utils
from Products.CMFPlone.browser.navigation import get_view_url
from plone.app.layout.navigation.root import getNavigationRoot

grok.context(Interface) 

# Viewlet for portal logo top

class LogoTopViewlet(grok.Viewlet): 
    grok.name('vindula.themedefault.logotop') 
    grok.require('zope2.View')
    grok.viewletmanager(IPortalHeader) 


class FaviconTopViewlet(grok.Viewlet): 
    grok.name('vindula.themedefault.favicon') 
    grok.require('zope2.View')
    grok.viewletmanager(IPortalHeader)     
    
    def getConfigurador(self):
        if 'control-panel-objects' in  getSite().keys():
            control = getSite()['control-panel-objects']
            if 'vindula_themeconfig' in control.keys():
                confg = control['vindula_themeconfig']
                try:
                    return confg.getFavicon().absolute_url()
                except:
                    return None
            else:
                return None
        else:
            return None

    def imagem(self):
        conf = self.getConfigurador()
        img = ''
        if conf:
            img = conf
        else:
            img =  getSite().absolute_url() + '/++resource++vindula.themedefault/images/icons/favicon.ico'
        
        return img
    

# Viewlet for portal footer

class FooterViewlet(grok.Viewlet): 
    grok.name('vindula.themedefault.footer') 
    grok.require('zope2.View')
    grok.viewletmanager(IPortalFooter) 

            

# Viewlet for useful links

class UsefulLinksViewlet(grok.Viewlet): 
    grok.name('vindula.themedefault.usefullinks') 
    grok.require('zope2.View')
    grok.viewletmanager(IPortalHeader) 

    def getLinks(self):
        portal = self.context.portal_url.getPortalObject()
        if 'links' in portal.objectIds():
            pasta = portal['links']
            self.pc = getToolByName(self.context, 'portal_catalog')
            links = self.pc(path={'query':'/'.join(pasta.getPhysicalPath())},
                            portal_type='Link',
                            #review_state=('published','internal','external'),
                            sort_on="getObjPositionInParent")
            
            if links:
                L = []
                for link in links:
                    L.append(link.getObject())
                return L
        
        else:
            return []

# Viewlet for menu and sub menu

class MenuViewlet(grok.Viewlet): 
    grok.name('vindula.themedefault.menu') 
    grok.require('zope2.View')
    grok.viewletmanager(IAboveContent) 

    def getContentTypes(self):
        portal = self.context.portal_url.getPortalObject()
        if 'control-panel-objects' in portal.keys():
            control = portal['control-panel-objects']
            if 'vindula_themeconfig' in control.keys():
                thema = control['vindula_themeconfig']    
                
                try:itens = thema.getItens_menu()
                except:itens = None
                
                if itens:
                    return itens
                else:
                    return ['Folder', 'Link']

            return ['Folder', 'Link']
        else:
            return ['Folder', 'Link']
        
    def getUseDropDown(self):
        result = False
        portal = self.context.portal_url.getPortalObject()
        if 'control-panel-objects' in portal.keys():
            control = portal['control-panel-objects']
            
            if 'vindula_themeconfig' in control.keys():
                thema = control['vindula_themeconfig']    
                
                try:result = thema.getAtiva_menudropdown()
                except:result = False

            return result
        else:
            return result
    
    def getQueryMenu(self, path):
        portal_properties = getToolByName(self.context, 'portal_properties')
        navtree_properties = getattr(portal_properties, 'navtree_properties')
        
        if navtree_properties.getProperty('enable_wf_state_filtering', False):
            state = navtree_properties.getProperty('wf_states_to_show', ['published','internal'])
        else:
            state = ['published','internal']        
                

        ctool = getSite().portal_catalog
        itens = ctool(portal_type = self.getContentTypes(), 
                     review_state = state,
                     path={'query': path, 'depth': 1},
                     sort_on = 'getObjPositionInParent')
        
        return itens

    def getMenu(self):
        portal = self.context.portal_url.getPortalObject()
        menus = self.getQueryMenu('/'.join(portal.getPhysicalPath()))
        
        if menus:
            L = []
            for obj in menus:
                if self.checkObj(obj.getObject()):
                    L.append(obj.getObject())
            return L
        
    def getSubMenu(self):
        portal = self.context.portal_url.getPortalObject()
        if self.context.portal_type == 'HomePage':
            if self.context.getRef_itemMenu():
                context = self.context.getRef_itemMenu()
            else:
                context = self.context
        else:
            context = self.context
        
        if context != portal:
            while context.aq_parent != portal:
                context = context.aq_parent
            
            submenus = self.getQueryMenu('/'.join(context.getPhysicalPath()))
            
            if submenus:
                L = []
                for obj in submenus:
                    if self.checkObj(obj.getObject()):
                        L.append(obj.getObject())
                return L

    def getSubMenuDrop(self, tab, nivel = 1):
        result=[]
        portal_properties = getToolByName(self.context, 'portal_properties')
        navtree_properties = getattr(portal_properties, 'navtree_properties')
        
        # Get ids not to list and make a dict to make the search fast
        idsNotToList = navtree_properties.getProperty('idsNotToList', ())
        excludedIds = {}
        for id in idsNotToList:
            excludedIds[id]=1

        try:  
            rootPath = getNavigationRoot(self.context)
            dpath='/'.join([rootPath,tab.id])
        except:
            url = tab['url'].split('/')
            plone_site = getSite()
            dpath = '/'
            if url[3] != plone_site.id:
                dpath += plone_site.id+'/'
            dpath += '/'.join(url[3:])
        
        rawresult = self.getQueryMenu(dpath)

        # now add the content to results
        for item in rawresult:
            if not (excludedIds.has_key(item.getId) or item.exclude_from_nav):
                id, item_url = get_view_url(item)
                data = {'name'       : utils.pretty_title_or_id(self.context, item),
                        'id'         : item.getId,
                        'url'        : item_url,
                        'description': item.Description}
                result.append(data)
        return result

    def checkObj(self, obj):
        roles = self.context.portal_membership.getAuthenticatedMember().getRoles()
        state = getToolByName(obj, 'portal_workflow').getInfoFor(obj, 'review_state', None)
        try:
            if obj.getExcludeFromNav() == True:
                return False
        except:
            try:
                if obj.exclude_from_nav == True:
                    return False
            except:
                return False
        
        if 'Anonymous' in roles and state == 'private':
            return False
        return True

        
    def isSelected(self, obj):
        if self.context.portal_type == 'HomePage':
            if self.context.getRef_itemMenu():
                try:
                    if obj.absolute_url() ==  self.context.getRef_itemMenu().absolute_url() or\
                       obj.absolute_url() in self.context.REQUEST.get('ACTUAL_URL'):
                        return 'selected'
                except:
                    if obj['url'] == self.context.getRef_itemMenu().absolute_url() or\
                       obj['url'] in self.context.REQUEST.get('ACTUAL_URL'):
                        return 'selected'
        try:
            if obj.absolute_url() in self.context.REQUEST.get('ACTUAL_URL'):
                return 'selected'
        except:
            if obj['url'] == self.context.REQUEST.get('ACTUAL_URL'):
                return'selected'
    
    def isSelectedSubmenu(self, obj):
        obj_url = obj.absolute_url().split('/')
        url = self.context.REQUEST.get('ACTUAL_URL').split('/')
        if (obj.id in url and obj_url.index(obj.id) == url.index(obj.id))or\
            self.context.id == obj.id:
            return 'selected'
        
        
class BannerViewlet(grok.Viewlet): 
    grok.name('vindula.themedefault.banner') 
    grok.require('zope2.View')
    grok.viewletmanager(IAboveContent) 
