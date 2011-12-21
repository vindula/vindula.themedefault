# coding: utf-8
from Acquisition import aq_inner
from five import grok
from plone.app.layout.navigation.interfaces import INavigationRoot
from Products.CMFCore.interfaces import ISiteRoot
from zope.interface import Interface
from plone.uuid.interfaces import IUUID

from zope.component import getUtility
from plone.i18n.normalizer.interfaces import IIDNormalizer

from plone.dexterity.utils import createContentInContainer
from plone.namedfile.field import NamedImage
from Products.CMFCore.utils import getToolByName
from zope.app.component.hooks import getSite

from plone.directives import form
from vindula.myvindula import MessageFactory as _
from z3c.form import button
from zope import schema
from Products.statusmessages.interfaces import IStatusMessage

from plone.z3cform.crud import crud
from datetime import date
from DateTime.DateTime import DateTime
from datetime import datetime 
import calendar
import base64

from vindula.myvindula.validation import valida_form

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from vindula.myvindula.user import BaseFunc, SchemaFunc, SchemaConfgMyvindula, ModelsDepartment, ModelsFuncDetails,\
                                   ImportUser, ModelsMyvindulaHowareu, ModelsMyvindulaComments, ModelsMyvindulaLike,\
                                   ManageCourses, ManageLanguages, ModelsMyvindulaFuncdetailCouses,ModelsMyvindulaCourses,\
                                   ModelsMyvindulaFuncdetailLanguages, ModelsMyvindulaLanguages, ModelsMyvindulaRecados

class MyVindulaView(grok.View):
    grok.context(INavigationRoot)
    grok.require('zope2.View')
    grok.name('myvindula')

    def get_prefs_user(self, user):
        try:
            user_id = unicode(user, 'utf-8')    
        except:
            user_id = user 

        return ModelsFuncDetails().get_FuncDetails(user_id)
    
    def get_howareu(self, user):
        D={}
        D['username'] = user
        return ModelsMyvindulaHowareu().get_myvindula_howareu(**D)
    

    def get_department(self):
        return ModelsDepartment().get_department()

    def get_photo_user(self,prefs_user):
        if prefs_user:
            if prefs_user.photograph is not None and \
                not ' ' in prefs_user.photograph  and \
                not prefs_user.photograph == '':
                #return self.context.absolute_url()+'/'+prefs_user.photograph #+ '/image_thumb'
                return BaseFunc().get_imageVindulaUser(prefs_user.photograph)
            
            else:
                return self.context.absolute_url()+'/defaultUser.png'
        else:
            return self.context.absolute_url()+'/defaultUser.png'
    
    
    def checkHomeFolder(self):
        """ Check if exist homeFolder """
        homefolder = self.context.portal_membership.getHomeFolder()
        if homefolder:
            return True
        else:
            return False

    def update(self):
        """ Receive itself from request and do some actions """
        form = self.request.form
        submitted = form.get('form.submitted', False)
            
        if submitted:
            visible_area = form.get('visible_area')
            if not eval(visible_area):
                form['visible_area'] = form.get('departamento','0')
            return  ModelsMyvindulaHowareu().set_myvindula_howareu(**form)        

class MyVindulaPanelView(grok.View):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('myvindulapanel')
    
    def _checkPermission(self, permission, context):
        mt = getToolByName(context, 'portal_membership')
        return mt.checkPermission(permission, context)
    
    
    def getPersonalInfoLink(self):
        """ Get the link for vindula home """
        
        context = aq_inner(self.context)        
        template = None
        if self._checkPermission('Set own properties', context):
            template = '@@myvindulapanel?section=myvindula'
        return template

    def getPersonalPrefsLink(self):
        """ Get the link for user preferences """
        
        context = aq_inner(self.context)        
        template = None
        if self._checkPermission('Set own properties', context):
            template = '@@myvindulapanel?section=myvindulaprefs'
        return template
    
    def check_recados(self):
        if 'control-panel-objects' in getSite().keys():
            control = getSite()['control-panel-objects']
            if 'vindula_vindularecadosconfig' in control.keys():
                config = control['vindula_vindularecadosconfig']
                return config.ativa_recados
            else:
                return False
          
        else:
            return False


