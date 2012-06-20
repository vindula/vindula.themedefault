# coding: utf-8
from Acquisition import aq_inner
from five import grok
from plone.app.layout.navigation.interfaces import INavigationRoot
from Products.CMFCore.interfaces import ISiteRoot
from zope.interface import Interface
from plone.uuid.interfaces import IUUID

from zope.component import getUtility
from plone.i18n.normalizer.interfaces import IIDNormalizer
from Products.TinyMCE.interfaces.utility import ITinyMCE

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
import calendar, logging, base64, pickle

from vindula.myvindula.validation import valida_form

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from vindula.myvindula.user import BaseFunc, ModelsDepartment, ModelsFuncDetails,\
                                   ModelsMyvindulaHowareu, ModelsMyvindulaComments, ModelsMyvindulaLike,\
                                   ModelsMyvindulaFuncdetailCouses,ModelsMyvindulaCourses,\
                                   ModelsMyvindulaFuncdetailLanguages, ModelsMyvindulaLanguages, ModelsMyvindulaRecados ,\
                                   ModelsFuncHolerite, ModelsFuncHoleriteDescricao, ModelsConfgMyvindula

from vindula.myvindula.registration import SchemaFunc, SchemaConfgMyvindula, ImportUser, ManageCourses, ManageLanguages
                                   
from vindula.controlpanel.browser.models import ModelsCompanyInformation
from vindula.chat.utils.models import ModelsUserOpenFire

from vindula.myvindula.utils import UtilMyvindula

logger = logging.getLogger('vindula.myvindula')

class MyVindulaView(grok.View, UtilMyvindula):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('myvindula')

    
    def get_howareu(self, user):
        D={}
        D['username'] = user
        return ModelsMyvindulaHowareu().get_myvindula_howareu(**D)
    

    def get_department(self):
        return ModelsDepartment().get_department()

#    def get_photo_user(self,prefs_user):
#        if prefs_user:
#            if prefs_user.photograph is not None and \
#                not ' ' in prefs_user.photograph  and \
#                not prefs_user.photograph == '':
#                #return self.context.absolute_url()+'/'+prefs_user.photograph #+ '/image_thumb'
#                return BaseFunc().get_imageVindulaUser(prefs_user.photograph)
#            
#            else:
#                return self.context.absolute_url()+'/defaultUser.png'
#        else:
#            return self.context.absolute_url()+'/defaultUser.png'
    
    
    def checkHomeFolder(self):
        """ Check if exist homeFolder """
        homefolder = self.context.portal_membership.getHomeFolder()
        if homefolder:
            return True
        else:
            return False
        
    def getConfTyneMCE(self):
        utility = getUtility(ITinyMCE)
        conf = utility.getConfiguration(context=self.context,
                                        field='text',
                                        request=self.request)
        return conf
        

    def update(self):
        """ Receive itself from request and do some actions """
        form = self.request.form
        submitted = form.get('form.submitted', False)
        excluir = form.get('form.excluir', False)
            
        if submitted:
            visible_area = form.get('visible_area')
            if not eval(visible_area):
                form['visible_area'] = form.get('departamento','0')
            
            upload_foto = form.get('upload_image')
            if upload_foto:
                data = upload_foto.read()
                if len(data) != 0 : 
                    form['upload_image'] = pickle.dumps(data)
                else:
                    form['upload_image'] = ''                
            else:
                form['upload_image'] = ''
            ModelsMyvindulaHowareu().set_myvindula_howareu(**form)
                
        elif excluir:
            id_howareu = int(form.get('id_howareu','0'))
            ModelsMyvindulaHowareu().del_myvindula_howareu(id_howareu)
               
            IStatusMessage(self.request).addStatusMessage(_(u'Registro removido com sucesso.'),"info")
                     

#Views de renderização das imagem do howareu ---------------------------------------------------   
class VindulahowareuImage(grok.View, BaseFunc):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('howareu-image')
    
    def render(self):
        pass
    
    def update(self):
        form = self.request.form
        if 'id' in form.keys():
            id = form.get('id','0')
            if id != 'None':
                campo_image = ModelsMyvindulaHowareu().get_myvindula_howareu_By_Id(id)
                valor = campo_image.upload_image
                x = self.decodePickle(valor)
                
                self.request.response.setHeader("Content-Type", "image/jpeg", 0)
                self.request.response.write(x)                

class VindulaHowAreUListAll(grok.View, BaseFunc):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('howareu-list-all')
    
    def load_dados(self):
         result =  ModelsMyvindulaHowareu().get_myvindula_howareu()
         
         if result:
             return self.rs_to_list(result)
         else:
             return []
         
    def update(self):
        """ Receive itself from request and do some actions """
        form = self.request.form
        excluir = form.get('form.excluir', False)
            
        if excluir:
            id_howareu = int(form.get('id_howareu','0'))
            ModelsMyvindulaHowareu().del_myvindula_howareu(id_howareu)
               
            IStatusMessage(self.request).addStatusMessage(_(u'Registro removido com sucesso.'),"info")         
         

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

