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
                    return confg.favicon
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
            img = conf.to_object.absolute_url()
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
                            review_state=('published','internal','external'),
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
                
                if itens:
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
        #import pdb;pdb.set_trace()
        
        portal = self.context.portal_url.getPortalObject()
        types = self.getContentTypes()
        
        if self.context.portal_type == 'vindula.themedefault.content.homepage':
            if self.context.ref_itemMenu:
                context = self.context.ref_itemMenu.to_object
            else:
                context = self.context
        else:
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
            try:
                if obj.exclude_from_nav == True:
                    return False
            except:
                return False
        
        if 'Anonymous' in roles and state == 'private':
            return False
        return True

        
    def isSelected(self, obj):
        if self.context.portal_type == 'vindula.themedefault.content.homepage':
            if self.context.ref_itemMenu:
                if obj.absolute_url() ==  self.context.ref_itemMenu.to_object.absolute_url() or\
                   obj.absolute_url() in self.context.REQUEST.get('ACTUAL_URL'):
                    return 'selected'
            
            elif obj.absolute_url() in self.context.REQUEST.get('ACTUAL_URL'):
                return 'selected'
        else:
            if obj.absolute_url() in self.context.REQUEST.get('ACTUAL_URL'):
                return 'selected'
    
    def isSelectedSubmenu(self, obj):
        if obj.absolute_url() in self.context.REQUEST.get('ACTUAL_URL') or\
            self.context.id == obj.id : 
            return 'selected'