class MyVindulaConfgsView(grok.View, BaseFunc):
    grok.context(INavigationRoot)
    grok.require('cmf.ManagePortal')
    grok.name('myvindulaconfgs')
    
    ignoreContext = True
    
    label = _(u"The Configuration Register myvindula")
    description = _(u"Change the Settings of the Register myvindula.")   
    
    def load_form(self):
        return SchemaConfgMyvindula().configuration_processes(self)


class MyVindulaPrefsView(grok.View, BaseFunc):
    grok.context(ISiteRoot)
    grok.require('zope2.View')
    grok.name('myvindulaprefs')
    
    ignoreContext = True
    
    label = _(u"Personal Information")
    description = _(u"Change your available information below.")   
    
    def load_form(self):
        portal_workflow = getToolByName(getSite(), 'portal_workflow')
        if not 'one_state_workflow' in portal_workflow.getChainForPortalType('vindula.myvindula.vindulaphotouser'):
            portal_workflow.setChainForPortalTypes(pt_names = ('vindula.myvindula.vindulaphotouser',),
                                                   chain=['one_state_workflow',])
        form = self.request.form
        membership = self.context.portal_membership
        user_login = membership.getAuthenticatedMember()
        error_url = self.context.absolute_url() + '/@@myvindulamanagealluser'
        
        if 'user' in form.keys():
            user_cod = base64.b16decode(form.get('user',''))
            user = membership.getMemberById(user_cod)
            
        else:    
            user = membership.getAuthenticatedMember()
            

        if user:
            if 'Manager' in user_login.getRoles():
                if str(user.id) == str(user_login.id):
                    return SchemaFunc().registration_processes(self, user, False)
                else:
                    return SchemaFunc().registration_processes(self, user, True)
                    #return self.request.response.redirect(error_url)
            else:
                if str(user.id) == str(user_login.id):
                    return SchemaFunc().registration_processes(self, user, False)
                else:
                    return self.request.response.redirect(error_url)
        else:
            return self.request.response.redirect(error_url)
       
       
    
    def update(self):
        # disable Plone's editable border
        self.request.set('disable_border', True)
        return super(MyVindulaPrefsView, self).update()

class MyVindulaImportUser(grok.View, BaseFunc):
    grok.context(INavigationRoot)
    grok.require('cmf.ManagePortal')
    grok.name('myvindulaimportuser')
    
    ignoreContext = True
    
    label = _(u"users to import the database")
    description = _(u"User import for plone site from mysql database.")   
    
    def load_form(self):
        return ImportUser().databaseUser(self)

    def update(self):
        # disable Plone's editable border
        self.request.set('disable_border', True)
        return super(MyVindulaImportUser, self).update()
    
class AjaxView(grok.View):
    grok.context(ISiteRoot)
    grok.require('cmf.ManagePortal')
    grok.name('ajax_view')
    
    def defaultMethod(self,form):
        method = form.get('method',None)
        method = getattr(self,method,None)
        if method != None:
            return method(form)
        return None
    
    def importUser(self,form):
        return ImportUser().importUser(self,form)
    