class MyVindulaConfgsView(grok.View, BaseFunc):
    grok.context(INavigationRoot)
    grok.require('cmf.ManagePortal')
    grok.name('myvindulaconfgs')
    
    ignoreContext = True
    
    label = _(u"The Configuration Register myvindula")
    description = _(u"Change the Settings of the Register myvindula.")   
    
    def load_form(self):
        return SchemaConfgMyvindula().configuration_processes(self)


class MyVindulaRecursosHumanosView(grok.View, BaseFunc):
    grok.context(ISiteRoot)
    grok.require('zope2.View')
    grok.name('myvindula-recursos-humanos')
    
    def getMacro(self,link='myvindula-documents'):
        if 'id' in self.request.keys():
            set_macro = self.request['id']
            return 'context/'+ set_macro +'/macros/page'
        else:
            return 'context/'+link+'/macros/page'


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
        user_login = membership.getAuthenticatedMember().getUserName()
        error_url = self.context.absolute_url() + '/@@myvindulamanagealluser'
        
        if 'user' in form.keys() and not'newuser' in form.keys():
            user_cod = base64.b16decode(form.get('user',''))
            try:user_decodficado = unicode(user_cod, 'utf-8')
            except:user_decodficado = user_cod
            #user = membership.getMemberById(user_decodficado)

            user = ModelsFuncDetails().get_FuncDetails(user_decodficado)
            user_DB = True 
        
        elif 'newuser' in form.keys():
            return SchemaFunc().registration_processes(self, 'acl_users', True)    
        
        else:    
            user = membership.getAuthenticatedMember()
            user_DB = False

        if user:
            if self.checa_login():
                if user_DB:
                    if str(user.id) == str(user_login):
                        return SchemaFunc().registration_processes(self, user, False)
                    else:
                        return SchemaFunc().registration_processes(self, user, True)
                else:
                    if str(user.getUserName()) == str(user_login):
                        return SchemaFunc().registration_processes(self, user, False)
                    else:
                        return SchemaFunc().registration_processes(self, user, True)
                    #return self.request.response.redirect(error_url)
            else:
                if user_DB:
                    if str(user.id) == str(user_login):
                        return SchemaFunc().registration_processes(self, user, False)
                    else:
                        return self.request.response.redirect(error_url)
                else:
                    if str(user.getUserName()) == str(user_login):
                        return SchemaFunc().registration_processes(self, user, False)
                    else:
                        return self.request.response.redirect(error_url)
        
        else:
            return self.request.response.redirect(error_url)
       
    def checa_login(self):
        membership = self.context.portal_membership
        groups = self.context.portal_groups
        
        user_login = membership.getAuthenticatedMember()
        user_groups = groups.getGroupsByUserId(user_login.getId())
        
        checa = False
        if 'Manager' in user_login.getRoles():
            checa = True
        else:
            for i in user_groups:
                if i.id == 'manage-user':
                    checa = True 
                    break
        
        return checa         
    
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
    
class MyVindulaListUser(grok.View, UtilMyvindula):
    #grok.context(ISiteRoot)
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('myvindulalistuser')
    
    def get_campos(self):
        conf = {}
        campos = SchemaConfgMyvindula().campos
        for item in campos.keys():
            dado = ModelsConfgMyvindula().getConfig_edit(item)
            if dado:
                conf[item] = dado
            else:
                conf[item] = True
        
    
        return conf
    
    
    def get_ConfugCampos(self, campo):
        configuracao= ModelsConfgMyvindula().getConfig_views(campo)
        return configuracao
   
    def valida_pessoal(self):
        #configuracao1= self.get_campos()
        
        campos = ['employee_id','nickname','pronunciation_name','date_birth']
        for i in campos:
            if ModelsConfgMyvindula().getConfig_views(i):
                return True
            
        return False
        
    def valida_contato(self):
        #configuracao1= self.get_campos()
        
        campos = ['email','phone_number','location','postal_address']
        for i in campos:
            if ModelsConfgMyvindula().getConfig_views(i):
                return True
            
        return False
         
    def valida_corporativo(self):
        #configuracao1= self.get_campos()
        campos = ['enterprise','registration','position','admission_date','registration','cost_center',\
                  'profit_centre','special_roles','organisational_unit','delegations','reports_to']

        for i in campos:
            if ModelsConfgMyvindula().getConfig_views(i):
                return True            
            
        return False
        
    def valida_others(self):
        #configuracao1= self.get_campos()
        campos = ['committess','registration','projects','personal_information','skills_expertise','languages',\
                  'availability','papers_published','teaching_research','resume','blogs','customised_message']
        
        for i in campos:
            if ModelsConfgMyvindula().getConfig_views(i):
                return True    
        
        return False

    def get_howareu(self, user):
        member =  self.context.restrictedTraverse('@@plone_portal_state').member().getUserName();
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
        member =  self.context.restrictedTraverse('@@plone_portal_state').member().getUserName();
        user = self.request.form.get('user',str(member))
        return ModelsFuncDetails().get_FuncDetails(unicode(user, 'utf-8'))

    def update(self):
        form = self.request.form
        submitted = form.get('form.submitted', False)
        
        excluir_howareu = form.get('form.excluir.howareu', False)
        excluir_recados = form.get('form.excluir.recados', False)
        
        if submitted:
            return  ModelsMyvindulaRecados().set_myvindula_recados(**form)
        
        elif excluir_howareu:
            id_howareu = int(form.get('id_howareu','0'))
            ModelsMyvindulaHowareu().del_myvindula_howareu(id_howareu)
               
            IStatusMessage(self.request).addStatusMessage(_(u'Registro removido com sucesso.'),"info")
        
        elif excluir_recados:       
            id_recado = int(form.get('id_recado','0'))
            ModelsMyvindulaRecados().del_myvindula_recados(id_recado)
               
            IStatusMessage(self.request).addStatusMessage(_(u'Registro removido com sucesso.'),"info")        
              

