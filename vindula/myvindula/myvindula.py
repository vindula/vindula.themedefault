# coding: utf-8
from Acquisition import aq_inner
from five import grok
from plone.app.layout.navigation.interfaces import INavigationRoot
from Products.CMFCore.interfaces import ISiteRoot
from zope.interface import Interface
from plone.uuid.interfaces import IUUID

from plone.dexterity.utils import createContentInContainer
from plone.namedfile.field import NamedImage
from Products.CMFCore.utils import getToolByName

from plone.directives import form
from vindula.myvindula import MessageFactory as _
from z3c.form import button
from zope import schema
from Products.statusmessages.interfaces import IStatusMessage

from plone.z3cform.crud import crud

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from vindula.myvindula.user import BaseFunc, SchemaFunc, SchemaConfgMyvindula, ModelsDepartment, ModelsFuncDetails,\
                                   ImportUser, ModelsMyvindulaHowareu, ModelsMyvindulaComments, ModelsMyvindulaLike,\
                                   ManageCourses, ManageLanguages
                                   
                                   
from zope.component import getUtility

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
                return self.context.absolute_url()+'/'+prefs_user.photograph + '/image_thumb'
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
    grok.context(INavigationRoot)
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


class MyVindulaPrefsView(grok.View, BaseFunc):
    grok.context(ISiteRoot)
    grok.require('zope2.View')
    grok.name('myvindulaprefs')
    
    ignoreContext = True
    
    label = _(u"Personal Information")
    description = _(u"Change your available information below.")   
    
    def load_form(self):
        return SchemaFunc().registration_processes(self)
       
    
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
    grok.context(ISiteRoot)
    grok.require('zope2.View')
    grok.name('myvindulalistuser')
    
    def load_list(self):
        #vars = BaseFunc().getParametersFromURL(self)
        member =  self.context.restrictedTraverse('@@plone_portal_state').member().getId();
        user = self.request.form.get('user',str(member))
        return ModelsFuncDetails().get_FuncDetails(unicode(user, 'utf-8'))

    def getPhoto(self,photo):
        if photo is not None and not ' ' in photo:
                return self.context.absolute_url()+'/'+photo
        else:
                return self.context.absolute_url()+'/'+'defaultUser.png'

    def get_department(self, user):
        try:
            user_id = unicode(user, 'utf-8')    
        except:
            user_id = user

        return ModelsDepartment().get_departmentByUsername(user)     


class MyVindulalistAll(grok.View):
    grok.context(ISiteRoot)
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
                return self.context.absolute_url()+'/'+prefs_user.photograph + '/image_thumb'
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

        