class MyVindulaListUser(grok.View):
    #grok.context(ISiteRoot)
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('myvindulalistuser')
    
    
    def check_recados(self):
        if 'control-panel-objects' in getSite().keys():
            control = getSite()['control-panel-objects']
            if 'vindula_vindularecadosconfig' in control.keys():
                config = control['vindula_vindularecadosconfig']
                return config.ativa_recados
            else:
                return False
          
        else:
            return False
    
    
    def get_howareu(self, user):
        member =  self.context.restrictedTraverse('@@plone_portal_state').member().getId();
        user = self.request.form.get('user',str(member))
        D={}
        D['username'] = user
        return ModelsMyvindulaHowareu().get_myvindula_howareu(**D)
    
    
    def get_recados(self, user):
        D={}
        D['destination'] = user
        return ModelsMyvindulaRecados().get_myvindula_recados(**D)
    
    def load_list(self):
        #vars = BaseFunc().getParametersFromURL(self)
        member =  self.context.restrictedTraverse('@@plone_portal_state').member().getId();
        user = self.request.form.get('user',str(member))
        return ModelsFuncDetails().get_FuncDetails(unicode(user, 'utf-8'))

    def update(self):
        form = self.request.form
        submitted = form.get('form.submitted', False)
           
        if submitted:
            return  ModelsMyvindulaRecados().set_myvindula_recados(**form)      

        
    def get_prefs_user(self, user):
        try:
            user_id = unicode(user, 'utf-8')    
        except:
            user_id = user 

        return ModelsFuncDetails().get_FuncDetails(user_id)

    def getPhoto(self,photo):
        prefs_user = self.get_prefs_user(photo)
        if prefs_user:
            if prefs_user.photograph is not None and \
                not ' ' in prefs_user.photograph  and \
                not prefs_user.photograph == '':
                return BaseFunc().get_imageVindulaUser(prefs_user.photograph)
                #return self.context.absolute_url()+'/'+prefs_user.photograph # + '/image_thumb'
            else:
                return self.context.absolute_url()+'/defaultUser.png'
        else:
            return self.context.absolute_url()+'/defaultUser.png'


    def get_department(self, user):
        try:
            user_id = unicode(user, 'utf-8')    
        except:
            user_id = user

        return ModelsDepartment().get_departmentByUsername(user)     

    def get_Courses(self, user):
        try:
            user_id = unicode(user, 'utf-8')    
        except:
            user_id = user

        return ModelsMyvindulaFuncdetailCouses().get_funcdetailCouserByUsername(user)     
    
    def getCouses_byID(self,id):
        return ModelsMyvindulaCourses().get_courses_byID(int(id))

    def get_Languages(self, user):
        try:
            user_id = unicode(user, 'utf-8')    
        except:
            user_id = user

        return ModelsMyvindulaFuncdetailLanguages().get_funcdetailLanguagesByUsername(user)     
    
    def getLanguages_byID(self,id):
        return ModelsMyvindulaLanguages().get_languages_byID(int(id))


    def get_department(self, user):
        try:
            user_id = unicode(user, 'utf-8')    
        except:
            user_id = user

        return ModelsDepartment().get_departmentByUsername(user)     

class MyVindulaListRecados(grok.View):
    grok.context(ISiteRoot)
    grok.require('zope2.View')
    grok.name('myvindulalistrecados')

    def get_recados(self, user):
        D={}
        D['destination'] = user
        return ModelsMyvindulaRecados().get_myvindula_recados(**D)

       
    def get_prefs_user(self, user):
        try:
            user_id = unicode(user, 'utf-8')    
        except:
            user_id = user 

        return ModelsFuncDetails().get_FuncDetails(user_id)

    def getPhoto(self,photo):
        prefs_user = self.get_prefs_user(photo)
        if prefs_user:
            if prefs_user.photograph is not None and \
                not ' ' in prefs_user.photograph  and \
                not prefs_user.photograph == '':
                return BaseFunc().get_imageVindulaUser(prefs_user.photograph)
                #return self.context.absolute_url()+'/'+prefs_user.photograph # + '/image_thumb'
            else:
                return self.context.absolute_url()+'/defaultUser.png'
        else:
            return self.context.absolute_url()+'/defaultUser.png'

class MyVindulalistAll(grok.View):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('myvindulalistall')
    
    def load_list(self):
        form = self.request.form
        #vars = BaseFunc().getParametersFromURL(self)
        title = form.get('title','').strip()
        departamento= form.get('departamento','0')
        ramal = form.get('ramal','').strip()
        result = ModelsFuncDetails().get_FuncBusca(unicode(title, 'utf-8'),unicode(departamento,'utf-8'),unicode(ramal, 'utf-8'))
        return result

