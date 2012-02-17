# -*- coding: utf-8 -*-

from plone.app.controlpanel.security import SecurityControlPanelAdapter
from vindula.myvindula.user import ModelsConfgMyvindula
from Products.CMFCore.utils import getToolByName

from zope.component import getUtility
from plone.dexterity.interfaces import IDexterityFTI

def user_folder(context):
    ctx = context.getSite()
    folder_user = ctx.portal_membership.memberareaCreationFlag
    if not folder_user:
        SecurityControlPanelAdapter(ctx).set_enable_user_folders(True)
        
    # Creating Migration Users Folder
    if 'control-panel-objects' in ctx.objectIds():
        folder_control_panel = ctx['control-panel-objects']
        if not 'migration-users' in folder_control_panel.objectIds():
            folder_control_panel.invokeFactory('Folder', 
                                               id='migration-users', 
                                               title='Migração de usuários',
                                               description='Pasta que guarda os arquivos CSV da importação de usuários.',
                                               excludeFromNav = True)
            migration = folder_control_panel['migration-users']
            
            if not 'upload' in folder_control_panel.objectIds():
                migration.invokeFactory('Folder', 
                                        id='upload-csv', 
                                        title='Upload',
                                        description='Pasta que guarda os arquivos CSV da importação de usuários.',
                                        excludeFromNav = True)

            if not 'errors' in folder_control_panel.objectIds():
                migration.invokeFactory('Folder', 
                                        id='errors-import', 
                                        title='Erros na Importação',
                                        description='Pasta que guarda os arquivos CSV sobre os erros na importação de usuários.',
                                        excludeFromNav = True)
                
    portalGroup = context.getSite().portal_groups 
    if not 'manage-user' in portalGroup.listGroupIds():
        nome_grupo = 'Gerenciadores dos usuarios'
        portalGroup.addGroup('manage-user', title=nome_grupo)
        #Adiciona o grupo a 'AuthenticatedUsers'
        portalGroup.getGroupById('AuthenticatedUsers').addMember('manage-user')  
    
                
        

def set_AllowedType_Members(context):
    portal = context.getSite()
    Types = ['vindula.myvindula.vindulaphotouser', 'Folder','Image','RTRemoteVideo','RTInternalVideo', 'Document', 'File',] 
    
    if 'Members' in portal.keys():
        folder_members = portal['Members']
        folder_members.setConstrainTypesMode(1) # 1 pasta com restrição de conteudo / 0 sem restrição de conteudo
        folder_members.setImmediatelyAddableTypes(Types)
        folder_members.setLocallyAllowedTypes(Types)
        
        if 'index_html' in folder_members.keys():
            index = folder_members['index_html']
            #index.write("member_search = '/myvindulalistall'\nreturn container.REQUEST.RESPONSE.redirect(member_search)")
            
        


        
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
