## Script (Python) "AddUserGroup"
##bind context=context
##parameters=user_id, departament
##title= Add User Group
##
from Products.CMFCore.utils import getToolByName

portalGroup = getToolByName(context, 'portal_groups')
ctool = getToolByName(context, 'portal_catalog')

dept = ctool(UID = departament)        
if dept:
    obj = dept[0].getObject()
    grup =  portalGroup.getGroupById(obj.id)
    if grup:
        #grup.addMember(user_id)
        pass
