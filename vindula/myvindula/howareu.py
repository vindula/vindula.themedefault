from five import grok
from plone.directives import dexterity, form

from zope import schema

from z3c.form import group, field
from plone.app.z3cform.wysiwyg import WysiwygFieldWidget

from vindula.myvindula import MessageFactory as _



class IHowAreU(form.Schema):
    """
    How are u
    """
    


class HowAreU(dexterity.Item):
    grok.implements(IHowAreU)
    


#class SampleView(grok.View):
#    grok.context(IHowAreU)
#    grok.require('zope2.View')
#    
#    # grok.name('view')