#    def get_prefs_user(self, user):
#        try:
#            user_id = unicode(user, 'utf-8')    
#        except:
#            user_id = user 
#
#        return ModelsFuncDetails().get_FuncDetails(user_id)

    def getPhoto(self,photo):
        prefs_user = UtilMyvindula().get_prefs_user(photo)
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
    
class MyVindulaUserPerfil(grok.View):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('myvindula-user-perfil')     
    
    

class MyVindulaListRecados(grok.View,UtilMyvindula):
    grok.context(ISiteRoot)
    grok.require('zope2.View')
    grok.name('myvindulalistrecados')

    def get_recados(self, user):
        D={}
        D['destination'] = user
        return ModelsMyvindulaRecados().get_myvindula_recados(**D)

       
#    def get_prefs_user(self, user):
#        try:
#            user_id = unicode(user, 'utf-8')    
#        except:
#            user_id = user 
#
#        return ModelsFuncDetails().get_FuncDetails(user_id)

#    def getPhoto(self,photo):
#        prefs_user = self.get_prefs_user(photo)
#        if prefs_user:
#            if prefs_user.photograph is not None and \
#                not ' ' in prefs_user.photograph  and \
#                not prefs_user.photograph == '':
#                return BaseFunc().get_imageVindulaUser(prefs_user.photograph)
#                #return self.context.absolute_url()+'/'+prefs_user.photograph # + '/image_thumb'
#            else:
#                return self.context.absolute_url()+'/defaultUser.png'
#        else:
#            return self.context.absolute_url()+'/defaultUser.png'
        
    def update(self):
        form = self.request.form
        excluir = form.get('form.excluir', False)
                
        if excluir:
            id_recado = int(form.get('id_recado','0'))
            ModelsMyvindulaRecados().del_myvindula_recados(id_recado)
               
            IStatusMessage(self.request).addStatusMessage(_(u'Registro removido com sucesso.'),"info")        
        
        

class MyVindulalistAll(grok.View, BaseFunc):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('myvindulalistall')
    
       
    def load_list(self):
        form = self.request.form
        result = None
        config_muit_user = self.context.restrictedTraverse('@@myvindula-conf-userpanel').config_muit_user()
        filtro_busca = self.context.restrictedTraverse('@@myvindula-conf-userpanel').check_filtro_busca_user()
        
        if 'title' in form.keys() or 'SearchSubmit' in form.keys():
            title = form.get('title','').strip()
            departamento= form.get('departamento','0')
            ramal = form.get('ramal','').strip()
            filtro = form.get('filtro','departamentos').strip()
            
            if title or departamento !='0' or ramal:
            
                if type(title) != unicode:
                    title = unicode(title, 'utf-8')
                
                if type(departamento) != unicode:
                    departamento = unicode(departamento, 'utf-8')
                    
                if type(ramal) != unicode:
                    ramal = unicode(ramal, 'utf-8')

                result = ModelsFuncDetails().get_FuncBusca(title,'0',ramal,filtro_busca)
                if result:

                    if departamento != '0' and filtro != 'departamentos':
                        busca = "result.find("+ filtro + "=u'" + departamento+"')"
                        data = eval(busca)
                        if data.count() != 0:
                            result = self.rs_to_list(data)
                        else:
                            result = []
                    elif departamento == 'departamentos':
                        data = ModelsFuncDetails().get_FuncBusca(title,departamento,ramal,filtro_busca)
                        if data:
                            result = self.rs_to_list(data)
                        else:
                            result = []
                    else:
                        result = self.rs_to_list(result)
            
        elif not config_muit_user or 'all' in form.keys():
            result_set = ModelsFuncDetails().get_FuncBusca(unicode('', 'utf-8'),unicode('0','utf-8'),unicode('', 'utf-8'),filtro_busca)
            if result_set:
                    result = self.rs_to_list(result_set)
                    
        return result
    
      
