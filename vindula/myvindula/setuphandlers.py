# -*- coding: utf-8 -*-

from plone.app.controlpanel.security import SecurityControlPanelAdapter

def user_folder(context):
    ctx = context.getSite()
    folder_user = ctx.portal_membership.memberareaCreationFlag
    if not folder_user:
        SecurityControlPanelAdapter(ctx).set_enable_user_folders(True)
        
    