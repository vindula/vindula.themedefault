# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName

def installTheme(context):    
    portal = context.getSite()
    portal_workflow = getToolByName(portal, 'portal_workflow')
    
    if not 'links' in portal.objectIds():
        portal.invokeFactory('Folder', 
                              id='links', 
                              title='Links Úteis',
                              excludeFromNav = True)
        
        pasta = portal['links']
        pasta.setConstrainTypesMode(1)
        pasta.setLocallyAllowedTypes(('Link',))
        portal_workflow.doActionFor(pasta, 'publish')