#    def rs_to_list(self, rs):
#        if rs:
#            return [i for i in rs]
    
    def check_no_result(self):
        form = self.request.form
        if 'title' in form.keys():
            title = form.get('title','').strip()
            departamento= form.get('departamento','0')
            ramal = form.get('ramal','').strip()
            if title or departamento !='0' or ramal:
                return 'Não há resultados.'
        if 'SearchSubmit' in form.keys():
            return 'Digite um filtro para a busca.'
        else:
            return ''
   
class MyVindulaNewsEmployeeView(grok.View, BaseFunc):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('myvindula-news-employee')
    
       
    def load_list(self):
        result = None
        result_set = ModelsFuncDetails().get_allFuncDetails('admicao')
        if result_set:
            result = self.rs_to_list(result_set)
                    
        return result
    
#    def rs_to_list(self, rs):
#        if rs:
#            return [i for i in rs]
    
    def check_no_result(self):
        form = self.request.form
        if 'title' in form.keys():
            title = form.get('title','').strip()
            departamento= form.get('departamento','0')
            ramal = form.get('ramal','').strip()
            if title or departamento !='0' or ramal:
                return 'Não há resultados.'
        if 'SearchSubmit' in form.keys():
            return 'Digite um filtro para a busca.'
        else:
            return ''



#class MyVindulaListMyContent(grok.View):
#    grok.context(Interface)
#    grok.require('zope2.View')
#    grok.name('myvindula-meus-conteudos')
#    
#    def load_list(self):        
#        membership = self.context.portal_membership
#        user_login = membership.getAuthenticatedMember()
#        
#        if user_login.getUserName():
#            ctool = getSite().portal_catalog
#            items = ctool(path = {'query': '/', 'depth': 99},
#                          Creator=user_login.getId())        
#        
#            return items
#            
#        else:
#            self.request.response.redirect(self.context.absolute_url() + '/login')


class MyVindulaManageAllUser(grok.View, BaseFunc):
    grok.context(INavigationRoot)
    grok.require('zope2.View')
    grok.name('myvindulamanagealluser')
    
    def checa_login(self):
        membership = self.context.portal_membership
        groups = self.context.portal_groups
        
        user_login = membership.getAuthenticatedMember()
        user_groups = groups.getGroupsByUserId(user_login.getId())
        
        checa = False
        if 'Manager' in user_login.getRoles():
            checa = True
        else:
            for i in user_groups:
                if i.id == 'manage-user':
                    checa = True
                    break 
        
        return checa            
    
    def load_list(self):
        form = self.request.form
        config_muit_user = self.context.restrictedTraverse('@@myvindula-conf-userpanel').config_muit_user()
        
        if self.checa_login():
            #vars = BaseFunc().getParametersFromURL(self)
            if 'title' in form.keys() and not 'all' in form.keys():
                title = form.get('title','').strip()
                departamento= form.get('departamento','0')
                ramal = form.get('ramal','').strip()
                result = self.rs_to_list(ModelsFuncDetails().get_FuncBusca(unicode(title, 'utf-8'),
                                                           unicode(departamento,'utf-8'),
                                                           unicode(ramal, 'utf-8')))
            
            elif not config_muit_user:
                result = self.rs_to_list(ModelsFuncDetails().get_FuncBusca('','0',''))
                
            elif 'all' in form.keys():
                result = self.rs_to_list(ModelsFuncDetails().get_FuncBusca('','0',''))
            
            else:
                result = None
            
            return result
        else:
            self.request.response.redirect(self.context.absolute_url() + '/login')

#    def rs_to_list(self, rs):
#        if rs:
#            return [i for i in rs]
#        else:
#            return []

    def encodeUser(self,user):
        return base64.b16encode(user)
    
class MyVindulaFirstRegistreView(grok.View, UtilMyvindula):
    grok.context(ISiteRoot)
    grok.require('zope2.View')
    grok.name('myvindula-first-registre')
    
    def to_utf8(self,value):
        return unicode(value, 'utf-8') 
    
    def load_list(self):
        form = self.request # var tipo 'dict' que guarda todas as informacoes do formulario (keys,items,values)
        form_keys = form.keys() # var tipo 'list' que guarda todas as chaves do formulario (keys)
        
        continuar_url = self.context.absolute_url() + '/myvindulaprefs'
        voltar_url = self.context.absolute_url() + '/'
        
        if 'continuar' in form_keys:
            self.request.response.redirect(continuar_url) 
        
        elif 'voltar' in form_keys:
            self.request.response.redirect(voltar_url)
        
        else:
            result = ModelsCompanyInformation().get_CompanyInformation()
            if result:
                return result[0]
            else:
                return {}
            
    def checkCampoVazio(self,campo):
          member = getSite().portal_membership
          data = self.get_prefs_user(member.getAuthenticatedMember().getUserName())
          if data:
              if campo == 'name':
                  if data.__getattribute__('name') == member.getAuthenticatedMember().getUserName():
                      return True
              
              elif data.__getattribute__(campo):
                  # Campo Não Esta vazio
                  return False

              else:
                  # Campo Esta vazio
                  return True
          else:
              # Campo Esta vazio
              return True
    
    def checkUserXMPP(self):
        member = getSite().portal_membership
        try: user = self.to_utf8(member.getAuthenticatedMember().getUserName())
        except: user =  member.getAuthenticatedMember().getUserName()
        data = ModelsUserOpenFire().get_UserOpenFire_by_username(user)
        if data:
            return True
        else:
            return False
    
            
    def get_saldacao(self):
        hora = datetime.now().strftime('%H')
        if hora > '17':
            return 'Boa noite, '
        elif hora > '12':
            return 'Boa tarde, '
        else:
            return 'Bom dia, '
    
