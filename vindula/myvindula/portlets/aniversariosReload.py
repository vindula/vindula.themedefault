# -*- coding: utf-8 -*-
""" Liberiun Technologies Sistemas de Informação Ltda. """
""" Produto:                 """

from zope.interface import implements
from zope.formlib import form 
from zope import schema

from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

from vindula.myvindula.user import BaseFunc, ModelsDepartment, ModelsFuncDetails
from datetime import date
from storm.expr import Desc
#import datetime
from DateTime.DateTime import DateTime
import calendar 

from five import grok
from zope.interface import Interface

class TypesSearch():
    """ Cria SimpleVocabulary """

    def __call__(self):
        itens=[(1,'Aniversariantes do dia'), (7,'Aniversariantes da semana'),  (30,'Aniversariantes do mês'), ('prox', 'Próximos Aniversariantes')]
        L=[]
        for i in itens:
            L.append(SimpleTerm(i[0], i[0], unicode(i[1])))
                
        return SimpleVocabulary(L)

class IPortletAniversariosReload(IPortletDataProvider):
      
    """A portlet
    It inherits from IPortletDataProvider because for this portlet, the
    data that is being rendered and the portlet assignment itself are the
    same.
    """

    title_portlet = schema.TextLine(title=unicode("Título", 'utf-8'),
                                  description=unicode("Título que aparecerá no cabeçalho do portlet.", 'utf-8'),
                                  required=True)
    
    quantidade_portlet = schema.Int(title=unicode("Quantidade de Itens", 'utf-8'),
                                  description=unicode("Quantidade limite de itens mostrado no portlet.", 'utf-8'),
                                  required=True)
   
    type_search = schema.Choice(title=unicode("Tipo do filtro", 'utf-8'),
                                description=unicode("Selecione o fitro que sera usado no portlet", 'utf-8'),
                                vocabulary=TypesSearch().__call__())
    
    show_picture = schema.Bool(title=unicode("Exibir foto", 'utf-8'),
                                       description=unicode("Selecione para mostrar a foto dos aniversarientes no portlet.", 'utf-8'))
    
    tempo_rotacao = schema.Int(title=unicode("Tempo de Rodação do Itens", 'utf-8'),
                               description=unicode("Tempo em milisegundos que o portlet leva para rotacionar os itens, \
                                                      insira apenas números iteiros..", 'utf-8'),
                               default=8000,
                               required=True)
    
    search_random = schema.Bool(title=unicode("Ordem Randomica dos resultados", 'utf-8'),
                                       description=unicode("Selecione para mostrar abilitar a ordenação randomica dos aniversarientes no portlet.", 'utf-8'))
    
    details_user = schema.Text(title=unicode("Detalhes do aniversariante", 'utf-8'),
                                  description=unicode("Adicione detalhes sobre o aniversariante como Empresa, Matricula e outros. \
                                                       Adicione um campo por linha, no formato [Label] | [Campo].", 'utf-8'),
                                  required=False)

class Assignment(base.Assignment):
    """Portlet assignment.
    This is what is actually managed through the portlets UI and associated
    with columns.
    """

    implements(IPortletAniversariosReload)
    # TODO: Add keyword parameters for configurable parameters here
    def __init__(self, title_portlet=u'', quantidade_portlet=u'',type_search=u'',\
                 details_user=u'',show_picture=u'',search_random=u'',tempo_rotacao=u''):
       
       self.title_portlet = title_portlet
       self.quantidade_portlet = quantidade_portlet
       self.type_search = type_search
       self.details_user = details_user
       self.show_picture = show_picture
       self.search_random = search_random
       self.tempo_rotacao = tempo_rotacao

    @property
    def title(self):
        """This property is used to give the title of the portlet in the
        "manage portlets" screen.
        """
        return "Portlet Aniversarios - Reloading"
    
class Renderer(base.Renderer):
    """Portlet renderer.

    This is registered in configure.zcml. The referenced page template is
    rendered, and the implicit variable 'view' will refer to an instance
    of this class. Other methods can be added and referenced in the template.
    """
    render = ViewPageTemplateFile('portlet_aniversarios_reload.pt')            
    
    def get_title(self):
        return self.data.title_portlet
    
    def get_type_search(self):
        return self.data.type_search
    
    def show_picture(self):
        return self.data.show_picture
    
    def get_details_user(self, user):
        return self.data.details_user 
    
    def get_quantidade_portlet(self):
        return self.data.quantidade_portlet
   
    def get_search_random(self):
        return self.data.search_random
    
    def get_tempo_rotacao(self):
        return self.data.tempo_rotacao
        
class AddForm(base.AddForm):
    """Portlet add form.

    This is registered in configure.zcml. The form_fields variable tells
    zope.formlib which fields to display. The create() method actually
    constructs the assignment that is being added.
    """
    
    form_fields = form.Fields(IPortletAniversariosReload)
    
    def create(self, data):
       return Assignment(**data)
   
class EditForm(base.EditForm):
    """Portlet edit form.

    This is registered with configure.zcml. The form_fields variable tells
    zope.formlib which fields to display.
    """
    form_fields = form.Fields(IPortletAniversariosReload)


#--------------View de reload--------------------------------
class ReloadPortletView(grok.View):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('reload-aniversariantes')
    
    # This may be overridden in ZCML
    index = ViewPageTemplateFile("reload-aniversariantes.pt")    
    
    def render(self):
        return self.index()
    
    def show_picture(self):
        if 'show_picture' in self.request.keys():
            valor = self.request['show_picture']
            return eval(valor)
        
    
    def get_details_user(self, user):
        if 'details_user' in self.request.keys(): 
            try:
                lines = self.request['details_user'].splitlines()
                L = []
                for line in lines:
                    D = {}
                    line = line.replace('[', '').replace(']', '').split(' | ')
                    D['label'] = line[0]
                    D['content'] = user.get(line[1])
                    L.append(D)
                return L
            except:
                pass
        return None
    
        
    def get_department(self, user):
        try:
            user_id = unicode(user, 'utf-8')    
        except:
            user_id = user
        
        return ModelsDepartment().get_departmentByUsername(user)        

    def get_birthdaysToday(self, type_filter):
        results = None
        random = False
        if 'search_random' in self.request.keys():
            random = eval(self.request['search_random'])
        
        if type_filter == 1:
            date_start = date.today().strftime('%Y-%m-%d')
            date_end = date.today().strftime('%Y-%m-%d')
            
            results = ModelsFuncDetails().get_FuncBirthdays(date_start,date_end,random)
        
        elif type_filter == 7:
            now = DateTime()
            dow = now.dow()
            date_start = (now + 1 - dow).strftime('%Y-%m-%d')
            date_end = (now + 1 - dow + 6).strftime('%Y-%m-%d')
            
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


    def birthdaysToday(self):
        if 'type_search' in self.request.keys():
            type_filter = int(self.request['type_search'])
            
            results = self.get_birthdaysToday(type_filter)
        else:
            results = None
        
        if results:
            return results 
        else:
            return []
        
    
    def getEnd(self,i):
        if i:
            return 'info_boxTipo2'
        else:
            return 'info_boxTipo2 borderDif'
        
    def getPhoto(self,photo):
        if photo is not None and not ' ' in photo:
            url_foto = BaseFunc().get_imageVindulaUser(photo)
            if url_foto:
                return url_foto
                #return self.context.absolute_url()+'/'+photo #+ '/image_thumb'
            else:
                return self.context.absolute_url()+'/defaultUser.png'
        else:
            return self.context.absolute_url()+'/defaultUser.png'     

