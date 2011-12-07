# -*- coding: utf-8 -*-
from five import grok
from zope.interface import Interface
from plone.app.layout.viewlets.interfaces import IPortalHeader, IAboveContent, IPortalFooter
from Products.CMFCore.utils import getToolByName
from zope.app.component.hooks import getSite

grok.context(Interface) 

# Viewlet for portal logo top

class LogoTopViewlet(grok.Viewlet): 
    grok.name('vindula.themedefault.logotop') 
    grok.require('zope2.View')
    grok.viewletmanager(IPortalHeader) 
    

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
                            review_state='published',
                            sort_on="getObjPositionInParent")
            
            if links:
                L = []
                for link in links:
                    L.append(link.getObject())
                return L
                 

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
                itens = thema.itens_menu
                if itens != []:
                    return itens
                else:
                    return ['Folder', 'Link']

            return ['Folder', 'Link']
        else:
            return ['Folder', 'Link']
    

    def getMenu(self):
        portal = self.context.portal_url.getPortalObject()
        types = self.getContentTypes()
                
        urltool = getSite().portal_url
        caminho = {'query': '/'.join(portal.getPhysicalPath()), 'depth': 1}
        ctool = getSite().portal_catalog
        menus = ctool(portal_type=types, path=caminho, sort_on='getObjPositionInParent')        
        
        #menus = portal.objectValues(['ATFolder','ATLink','vindula.content.content.vindulacontentmacro'])
        if menus:
            L = []
            for obj in menus:
                if self.checkObj(obj.getObject()):
                    L.append(obj.getObject())
            return L
        
    def getSubMenu(self):
        portal = self.context.portal_url.getPortalObject()
        types = self.getContentTypes()
        context = self.context
        if context != portal:
            while context.aq_parent != portal:
                context = context.aq_parent
                
            urltool = getSite().portal_url
            caminho = {'query': '/'.join(context.getPhysicalPath()), 'depth': 1}
            ctool = getSite().portal_catalog
            submenus = ctool(portal_type=types, path=caminho,sort_on='getObjPositionInParent')        
            
            #defaultView()
            #submenus = context.objectValues(('ATFolder','ATLink','vindula.content.content.vindulacontentmacro'))
            if submenus:
                L = []
                for obj in submenus:
                    if self.checkObj(obj.getObject()):
                        L.append(obj.getObject())
                return L

    def checkObj(self, obj):
        roles = self.context.portal_membership.getAuthenticatedMember().getRoles()
        state = getToolByName(obj, 'portal_workflow').getInfoFor(obj, 'review_state', None)
        try:
            if obj.getExcludeFromNav() == True:
                return False
        except:
            return False
        
        if 'Anonymous' in roles and state == 'private':
            return False
        return True

        
    def isSelected(self, obj):
        if obj.absolute_url() in self.context.REQUEST.get('ACTUAL_URL'): 
            return 'selected'
    
    def isSelectedSubmenu(self, obj):
        if obj.absolute_url() in self.context.REQUEST.get('ACTUAL_URL') or\
            self.context.id == obj.id : 
            return 'selected'