#    def get_prefs_user(self, user):
#        try:
#            user_id = unicode(user, 'utf-8')    
#        except:
#            user_id = user 
#
#        return ModelsFuncDetails().get_FuncDetails(user_id)    


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
        
    def get_campos_list_user(self):
        if 'control-panel-objects' in  getSite().keys():
            control = getSite()['control-panel-objects']
            if 'vindula_aniversariantesconfig' in control.keys():
                list = control['vindula_aniversariantesconfig']
            else:
                list = None
        
        if list: 
            lines = list.list_campos_user.splitlines()
            L = []

            for line in lines:
                D = {}
                line = line.replace('[', '').replace(']', '').split(' | ')
                try:D['label'] = line[0]
                except:D['label'] = ''
                
                try:D['content'] = line[1]
                except:D['content'] = ''
                
                L.append(D)
            return L
        
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
            
        elif type_filter == 'prox':
            results = ModelsFuncDetails().get_FuncBirthdays('','','proximo')
        
        if results:
            return results #results[:int(quant)]
        else:
            return []

    
    def load_list(self):
        form = self.request.form
        filtro = form.get('filtro',1)
        if filtro == 'prox':
            results = self.get_birthdaysToday(filtro)
        else:
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
        member = getSite().portal_membership
        form = self.request.form
        dislike = form.get('dislike','False')
        
        if not member.isAnonymousUser():
            form['username'] = member.getAuthenticatedMember().getUserName()
            if eval(dislike):     
                ModelsMyvindulaLike().del_myvindula_like(**form)
  
            else:
                ModelsMyvindulaLike().set_myvindula_like(**form)



class MyVindulaLikeMacro(grok.View):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('myvindula-like-macro')  
    
    
class MyVindulaComments(grok.View, UtilMyvindula):
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
#            elif not conf_context:
#                return False
            else:
                return False
        else:
            if replies:
                return True
#            if conf_context:
#                return True
            else:
                return conf_global
            
    
    
#    def get_prefs_user(self, user):
#        try:
#            user_id = unicode(user, 'utf-8')    
#        except:
#            user_id = user 
#
#        return ModelsFuncDetails().get_FuncDetails(user_id)
    
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
    
#    def get_photo_user(self,prefs_user):
#        if prefs_user:
#            if prefs_user.photograph is not None and \
#                not ' ' in prefs_user.photograph  and \
#                not prefs_user.photograph == '':
#                return BaseFunc().get_imageVindulaUser(prefs_user.photograph)
#                #return self.context.absolute_url()+'/'+prefs_user.photograph # + '/image_thumb'
#            else:
#                return self.context.absolute_url()+'/defaultUser.png'
#        else:
#            return self.context.absolute_url()+'/defaultUser.png'
#    
    def update(self):
        """ Receive itself from request and do some actions """
        form = self.request.form
        submitted = form.get('form.submitted-comment', False)
        excluir = form.get('form.excluir', False)
        request = self.request.environ
        
        if 'HTTP_REFERER' in request:
            redirect = request.get('HTTP_REFERER',self.context.absolute_url())
        else:
            redirect = self.context.absolute_url()
        
        if submitted:
            member = getSite().portal_membership
            if not member.isAnonymousUser():
                form['username'] = member.getAuthenticatedMember().getUserName()
                form['ip'] = self.get_ip(self.request)
            
                ModelsMyvindulaComments().set_myvindula_comments(**form)
                return self.request.response.redirect(redirect)
        
        elif excluir:
            id_comments = int(form.get('id_comments','0'))
            ModelsMyvindulaComments().del_myvindula_comments(id_comments)
               
            IStatusMessage(self.request).addStatusMessage(_(u'Registro removido com sucesso.'),"info")
            
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
                
