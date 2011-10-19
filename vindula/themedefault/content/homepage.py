# coding=utf-8
from five import grok
from zope import schema
from plone.directives import dexterity, form
from plone.formwidget.contenttree import ObjPathSourceBinder
from vindula.themedefault import MessageFactory as _
from z3c.relationfield.schema import RelationList, RelationChoice

# Interface and schema

class IHomePage(form.Schema):
    """ Home Page """
    
    title = schema.TextLine(
        title=_(u"Título"),
        )


    refnewsitem = RelationList(
        title=u"Notícias destaque",
        description=u"Selecione as notícias que deverão rotacionar na área de destaque.",
        default=[],
        value_type=RelationChoice(
            title=_(u"Notícias destaque"),
            source=ObjPathSourceBinder(
                portal_type = 'News Item',  
                review_state='published'                                                  
                )
            ),
            required=False,
        )
    
    
# Methods   
    
class HomePage(dexterity.Item):
    grok.implements(IHomePage)
    
    def getNews(self):
        return 'news'

# View
    
class SampleView(grok.View):
    grok.context(IHomePage)
    grok.require('zope2.View')
    grok.name('view')