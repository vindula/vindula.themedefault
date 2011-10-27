# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName

# Add additional setup code here
#def installTheme(context):    
#    import pdb;pdb.set_trace()
#    portal = context.getSite()
#    portal_workflow = getToolByName(portal, 'portal_workflow')
#
#    if not 'links' in portal.objectIds():
#
#        portal.invokeFactory('Folder', 
#                              id='links', 
#                              title='Links Úteis',
#                              excludeFromNav = True)
#        
#        pasta = portal['links']
#        pasta.setConstrainTypesMode(1)
#        pasta.setLocallyAllowedTypes(('Link',))
#        portal_workflow.doActionFor(pasta, 'publish')