class MyVindulaListMyContent(grok.View):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('myvindula-meus-conteudos')
    
    def load_list(self):        
        membership = self.context.portal_membership
        user_login = membership.getAuthenticatedMember()
        
        if user_login.getId():
            #import pdb;pdb.set_trace()
            ctool = getSite().portal_catalog
            items = ctool(path = {'query': '/', 'depth': 99},
                          Creator=user_login.getId())        
        
            return items
            
        else:
            self.request.response.redirect(self.context.absolute_url() + '/login')


class MyVindulaManageAllUser(grok.View):
    grok.context(INavigationRoot)
    grok.require('cmf.ManagePortal')
    grok.name('myvindulamanagealluser')
    
    def load_list(self):
#        form = self.request.form
#        #vars = BaseFunc().getParametersFromURL(self)
#        title = form.get('title','').strip()
#        departamento= form.get('departamento','0')
#        ramal = form.get('ramal','').strip()
        result = ModelsFuncDetails().get_allFuncDetails()
        return result

    def encodeUser(self,user):
        return base64.b16encode(user)


class MyVindulaListBirthdays(grok.View):
    grok.context(ISiteRoot)
    grok.require('zope2.View')
    grok.name('myvindulalistbirthdays')
    
    def nome_filtro(self):
        filtro = self.request.form.get('filtro',1)
        if filtro == '1':
            return "do Dia"
        elif filtro == '7':
            return "da Semana"
        elif filtro == '30':
            return "do Mês"
        else:
            return ''
    
    def get_department(self, user):
        try:
            user_id = unicode(user, 'utf-8')    
        except:
            user_id = user
        
        return ModelsDepartment().get_departmentByUsername(user)     
        
    def get_birthdaysToday(self, type_filter):
        results = []
        if type_filter == 1:
            date_start = date.today().strftime('%Y-%m-%d')
            date_end = date.today().strftime('%Y-%m-%d')
        
            results = ModelsFuncDetails().get_FuncBirthdays(date_start,date_end)
        
        elif type_filter == 7:
            now = DateTime()
            dow = now.dow()
            date_start = (now - dow).strftime('%Y-%m-%d')
            date_end = (now - dow + 6).strftime('%Y-%m-%d')
            
            results = ModelsFuncDetails().get_FuncBirthdays(date_start,date_end)
        
        elif type_filter == 30:
            now = DateTime()
                        
            dia = calendar.monthrange(now.year(),now.month())[1]
            date_start = now.strftime('%Y-%m-1')
            date_end = now.strftime('%Y-%m-'+str(dia))
            
            results = ModelsFuncDetails().get_FuncBirthdays(date_start,date_end)
        
        if results:
            return results #results[:int(quant)]
        else:
            return []

    
    def load_list(self):
        form = self.request.form
        filtro = form.get('filtro',1)
        results = self.get_birthdaysToday(int(filtro))
        
        if results:
            return results
        else:
            return []

class MyVindulaLike(grok.View):
    grok.context(ISiteRoot)
    grok.require('zope2.View')
    grok.name('myvindula-like')
    
    def render(self):
        pass
    
    def update(self):
        """ Receive itself from request and do some actions """
        form = self.request.form
        dislike = form.get('dislike','False')

        if eval(dislike):     
            ModelsMyvindulaLike().del_myvindula_like(**form)
  
        else:
            ModelsMyvindulaLike().set_myvindula_like(**form)



class MyVindulaLikeMacro(grok.View):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('myvindula-like-macro')  
    
    
    
