# -*- coding: utf-8 -*-
from five import grok

from vindula.themedefault import MessageFactory as _
from Products.CMFCore.utils import getToolByName
from zope.app.component.hooks import getSite

from AccessControl import ClassSecurityInfo
from vindula.themedefault.browser.viewlets import MenuViewlet 

from zope.interface import Interface

from vindula.themedefault.content.interfaces import IHomePage
from Products.ATContentTypes.content.document import ATDocumentSchema
from Products.ATContentTypes.content.document import ATDocumentBase

from zope.interface import implements
from Products.Archetypes.atapi import *
from archetypes.referencebrowserwidget.widget import ReferenceBrowserWidget
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from vindula.themedefault.config import *


HomePage_schema =  ATDocumentSchema.copy() + Schema((
                                                     
#Configurar Banner  -------------------------------------
                                                     
    BooleanField(
        name='active_banner',
        widget=BooleanWidget(
            label=_(u"Ativar banner na homepage"),
            description=_(u"Selecione para ativar o banner na homepage"),
            label_msgid='vindula_themedefault_label_active_banner',
            description_msgid='vindula_themedefault_help_active_banner',
            i18n_domain='vindula_themedefault',
        ),
    ),

    ReferenceField('ref_banner',
        multiValued=1,
        allowed_types=('Image', 'Banner'),
        relationship='ref_banner',
        widget=ReferenceBrowserWidget(
            default_search_index='SearchableText',
            label=_(u"Seleção do objeto de seleção do banner"),
            description=_(u"Selecione o objeto que será mostrado no banner."),
            
            label_msgid='vindula_themedefault_label_ref_banner',
            description_msgid='vindula_themedefault_help_ref_banner',
            i18n_domain='vindula_themedefault',
            ),
        required=False
    ),
    
    IntegerField(
        name='time_transition_banner',
        widget=IntegerWidget(
            label=_(u"Velocidade da rotação do banner"),
            description=_(u"Tempo em milissegundos que a imagem do banner leva para rotacionar, \
                          insira apenas números inteiros."),
            
            label_msgid='vindula_themedefault_label_time_transition_banner',
            description_msgid='vindula_themedefault_help_time_transition_banner',
            i18n_domain='vindula_themedefault',
        ),
        default=8000,
        required=True,
    ),
    
#Fim Configurar Banner  -------------------------------------

    TextField(
            name='content_top',
            default_content_type = 'text/restructured',
            default_output_type = 'text/x-html-safe',
            widget=RichWidget(
                label=_(u"Conteúdo do Topo"),
                description=_(u"Campo de preenchimento livre, seu conteúdo ficará posicionado no topo da página \
                             acima das notícias em destaque."),
                rows="10",
                label_msgid='vindula_themedefault_label_content_top',
                description_msgid='vindula_themedefault_help_content_top',
                i18n_domain='vindula_themedefault',

            ),
            required=False,
    ),

    TextField(
            name='content_middle_top',
            default_content_type = 'text/restructured',
            default_output_type = 'text/x-html-safe',
            widget=RichWidget(
                label=_(u"Conteúdo do Meio (ACIMA da listagem de notícias)"),
                description=_(u"Campo de preenchimento livre, seu conteúdo ficará posicionado entre as notícias \
                                de destaque e a listagem principal das demais notícias."),
                rows="10",
                label_msgid='vindula_themedefault_label_content_middle_top',
                description_msgid='vindula_themedefault_help_content_middle_top',
                i18n_domain='vindula_themedefault',                            
            ),
            required=False,
    ),
    
    TextField(
            name='content_middle_bottom',
            default_content_type = 'text/restructured',
            default_output_type = 'text/x-html-safe',
            widget=RichWidget(
                label=_(u"Conteúdo do Meio (ABAIXO da listagem de notícias)"),
                description=_(u"Campo de preenchimento livre, seu conteúdo ficará posicionado entre a listagem \
                                principal das demais notícias e a área das outras notícias."),
                rows="10",
                label_msgid='vindula_themedefault_label_content_middle_bottom',
                description_msgid='vindula_themedefault_help_content_middle_bottom',
                i18n_domain='vindula_themedefault',                              
            ),
            required=False,
    ),
    
    TextField(
            name='content_bottom',
            default_content_type = 'text/restructured',
            default_output_type = 'text/x-html-safe',
            widget=RichWidget(
                label=_(u"Conteúdo Inferior"),
                description=_(u"Campo de preenchimento livre, seu conteúdo ficará posicionado no final da página \
                                abaixo de todas as notícias."),
                rows="10",
                label_msgid='vindula_themedefault_label_content_bottom',
                description_msgid='vindula_themedefault_help_content_bottom',
                i18n_domain='vindula_themedefault',                              
            ),
            required=False,
    ),
    
    ReferenceField('ref_itemMenu',
        multiValued=0,
        allowed_types=('Folder', 'Link'),
        relationship='ref_itemMenu',
        widget=ReferenceBrowserWidget(
            default_search_index='SearchableText',
            label=_(u"Seleção do objeto de seleção do menu"),
            description=_(u"Selecione o objeto que será mostrado no menu."),
            
            label_msgid='vindula_themedefault_label_ref_itemMenu',
            description_msgid='vindula_themedefault_help_ref_itemMenu',
            i18n_domain='vindula_themedefault',
            ),
        required=False
    ),


#FieldSet Noticias-------------------------------------
#*********Destaque de  Noticias*****************
    TextField(
            name='title_highlightednews',
            widget=StringWidget(
                label=_(u"Título da área de destaques"),
                description=_(u"Título para a área das notícias em destaque."),
                
                label_msgid='vindula_themedefault_label_title_highlightednews',
                description_msgid='vindula_themedefault_help_title_highlightednews',
                i18n_domain='vindula_themedefault',
            ),
        default="Destaques",
        required=True,
    ),

    ReferenceField('ref_newsitem',
        multiValued=1,
        allowed_types=('VindulaNews', 'News Item'),
        relationship='ref_newsitem',
        widget=ReferenceBrowserWidget(
            default_search_index='SearchableText',
            label=_(u"Notícias da área de destaque"),
            description=_(u"Selecione as notícias que deverão rotacionar na área de destaque."),
            base_query={'review_state':'published'},
            
            label_msgid='vindula_themedefault_label_ref_itemMenu',
            description_msgid='vindula_themedefault_help_ref_itemMenu',
            i18n_domain='vindula_themedefault',
            ),
        required=False
    ),

    IntegerField(
        name='time_transitionsnews',
        widget=IntegerWidget(
            label=_(u"Velocidade da rotação"),
            description=_(u"Tempo em milissegundos que a notícia destaque leva para rotacionar, \
                          insira apenas números inteiros."),
            
            label_msgid='vindula_themedefault_label_time_transitionsnews',
            description_msgid='vindula_themedefault_help_time_transitionsnews',
            i18n_domain='vindula_themedefault',
        ),
        default=8000,
        required=True,
    ),

#*********Outras Noticias*****************
    TextField(
            name='title_othernews',
            widget=StringWidget(
                label=_(u"Título da área de sub destaque"),
                description=_(u"Título para a área das notícias em sub destaque."),
            
                label_msgid='vindula_themedefault_label_title_othernews',
                description_msgid='vindula_themedefault_help_title_othernews',
                i18n_domain='vindula_themedefault',                                                  
            ),
            default=u"Mais Notícias",
            required=True,
    ),

    ReferenceField('local_othernews',
        multiValued=0,
        allowed_types=('Folder'),
        relationship='news_othernews',
        widget=ReferenceBrowserWidget(
            default_search_index='SearchableText',
            label=_(u"Local das outras notícias"),
            description=_(u"Selecione o local das notícias. \
                            Se nada for selecionado, o sistema irá buscar notícias em todo o portal."),
            base_query={'review_state':'published'},
            
            label_msgid='vindula_themedefault_label_local_othernews',
            description_msgid='vindula_themedefault_help_local_othernews',
            i18n_domain='vindula_themedefault'),                   
        required=False
    ),
    
    IntegerField(
        name='number_othernews',
        widget=IntegerWidget(
            label=_(u"Quantidade de notícias da área de sub destaque"),
            description=_(u"Quantidade de notícias que deverão aparecer na área de sub destaques, \
                      insira apenas números inteiros."),
            
            label_msgid='vindula_themedefault_label_number_othernews',
            description_msgid='vindula_themedefault_help_number_othernews',
            i18n_domain='vindula_themedefault',                             
        ),
        default=3,
        required=True,
    ),
    
#*********Noticias secundarias*****************   
    TextField(
            name='title_medianews',
            widget=StringWidget(
                label=_(u"Título da área das outras notícias"),
                description=_(u"Título para a área das notícias sem destaque."),
            
                label_msgid='vindula_themedefault_label_title_medianews',
                description_msgid='vindula_themedefault_help_title_medianews',
                i18n_domain='vindula_themedefault'),
            default=u"Outras Notícias",
            required=True,
        ),

    ReferenceField('local_medianews',
        multiValued=0,
        allowed_types=('Folder'),
        relationship='news_medianews',
        widget=ReferenceBrowserWidget(
            default_search_index='SearchableText',
            label=_(u"Local das noticias mídia"),
            description=_(u"Selecione o local das notícias. \
                           Se nada for selecionado, o sistema irá buscar notícias em todo o portal."),   
            base_query={'review_state':'published'},
            
            label_msgid='vindula_themedefault_label_local_medianews',
            description_msgid='vindula_themedefault_help_local_medianews',
            i18n_domain='vindula_themedefault'),
        required=False
    ),
    
    IntegerField(
        name='number_medianews',
        widget=IntegerWidget(
            label=_(u"Quantidade de itens na área das outras notícias"),
            description=_(u"Quantidade de notícias sem destaque que deverão aparecer, \
                          insira apenas números inteiros."),
            
            label_msgid='vindula_themedefault_label_number_medianews',
            description_msgid='vindula_themedefault_help_number_medianews',
            i18n_domain='vindula_themedefault',                             
        ),
        default=3,
        required=True,
    ),
                                                      

))

