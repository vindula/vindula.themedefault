# -*- coding: utf-8 -*-
from Products.CMFCore.permissions import setDefaultRoles

PROJECTNAME = 'vindula.themedefault'

# Permissions
DEFAULT_ADD_CONTENT_PERMISSION = "Add portal content"
setDefaultRoles(DEFAULT_ADD_CONTENT_PERMISSION, ('Manager', 'Owner'))
ADD_CONTENT_PERMISSIONS = {
    'HomePage': 'vindula.themedefault: AddHomePage',
   
}

setDefaultRoles('vindula.themedefault: AddHomePage', ('Manager','Owner'))


product_globals = globals()