class MyVindulaComments(grok.View):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('myvindula-comments')
    
    def get_UID(self):
        return IUUID(self.context)
    
    def discussionAllowed(self,conf_global, replies,conf_context):
        if conf_global:
            if replies:
                return True
            elif conf_context:
                return True
            elif not conf_context:
                return False
            else:
                return conf_global
        else:
            if replies:
                return True
            if conf_context:
                return True
            else:
                return conf_global
            
    
    
    def get_prefs_user(self, user):
        try:
            user_id = unicode(user, 'utf-8')    
        except:
            user_id = user 

        return ModelsFuncDetails().get_FuncDetails(user_id)
    
    def get_comments(self,id,type):
        D={}
        D['id_obj'] = id
        D['type'] = type
        return ModelsMyvindulaComments().get_myvindula_comments(**D)
    
    def get_like(self,id,type_obj):
        D={}
        D['id_obj'] = id
        D['type'] = type_obj
        return ModelsMyvindulaLike().get_myvindula_like(**D)
    
    def get_photo_user(self,prefs_user):
        if prefs_user:
            if prefs_user.photograph is not None and \
                not ' ' in prefs_user.photograph  and \
                not prefs_user.photograph == '':
                return BaseFunc().get_imageVindulaUser(prefs_user.photograph)
                #return self.context.absolute_url()+'/'+prefs_user.photograph # + '/image_thumb'
            else:
                return self.context.absolute_url()+'/defaultUser.png'
        else:
            return self.context.absolute_url()+'/defaultUser.png'
    
    def update(self):
        """ Receive itself from request and do some actions """
        form = self.request.form
        submitted = form.get('form.submitted-comment', False)
        redirect = form.get('url_context',self.context.absolute_url())
                            
        if submitted:
            ModelsMyvindulaComments().set_myvindula_comments(**form)
            return self.request.response.redirect(redirect)
        
class MyVindulaCommentsMacro(grok.View):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('myvindula-comments-macro')        
     
 
class MyVindulaCoursesView(grok.View, BaseFunc):
    grok.context(INavigationRoot)
    grok.require('cmf.ManagePortal')
    grok.name('myvindula-courses')
    
    def load_list(self):
        return ManageCourses().load_courses(self)

        
class MyVindulaManageCoursesView(grok.View, BaseFunc):        
    grok.context(INavigationRoot)
    grok.require('cmf.ManagePortal')
    grok.name('myvindula-manage-courses')    

    def load_form(self):
        return ManageCourses().registration_processes(self)      

class MyVindulaLanguagesView(grok.View, BaseFunc):
    grok.context(INavigationRoot)
    grok.require('cmf.ManagePortal')
    grok.name('myvindula-languages')
    
    def load_list(self):
        return ManageLanguages().load_languages(self)

        
class MyVindulaManageLanguagesView(grok.View, BaseFunc):        
    grok.context(INavigationRoot)
    grok.require('cmf.ManagePortal')
    grok.name('myvindula-manage-languages')    

    def load_form(self):
        return ManageLanguages().registration_processes(self)
    
class MyVindulaImportFirstView(grok.View):
    grok.context(INavigationRoot)
    grok.require('cmf.ManagePortal')
    grok.name('myvindula-import-first')
    
    
    def load_file(self):
        form = self.request.form               
        if 'load_file' in form.keys():
            if 'csv_file' in form.keys():
                portal = self.context
                pasta_control = getattr(portal, 'control-panel-objects')
                if pasta_control:
                    pasta_migracao = getattr(pasta_control, 'migration-users')
                    if pasta_migracao:
                        pasta = getattr(pasta_migracao, 'upload-csv')
                        if pasta:
                            arquivo = self.request.get('csv_file')
                            nome = arquivo.filename
                            
                            normalizer = getUtility(IIDNormalizer)
                            nome_arquivo = normalizer.normalize(unicode(nome, 'utf-8'))
                            
                            count = 0
                            while nome_arquivo in pasta.objectIds():
                                count +=1
                                if count != 1:
                                    nome_arquivo = nome_arquivo[:-2]
                                nome_arquivo = nome_arquivo + '-' + str(count)         
                            
                            pasta.invokeFactory('File', 
                                                id=nome_arquivo,
                                                title=nome_arquivo,
                                                description='',
                                                file=self.request.get('csv_file')
                                                )
                            campos_csv = pasta.get(nome_arquivo).data.split('\n')[0].replace('"', '').split(';')
                            arquivo = pasta.get(nome_arquivo).virtual_url_path()
                            redirect = self.context.absolute_url() + '/myvindula-import-second?url_arquivo=%s' % (arquivo)
                            return self.request.response.redirect(redirect)          
                        else:
                            IStatusMessage(self.request).addStatusMessage(_(u"Erro ao carregar arquivo, contate o administrados do portal."), "error")
                    else:
                        IStatusMessage(self.request).addStatusMessage(_(u"Erro ao carregar arquivo, contate o administrados do portal."), "error")
                else:
                    IStatusMessage(self.request).addStatusMessage(_(u"Erro ao carregar arquivo, contate o administrados do portal."), "error")
                
