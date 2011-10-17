from Acquisition import aq_inner
from five import grok
from plone.app.layout.navigation.interfaces import INavigationRoot
from Products.CMFCore.interfaces import ISiteRoot

from plone.dexterity.utils import createContentInContainer
from plone.namedfile.field import NamedImage
from Products.CMFCore.utils import getToolByName
#from vindula.myvindula.user import IFuncDetails
from plone.directives import form
from vindula.myvindula import MessageFactory as _
from z3c.form import button
from zope import schema
from Products.statusmessages.interfaces import IStatusMessage

from plone.z3cform.crud import crud

from vindula.myvindula.user import BaseStore, IFuncDetails, ModelsFuncDetails
from storm.zope.interfaces import IZStorm
from plone.i18n.normalizer.interfaces import IIDNormalizer
from zope.component import getUtility

class BaseFunc(BaseStore):
    #default class for standard functions
        
    def uploadFile(self, path, file):
        """ function used to upload the file to the Plone site, 
           with the parameter where the file will be saved and the file will be saved
        """
        normalizer = getUtility(IIDNormalizer)
        name_file = normalizer.normalize(file.filename)    #unicode(file.filename, 'utf-8')) #takes the name of the file

        count = 0
        while name_file in path.objectIds():
            name_file = name_file + '-' + str(count)
            count +=1
        
        #starts the upload process     
        else:
            try:
                #if image ...    
                if name_file.endswith('png') or \
                    name_file.endswith('jpg') or \
                        name_file.endswith('gif'):                

                    createContentInContainer(path, "vindulaimage",
                                             id= name_file,
                                             title=name_file,
                                             image=file)                
                    
                #if file ...
                else:
                    createContentInContainer(path, "File",
                         id= name_file,
                         title=name_file,
                         image=file)                
                    
                #takes the url of the file to save the database  
                content = getattr(path, name_file, None)
                url = ''
                if content is not None:
                    url = content.absolute_url() 
                
                return unicode(url)
                IStatusMessage(self.request).addStatusMessage(_(u"File upload successful."), 
                                                              "info")
                
            except:
                IStatusMessage(self.request).addStatusMessage(_(u'Error when trying to upload the file.'), 
                                                              "erro")
                access_denied = self.context.absolute_url() + '/portal_skins/plone_login/require_login'
                self.request.response.redirect(access_denied)


            
            
class MyVindulaView(grok.View):
    grok.context(INavigationRoot)
    grok.require('zope2.View')
    grok.name('myvindula')
    
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
            
            homefolder = self.context.portal_membership.getHomeFolder()
            howareu = form.get('howareu')
            item = createContentInContainer(homefolder, "vindula.myvindula.howareu", title=howareu)

            

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

    def getMacroLink(self, page):
        #import pdb; pdb.set_trace()

        path = 'context/@@%s/macros/page' % page
        return path



class MyVindulaPrefsView(form.SchemaForm):
    grok.context(ISiteRoot)
    grok.require('zope2.View')
    grok.name('myvindulaprefs')
    
    schema = IFuncDetails
    ignoreContext = True
    
    
    label = _(u"Personal Informations")
    description = _(u"Change your available information below.")   
            
    
    def update(self):
        # disable Plone's editable border
        self.request.set('disable_border', True)
        return super(MyVindulaPrefsView, self).update()
        
    
    @button.buttonAndHandler(_(u'Order'))
    def handleApply(self, action):
        self.store = getUtility(IZStorm).get('myvindula')
        
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        
        # Put the threatment to database
        
        # Upload of Photograph
        if data['photograph'] != None:
            #convertidos['photograph'] = to_utf8(form['photograph'])
            if data['photograph'].filename != '': 
                path = self.context.portal_membership.getHomeFolder()
                file = data['photograph']
                data['photograph'] = BaseFunc().uploadFile(path,file)
            else:
                data['photograph'] = None    
        
        # adicionando...
        data['username'] = unicode(self.context.portal_membership.getAuthenticatedMember().id, 'utf-8')
        #data['Department_id'] = 1
        
        database = ModelsFuncDetails(**data)
        
        self.store.add(database)
        self.store.flush()
        
        # Redirect back to the front page with a status message

        IStatusMessage(self.request).addStatusMessage(
                _(u"Thank you for your order. We will contact you shortly"), 
                "info"
            )
        
        contextURL = self.context.absolute_url()
        self.request.response.redirect(contextURL)
        
    @button.buttonAndHandler(_(u"Cancel"))
    def handleCancel(self, action):
        """User cancelled. Redirect back to the front page.
        """
        contextURL = self.context.absolute_url()
        self.request.response.redirect(contextURL)
        



   
