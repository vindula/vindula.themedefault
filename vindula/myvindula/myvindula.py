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
from vindula.myvindula.user import IFuncDetails



class MyVindulaSearchForm(grok.View):
    grok.context(INavigationRoot)
    grok.require('zope2.View')
    grok.name('myvindulasearchform')
    
    def update(self):
        # disable Plone's editable border
        self.request.set('disable_border', True)
        

    




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
        
        # call the base class version - this is very important!
        super(MyVindulaPrefsView, self).update()
    
    @button.buttonAndHandler(_(u'Send'))
    def handleApply(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        
        
        # Put the threatment to database

        
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
        
        


