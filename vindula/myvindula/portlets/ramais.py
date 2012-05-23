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
    
    quantidade_portlet = schema.Int(title=unicode("Quantidade de Itens", 'utf-8'),
                                  description=unicode("Quantidade limite de item mostrado no portlet.", 'utf-8'),
                                  required=True)
    
    filtro_departamento = schema.TextLine(title=unicode("Dados do campo departamento", 'utf-8'),
                                  description=unicode("Adicione qual dado do banco de dados será usado para filtro dos usuários,\
                                                      (Valor Padrão: 'departamentos')", 'utf-8'),
                                  default=unicode('departamentos','utf-8'),
                                  required=True) 

    show_picture = schema.Bool(title=unicode("Exibir foto", 'utf-8'),
                                       description=unicode("Selecione para mostrar a foto dos aniversariantes no portlet.", 'utf-8'))
    
    details_user = schema.Text(title=unicode("Detalhes do ramais", 'utf-8'),
                                  description=unicode("Adicione detalhes sobre os usuários como Empresa, Matricula e outros. \
                                                       Adicione um campo por linha, no formato [Label] | [Campo].", 'utf-8'),
                                  required=False)
    
    details_text = schema.Text(title=unicode("Texto do portlet", 'utf-8'),
                                  description=unicode("Adicione o texto que será mostrado no final da busca de ramais.", 'utf-8'),
                                  required=False)


class Assignment(base.Assignment):
    """Portlet assignment.

    This is what is actually managed through the portlets UI and associated
    with columns.
    """

    implements(IPortletRamais)

    # TODO: Add keyword parameters for configurable parameters here
    def __init__(self, title_portlet=u'', quantidade_portlet=u'', filtro_departamento=u'', show_picture=u'', details_user=u'',details_text=u''):
       self.title_portlet = title_portlet
       self.quantidade_portlet = quantidade_portlet
       self.filtro_departamento = filtro_departamento
       self.show_picture = show_picture
       self.details_user = details_user
       self.details_text = details_text

    @property
    def title(self):
        """This property is used to give the title of the portlet in the
        "manage portlets" screen.
        """
        return "Portlet busca de pessoas"
    

    
class Renderer(base.Renderer):
    """Portlet renderer.

    This is registered in configure.zcml. The referenced page template is
    rendered, and the implicit variable 'view' will refer to an instance
    of this class. Other methods can be added and referenced in the template.
    """
    render = ViewPageTemplateFile('portlet_ramais.pt')            
    
    def get_title(self):
        return self.data.title_portlet
    
    def show_picture(self):
        return self.data.show_picture
    
    def filtro_departamento(self):
        return self.data.filtro_departamento
    
    def get_details_text(self):
        return self.data.details_text
    
    def get_details_user(self, user):
        if self.data.details_user: 
            try:
                lines = self.data.details_user.splitlines()
                L = []
                
                for line in lines:
                    D = {}
                    line = line.replace('[', '').replace(']', '').split(' | ')
                    D['label'] = line[0]
                    D['content'] = user.__getattribute__(line[1])
                    L.append(D)
                return L
            except:
                pass
        return None
    
    def get_uid_struct_org(self,ctx):
        #import pdb;pdb.set_trace()
        if ctx.portal_type != 'Plone Site' and ctx.portal_type != 'OrganizationalStructure':
            return self.get_uid_struct_org(ctx.aq_inner.aq_parent)
        elif ctx.portal_type == 'OrganizationalStructure': 
            return ctx.UID()
        else:
            return None
    
    def list_filtro(self):
        campo = self.data.filtro_departamento
        result = ModelsFuncDetails().get_allFuncDetails()
        if result:
            classe = 'ModelsFuncDetails.'+str(campo)
            return result.group_by(eval(classe)).order_by()
    
    def list_departamentos(self):
        return  ModelsDepartment().get_department()
    
    def get_quantidade_portlet(self):
        return self.data.quantidade_portlet

    def get_department(self, user):
        try:
            user_id = unicode(user, 'utf-8')    
        except:
            user_id = user
        
        return ModelsDepartment().get_departmentByUsername(user_id)      

            
#    @view.memoize
    def busca_usuarios(self):
        form = self.request.form
        result = None
        filtro_busca = self.context.restrictedTraverse('@@myvindula-conf-userpanel').check_filtro_busca_user()
        
        if 'SearchSubmit' in form.keys():
            title = form.get('title','').strip()
            departamento= form.get('departamento','')
            ramal = form.get('ramal','').strip()
            if title or departamento !='0' or ramal:
            
                if type(title) != unicode:
                    title = unicode(title, 'utf-8')
                
                if type(departamento) != unicode:
                    departamento = unicode(departamento, 'utf-8')
                    
                if type(ramal) != unicode:
                    ramal = unicode(ramal, 'utf-8')
                    
                result = ModelsFuncDetails().get_FuncBusca(title,'0',ramal,True)
                if result:

                    if departamento != '0' and self.data.filtro_departamento != 'departamentos':
                        busca = "result.find("+self.data.filtro_departamento + "=u'" + departamento+"')"
                        data = eval(busca)
                        if data.count() != 0:
                            result = data
                        else:
                            result = None
                    elif self.data.filtro_departamento == 'departamentos':
                        data = ModelsFuncDetails().get_FuncBusca(title,departamento,ramal,filtro_busca)
                        if data:
                            result = data
                        else:
                            result = None
        return result
    
    
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
                #return self.context.absolute_url()+'/'+photo # + '/image_thumb'
            else:
                return self.context.absolute_url()+'/defaultUser.png'
        else:
            return self.context.absolute_url()+'/defaultUser.png'
        
    def check_filter(self):
        form = self.request.form
        if 'SearchSubmit' in form.keys():
            title = form.get('title','').strip()
            departamento= form.get('departamento','')
            ramal = form.get('ramal','').strip()
            if title or departamento !='0' or ramal:
                return 'Não há resultados.'
            else:
                return 'Defina um filtro acima e execute a busca novamente.'
        
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
