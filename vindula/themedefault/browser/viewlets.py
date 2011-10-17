# -*- coding: utf-8 -*-
from five import grok
from zope.interface import Interface
from plone.app.layout.viewlets.interfaces import IAboveContent
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

grok.context(Interface) 

class MenuViewlet(grok.Viewlet): 
    grok.name('vindula.themedefault.menu') 
    grok.require('zope2.View')
    grok.viewletmanager(IAboveContent) 
    
    template_menu = ViewPageTemplateFile('viewlets_templates/menuviewlet.pt')
    
    def render(self):
        return self.template_menu()
    
    def getMenu(self):
        portal = self.context.portal_url.getPortalObject()
        menus = portal.objectValues('ATFolder')
        if menus:
            L = []
            for obj in menus:
                if self.checkObj(obj):
                    D = {}
                    D['obj'] = obj
                    if obj.absolute_url() in self.context.REQUEST.get('ACTUAL_URL'): 
                        D['class'] = 'link_ativo'
                    else:
                        D['class'] = 'link_inativo'
                    L.append(D)
            return L
        
    def getSubMenu(self):
        L = []
        portal = self.context.portal_url.getPortalObject()
        context = self.context

        if context != portal:
            while context.aq_parent != portal:
                context = context.aq_parent
            
            submenus = context.objectValues('ATFolder')
            for obj in submenus:
                if self.checkObj(obj):
                    L.append(obj)
        return L

    def checkObj(self, obj):
        roles = self.context.portal_membership.getAuthenticatedMember().getRoles()
        state = getToolByName(obj, 'portal_workflow').getInfoFor(obj, 'review_state', None)
        if 'Anonymous' in roles and state == 'private':
            return False
        else:
            return True