class MyVindulaImportSecondView(grok.View, BaseFunc): 
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
                if field != 'username':
                    D['label'] = self.get_label_filed(field)

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
            error = 0
            url = ''
            
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

                                username = name[0] + name[-1]
                                cont = 1
 
                                if form['registration']:
                                    matricula = dados_linha[int(form['registration'])-1].replace('"','')    
                                    username += str(matricula)
                                
                                usr = username
                                while ModelsFuncDetails().get_FuncDetails(self.to_utf8(usr)):
                                    usr = username + str(cont)
                                    cont +=1
                                  
                                dados[campo] = self.to_utf8(usr)
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
                
                logger.info("%s - %s "% (erros,data_user))
                    
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

class MyVindulaImportHoleriteView(grok.View, BaseFunc):
    grok.context(INavigationRoot)
    grok.require('cmf.ManagePortal')
    grok.name('myvindula-import-holerite')
    
    def get_lastImport(self):
        result = ModelsFuncHolerite().get_FuncHolerites_Import()
        if result: 
            return result
        else:
            return []
        
#    def CountDados(self, data):
#        result = ModelsFuncHolerite().get_FuncHolerites_byData(data)
#        if result: 
#            return result.count()
#        else:
#            return 0
              
    def load_file(self):
        from pprint import pprint
        from copy import copy
        form = self.request.form
        erro = False
        holerite_erro = None
        holerites = []
        modelo_holerite = {'cod_empresa':None,
                           'empresa':None,
                           'endereco_empresa':None,
                           'estado_empresa':None,
                           'cnpj_empresa':None,
                           'competencia':None,
                           'matricula':None,
                           'nome':None,
                           'cpf':None,
                           'completo':False,
                           'itens_holerite':[],
                           'itens_holerite_check':False,
                           'total_vencimento':None,
                           'total_desconto':None,
                           'valor_liquido':None,
                           'salario_base':None,
                           'base_Inss':None,
                           'base_fgts':None,
                           'fgts_mes':None,
                           'base_irrf':None}
        
        holerite = copy(modelo_holerite)
        
        if 'load_file' in form.keys():            
            if 'txt_file' in form.keys():
                file = form.get('txt_file','')
                if file:
                    texto = file.read()
                    texto = texto.replace('\r','').replace('\x1b2','') #.replace('#','')
                    cont = 1
                    
                    for linha in texto.split('\n'):
                        #Checando linhas vazias, se a linha for vazia ou só espaço, vai retornar uma lista vazia e nao entrar no if.
                        check_linha = [i for i in linha.split(' ') if i != '']
                        
                        #Pulando linhas vazias
                        if check_linha != []:
                            #Buscando cod_empresa e empresa
                            if holerite['cod_empresa'] == None:                                
                                holerite['cod_empresa'] = linha[:4]
                                holerite['empresa'] = linha[5:]
                            
                            #Buscando dados de endereço
                            elif holerite['endereco_empresa'] == None: 
                                linha_list = [i for i in linha.lstrip().rstrip().split('  ') if i != '']
                                holerite['endereco_empresa'] = ' '.join(linha_list[:-1])
                                holerite['estado_empresa'] = linha[len(linha_list)-1].lstrip()
                                                        
                            elif holerite['cnpj_empresa'] == None:
                                linha_list = [i for i in linha.lstrip().rstrip().split(' ') if i != '']
                                holerite['cnpj_empresa'] = linha_list[0]
                                holerite['competencia'] = linha_list[1]
                                
                            elif holerite['matricula'] == None:
                                holerite['matricula'] = linha.split(' ')[0]
                                linha_list = [i for i in linha.split(' ')[+1:] if i != '']
                                holerite['nome'] = ' '.join(linha_list[:-1]) 
                                holerite['cpf'] = linha_list[len(linha_list)-1]
                            
                            #Importando itens do holerite
                            elif holerite['matricula'] != None and holerite['itens_holerite_check'] == False:
                                    itens_holerite = {'codigo':None,
                                                      'descricao':None,
                                                      'ref':None,
                                                      'vencimentos':None,
                                                      'descontos':None,}
                                    
                                    itens = copy(itens_holerite)
                                    
                                    itens['codigo'] = linha.split('  ')[0].split(' ')[0] 
                                    itens['descricao'] = ' '.join(linha.split('  ')[0].split(' ')[+1:])
                                    
                                    if itens['codigo'] != '' and itens['codigo'].isdigit() and cont <= 15:
                                        linha_valores = [i for i in linha.split('  ')[+1:] if i != '']
                                        
                                        if len(linha_valores) > 1:
                                            itens['ref'] = linha_valores[0]
                                            valor_indefinido = linha_valores[1]
                                        else:
                                            valor_indefinido = linha_valores[0]
            
                                        if linha[linha.find(valor_indefinido):].count(' ') >= 26:                                    
                                            itens['vencimentos'] = valor_indefinido
                                        else:
                                            itens['descontos'] = valor_indefinido
                                        
                                        holerite['itens_holerite'].append(itens)
                                        cont = cont + 1    
                                    else:
                                        holerite['itens_holerite_check'] = True
                                        
                            #Separando valores da linha, para distinguir observacao de valor liquido e valor desconto
                            linha_obervacao = [i for i in linha.split('  ') if i != '' and i != ' ']
                            
                            if linha.lstrip().rstrip() == '##########':                    
                                #Marca o holerite como completo e vai para o proximo
                                holerite['completo'] = True   
                            
                            elif holerite['total_vencimento'] == None and holerite['itens_holerite_check'] == True:
                                linha_list = [i for i in linha.lstrip( ).rstrip().split('  ') if i != '']
                                if len(linha_list) == 3:
                                    # Linha[0] mensagem ignorada
                                    holerite['observacao'] = linha_list[0]
                                    holerite['total_vencimento'] = linha_list[1]
                                    holerite['total_desconto'] = linha_list[2]
                                elif len(linha_list) == 2:
                                    holerite['total_vencimento'] = linha_list[0]
                                    holerite['total_desconto'] = linha_list[1]
                                
                                elif len(linha_list) == 1:
                                    holerite['observacao'] = linha_list[0]
                                #else:
                                #    #Marca o holerite como completo e vai para o proximo
                                #    holerite['completo'] = True
                            elif holerite.has_key('observacao') and len(linha_obervacao) == 1 and linha[0] != ' ' and holerite['valor_liquido'] == None:
                                holerite['observacao'] = holerite['observacao'] +' '+ linha_obervacao[0]
                                

                            elif holerite['total_desconto'] != None and holerite['valor_liquido'] == None:
                                linha_list = [i for i in linha.lstrip().rstrip().split(' ') if i != '']
                                holerite['valor_liquido'] = linha_list[0] 
                            
                            elif holerite['valor_liquido'] != None and  holerite['salario_base'] == None:
                                linha_list = [i for i in linha.lstrip().rstrip().split(' ') if i != '']
                                holerite['salario_base'] = linha_list[0]
                                holerite['base_Inss'] = linha_list[1]
                                holerite['base_fgts'] = linha_list[2]
                                holerite['fgts_mes'] = linha_list[3]
                                holerite['base_irrf'] = linha_list[4]
                               
                                holerite['completo'] = True

                                
                            if holerite['completo'] == True:
                                holerites.append(holerite)
                                holerite = copy(modelo_holerite)
                                holerite['itens_holerite'] = []
                                cont = 1
                            
                    if holerites:
                        for holerite in holerites:
                            itens = copy(holerite['itens_holerite'])
                            convertido = self.converte_dadosByDB(holerite)
                            id = ModelsFuncHolerite().set_FuncHolerite(**convertido)
                            
                            for item in itens:
                                item['vin_myvindula_holerite_id'] = id
                                desc_convertido = self.converte_dadosByDB(item)
                                ModelsFuncHoleriteDescricao().set_FuncHoleriteDescricao(**desc_convertido)
                            
                    
        else:
            return None
     
