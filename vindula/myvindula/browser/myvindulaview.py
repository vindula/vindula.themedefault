from zope.interface import implements

from Products.Five import BrowserView

from vindula.myvindula.browser.interfaces import IMyVindulaView
#from plone.dexterity.utils import createContent
from plone.dexterity.utils import createContentInContainer





_marker = []


class MyVindulaView(BrowserView):
    implements(IMyVindulaView)

    # Utility methods

	#index = ViewPageTemplateFile('myvindulaview.pt')
    

    def getPortrait(self):
        
        import pdb; pdb.set_trace()
        
	
        return self.context.portal_membership.getPersonalPortrait().tag()
        
		
		
    def __call__(self):
        form = self.request.form
        submitted = form.get('form.submitted', False)
        if submitted:
            
            homefolder = self.context.portal_membership.getHomeFolder()
            howareu = form.get('howareu')          
            
            item = createContentInContainer(homefolder, "vindula.myvindula.howareu", title=howareu)
                    
            
            #homefolder.createContent('vindula.myvindula.howareu', title=howareu)
            
            return self.index()

        return self.index()