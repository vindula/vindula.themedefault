# coding: utf-8

from zope.app.component.hooks import getSite
from Products.CMFCore.utils import getToolByName

from Products.statusmessages.interfaces import IStatusMessage
from vindula.myvindula import MessageFactory as _

#Imports regarding the connection of the database 'strom'
from storm.locals import *
from storm.locals import Store
from vindula.myvindula.user import BaseStore, BaseFunc

from vindula.myvindula.validation import valida_form
from datetime import date , datetime 
import pickle

class ModelsConfigDocuments(Storm, BaseStore):    
    __storm_table__ = 'vin_myvindula_config_documents'
    
    id = Int(primary=True)
    name_document = Unicode()
    date_creation = DateTime()
    flag_ativo = Bool()
    
    
    def set_ConfigDocuments(self, **kwargs):
        # adicionando...
        confDoc = ModelsConfigDocuments(**kwargs)
        self.store.add(confDoc)
        self.store.flush()        
    
    def get_allConfigDocuments(self):
        data = self.store.find(ModelsConfigDocuments).order_by(ModelsConfigDocuments.name_document)
        if data.count() == 0:
            return None
        else:
            return data
        
    
    def get_ConfigDocuments_byID(self,id):
        data = self.store.find(ModelsConfigDocuments, ModelsConfigDocuments.id == id).one()
        if data:
            return data
        else:
            return None
                
    
    
class ModelsUserDocuments(Storm, BaseStore):    
    __storm_table__ = 'vin_myvindula_user_documents'
    
    id = Int(primary=True)
    documento = Pickle()
    date_creation = DateTime()
    vin_myvindula_funcdetails_username = Unicode()
    vin_myvindula_config_documents_id = Int()
    
    funcionario = Reference(vin_myvindula_funcdetails_username, "ModelsFuncDetails.username")
    nome_documento = Reference(vin_myvindula_config_documents_id, "ModelsConfigDocuments.id")
    
    def set_UserDocuments(self, **kwargs):
        # adicionando...
        userDoc = ModelsUserDocuments(**kwargs)
        self.store.add(userDoc)
        self.store.flush()
        
    def del_UserDocuments(self, user,doc):
        results = self.get_UserDocuments_by_user_and_doc(user, doc)
        if results:
            self.store.remove(results)
            self.store.flush()
        
    def get_UserDocuments(self):
        data = self.store.find(ModelsUserDocuments)
        if data.count() > 0:
            return data
        else:
            return None                

    def get_UserDocuments_byUsername(self, username):
        data = self.store.find(ModelsUserDocuments, ModelsUserDocuments.vin_myvindula_funcdetails_username == username)
        if data.count() > 0:
            return data
        else:
            return None

    def get_UserDocuments_byID(self, id):
        data = self.store.find(ModelsUserDocuments, ModelsUserDocuments.id == id).one()
        if data:
            return data
        else:
            return None    
    
    
    def get_UserDocuments_by_user_and_doc(self, user, doc):
        data = self.store.find(ModelsUserDocuments, ModelsUserDocuments.vin_myvindula_funcdetails_username == user,
                                                    ModelsUserDocuments.vin_myvindula_config_documents_id == doc).one()
        if data:
            return data
        else:
            return None
    
class SchemaManageDocument(BaseFunc):
    def to_utf8(value):
        return unicode(value, 'utf-8')
    
    campos = {'name_document'  : {'required': True,  'type' : to_utf8,},
              'flag_ativo'     : {'required': False, 'type' : bool,}}
    
    def registration_processes(self,ctx):
        success_url = ctx.context.absolute_url() + '/myvindula-manage-documents'
        access_denied = ctx.context.absolute_url() + '/@@vindula-control-panel'
        form = ctx.request.form # var tipo 'dict' que guarda todas as informacoes do formulario (keys,items,values)
        form_keys = form.keys() # var tipo 'list' que guarda todas as chaves do formulario (keys)
        campos = self.campos
        
        # divisao dos dicionarios "errors" e "convertidos"
        form_data = {
            'errors': {},
            'data': {},
            'campos':campos,}
        
        # se clicou no botao "Voltar"
        if 'form.voltar' in form_keys:
            ctx.request.response.redirect(success_url)
          
        # se clicou no botao "Salvar"
        elif 'form.submited' in form_keys:
            # Inicia o processamento do formulario
            # chama a funcao que valida os dados extraidos do formulario (valida_form) 
            errors, data = valida_form(campos, form)  

            if not errors:
                
                if 'id' in form_keys:
                    # editando...
                    id = int(form.get('id'))
                    result = ModelsConfigDocuments().get_ConfigDocuments_byID(id)
                    if result:
                        for campo in campos.keys():
                            value = data.get(campo, None)
                            setattr(result, campo, value)

                else:
                    ModelsConfigDocuments().set_ConfigDocuments(**data)
                    #adicionando...
                        
                #Redirect back to the front page with a status message
                IStatusMessage(ctx.request).addStatusMessage(_(u"Documento Cadastrado com sucesso"), "info")
                ctx.request.response.redirect(success_url)
                                   
            else:
                form_data['errors'] = errors
                form_data['data'] = data
                return form_data
          
        # se for um formulario de edicao 
        elif 'id' in form_keys:

            id = int(form.get('id'))
            data = ModelsConfigDocuments().get_ConfigDocuments_byID(id)
            
            D = {}
            for campo in campos.keys():
                D[campo] = getattr(data, campo, '')
              
            if data:
               form_data['data'] = D
               return form_data
            else:
               return form_data
              
        # se o usuario não estiver logado
        else:
            return form_data    
    
    
    