#    def load_file_old(self):
#        form = self.request.form
#        if 'load_file' in form.keys():
#            
#            if 'txt_file' in form.keys():
#                file = form.get('txt_file','')
#                if file:
#                    texto = file.read()
#                    texto = texto.replace('\r','')
#                    registros = texto.split('\x1b2\n')
#                    for reg in registros:
#                        D = {}
#                        L = []
#                        linhas = reg.split('\n')
#                        max = len(linhas)-1
#                        cont = 0
#                        entra = False
#                        #while cont <= max:
#                        
#                        for linha in linhas:
#                            
#                            #linha = linhas[cont]
#                            if len(linha) == 80:
#                                entra = True
#                                if cont == 0:
#                                    D['cod_empresa'] = linha[0:3] 
#                                    D['empresa'] = linha[5:51]
#                                    #D['cnomeidade_empresa'] = linha[] 
#                                
#                                elif cont == 1:
#                                    D['endereco_empresa'] = linha[5:60]                    
#                                    D['estado_empresa'] = linha[60:62]
#                                
#                                elif cont == 2:    
#                                    D['cnpj_empresa'] = linha[5:23]
#                                    tmp = linha[56:63]
#                                    tmp = tmp.strip()
#                                    tmp = tmp.split('/')
#                                    D['competencia'] = tmp[1]+'/'+tmp[0] 
#                                
#                                elif cont == 4:
#                                    
#                                    D['matricula'] = linha[0:5]
#                                    D['nome'] = linha[6:51]
#                                    D['cpf']  = linha[69:80]
#                    
#                                elif cont >= 8 and cont <= 23:
#                                    E = {}
#                                    E['codigo'] = linha[0:3]
#                                    E['descricao'] = linha[4:33]
#                                    E['ref'] = linha[34:43]
#                                    E['vencimentos'] = linha[44:57]
#                                    E['descontos'] = linha[58:70]
#                                    
#                                    L.append(E)
#                                elif cont == 24:
#                                    D['total_vencimento'] = linha[42:55]
#                                    D['total_desconto'] = linha[56:70]
#                                
#                                elif cont == 26:
#                                    D['valor_liquido'] = linha[56:70]
#                                    
#                                elif cont == 28:
#                                    D['salario_base'] = linha[0:13]
#                                    D['base_Inss'] = linha[14:25]
#                                    D['base_fgts'] = linha[26:38]
#                                    D['fgts_mes'] = linha[40:50]
#                                    D['base_irrf'] = linha[52:70]
#                            if entra:    
#                                cont += 1
#                        if D:
#                            convertido = self.converte_dadosByDB(D)
#                            id = ModelsFuncHolerite().set_FuncHolerite(**convertido)
#                            for item in L:
#                                try:
#                                    item['vin_myvindula_holerite_id'] = id
#                                    desc_convertido = self.converte_dadosByDB(item)
#                                    ModelsFuncHoleriteDescricao().set_FuncHoleriteDescricao(**item)
#                                except:
#                                    item['vin_myvindula_holerite_id'] = id
#                                    desc_convertido = self.converte_dadosByDB(item)
#                                    ModelsFuncHoleriteDescricao().set_FuncHoleriteDescricao(**item)
#        
#        else:
#            return None
        
