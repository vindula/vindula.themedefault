# -*- coding: utf-8 -*-
from five import grok
from zope import schema
from plone.directives import form
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.app.textfield import RichText
from vindula.themedefault import MessageFactory as _
from z3c.relationfield.schema import RelationList, RelationChoice
from Products.CMFCore.utils import getToolByName
from zope.app.component.hooks import getSite

from vindula.themedefault.browser.viewlets import MenuViewlet 
# Interface and schema

class IHomePage(form.Schema):
    """ Home Page """
   
    title = schema.TextLine(
        title=_(u"Título"),
        description=_(u"Insira um nome para Home Page."),
        )
    
    content_top = RichText(
        title=_(u"Conteúdo do Topo"),
        description=_(u"Campo de preenchimento livre, seu conteúdo ficará posicionado no topo da página \
                        acima das notícias em destaque."),
        required=False,
        )
    
    content_middle_top = RichText(
        title=_(u"Conteúdo do Meio (ACIMA da listagem de notícias)"),
        description=_(u"Campo de preenchimento livre, seu conteúdo ficará posicionado entre as notícias \
                        de destaque e a listagem principal das demais notícias."),
        required=False,
        )
    
    content_middle_bottom = RichText(
        title=_(u"Conteúdo do Meio (ABAIXO da listagem de notícias)"),
        description=_(u"Campo de preenchimento livre, seu conteúdo ficará posicionado entre a listagem \
                        principal das demais notícias e a área das outras notícias."),
        required=False,
        )
    
    content_bottom = RichText(
        title=_(u"Conteúdo Inferior"),
        description=_(u"Campo de preenchimento livre, seu conteúdo ficará posicionado no final da página \
                        abaixo de todas as notícias."),
        required=False,
        )
    
    ref_itemMenu = RelationChoice(title=_(u"Seleção do objeto de seleção do menu"),
                                  description=_(u"Selecione o objeto que sera mostrada no menu."),                      
                                  source=ObjPathSourceBinder(portal_type = ('Folder', 'Link'),  
                                                             review_state = ('published','internal','external')),
                                  required=False)
    
    # Fieldset News
    form.fieldset('news',
            label=_(u"Notícias"),
            fields=['title_highlightednews', 
                    'ref_newsitem', 
                    'time_transitionsnews',
                    'title_othernews',
                    'local_othernews',
                    'number_othernews',
                    'title_medianews',
                    'local_medianews',
                    'number_medianews',
                    ])
    
    title_highlightednews = schema.TextLine(
        title=_(u"Título da área de destaques"),
        description=_(u"Título para a área das notícias em destaque."),
        default=_(u"Destaques"),
        required=False,
        )

    ref_newsitem = RelationList(
        title=_(u"Notícias da área de destaque"),
        description=_(u"Selecione as notícias que deverão rotacionar na área de destaque."),
        default=[],
        value_type=RelationChoice(
            title=_(u"Notícias em destaque"),
            source=ObjPathSourceBinder(
                portal_type = ('vindula.content.content.vindulanews', 'News Item'),  
                review_state='published'                                                  
                )
            ),
            required=False,
        )
    
    time_transitionsnews = schema.Int(
        title=_(u"Velocidade da rotação"),
        description=_(u"Tempo em milisegundos que a notícia destaque leva para rotacionar, \
                      insira apenas números iteiros."),
        default=8000,
        required=True,
        )

    title_othernews = schema.TextLine(
        title=_(u"Título da área de sub destaque"),
        description=_(u"Título para a área das notícias em sub destaque."),
        default=_(u"Mais Notícias"),
        required=False,
        )
    
    local_othernews = RelationChoice(
        title=_(u"Local das outras noticias"),
        description=_(u"Selecione o local das notícias. \
                        Se nada for selecionado, o sistema irá buscar notícias em todo o portal."),                      
        source=ObjPathSourceBinder(
            portal_type = 'Folder',  
            review_state='published'       
            ),
        required=False,
        )
    
    number_othernews = schema.Int(
        title=_(u"Quantidade de notícias da área de sub destaque"),
        description=_(u"Quantidade de notícias que deverão aparecer na área de sub destaques, \
                      insira apenas números iteiros."),
        default=3,
        required=True,
        )
    
    title_medianews = schema.TextLine(
        title=_(u"Título da área das outras notícias"),
        description=_(u"Título para a área das notícias sem destaque."),
        default=_(u"Outras Notícias"),
        required=False,
        )
    
    local_medianews = RelationChoice(
        title=_(u"Local das noticias mídia"),
        description=_(u"Selecione o local das notícias. \
                        Se nada for selecionado, o sistema irá buscar notícias em todo o portal."),                           
        source=ObjPathSourceBinder(
            portal_type = 'Folder',  
            review_state='published'       
            ),
        required=False,
        )
    
    number_medianews = schema.Int(
        title=_(u"Quantidade de itens na área das outras notícias"),
        description=_(u"Quantidade de notícias sem destaque que deverão aparecer, \
                      insira apenas números iteiros."),
        default=3,
        required=True,
        )
    
