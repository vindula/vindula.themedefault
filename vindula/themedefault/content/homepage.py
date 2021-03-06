# -*- coding: utf-8 -*-
from five import grok

from datetime import datetime, timedelta

from vindula.themedefault import MessageFactory as _
from Products.CMFCore.utils import getToolByName
from zope.app.component.hooks import getSite

from AccessControl import ClassSecurityInfo
# from vindula.themedefault.browser.viewlets import MenuViewlet

from zope.interface import Interface

from vindula.themedefault.content.interfaces import IHomePage
from Products.ATContentTypes.content.document import ATDocumentSchema
from Products.ATContentTypes.content.document import ATDocumentBase

from zope.interface import implements
from Products.Archetypes.atapi import *
from archetypes.referencebrowserwidget.widget import ReferenceBrowserWidget
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from vindula.themedefault.config import *

from vindula.controlpanel.browser.at.widget import VindulaReferenceSelectionWidget

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
        widget=VindulaReferenceSelectionWidget(
            default_search_index='SearchableText',
            label=_(u"Seleção de banner(s)"),
            description=_(u"Selecione o objeto que será mostrado no banner."),
            review_state = ('published', 'external'),

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

    StringField(
        name='type_navigation',
        widget=SelectionWidget(
            label=_(u"Tipo da paginação dos banners"),
            description=_(u"Selecione o tipo de paginação dos banners rotativos da página inicial."),
            label_msgid='vindula_themedefault_label_type_navigation',
            description_msgid='vindula_themedefault_help_type_navigation',
            i18n_domain='vindula_themedefault',
            format='radio',
        ),
        vocabulary=[("number","Número"),("image","Imagem")],
        default="image",
        required=True,
    ),

    BooleanField(
        name='disable_breadcrumbs',
        widget=BooleanWidget(
            label=_(u"Desativa o breadcrumbs na homepage"),
            description=_(u"Selecione para desativar o breadcrumbs na visualização do objeto homepage"),
            label_msgid='vindula_themedefault_label_disable_breadcrumbs',
            description_msgid='vindula_themedefault_help_disable_breadcrumbs',
            i18n_domain='vindula_themedefault',
        ),
        default=False
    ),

#Fim Configurar Banner  -------------------------------------
    TextField(
            name='content_top',
            default_content_type = 'text/html',
            default_output_type = 'text/x-html-safe',

            searchable = True,
            widget=RichWidget(
                label=_(u"Conteúdo do Topo"),
                description=_(u"Campo de preenchimento livre, seu conteúdo ficará posicionado no topo da página \
                             acima das notícias em destaque."),
                rows=10,
                label_msgid='vindula_themedefault_label_content_top',
                description_msgid='vindula_themedefault_help_content_top',
                i18n_domain='vindula_themedefault',

            ),
            required=False,
    ),

    TextField(
            name='content_middle_top',
            default_content_type = 'text/html',
            default_output_type = 'text/x-html-safe',

            searchable = True,
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
            default_content_type = 'text/html',
            default_output_type = 'text/x-html-safe',

            searchable = True,
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
            default_content_type = 'text/html',
            default_output_type = 'text/x-html-safe',

            searchable = True,
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
        allowed_types=('Folder', 'Link', 'VindulaFolder'),
        relationship='ref_itemMenu',
        widget=VindulaReferenceSelectionWidget(
            default_search_index='SearchableText',
            label=_(u"Selecionar menu"),
            description=_(u"Selecione o objeto que será mostrado no menu."),
            review_state = ('published', 'external'),

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
        widget=VindulaReferenceSelectionWidget(
            default_search_index='SearchableText',
            label=_(u"Notícias da área de destaque"),
            description=_(u"Selecione as notícias que deverão rotacionar na área de destaque."),
            typeview='list',
            review_state = ('published', 'external'),

            label_msgid='vindula_themedefault_label_ref_itemMenu',
            description_msgid='vindula_themedefault_help_ref_itemMenu',
            i18n_domain='vindula_themedefault',
            ),
        required=False
    ),

    BooleanField(
        name='active_autonews',
        widget=BooleanWidget(
            label=_(u"Ativar destaques de notícias automáticas"),
            description=_(u"Mostrar automaticamente as novas notícias adicionadas no portal."),
            label_msgid='vindula_themedefault_label_active_autonews',
            description_msgid='vindula_themedefault_help_active_autonews',
            i18n_domain='vindula_themedefault',
        ),
        required=False
    ),

    IntegerField(
        name='amount_autonews',
        widget=IntegerWidget(
            label=_(u"Quantidade máxima de notícias automáticas"),
            description=_(u"Indique a quantidade máxima de novas notícias automáticas a serem exibidos no destaque."),
            label_msgid='vindula_themedefault_label_amount_autonews',
            description_msgid='vindula_themedefault_help_amount_autonews',
            i18n_domain='vindula_themedefault',
        ),
        default=3,
        required=True,
    ),

    IntegerField(
        name='period_autonews',
        widget=IntegerWidget(
            label=_(u"Quantidade de dias para a notícia ser nova"),
            description=_(u"Indique a quantidade máxima de dias que uma notícia é válida."),
            label_msgid='vindula_themedefault_label_amount_autonews',
            description_msgid='vindula_themedefault_help_amount_autonews',
            i18n_domain='vindula_themedefault',
        ),
        default=3,
        required=True,
    ),

    ReferenceField('local_autonews',
        multiValued=0,
        allowed_types=('Folder', 'VindulaFolder'),
        relationship='local_autonews',
        widget=VindulaReferenceSelectionWidget(
            default_search_index='SearchableText',
            label=_(u"Local das notícias automaticas"),
            description=_(u"Selecione o local das notícias. \
                            Se nada for selecionado, o sistema irá buscar notícias em todo o portal."),
            review_state = ('published', 'external'),
            typeview='list',

            label_msgid='vindula_themedefault_label_local_autonews',
            description_msgid='vindula_themedefault_help_local_autonews',
            i18n_domain='vindula_themedefault'),
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
        allowed_types=('Folder', 'VindulaFolder'),
        relationship='news_othernews',
        widget=VindulaReferenceSelectionWidget(
            default_search_index='SearchableText',
            label=_(u"Local das outras notícias"),
            description=_(u"Selecione o local das notícias. \
                            Se nada for selecionado, o sistema irá buscar notícias em todo o portal."),
            review_state = ('published', 'external'),
            typeview='list',

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

    StringField(
        name='tags_othernews',
        widget=InAndOutWidget(
            label=_(u"Filtro de Exibição (por Tags)"),
            description=_(u"Somente serão exibidos na listagem as notícias que tiverem as Tags selecionadas na coluna da direita."),
        ),
        vocabulary='voc_keywords',
        required=False,
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
        allowed_types=('Folder', 'VindulaFolder'),
        relationship='news_medianews',
        widget=VindulaReferenceSelectionWidget(
            #default_search_index='SearchableText',
            typeview='list',
            label=_(u"Local das noticias mídia"),
            description=_(u"Selecione o local das notícias. \
                           Se nada for selecionado, o sistema irá buscar notícias em todo o portal."),
            review_state = ('published', 'external'),

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

    StringField(
        name='tags_medianews',
        widget=InAndOutWidget(
            label=_(u"Filtro de Exibição (por Tags)"),
            description=_(u"Somente serão exibidos na listagem as notícias que tiverem as Tags selecionadas na coluna da direita."),
        ),
        vocabulary='voc_keywords',
        required=False,
    ),


    BooleanField(
        name='active_banner_html',
        widget=BooleanWidget(
            label=_(u"Ativar o banner HTML na homepage"),
            description=_(u"Mostrar o banner HTML no cabeçalho da homepage"),
            label_msgid='vindula_themedefault_label_active_banner_html',
            description_msgid='vindula_themedefault_help_active_banner_html',
            i18n_domain='vindula_themedefault',
        ),
        required=False
    ),

    TextField(
        name='banner_html',
        allowable_content_types=('text/plain',),
        default_content_type='text/plain',
        widget=TextAreaWidget(
            label=_(u"Banner da homepage HTML"),
            description=_(u"Insira um código em HTML para ser inserido no cabeçalho da homepage."),
            rows=10,
        ),
        required=False,
    ),

))

finalizeATCTSchema(HomePage_schema, folderish=False)
HomePage_schema.changeSchemataForField('title_highlightednews', 'Notícias')
HomePage_schema.changeSchemataForField('ref_newsitem', 'Notícias')
HomePage_schema.changeSchemataForField('active_autonews', 'Notícias')
HomePage_schema.changeSchemataForField('period_autonews', 'Notícias')
HomePage_schema.changeSchemataForField('amount_autonews', 'Notícias')
HomePage_schema.changeSchemataForField('local_autonews', 'Notícias')
HomePage_schema.changeSchemataForField('time_transitionsnews', 'Notícias')
HomePage_schema.changeSchemataForField('title_othernews', 'Notícias')
HomePage_schema.changeSchemataForField('local_othernews', 'Notícias')
HomePage_schema.changeSchemataForField('number_othernews', 'Notícias')
HomePage_schema.changeSchemataForField('tags_othernews', 'Notícias')
HomePage_schema.changeSchemataForField('title_medianews', 'Notícias')
HomePage_schema.changeSchemataForField('local_medianews', 'Notícias')
HomePage_schema.changeSchemataForField('number_medianews', 'Notícias')
HomePage_schema.changeSchemataForField('tags_medianews', 'Notícias')

HomePage_schema.changeSchemataForField('banner_html', 'Banner')
HomePage_schema.changeSchemataForField('active_banner_html', 'Banner')


invisivel = {'view':'invisible','edit':'invisible',}
HomePage_schema['description'].widget.visible = invisivel
HomePage_schema['text'].widget.visible = invisivel

# Dates
L = ['effectiveDate','expirationDate','creation_date','modification_date']
# Categorization
L += ['subject','relatedItems','location','language']
# Ownership
L += ['creators','contributors','rights']
# Settings
# L += ['allowDiscussion','excludeFromNav', 'presentation','tableContents']

for i in L:
    HomePage_schema[i].widget.visible = invisivel


class HomePage(ATDocumentBase):
    """ HomePage """
    security = ClassSecurityInfo()

    implements(IHomePage)
    portal_type = 'HomePage'
    _at_rename_after_creation = True
    schema = HomePage_schema

    def voc_keywords(self):
        #keywords = self.collectKeywords('NewsVindula', 'Subject')
        keywords = self.portal_catalog.uniqueValuesFor('Subject')
        return keywords

registerType(HomePage, PROJECTNAME)

# View
class HomePageView(grok.View):
    grok.context(IHomePage)
    grok.require('zope2.View')
    grok.name('view')

    UIDS_NEWS = []

    # Methods for News
    def getHighlightedNews(self):
        news = self.context.getRef_newsitem()
        self.UIDS_NEWS = []

        if self.context.getActive_autonews():
            auto_news = self.searchNews(local=self.context.getLocal_autonews(), limit=self.context.getAmount_autonews())
            if auto_news:
                period_min = datetime.now() - timedelta(days=self.context.getPeriod_autonews())
                if not news: news = []
                for new in auto_news:
                    if new.effective().asdatetime().date() >= period_min.date():
                        news.append(new)

        if news:
            L = []
            for obj in news:
                if obj is None:
                    news.remove(new)
                    continue
                D = {}
                D['UID'] = obj.UID()
                D['title'] = obj.Title()
                D['author'] = obj.getOwner().getUserName()
                try:D['date'] = obj.effective_date.strftime('%d/%m/%Y / %H:%m')
                except:D['date'] = ''
                D['link'] = obj.absolute_url()
                D['summary'] = ''
                if obj.Description() != '' or obj.Description() is not None:
                    D['summary'] = self.limitTextSize(350, obj.Description())
                D['image'] = ''

                if obj.portal_type == 'News Item':
                    if obj.getImage():
                        try:
                            D['image'] = obj.getImage().absolute_url() + '_mini'
                        except:
                            D['image'] = ''

                else:
                    if obj.getImageRelac():
                        try:
                            D['image'] = obj.getImageRelac().absolute_url() + '/image_mini'
                        except:
                            D['image'] = ''

                L.append(D)
            self.UIDS_NEWS = [i['UID'] for i in L]
            return L


    def getOtherNews(self):
        ctx = self.context
        news = self.searchNews(ctx.getLocal_othernews(), ctx.getNumber_othernews(), ctx.getTags_othernews())
        if ctx.getLocal_othernews() is None:
            url = ''
        else:
            url = ctx.getLocal_othernews().absolute_url()
        if news:
            L = []
            for obj in news:
                D = {}
                D['title'] = obj.Title()
                D['author'] = obj.getOwner().getUserName()
                try:D['date'] = obj.effective_date.strftime('%d/%m/%Y / %H:%m')
                except:D['date'] = ''
                D['link'] = obj.absolute_url()
                D['summary'] = obj.Description()
                D['uid'] = obj.UID()
                D['cotent_type'] = obj.portal_type

                L.append(D)
            return {'news' : L, 'url': url }
        else:
            return {'news' : [], 'url': url }

    def getMediaNews(self):
        L=[]
        ctx = self.context
        news = self.searchNews(ctx.getLocal_medianews(), ctx.getNumber_medianews(), ctx.getTags_medianews())
        if news:
            for obj in news:
                    D = {}
                    D['title'] = obj.Title()
                    D['link'] = obj.absolute_url()
                    L.append(D)
        return L

    def searchNews(self, local=None, limit=5, keywords=[]):
        L = []
        if limit:
            query = {}
            keywords = [i for i in keywords if i != '']

            if local is None:
                local = self.context.portal_url.getPortalObject().getPhysicalPath()
            else:
                local = local.getPhysicalPath()

            self.pc = getToolByName(self.context, 'portal_catalog')
            query['portal_type'] = ('VindulaNews', 'News Item')
            query['review_state'] = ['published', 'internally_published', 'external']
            query['path'] = {'query':'/'.join(local)}
            query['sort_on'] = 'effective'
            query['sort_order'] = 'descending'
            if keywords:
                query['Subject'] = keywords

            news = self.pc(**query)
            if news:
                for new in news:
                    try: new = new.getObject()
                    except: continue
                    if new.UID() not in self.UIDS_NEWS:
                        L.append(new)
                        self.UIDS_NEWS.append(new.UID())
                        if len(L) == limit: break
        return L

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

    def limitTextSize(self, size, text):
        if len(text) > size:
            i = size
            while text[i] != " " and (text[i] < len(text)):
                i += 1
            return text[:i]+'...'
        else:
            return text
