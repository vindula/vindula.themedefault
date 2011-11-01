# -*- coding: utf-8 -*-

from plone.app.controlpanel.security import SecurityControlPanelAdapter
from vindula.myvindula.user import ModelsConfgMyvindula

def user_folder(context):
    ctx = context.getSite()
    folder_user = ctx.portal_membership.memberareaCreationFlag
    if not folder_user:
        SecurityControlPanelAdapter(ctx).set_enable_user_folders(True)
        

def set_AllowedType_Members(context):
    portal = context.getSite()
    Types = ['Folder','Image','RTRemoteVideo','RTInternalVideo', 'Document', 'File'] 
    
    if 'Members' in portal.keys():
        folder_members = portal['Members']
        folder_members.setConstrainTypesMode(1) # 1 pasta com restrição de conteudo / 0 sem restrição de conteudo
        folder_members.setImmediatelyAddableTypes(Types)
        folder_members.setLocallyAllowedTypes(Types)
        
        
        
def set_field_default(context):
    try:
        if not ModelsConfgMyvindula().get_configuration():
            D={}    
            D['name'] = True
            D['phone_number'] = True
            D['cell_phone'] = True
            D['email'] = True
            D['employee_id'] = False
            #D['username'] = False
            D['date_birth'] = True
            D['registration'] = False
            D['enterprise'] = False
            D['position'] = False
            D['admission_date'] = False
            D['cost_center'] = False 
            D['organisational_unit'] = False
            D['reports_to'] = False
            D['location'] = False
            D['postal_address'] = False
            D['special_roles'] = False
            D['photograph'] = True
            D['nickname'] = False
            D['pronunciation_name'] = False
            D['committess'] = False
            D['projetcs'] = False
            D['personal_information'] = False
            D['skills_expertise'] = True
            D['profit_centre'] = False
            D['languages'] = True    
            D['availability'] = False
            D['papers_published'] = False
            D['teaching_research'] = False
            D['delegations'] = False
            D['resume'] = False
            D['blogs'] = False
            D['customised_message'] = True
            D['vin_myvindula_department_id'] = True
            ModelsConfgMyvindula().set_configuration(**D)
    
    except:
        print "Error" 
