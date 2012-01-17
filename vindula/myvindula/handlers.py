# -*- coding: utf-8 -*-
from zope.app.component.hooks import getSite
from Products.CMFCore.interfaces import ISiteRoot

from vindula.myvindula.user import ModelsFuncDetails

def to_utf8(value):
    return unicode(value, 'utf-8') 


def userupdate(event):
    """ Handler for User Login in Site """
    membership = getSite().portal_membership
    user_login = membership.getAuthenticatedMember()
    registro_url = getSite().absolute_url() + '/myvindula-first-registre'
    #import pdb;pdb.set_trace()
    try:
        user_id = to_utf8(user_login.getId())
    except:
        user_id = user_login.getId()
        
    if not ModelsFuncDetails().get_FuncDetails(user_id):
        D = {}
        D['username'] = user_id
        D['name'] = to_utf8(user_login.getProperty('fullname'))
        D['email'] = to_utf8(user_login.getProperty('email'))
        ModelsFuncDetails().set_FuncDetails(**D)
    else:
        user_data = ModelsFuncDetails().get_FuncDetails(user_id)
        
        if user_data.name is None or ' ' in user_data.name:
            #getSite.context.request.response.redirect(success_url)
            pass
        
        elif user_data.date_birth is None:
            #getSite.context.request.response.redirect(success_url)
            pass