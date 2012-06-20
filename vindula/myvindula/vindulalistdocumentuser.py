# coding=utf-8
from five import grok
from zope import schema
from plone.directives import form

from vindula.content import MessageFactory as _
from zope.interface import Interface

from vindula.myvindula.validation import valida_form

from vindula.myvindula.document_models import BaseFunc, ModelsUserDocuments

from vindula.myvindula.user import ModelsFuncDetails


# Interface and schema
class IVindulaListDocumentUser(form.Schema):
    """ Vindula List Document User """
    
    form.mode(title='hidden')
    title = schema.TextLine(
        title=_(u"Título"),
        description=_(u"Título para o conteudo"),)
    
    
    field_filter = schema.Text(title=unicode("Campos para filtro dos documentos do usuários", 'utf-8'),
                              description=unicode("Adicione dos campo para fazer filtro como Empresa, Matricula , Nome e outros. \
                                                   Adicione um campo por linha, no formato [Label] | [Campo].", 'utf-8'),
                              default=unicode('[Nome] | [name]\n[Email] | [email]\n[Unidade Organizacional] | [organisational_unit]\n[Matricula] | [registration]'),
                              required=False)
    
    
class MyVindulaListDocumentView(grok.View, BaseFunc):
    grok.context(IVindulaListDocumentUser)
    grok.require('zope2.View')
    grok.name('view')
    
    
    def load_list(self):
        form = self.request.form # var tipo 'dict' que guarda todas as informacoes do formulario (keys,items,values)
        form_keys = form.keys() # var tipo 'list' que guarda todas as chaves do formulario (keys)
        
        if 'SearchSubmit' in form_keys:
            if 'filtro' in form_keys and 'title' in form_keys:
                filtro = form.get('filtro','')
                try:title = unicode(form.get('title',''),'utf-8')
                except:title = form.get('title','')
                status = int(form.get('status',''))
                L=[]
                
                if filtro == 'departamento':  
                    data = ModelsFuncDetails().get_FuncDetails_by_DepartamentName(title)
                else:
                    data = ModelsFuncDetails().get_FuncDetails_by_dinamicFind(filtro,title) 
                 
                if data:   
                    for item in data:
                        D = {}
                        try:user = unicode(item.username, 'utf-8')    
                        except:user = item.username
                        
                        if status == 0:
                            D['user'] = item
                        elif status == 1:
                            result = ModelsUserDocuments().get_UserDocuments_byUsername(user)
                            if result:
                                D['user'] = item
                        elif status == 2:
                            result = ModelsUserDocuments().get_UserDocuments_byUsername(user)
                            if not result:
                                D['user'] = item
                        if D:    
                            L.append(D)
                
                return L
    
    def get_filtro(self):
        filtros = self.context.field_filter
        if filtros: 
            try:
                lines = filtros.splitlines()
                L = []
                
                for line in lines:
                    D = {}
                    line = line.replace('[', '').replace(']', '').split(' | ')
                    D['label'] = line[0]
                    D['content'] = line[1]
                    L.append(D)
                return L
            except:
                pass
        return []
    
#    def doc_enviado(self, id):
#        membership = self.context.portal_membership
#        user_login = membership.getAuthenticatedMember()
#        
#        try:user = unicode(user_login.id, 'utf-8')
#        except:user = user_login.id
#        
#        doc_user = ModelsUserDocuments().get_UserDocuments_by_user_and_doc(user,int(id)) 
#        
#        if doc_user:
#            return doc_user.id
#        else:
#            return False
#        
#
#        
#        
#    
#            