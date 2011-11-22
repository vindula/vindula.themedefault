# -*- coding: utf-8 -*-
""" Liberiun Technologies Sistemas de Informação Ltda. """
""" Produto:                 """

from zope.interface import implements
from zope.formlib import form 
from zope import schema

from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

from vindula.myvindula.user import BaseFunc, ModelsDepartment, ModelsFuncDetails

class IPortletRamais(IPortletDataProvider):
      
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
    

class Assignment(base.Assignment):
    """Portlet assignment.

    This is what is actually managed through the portlets UI and associated
    with columns.
    """

    implements(IPortletRamais)

    # TODO: Add keyword parameters for configurable parameters here
    def __init__(self, title_portlet=u'', quantidade_portlet=u''):
       self.title_portlet = title_portlet
       self.quantidade_portlet = quantidade_portlet


    @property
    def title(self):
        """This property is used to give the title of the portlet in the
        "manage portlets" screen.
        """
        return "Portlet Ramais"
    

    
class Renderer(base.Renderer):
    """Portlet renderer.

    This is registered in configure.zcml. The referenced page template is
    rendered, and the implicit variable 'view' will refer to an instance
    of this class. Other methods can be added and referenced in the template.
    """
    render = ViewPageTemplateFile('portlet_ramais.pt')            
    
    def get_title(self):
        return self.data.title_portlet
    
    
    def list_departamentos(self):
        return  ModelsDepartment().get_department()
    
    def get_quantidade_portlet(self):
        return self.data.quantidade_portlet

    def get_department(self, user):
        try:
            user_id = unicode(user, 'utf-8')    
        except:
            user_id = user
        
        return ModelsDepartment().get_departmentByUsername(user)      

            
#    @view.memoize
    def busca_usuarios(self):
        form = self.request.form
        title = form.get('title','').strip()
        departamento= form.get('departamento','')
        ramal = form.get('ramal','').strip()
        result = ModelsFuncDetails().get_FuncBusca(unicode(title, 'utf-8'),unicode(departamento,'utf-8'),unicode(ramal, 'utf-8'))
        return result
    
    
    def getEnd(self,i):
        if i:
            return 'info_boxTipo2'
        else:
            return 'info_boxTipo2 borderDif'
        
    def getPhoto(self,photo):
        if photo is not None and not ' ' in photo:
            return BaseFunc().get_imageVindulaUser(photo)
            #return self.context.absolute_url()+'/'+photo # + '/image_thumb'
        else:
            return self.context.absolute_url()+'/defaultUser.png'            
        
class AddForm(base.AddForm):
    """Portlet add form.

    This is registered in configure.zcml. The form_fields variable tells
    zope.formlib which fields to display. The create() method actually
    constructs the assignment that is being added.
    """
    
    form_fields = form.Fields(IPortletRamais)
    
    def create(self, data):
       return Assignment(**data)
   
   
class EditForm(base.EditForm):
    """Portlet edit form.

    This is registered with configure.zcml. The form_fields variable tells
    zope.formlib which fields to display.
    """
    form_fields = form.Fields(IPortletRamais)