finalizeATCTSchema(HomePage_schema, folderish=False)
HomePage_schema.changeSchemataForField('title_highlightednews', 'Notícias')
HomePage_schema.changeSchemataForField('ref_newsitem', 'Notícias')
HomePage_schema.changeSchemataForField('time_transitionsnews', 'Notícias')
HomePage_schema.changeSchemataForField('title_othernews', 'Notícias')
HomePage_schema.changeSchemataForField('local_othernews', 'Notícias')
HomePage_schema.changeSchemataForField('number_othernews', 'Notícias')
HomePage_schema.changeSchemataForField('title_medianews', 'Notícias')
HomePage_schema.changeSchemataForField('local_medianews', 'Notícias')
HomePage_schema.changeSchemataForField('number_medianews', 'Notícias')

invisivel = {'view':'invisible','edit':'invisible',}
HomePage_schema['description'].widget.visible = invisivel
HomePage_schema['text'].widget.visible = invisivel

class HomePage(ATDocumentBase):
    """ HomePage """
    security = ClassSecurityInfo()
    
    implements(IHomePage)    
    portal_type = 'HomePage'
    _at_rename_after_creation = True
    schema = HomePage_schema

registerType(HomePage, PROJECTNAME) 

    
# View
class HomePageView(grok.View):
    grok.context(IHomePage)
    grok.require('zope2.View')
    grok.name('view')
    
    # Methods for News
    def getHighlightedNews(self):
        news = self.context.getRef_newsitem()
        if news:
            L = []
            for obj in news[:24]:
                #obj = new.to_object
                if obj is None:
                    news.remove(new)
                    continue
                D = {}
                D['title'] = obj.Title()
                D['author'] = obj.getOwner().getUserName()
                try:D['date'] = obj.effective_date.strftime('%d/%m/%Y / %H:%m')
                except:D['date'] = ''
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
                    if obj.Description() != '' and obj.Description() is not None:
                        D['summary'] = obj.Description()[:350]
                    
                    
                    if obj.getImageRelac():
                        try:
                            D['image'] = obj.getImageRelac().absolute_url() + '/image_mini'
                        except:
                            D['image'] = ''
                    
                if len(D['summary']) == 350:
                    D['summary'] += '...'

                L.append(D)
            return L
        
    def getOtherNews(self):
        news = self.searchNews(self.context.getLocal_othernews())
        if self.context.getLocal_othernews() is None:
                url = ''
        else:
            url = self.context.getLocal_othernews().absolute_url()
        
        if news and self.context.getNumber_othernews():
            L = []
            for new in news[:self.context.getNumber_othernews()]:
                obj = new.getObject()
                D = {}
                D['title'] = obj.Title()
                D['author'] = obj.getOwner().getUserName()
                try:D['date'] = obj.effective_date.strftime('%d/%m/%Y / %H:%m')
                except:D['date'] = ''
                D['link'] = obj.absolute_url()
                
                if obj.portal_type == 'News Item':
                    D['summary'] = obj.Description()
                else:
                    D['summary'] = obj.Description()
                     
                L.append(D)
                
            return {'news' : L, 'url': url }
        else:
            return {'news' : [], 'url': url }
    def getMediaNews(self):
        news = self.searchNews(self.context.getLocal_medianews())
