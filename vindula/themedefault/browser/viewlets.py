# -*- coding: utf-8 -*-
from five import grok
from zope.interface import Interface
from plone.app.layout.viewlets.interfaces import IAboveContent
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

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
        menus = portal.objectValues('Folder')
        if menus:
            L = []
            for obj in menus:
                D = {}
                D['title'] = obj.Title()
                D['url'] = obj.absolute_url()
                if D['url'] in self.context.REQUEST.get('ACTUAL_URL'): 
                    D['items'] = self.getSubMenu(obj)
                    D['class'] = 'link_ativo'
                else:
                    D['items'] = []
                    D['class'] = 'link_inativo'
                L.append(D)
            return L
    
    def getSubMenu(self, menu):
        items = menu.objectValues('Folder')
        if items:
            L = []
            for obj in items:
                D = {}
                D['title'] = obj.Title()
                D['url'] = obj.absolute_url()
                L.append(D)
            print L
            return L
            