class MyVindulaImportSecondView(grok.View):
    grok.context(INavigationRoot)
    grok.require('cmf.ManagePortal')
    grok.name('myvindula-import-second')
    
    def to_utf8(self, value):
        return unicode(value, 'utf-8')    
    
    def load_archive(self):
        form = self.request.form
        if 'url_arquivo' in form.keys():
            path_file = form.get('url_arquivo').split('/')
            if len(path_file) == 3:
                folder = path_file[1]
                file = path_file[2]
            else:
                folder = path_file[0]
                file = path_file[1]
            folder = self.context.get(folder)
            file = folder.get(file)
            
            return file.title
            
    
    def load_fields_vindula(self):
        form = self.request.form
        fields_vin = []
        i=0
        fields = SchemaFunc().campos
        while i < len(fields.keys())-1:
              fields_vin.append(i)
              i+=1
        
        if fields:
            for field in fields:
                index = fields[field].get('ordem',0)
                D = {}
                D['name'] = field
                D['label'] = fields.get(field).get('label')
                fields_vin.pop(index)
                fields_vin.insert(index, D)    
                
                #fields_vin.append(D)
        return fields_vin
        
            
    def load_fields_csv(self):
        form = self.request.form
        if 'url_arquivo' in form.keys():
            path_file = form.get('url_arquivo').split('/')
            folder = getSite()[path_file[0]][path_file[1]][path_file[2]]
            file = folder.get(path_file[3])
            
#            if len(path_file) == 3:
#                folder = path_file[1]
#                file = path_file[2]
#            else:
#                folder = path_file[0]
#                file = path_file[1]
#            folder = self.context.get(folder)
#            file = folder.get(file)
            
            return file.data.split('\n')[0].replace('"', '').split(';')
        
            
    def importar_valores(self):
        form = self.request.form
        if 'import' in form.keys():
            path_file = form.get('url_arquivo').split('/')
            folder = getSite()[path_file[0]][path_file[1]][path_file[2]]
            arquivo = folder.get(path_file[3])
            
            linhas_error =[]
            lista_erros = []
            
