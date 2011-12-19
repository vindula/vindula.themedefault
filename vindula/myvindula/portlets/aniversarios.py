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
#import datetime
from DateTime.DateTime import DateTime
import calendar 

class TypesSearch():
    """ Cria SimpleVocabulary """

    def __call__(self):
        itens=[(1,'Aniversariantes do dia'), (7,'Aniversariantes da semana'),  (30,'Aniversariantes do mês')]
        L=[]
        for i in itens:
            L.append(SimpleTerm(i[0], i[0], unicode(i[1])))
                
        return SimpleVocabulary(L)


class IPortletAniversarios(IPortletDataProvider):
      
    """A portlet
    It inherits from IPortletDataProvider because for this portlet, the
    data that is being rendered and the portlet assignment itself are the
    same.
    """

    title_portlet = schema.TextLine(title=unicode("Título", 'utf-8'),
                                  description=unicode("Título que aparecerá no cabeçalho do portlet.", 'utf-8'),
                                  required=True)
    
    quantidade_portlet = schema.Int(title=unicode("Quantidade de Items", 'utf-8'),
                                  description=unicode("quantidade limite de item mostrado no portlet.", 'utf-8'),
                                  required=True)
   
    type_search = schema.Choice(title=unicode("Tipo do filtro", 'utf-8'),
                                description=unicode("Selecione o Fitro que sera usado no portlet", 'utf-8'),
                                vocabulary=TypesSearch().__call__())

class Assignment(base.Assignment):
    """Portlet assignment.
    This is what is actually managed through the portlets UI and associated
    with columns.
    """

    implements(IPortletAniversarios)
    # TODO: Add keyword parameters for configurable parameters here
    def __init__(self, title_portlet=u'', quantidade_portlet=u'',type_search=u''):
       self.title_portlet = title_portlet
       self.quantidade_portlet = quantidade_portlet
       self.type_search = type_search

    @property
    def title(self):
        """This property is used to give the title of the portlet in the
        "manage portlets" screen.
        """
        return "Portlet Aniversarios"
    
class Renderer(base.Renderer):
    """Portlet renderer.

    This is registered in configure.zcml. The referenced page template is
    rendered, and the implicit variable 'view' will refer to an instance
    of this class. Other methods can be added and referenced in the template.
    """
    render = ViewPageTemplateFile('portlet_aniversarios.pt')            
    
    def get_title(self):
        return self.data.title_portlet
    
    def get_type_search(self):
        return self.data.type_search
   
    
    def get_quantidade_portlet(self):
        return self.data.quantidade_portlet
        
    def get_department(self, user):
        try:
            user_id = unicode(user, 'utf-8')    
        except:
            user_id = user
        
        return ModelsDepartment().get_departmentByUsername(user)        

    def get_birthdaysToday(self, type_filter):
        if type_filter == 1:
            date_start = date.today().strftime('%Y-%m-%d')
            date_end = date.today().strftime('%Y-%m-%d')
        
            results = ModelsFuncDetails().get_FuncBirthdays(date_start,date_end)
        
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
        
        if results:
            return results #results[:int(quant)]
        else:
            return []


    def birthdaysToday(self):
        type_filter = self.data.type_search
        #quant = self.data.quantidade_portlet
        
        results = self.get_birthdaysToday(type_filter)
        
        if results:
            return results #results[:int(quant)]
        else:
            return []
        
    
    def getEnd(self,i):
        if i:
            return 'info_boxTipo2'
        else:
            return 'info_boxTipo2 borderDif'
        
    def getPhoto(self,photo):
        if photo is not None and not ' ' in photo:
            return BaseFunc().get_imageVindulaUser(photo)
            #return self.context.absolute_url()+'/'+photo #+ '/image_thumb'
        else:
            return self.context.absolute_url()+'/defaultUser.png'    

    
        
class AddForm(base.AddForm):
    """Portlet add form.

    This is registered in configure.zcml. The form_fields variable tells
    zope.formlib which fields to display. The create() method actually
    constructs the assignment that is being added.
    """
    
    form_fields = form.Fields(IPortletAniversarios)
    
    def create(self, data):
       return Assignment(**data)
   
class EditForm(base.EditForm):
    """Portlet edit form.

    This is registered with configure.zcml. The form_fields variable tells
    zope.formlib which fields to display.
    """
    form_fields = form.Fields(IPortletAniversarios)