#        if self.context.getLocal_othernews():
#            path_otherNew = self.context.getLocal_othernews().absolute_url()
#        else:
#            path_otherNew = getSite().absolute_url()

        if news and self.context.getNumber_medianews():
            L = []
            path_otherNew = self.getOtherNews()
            if path_otherNew:
                items = path_otherNew.get('news')
                for i in items:
                    path_otherNew = i.get('link','')
                
            
            for new in news:  
                obj = new.getObject()

                if not obj.absolute_url() in path_otherNew : 
                    D = {}
                    D['title'] = obj.Title()
                    D['link'] = obj.absolute_url()
                    L.append(D)
                
                if len(L) == self.context.getNumber_medianews():
                    break
                
            
            return L
        else:
            return []
        
    def searchNews(self, local=None):
        if local is None:
            local = self.context.portal_url.getPortalObject().getPhysicalPath()
        else:
            local = local.getPhysicalPath()
        self.pc = getToolByName(self.context, 'portal_catalog')
        news = self.pc(portal_type=('VindulaNews', 'News Item'),
                       #review_state='published',
                       path={'query':'/'.join(local)},
                       sort_on='effective',
                       sort_order='descending',)
        return news
    
    def getBanner(self):
        L = []
        if self.context.getRef_banner():
            for banner in self.context.getRef_banner():
                try:
                    type_obj = banner.Type()
                except:
                    return L
                D={}
                D['url_image'] = ''
                D['image'] = ''
                D['title'] = banner.title
                if type_obj == 'Image':
                    D['image'] = banner.absolute_url()
                elif type_obj == 'Banner':
                    if banner.getLink():
                        D['target'] = banner.getTarget()
                        if banner.getRawImagem_banner():
                            D['image'] = banner.getRawImagem_banner().absolute_url()
                        link = banner.getLink()
                        if link: 
                            if link[:4] == 'http':
                                D['url_image'] = link
                            else:
                                D['url_image'] = 'http://%s' % link
                L.append(D)
        return L
