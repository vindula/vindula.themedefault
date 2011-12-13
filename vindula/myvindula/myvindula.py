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
                return SchemaFunc().registration_processes(self, user, True)
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
    
class MyVindulaImportUsersView(grok.View):
    grok.context(INavigationRoot)
    grok.require('cmf.ManagePortal')
    grok.name('myvindula-import-users')
    
    
    def load_labels_vindula(self):
        fields = SchemaFunc().campos
        campos_vin = []
        if fields:
            for field in fields:
                D = {}
                D['name'] = field
                D['label'] = fields.get(field).get('label')
                campos_vin.append(D)
        self.campos_vin = campos_vin
        return campos_vin
        
    def load_labels_csv(self):
        form = self.request.form
        if 'load_file' in form.keys():
            if 'csv_file' in form.keys():
                portal = self.context
                pasta = getattr(portal, 'migration-users')
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
                return {'campos': pasta.get(nome_arquivo).data.split('\n')[0].replace('"', '').split(';'), 
                        'url_arquivo': pasta.get(nome_arquivo).absolute_url()}
            
    def importar_valores(self):
        form = self.request.form
        if 'import' in form.keys():
            pasta = form.get('url_arquivo').split('/')[4]
            arquivo = form.get('url_arquivo').split('/')[5]
            pasta = self.context.get(pasta)
            arquivo = pasta.get(arquivo)
            ignore_fields = ['import',
                             'url_arquivo',]
            
            for linha in arquivo.data.split('\n')[1:-1]:
                dados = {}
                dados_linha = linha.split(';')                
                for campo in form.keys():
                    if form[campo] != '' and campo not in ignore_fields:
                        indice = int(form[campo])-1
                        dados[campo] = unicode(dados_linha[indice])
                    else:
                        dados[campo] = u''
                erros, data = valida_form(SchemaFunc().campos, dados)
                import pdb;pdb.set_trace()
                user = ModelsFuncDetails(**data)
                ModelsFuncDetails().store.add(user)
                ModelsFuncDetails().store.flush()