# View
    
class HomePageView(grok.View):
    grok.context(IHomePage)
    grok.require('zope2.View')
    grok.name('view')
    
    # Methods for News
    
    def getHighlightedNews(self):
        news = self.context.ref_newsitem
        if news:
            L = []
            for new in news[:24]:
                obj = new.to_object
                if obj is None:
                    news.remove(new)
                    continue
                D = {}
                D['title'] = obj.Title()
                D['author'] = obj.getOwner().getUserName()
                D['date'] = obj.effective_date.strftime('%d/%m/%Y / %H:%m')
                D['link'] = obj.absolute_url()
                D['summary'] = ''
                D['image'] = ''
                
                if obj.portal_type == 'News Item':
                    if obj.Description() != '' or obj.Description() is not None:
                        D['summary'] = obj.Description()[:350]
    
                    if obj.getImage():
                        try:
                            D['image'] = obj.getImage().absolute_url() + '_mini'
                        except:
                            D['image'] = ''
                    
                else:
                    if obj.summary != '' and obj.summary is not None:
                        D['summary'] = obj.summary[:350]
                    
                    
                    if obj.image:
                        try:
                            D['image'] = obj.image.to_object.absolute_url() + '/image_mini'
                        except:
                            D['image'] = ''
                    
                if len(D['summary']) == 350:
                    D['summary'] += '...'

                L.append(D)
            return L
        
    def getOtherNews(self):
        news = self.searchNews(self.context.local_othernews)
        if news:
            L = []
            for new in news[:self.context.number_othernews]:
                obj = new.getObject()
                D = {}
                D['title'] = obj.Title()
                D['author'] = obj.getOwner().getUserName()
                D['date'] = obj.effective_date.strftime('%d/%m/%Y / %H:%m')
                D['link'] = obj.absolute_url()
                
                if obj.portal_type == 'News Item':
                    D['summary'] = obj.Description()
                else:
                    D['summary'] = obj.summary
                     
                L.append(D)
                
            if self.context.local_othernews is None or \
               self.context.local_othernews.to_object is None:
                url = ''
            else:
                url = self.context.local_othernews.to_object.absolute_url()
                
            return {'news' : L, 'url': url }
        
    def getMediaNews(self):
        news = self.searchNews(self.context.local_medianews)
        if news:
            L = []
            for new in news[:self.context.number_medianews]:  
                obj = new.getObject()
                D = {}
                D['title'] = obj.Title()
                D['link'] = obj.absolute_url()
                L.append(D)
            return L
        
    def searchNews(self, local=None):
        if local is None or local.to_object is None:
            local = self.context.portal_url.getPortalObject().getPhysicalPath()
        else:
            local = local.to_object.getPhysicalPath()
        self.pc = getToolByName(self.context, 'portal_catalog')
        news = self.pc(portal_type=('vindula.content.content.vindulanews', 'News Item'),
                       review_state='published',
                       path={'query':'/'.join(local)},
                       sort_on='effective',
                       sort_order='descending',)
        return news