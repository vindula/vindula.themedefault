# -*- coding: utf-8 -*-
from five import grok
from zope.interface import Interface
from plone.app.layout.viewlets.interfaces import IAboveContent, IPortalHeader
from Products.CMFCore.utils import getToolByName

grok.context(Interface) 

# Viewlet for useful links

class UsefulLinksViewlet(grok.Viewlet): 
    grok.name('vindula.themedefault.usefullinks') 
    grok.require('zope2.View')
    grok.viewletmanager(IPortalHeader) 

    def getLinks(self):
        portal = self.context.portal_url.getPortalObject()
        if not 'links' in portal.objectIds():
            portal.invokeFactory('Folder', 
                                  id='links', 
                                  title='Links Úteis',
                                  excludeFromNav = True)
            
            pasta = portal['links']
            portal_workflow = getToolByName(portal, 'portal_workflow')
            pasta.setConstrainTypesMode(1)
            pasta.setLocallyAllowedTypes(('Link',))
            portal_workflow.doActionFor(pasta, 'publish')
            
        else:
            pasta = portal['links']
            self.pc = getToolByName(self.context, 'portal_catalog')
            links = self.pc(path={'query':'/'.join(pasta.getPhysicalPath())},
                            portal_type='Link',
                            review_state='published')
            
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

    def getMenu(self):
        portal = self.context.portal_url.getPortalObject()
        menus = portal.objectValues('ATFolder')
        if menus:
            L = []
            for obj in menus:
                if self.checkObj(obj):
                    L.append(obj)
            return L
        
    def getSubMenu(self):
        portal = self.context.portal_url.getPortalObject()
        context = self.context
        if context != portal:
            while context.aq_parent != portal:
                context = context.aq_parent
            submenus = context.objectValues('ATFolder')
            if submenus:
                L = []
                for obj in submenus:
                    if self.checkObj(obj):
                        L.append(obj)
                return L

    def checkObj(self, obj):
        roles = self.context.portal_membership.getAuthenticatedMember().getRoles()
        state = getToolByName(obj, 'portal_workflow').getInfoFor(obj, 'review_state', None)
        if obj.getExcludeFromNav() == True:
            return False
        if 'Anonymous' in roles and state == 'private':
            return False
        return True
        
    def isSelected(self, obj):
        if obj.absolute_url() in self.context.REQUEST.get('ACTUAL_URL'): 
            return 'selected'