#            folder = self.context.get(folder)
#            arquivo = folder.get(file)
            ignore_fields = ['import',
                             'url_arquivo',
                             'cria-username',
                             'atualiza-dados',
                             'username',]
            
            success = False
            criar_user = form.get('cria-username', False)
            merge_user = form.get('atualiza-dados', False)
            
            for linha in arquivo.data.split('\n')[1:-1]:
                dados = {}
                dados_linha = linha.split(';')
                check_user = False
                for campo in form.keys():
                    if form[campo] != '' and campo not in ignore_fields:
                        indice = int(form[campo])-1
                        dados[campo] = self.to_utf8(dados_linha[indice].replace('"',''))
                    else:
                        if campo == 'username':
                            if criar_user:                                    
                                name = dados_linha[int(form['name'])-1].replace('"','').lower().split(' ')
                                matricula = dados_linha[int(form['registration'])-1].replace('"','')
                                x = len(name)
                                username = name[0] + name[x-1] + str(matricula)
                                    
                                if not ModelsFuncDetails().get_FuncDetails(self.to_utf8(username)):    
                                    dados[campo] = self.to_utf8(username)
                                    check_user = True
                                    
                            elif merge_user:
                                if form[campo] != '':
                                    indice = int(form[campo])-1
                                    user = self.to_utf8(dados_linha[indice].replace('"',''))
                                    if ModelsFuncDetails().get_FuncDetails(user):    
                                            dados[campo] = user
                                            check_user = True
                            
                            else:                            
                                if form[campo] != '':
                                    indice = int(form[campo])-1
                                    user = self.to_utf8(dados_linha[indice].replace('"',''))
                                    if not ModelsFuncDetails().get_FuncDetails(user):    
                                        dados[campo] = user
                                        check_user = True

                        else:
                            dados[campo] = u''
                 
                erros, data_user = valida_form(SchemaFunc().campos, dados)
                if not erros:
                    if check_user:
                        if criar_user:
                            ModelsFuncDetails().set_FuncDetails(**data_user)
                            success = True
                        elif merge_user:
                            result = ModelsFuncDetails().get_FuncDetails(user)
                            if result:
                                success = True
                                campos = SchemaFunc().campos
                                for campo in campos.keys():
                                    value = data_user.get(campo, None)
                                    if value:
                                        setattr(result, campo, value)
                        else:
                            ModelsFuncDetails().set_FuncDetails(**data_user)
                            success = True
                    else:
                        error = 1
                else:
                    linhas_error.append(linha)
                    lista_erros.append(erros)
                    error = 2
                    success = False
                    
            if linhas_error:
                success = False
                campos = arquivo.data.split('\n')[0].replace('\r','')
                text = ''
                col = ''
                for campo in campos.split(';'):
                    col += campo+';'
                
                col += 'coluna erro;\n'
                text = col
                i = 0
                
                for linha in linhas_error:
                    text += linha.replace('\r','') + ';'+str(lista_erros[i].keys())+'\n'   
                    i +=1
                    
                text += '\n'
                
                nome_arquivo = 'error-import-'+ datetime.now().strftime('%Y-%M-%d_%H-%M-%S') +'.csv'
                pasta_error = getSite()['control-panel-objects']['migration-users']['errors-import']
                pasta_error.invokeFactory('File', 
                                            id=nome_arquivo,
                                            title=nome_arquivo,
                                            description='',
                                            file=text)
                url=pasta_error[nome_arquivo].absolute_url()
                             
            redirect = self.context.absolute_url() + '/myvindula-import-third?success=%s&error=%s&url=%s' % (success,error,url)
            return self.request.response.redirect(redirect)   
            
                
class MyVindulaImportThirdView(grok.View):
    grok.context(INavigationRoot)
    grok.require('cmf.ManagePortal')
    grok.name('myvindula-import-third')
                
class MyVindulaExportUsersView(grok.View):
    grok.context(INavigationRoot)
    grok.require('cmf.ManagePortal')
    grok.name('myvindula-export-users')
    
    def export_users(self):
        form = self.request.form
        if 'export' in form.keys():
            self.request.response.setHeader("Content-Type", "text/csv", 0)
            filename = 'myvindula-export-users.csv'
            self.request.response.setHeader('Content-Disposition','attachment; filename=%s'%(filename))
            
            fields_orig = ModelsFuncDetails()._storm_columns.values()

            campos_vin = []
            text = ''
            
            if fields_orig:
                for field in fields_orig:
                    campos_vin.append(field.name)
                    text += field.name + ';'
                text = text[:-1] + '\n'

            users = ModelsFuncDetails().get_allFuncDetails()

            for user in users:
                for campo in campos_vin:
                    if campo not in ('skills_expertise', 'languages'):
                        valor = user.__getattribute__(campo)
                        if valor == None:
                            valor = ''
                        
                        if campo == 'customised_message':
                            valor = str(valor).replace('\n', '').replace('\r', '').replace(';', '')
                        
                        text += '%s;' % (valor)
                text += '\n'
                 
            self.request.response.write(str(text))
            