class SchemaDocument(BaseFunc):
    def to_utf8(value):
        return unicode(value, 'utf-8')
    
    campos = {'vin_myvindula_funcdetails_username'  : {'required': True, 'type' : to_utf8,},
              'vin_myvindula_config_documents_id'   : {'required': True, 'type' : int,},
              'documento'                           : {'required': True, 'type' : 'pickle',}
              }
    
    def registration_processes(self,ctx):
        success_url = ctx.context.absolute_url() + '/@@myvindula-recursos-humanos?id=myvindula-documents'
        access_denied = ctx.context.absolute_url() + '/login'
        form = ctx.request.form # var tipo 'dict' que guarda todas as informacoes do formulario (keys,items,values)
        form_keys = form.keys() # var tipo 'list' que guarda todas as chaves do formulario (keys)

        membership = ctx.context.portal_membership
        user_login = membership.getAuthenticatedMember()
        try:user = unicode(user_login.getUserName(), 'utf-8')
        except:user = user_login.getUserName()
        
        campos = self.campos
               
        # divisao dos dicionarios "errors" e "convertidos"
        form_data = {
            'errors': {},
            'data': {},
            'campos':campos,}
        
        # se clicou no botao "Voltar"
        if 'form.voltar' in form_keys:
            ctx.request.response.redirect(success_url)
          
        # se clicou no botao "Salvar"
        elif 'form.submited' in form_keys:
            # Inicia o processamento do formulario
            # chama a funcao que valida os dados extraidos do formulario (valida_form) 
            
            if 'documento' in form_keys:
                documentos = form['documento']
                if type(documentos) == list:
                    for doc in documentos:
                        convertidos = {}
            
                        data = doc.read()
                        if data:
                            filename = doc.filename
                            if len(data) != 0 :
                                D ={}
                                D['data'] = data
                                D['filename'] = filename 
                                convertidos['documento'] = pickle.dumps(D)
                            else:
                                 convertidos['documento'] = ''      
                
                            index = documentos.index(doc)
                            id_doc = int(form['documents_id'][index])
                            convertidos['vin_myvindula_config_documents_id'] = id_doc
                            convertidos["vin_myvindula_funcdetails_username"] = user
               
                            #edição .....
                            if ModelsUserDocuments().get_UserDocuments_by_user_and_doc(user,id_doc):
                                ModelsUserDocuments().del_UserDocuments(user,id_doc)
                                
                                #adicionando novo...
                                ModelsUserDocuments().set_UserDocuments(**convertidos)
                
                            else:
                                #adicionando...
                                ModelsUserDocuments().set_UserDocuments(**convertidos)
                
#                else:
#                    convertidos = {}
#                    doc = form['documento']
#                    data = doc.read()
#                    
#                    filename = doc.filename
#                    if len(data) != 0 :
#                        D ={}
#                        D['data'] = data
#                        D['filename'] = filename 
#                        convertidos['documento'] = pickle.dumps(D)
#                    else:
#                         convertidos['documento'] = ''      
#        
#                    id_doc = int(form['documents_id'])
#                    convertidos['vin_myvindula_config_documents_id'] = id_doc
#                    convertidos["vin_myvindula_funcdetails_username"] = user
#       
#                    #edição .....
#                    if ModelsUserDocuments().get_UserDocuments_by_user_and_doc(user,id_doc):
#                        ModelsUserDocuments().del_UserDocuments(user,id_doc)
#                        
#                        #adicionando novo...
#                        ModelsUserDocuments().set_UserDocuments(**convertidos)
#        
#                    else:
#                        #adicionando...
#                        ModelsUserDocuments().set_UserDocuments(**convertidos)
                    
                #Redirect back to the front page with a status message
                IStatusMessage(ctx.request).addStatusMessage(_(u"Documento Cadastrado com sucesso"), "info")
                ctx.request.response.redirect(success_url)
              
        # se o usuario não estiver logado
        else:
            return form_data    