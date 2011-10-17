# coding: utf-8

from zope.component import getUtility
import urllib
from datetime import date
from storm.zope.interfaces import IZStorm
from plone.i18n.normalizer.interfaces import IIDNormalizer
from Products.Five import BrowserView


class BaseView(BrowserView):
    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.store = getUtility(IZStorm).get('myvindula')
        
    # define se aparece ou nao as mensagens e marcacoes de erros  
    def field_class(self, errors, field_name):
        if errors is not None:
            if errors.get(field_name, None) is not None:
                return 'field error'                   
            else:
                 return 'field'
        else:
              return 'field'
          
    def checaEstado(self,config, campo):
        if 'form.new' in self.request.form.keys():
            return True
        else:
            try:
                return config.__getattribute__(campo)
            except:
                return False
                
#def checaEstado(self,config, campo):
#       if 'id' in self.request.form.keys() and config != []:
#           try:
#               return config.__getattribute__(campo)
#           except:
#               return False
#       else:
#           return True
       
       
       
    def getValue(self,campo,request,data):
        if campo in request.keys():
            return request.get(campo, '')
        elif campo in data.keys():
            return data.get(campo,'')
        else:
            return ''
        
    def checked(self,campo,request,data):
        if campo in request.keys():
            if request.get(campo, '') == True:
                return "checked"
            else:
                return ""
        elif campo in data.keys():
            if data.get(campo,'') == True:
                return "checked"
            else:
                return ""
        else:
            return ""    
        
        
        
    # retorna dado convertido para o campos de data 
    def converte_data(self, data, data_atual=False):
        if data is not None and data != '':
            if type(data) == date:
                return data.strftime('%d/%m/%Y')
            else:
                return ''
        else:
            if data_atual == True:
                data = date.today()
                dia = data.day
                mes = data.month
                ano = data.year
        
                if dia < 10:
                    dia = '0' + str(dia)
                else:
                    dia = str(dia)
                    
                if mes < 10:
                    mes = '0' + str(mes)
                else:
                    mes = str(mes)
                    
                datastr = dia + '/' + mes + '/' + str(ano)
        
                return datastr  
            else:
                return ''        

    def geraCampos(self,form_data):
        html = []
        if form_data:
            errors = form_data.get('errors',None)
            data = form_data.get('data',None)
            campos = form_data.get('campos',None)
            config_myvindula = form_data.get('config_myvindula',None)
            for campo in campos.keys():
                if campo != 'departamentos_id' and campo != 'username':
                    tmp = ""
                    tmp += "<!-- Campo %s -->"%(campo)
                    tmp += "<div class='%s'>"%(self.field_class(errors, campo))
                    if config_myvindula.__getattribute__(campo) or 'form.new' in self.request.form.keys():
                        tmp += "   <label for='%s'>%s</label>"%(campo,campos[campo]['label'])
                        if campos[campo]['required'] == True:
                            tmp += "   <span class='fieldRequired' title='Obrigatório'>(Obrigatório)</span>"
    
                        tmp += "   <div class='formHelp'>%s.</div>"%(campos[campo]['decription'])   
                        tmp += "   <div >%s</div>"%(errors.get(campo,''))
                        
                        if campo == 'photograph':
                            if errors:
                                if data:
                                    tmp += "<img src='%s' style='width:100px;height:100px;' /><br />"%(data.get('photograph',))
                            else: 
                                 tmp += "<img src='%s' style='width:100px;height:100px;' /><br />"%(data.get('photograph',))
                            tmp += "<input id='photograph' type='file' value='' name='photograph' size='25'"
                        elif campo == 'data_nascimento' or campo == 'data_admissao':
                            tmp += "<input id='%s' type='text' value='%s' name='%s' size='25'/>"%(campo,self.converte_data(self.getValue(campo,self.request,data),True),campo)
                            
                        else:
                            tmp += "<input id='%s' type='text' value='%s' name='%s' size='25'/>"%(campo,self.getValue(campo,self.request,data),campo)
                    else:
                        if campo == 'data_nascimento' or campo == 'data_admissao':
                            tmp += "<input id='%s' type='hidden' value='%s' name='%s' size='25'/>"%(campo,self.converte_data(self.getValue(campo,self.request,data),True),campo)
                        else:
                            tmp += "<input id='%s' type='hidden' value='%s' name='%s' size='25'/>"%(campo,self.getValue(campo,self.request,data),campo)
                        
                    tmp += "</div>"    
                    html.append(tmp)
            
            return html

    def geraConfCampos(self,form_data):
        html = []
        if form_data:
            errors = form_data.get('errors',None)
            data = form_data.get('data',None)
            campos = form_data.get('campos',None)
            for campo in campos.keys():
                if campo != 'id':
                    tmp = ""
                    tmp += "<!-- Campo %s -->"%(campo)
                    tmp += "<div class='%s'>"%(self.field_class(errors, campo))
                    tmp += "   <label for='%s'>%s</label>"%(campo,campos[campo]['label'])
                    tmp += "   <div class='formHelp'>Abilita a edição deste campo pelo funcionario.</div>"   
                    tmp += "   <div >%s</div>"%(errors.get(campo,''))
                    tmp += "<input id='%s' type='checkbox' value='%s' name='%s' size='25' %s/>"%(campo,self.getValue(campo,self.request,data),campo,self.checked(campo,self.request,data))
                    tmp += "</div>"    
                    html.append(tmp)
            
            return html
        
        
    def salva_arquivo(self, arquivo):
        # verifica se tem anexo
        #portal = self.context.portal_url.getPortalObject() # pega a pasta raiz do plone site
        pasta = self.context.portal_membership.getHomeFolder() # pega o caminho da pasta do usuario
        #arquivo = self.request.get('anexo') # pega o arquivo do form
        nome = arquivo.filename # pega o nome do arquivo
        
        normalizer = getUtility(IIDNormalizer)
        nome_arquivo = normalizer.normalize(unicode(nome, 'utf-8'))
        
        count = 0
        while nome_arquivo in pasta.objectIds():
            nome_arquivo = nome_arquivo + '-' + str(count)
            count +=1
        
        # inicia o processo de upload    
        else:
            try:
                # se for imagem...      
                if nome_arquivo.endswith('png') or \
                    nome_arquivo.endswith('jpg') or \
                        nome_arquivo.endswith('gif'):                
                             
                    objeto = {'type_name':'Image',
                              'id': nome_arquivo,
                              'title':nome_arquivo,
                              'image': arquivo}
                    pasta.invokeFactory(**objeto)   
                    
                # se for arquivo...
                else:
                    objeto = {'type_name':'File',
                              'id': nome_arquivo,
                              'title':nome_arquivo,
                              'file': arquivo}
                    pasta.invokeFactory(**objeto)   
                # pega a url do arquivo para salvar no banco 
                content = getattr(pasta, nome_arquivo, None)
                url = ''
                if content is not None:
                    url = content.absolute_url() 
                
                return unicode(url)
                p_utils.addPortalMessage('Upload de arquivo realizado com sucesso.', 'info')  
            except:
                p_utils.addPortalMessage('Erro ao tentar efetuar o upload do arquivo.', 'erro')   
                acesso_negado = self.context.absolute_url() + '/portal_skins/plone_login/require_login'
                self.request.response.redirect(acesso_negado)