class MyVindulaFindHoleriteView(grok.View, BaseFunc):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('myvindula-find-holerite')
    
    def get_descricao_holerite(self, id_holerite):
        result = ModelsFuncHoleriteDescricao().get_FuncHoleriteDescricoes_byid(id_holerite)
        if result: 
            return result
        else:
            return [] 
    
    def load_list(self):
        form = self.request.form
        if 'cpf' in form.keys() and 'id' in form.keys():

            try:cpf = unicode(form.get('cpf',''),'utf-8')
            except:cpf = form.get('cpf','')
            
            id = int(form.get('id','0'))
               
            return ModelsFuncHolerite().get_FuncHolerites_byCPFAndID(cpf, id)


class MyVindulaDelHoleriteView(grok.View, BaseFunc):
    grok.context(INavigationRoot)
    grok.require('cmf.ManagePortal')
    grok.name('myvindula-del-holerite')
    
    def update(self):
        form = self.request.form
        success_url = self.context.absolute_url() + '/myvindula-import-holerite'
        if 'date' in form.keys() and 'empresa' in form.keys():
            data_lote = form['date']
            
            try:empresa = unicode(form['empresa'],'utf-8')
            except:empresa = form['empresa']

            data_lote = datetime.strptime(data_lote,'%Y-%m-%d %H:%M')
            ModelsFuncHolerite().del_HoleritesLote(data_lote,empresa)
            
        self.request.response.redirect(success_url)
    
    def render(self):
        pass
        
        
class MyVindulaHoleriteView(grok.View, UtilMyvindula):
    grok.context(ISiteRoot)
    grok.require('zope2.View')
    grok.name('myvindula-holerite')
    
#    def get_prefs_user(self, user):
#        user_id = unicode(user, 'utf-8')    
#        return ModelsFuncDetails().get_FuncDetails(user_id)
    
    def get_descricao_holerite(self, id_holerite):
        result = ModelsFuncHoleriteDescricao().get_FuncHoleriteDescricoes_byid(id_holerite)
        if result: 
            return result
        else:
            return [] 
    
    def load_list(self):
    
        membership = self.context.portal_membership
        user_login = membership.getAuthenticatedMember()
        user = str(user_login.getUserName())
        
        prefs_user = self.get_prefs_user(user)
        if prefs_user:
            cpf = prefs_user.teaching_research
            holerites = ModelsFuncHolerite().get_FuncHolerites_byCPF(cpf)
            D = {}
            if holerites:
                if holerites.count() > 1:
                    D['select'] = holerites 
                    D['data'] = holerites.last() 
                    return D
                else:
                    D['select'] = []
                    D['data'] = holerites.one() 
                    return D
            
            else:
                return []
        
        else:
                return []
            
            
class MyVindulaPrintHoleriteView(grok.View, UtilMyvindula):
    grok.context(ISiteRoot)
    grok.require('zope2.View')
    grok.name('imprimir-holerite')
    
#    def get_prefs_user(self, user):
#        user_id = unicode(user, 'utf-8')    
#        return ModelsFuncDetails().get_FuncDetails(user_id)
    
    def get_descricao_holerite(self, id_holerite):
        result = ModelsFuncHoleriteDescricao().get_FuncHoleriteDescricoes_byid(id_holerite)
        if result: 
            return result
        else:
            return [] 
    
    def load_list(self):
        form = self.request.form
        
        membership = self.context.portal_membership
        user_login = membership.getAuthenticatedMember()
        prefs_user = self.get_prefs_user(user_login.getUserName())
        
        
        if prefs_user and 'id' in form.keys():

            try:cpf = unicode(prefs_user.teaching_research,'utf-8')
            except:cpf = prefs_user.teaching_research
            
            id = int(form.get('id','0'))
                
            return ModelsFuncHolerite().get_FuncHolerites_byCPFAndID(cpf, id)      
