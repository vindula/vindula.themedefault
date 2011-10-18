# coding: utf-8
from five import grok
from plone.directives import form

from zope import schema
from z3c.form import button
from plone.namedfile.field import NamedImage

from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone.dexterity.utils import createContentInContainer

from vindula.myvindula import MessageFactory as _

#Imports regarding the connection of the database 'strom'
from storm.locals import *
from zope.component import getUtility
from storm.zope.interfaces import IZStorm
from storm.locals import Store
from plone.i18n.normalizer.interfaces import IIDNormalizer
from Products.statusmessages.interfaces import IStatusMessage
from vindula.myvindula.validation import valida_form
from datetime import date

class IFuncDetails(form.Schema):
    
    @grok.provider(IContextSourceBinder)
    def choiceDepartament(context):
        terms = []
        departaments = ModelsDepartment().get_department()
        if departaments != []:
            for departament in departaments:
                terms.append(SimpleVocabulary.createTerm(departament.id, str(departament.name)))
                
        return SimpleVocabulary(terms)    
        

    name = schema.TextLine(
        title=_(u"name"),
        description=_(u"Digite o nome deste funcionario"),
        required=False,
    )
    phone_number = schema.TextLine(
        title=_(u"Telefone"),
        description=_(u"Digite o Telefone do funcionario"),
        required=False,
    )
    email = schema.TextLine(
        title=_(u"E mail"),
        description=_(u"Digite o E-mail do funcionario"),
        required=False,
    )
    employee_id = schema.TextLine(
        title=_(u"Employee ID"),
        description=_(u"Digite o ID do funcionario"),
        required=False,
    )
    date_birth = schema.Date(  #TextLine(
        title=_(u"Data de Nascimento"),
        description=_(u"Digite a data de nascimneto do funcionario"),
        required=False,
    )

    registration = schema.TextLine(
        title=_(u"Matricula"),
        description=_(u"Digite a data de nascimneto do funcionario"),
        required=False,
    )    
    
    enterprise = schema.TextLine(
        title=_(u"Empresa"),
        description=_(u"Digite o nome da empresa do funcionario"),
        required=False,
    )                
    position = schema.TextLine(
        title=_(u"Cargo"),
        description=_(u"Digite o cargo do funcionario"),
        required=False,
    )    
    admission_date = schema.Date( #TextLine(
        title=_(u"Data de Admissao"),
        description=_(u"Digite a data de admissao do funcionario"),
        required=False,
    )    
    cost_center = schema.TextLine(
        title=_(u"Centro de Custo"),
        description=_(u"Digite o centro de custo do funcionario"),
        required=False,
    )    
    job_role = schema.TextLine(
        title=_(u"Job Role"),
        description=_(u"Digite o 'Job Role' do funcionario"),
        required=False,
    )        
    organisational_unit = schema.TextLine(
        title=_(u"Organisational Unit"),
        description=_(u"Digite o 'Organisational Unit' do funcionario"),
        required=False,
    )
    reports_to = schema.TextLine(
        title=_(u"Reports to"),
        description=_(u"Digite o 'Reports to' do funcionario"),
        required=False,
    )    
    location = schema.TextLine(
        title=_(u"Localizacao"),
        description=_(u"Digite a localizacao do funcionario"),
        required=False,
    )    
    postal_address = schema.TextLine(
        title=_(u"Endereco Postal"),
        description=_(u"Digite o endereco do funcionario"),
        required=False,
    )    
    special_roles = schema.TextLine(
        title=_(u"Special Roles"),
        description=_(u"Digite o 'Special Roles' do funcionario"),
        required=False,
    )    
    photograph = NamedImage(
        title=_(u"Foto"),
        description=_(u"Coloque a foto do funcionario"),
        required=False,
    )    
    nickname = schema.TextLine(
        title=_(u"NickName"),
        description=_(u"Digite o 'nickname' do funcionario"),
        required=False,
    )        
    pronunciation_name = schema.TextLine(
        title=_(u"Como pronuncia seu nome"),
        description=_(u"Como pronuncia o  nome do funcionario"),
        required=False,
    )        
    committess = schema.TextLine(
        title=_(u"Commitess"),
        description=_(u"Digite o 'Commitess' do funcionario"),
        required=False,
    )        
    projetcs = schema.TextLine(
        title=_(u"Projetos"),
        description=_(u"Digite o Projeto do funcionario"),
        required=False,
    )        
    personal_information = schema.TextLine(
        title=_(u"Informacoes pessoais"),
        description=_(u"Digite as informaoes pessoais do funcionario"),
        required=False,
    )        
    skills_expertise = schema.TextLine(
        title=_(u"Skills Expertise"),
        description=_(u"Digite o 'Skills Expertise' do funcionario"),
        required=False,
    )        
    license_plate_numbers = schema.TextLine(
        title=_(u"License Plate Numbers"),
        description=_(u"Digite as 'License Plate Numbers' do funcionario"),
        required=False,
    )        
    profit_centre = schema.TextLine(
        title=_(u"Profit Centre"),
        description=_(u"Digite o 'Profit Centre' do funcionario"),
        required=False,
    )        
    languages = schema.TextLine(
        title=_(u"Languages"),
        description=_(u"Digite a 'Languages' do funcionario"),
        required=False,
    )        
    availability = schema.TextLine(
        title=_(u"Avaliacao"),
        description=_(u"Digite a avaliacao do funcionario"),
        required=False,
    )        
    papers_published = schema.TextLine(
        title=_(u"Artigo Publicados"),
        description=_(u"Digite os artigo puclicados do funcionario"),
        required=False,
    )        
    profit_centre = schema.TextLine(
        title=_(u"Profit Centre"),
        description=_(u"Digite o 'Profit Centre' do funcionario"),
        required=False,
    )        
    teaching_research = schema.TextLine(
        title=_(u"Teaching Research"),
        description=_(u"Digite o 'Teaching Research' do funcionario"),
        required=False,
    )
    delegations = schema.TextLine(
        title=_(u"Delegacao"),
        description=_(u"Digite a delegacao do funcionario"),
        required=False,
    ) 
    resume = schema.TextLine(
        title=_(u"Resumo"),
        description=_(u"Digite o resumo do funcionario"),
        required=False,
    )          
    blogs = schema.TextLine(
        title=_(u"Blogs"),
        description=_(u"Digite o blogs do funcionario"),
        required=False,
    )          
    customised_message = schema.TextLine(
        title=_(u"Menssagem Costumizada"),
        description=_(u"Digite uma menssagem do funcionario"),
        required=False,
    )          
    
#    username = schema.TextLine(
#        title=_(u"Username"),
#        description=_(u"Digite uma username do funcionario"),
#        required=False,
#        )

    Department_id = schema.Choice(
        title=_(u"departamentos_id"),
        description=_(u"Selecione o departamento do funcionario"),
        source=choiceDepartament,
        required=False,
    )

class BaseStore(object):
   
    def __init__(self, *args, **kwargs):
        self.store = getUtility(IZStorm).get('myvindula')
        
        #Lazy initialization of the object
        for attribute, value in kwargs.items():
            if not hasattr(self, attribute):
                
                raise TypeError('unexpected argument %s' % attribute)
            else:
                setattr(self, attribute, value)        
  
    
class ModelsFuncDetails(Storm, BaseStore):    
    __storm_table__ = 'FuncDetails'
    
    id = Int(primary=True)
    name = Unicode()
    phone_number = Unicode()
    email = Unicode()
    employee_id = Unicode()
    username = Unicode()
    date_birth = Date()
    registration = Unicode()
    enterprise = Unicode()
    position = Unicode()
    admission_date = Date()
    cost_center = Unicode()
    job_role = Unicode()
    organisational_unit = Unicode()
    reports_to = Unicode()
    location = Unicode()
    postal_address = Unicode()
    special_roles = Unicode()
    photograph = Unicode()
    nickname = Unicode()
    pronunciation_name = Unicode()
    committess = Unicode()
    projetcs = Unicode()
    personal_information = Unicode()
    skills_expertise = Unicode()
    license_plate_numbers = Unicode()
    profit_centre = Unicode()
    languages = Unicode()
    availability = Unicode()
    papers_published = Unicode()
    teaching_research =Unicode()
    delegations = Unicode()
    resume = Unicode()
    blogs = Unicode()
    customised_message = Unicode()
    Department_id = Int()  
  
    #departamento = ReferenceSet(id, "Departamentos.departamentos_id")    
    
    def get_allFuncDetails(self):
        data = self.store.find(ModelsFuncDetails)
        if data.count() == 0:
            return []
        else:
            return data
    
    def get_FuncDetails(self, user):
        data = self.store.find(ModelsFuncDetails, ModelsFuncDetails.username==user).one()
        if data:
            return data
        else:
            return []
        
class ModelsDepartment(Storm, BaseStore):
    __storm_table__ = 'Department'
 
    id = Int(primary=True)
    name = Unicode()
    description = Unicode()
    
    #loads data into the combo "departamento_id"    
    def get_department(self):
        data = self.store.find(ModelsDepartment)
        if data.count() == 0:
            return []
        else:
            return data

class ModelsConfgMyvindula(Storm, BaseStore):
    __storm_table__ = 'ConfMyvindula'
    
    id = Int(primary=True)
    name = Bool()
    phone_number = Bool()
    email = Bool()
    employee_id = Bool()
    username = Bool()
    date_birth = Bool()
    registration = Bool()
    enterprise = Bool()
    position = Bool()
    admission_date = Bool()
    cost_center = Bool()
    job_role = Bool()
    organisational_unit = Bool()
    reports_to = Bool()
    location = Bool()
    postal_address = Bool()
    special_roles = Bool()
    photograph = Bool()
    nickname = Bool()
    pronunciation_name = Bool()
    committess = Bool()
    projetcs = Bool()
    personal_information = Bool()
    skills_expertise = Bool()
    license_plate_numbers = Bool()
    profit_centre = Bool()
    languages = Bool()
    availability = Bool()
    papers_published = Bool()
    teaching_research =Bool()
    delegations = Bool()
    resume = Bool()
    blogs = Bool()
    customised_message = Bool()
    Department_id = Bool()  

    #loads data into DataBase    
    def get_configuration(self):
        data = self.store.find(ModelsConfgMyvindula).one()
        if data:
            return data
        else:
            return []

        
class BaseFunc(BaseStore):
    #default class for standard functions
        
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
        if config:
            try:
                return config.__getattribute__(campo)
            except:
                return True
        else:
            return True
    
    def getValue(self,campo,request,data):
        if campo in request.keys():
            if request.get(campo, None):
                return request.get(campo,'')
            else:
                return ''
        elif campo in data.keys():
            if data.get(campo, None):
                return data.get(campo,'')
            else:
                return ''
        else:
            return ''
    
    def getPhoto(self,campo,request,data):
        if campo in request.keys():
            if request.get(campo, None):
                return request.get(campo, '')
            else:
                return 'defaultUser.png'
        elif campo in data.keys():
            if data.get(campo, None):
                return data.get(campo,'')
            else:
                return 'defaultUser.png'
        else:
            return 'defaultUser.png'        
        
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
                if campo != 'Department_id' and campo != 'username':
                    tmp = ""
                    tmp += "<!-- Campo %s -->"%(campo)
                    tmp += "<div class='%s'>"%(self.field_class(errors, campo))
                    if self.checaEstado(config_myvindula,campo):
                        tmp += "   <label for='%s'>%s</label>"%(campo,campos[campo]['label'])
                        if campos[campo]['required'] == True:
                            tmp += "   <span class='fieldRequired' title='Obrigatório'>(Obrigatório)</span>"
    
                        tmp += "   <div class='formHelp'>%s.</div>"%(campos[campo]['decription'])   
                        tmp += "   <div >%s</div>"%(errors.get(campo,''))
                        
                        if campo == 'photograph':
                            if errors:
                                if data:
                                    tmp += "<img src='%s' style='width:100px;height:100px;' /><br />"%(self.getPhoto(campo,self.request,data))
                            else: 
                                 tmp += "<img src='%s' style='width:100px;height:100px;' /><br />"%(self.getPhoto(campo,self.request,data))
                            tmp += "<input id='photograph' type='file' value='' name='photograph' size='25' />"
                        elif campo == 'date_birth' or campo == 'admission_date':
                            tmp += "<input id='%s' type='text' value='%s' name='%s' size='25'/>"%(campo,self.converte_data(self.getValue(campo,self.request,data),True),campo)
                            
                        else:
                            tmp += "<input id='%s' type='text' value='%s' name='%s' size='25'/>"%(campo,self.getValue(campo,self.request,data),campo)
                    else:
                        if campo == 'date_birth' or campo == 'admission_date':
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
                    tmp += "<input id='%s' type='checkbox' value='%s' name='%s' size='25' %s/>"%(campo,'true',campo,self.checked(campo,self.request,data))
                    tmp += "</div>"    
                    html.append(tmp)
            
            return html
        
        
    def uploadFile(self, path, file):
        """ function used to upload the file to the Plone site, 
           with the parameter where the file will be saved and the file will be saved
        """
        normalizer = getUtility(IIDNormalizer)
        name_file = normalizer.normalize(file.filename)    #unicode(file.filename, 'utf-8')) #takes the name of the file
        count = 0
        while name_file in path.objectIds():
            name_file = name_file + '-' + str(count)
            count +=1
        
        #starts the upload process     
        else:
            try:
                #if image ...    
                if name_file.endswith('png') or \
                    name_file.endswith('jpg') or \
                        name_file.endswith('gif'):                
                    
                    objects = {'type_name':'Image',
                              'id': name_file,
                              'title':name_file,
                              'image': file}
                    path.invokeFactory(**objects)   
                    
                #if file ...
                else:
                    objects = {'type_name':'Image',
                              'id': name_file,
                              'title':name_file,
                              'image': file}
                    path.invokeFactory(**objects)   
                    
                #takes the url of the file to save the database  
                content = getattr(path, name_file, None)
                url = ''
                if content is not None:
                    url = content.absolute_url() 
                
                return unicode(url)
                
            except:
                return None
                
                
                
class SchemaFunc(BaseFunc):
    def to_utf8(value):
        return unicode(value, 'utf-8')

    campos = {'name'                  : {'required': False, 'type' : to_utf8, 'label':'Nome',                    'decription':u'Digite o Nome deste funcionaro'             }, #Campo Obrigatorio
              'phone_number'          : {'required': False, 'type' : to_utf8, 'label':'Telefone',                'decription':u'Digite o Telefone do funcionaro'            },
              'email'                 : {'required': False, 'type' : to_utf8, 'label':'Email',                   'decription':u'Digite o Email do funcionaro'               }, #Campo Obrigatorio
              'employee_id'           : {'required': False, 'type' : to_utf8, 'label':'ID Funcionario',          'decription':u'Digite o ID do funcionaro'                  },
              'date_birth'            : {'required': False, 'type' : date,    'label':'Data de Nacimento',       'decription':u'Digite a data de nascimneto do funcionaro'  }, #Campo Obrigatorio
              'registration'          : {'required': False, 'type' : to_utf8, 'label':'Matricula',               'decription':u'Digite a matricula do funcionaro'           },
              'enterprise'            : {'required': False, 'type' : to_utf8, 'label':'Empresa',                 'decription':u'Digite o nome da empresa do funcionaro'     },
              'position'              : {'required': False, 'type' : to_utf8, 'label':'Cargo',                   'decription':u'Digite o cargo do funcionaro'               },
              'admission_date'        : {'required': False, 'type' : date,    'label':'Data Admição',            'decription':u'Digite a data de admição do funcionaro'     },
              'cost_center'           : {'required': False, 'type' : to_utf8, 'label':'Centro de Custo',         'decription':u'Digite o centro de custo do funcionaro'     },
              'job_role'              : {'required': False, 'type' : to_utf8, 'label':'Job Role',                'decription':u'Digite o Job Role do funcionaro'            },
              'organisational_unit'   : {'required': False, 'type' : to_utf8, 'label':'Organisational Unit',     'decription':u'Digite a Organisational Unit do funcionaro' },
              'reports_to'            : {'required': False, 'type' : to_utf8, 'label':'Reporta-se a',            'decription':u'Digite a quem o funcionario se reporta'     },
              'location'              : {'required': False, 'type' : to_utf8, 'label':'Localização',             'decription':u'Digite a localização do funcionaro'         },
              'postal_address'        : {'required': False, 'type' : to_utf8, 'label':'Endereço Postal',         'decription':u'Digite o endereço do funcionaro'            },
              'special_roles'         : {'required': False, 'type' : to_utf8, 'label':'Special Roles',           'decription':u'Digite o Special Roles do funcionaro'       },
              'photograph'            : {'required': False, 'type' : 'file',  'label':'Foto',                    'decription':u'Coloque a foto do funcionaro'               },
              'nickname'              : {'required': False, 'type' : to_utf8, 'label':'NickName',                'decription':u'Digite o nickname do funcionaro'            },
              'pronunciation_name'    : {'required': False, 'type' : to_utf8, 'label':'Como pronuncia seu nome', 'decription':u'Como pronuncia o  nome do funcionaro'       },
              'committess'            : {'required': False, 'type' : to_utf8, 'label':'Commitess',             'decription':u'Digite o Commitess do funcionaro'             },
              'projetcs'              : {'required': False, 'type' : to_utf8, 'label':'Projetos',              'decription':u'Digite o Projetos do funcionaro'              },
              'personal_information'  : {'required': False, 'type' : to_utf8, 'label':'Informações pessoais',  'decription':u'Digite as informações pessoais do funcionaro' },
              'skills_expertise'      : {'required': False, 'type' : to_utf8, 'label':'Skills Expertise',      'decription':u'Digite o Skills Expertise do funcionaro'      },
              'license_plate_numbers' : {'required': False, 'type' : to_utf8, 'label':'License Plate Numbers', 'decription':u'Digite a License Plate Numbers do funcionaro' },
              'profit_centre'         : {'required': False, 'type' : to_utf8, 'label':'Profil Centre',         'decription':u'Digite o Profil Centre do funcionaro'         },
              'languages'             : {'required': False, 'type' : to_utf8, 'label':'Linguages',             'decription':u'Digite a lingua do funcionaro'                },
              'availability'          : {'required': False, 'type' : to_utf8, 'label':'Avaliação',             'decription':u'Digite a avaliação do funcionaro'             },
              'papers_published'      : {'required': False, 'type' : to_utf8, 'label':'Artigo Publicados',     'decription':u'Digite os artigo puclicados do funcionaro'    },
              'teaching_research'     : {'required': False, 'type' : to_utf8, 'label':'Teaching Research',     'decription':u'Digite o Teaching Research do funcionaro'     },
              'delegations'           : {'required': False, 'type' : to_utf8, 'label':'Delegação',             'decription':u'Digite a delegação do funcionaro'             },
              'resume'                : {'required': False, 'type' : to_utf8, 'label':'Resumo',                'decription':u'Digite um resumo do funcionaro'               },
              'blogs'                 : {'required': False, 'type' : to_utf8, 'label':'Blogs',                 'decription':u'Digite o Blog do funcionaro'                  },
              'customised_message'    : {'required': False, 'type' : to_utf8, 'label':'Menssagem Costumizada', 'decription':u'Digite uma menssagem do funcionaro'           },
              
              'username'              : {'required': False, 'type' : to_utf8,  'label':'Username'              }, #Campo Obrigatorio
              'Department_id'         : {'required': False, 'type' : int,     'label':'Departamento'           },} #Campo Obrigatorio
                    
    def registration_processes(self,context):
        success_url = context.context.absolute_url() + '/@@myvindula'
        access_denied = context.context.absolute_url() + '/@@myvindulaprefs'
        form = context.request # var tipo 'dict' que guarda todas as informacoes do formulario (keys,items,values)
        form_keys = form.keys() # var tipo 'list' que guarda todas as chaves do formulario (keys)
        campos = self.campos
        user = unicode(context.context.portal_membership.getAuthenticatedMember().id, 'utf-8')
        
        # divisao dos dicionarios "errors" e "convertidos"
        form_data = {
            'errors': {},
            'data': {},
            'campos':campos,
            'departametos': ModelsDepartment().get_department(),
            'username' : user,
            'config_myvindula':ModelsConfgMyvindula().get_configuration()}
        
        # se clicou no botao "Voltar"
        if 'form.voltar' in form_keys:
            context.request.response.redirect(success_url)
          
        # se clicou no botao "Salvar"
        elif 'form.submited' in form_keys:
            # Inicia o processamento do formulario
            # chama a funcao que valida os dados extraidos do formulario (valida_form) 
            errors, data = valida_form(campos, context.request.form)  

            if not errors:
                # Upload of Photograph
                if 'photograph' in form_keys:
                    if type(form['photograph']) == str:
                        data['photograph'] = to_utf8(form['photograph'])
                    else:
                        if form['photograph'].filename != '':
                            path = context.context.portal_membership.getHomeFolder()
                            file = data['photograph']
                            photo = BaseFunc().uploadFile(path,file)
                            if photo:
                                data['photograph'] = photo
                            else:
                                IStatusMessage(context.request).addStatusMessage(_(u'Error when trying to upload the file.'),"erro")
                                access_denied = context.context.absolute_url() + '/@@myvindulaprefs'
                                context.request.response.redirect(access_denied) 
                            
                        else:
                            data['photograph'] = None      
                
                if user != 'acl_users':
                    # editando...
                    result = self.store.find(ModelsFuncDetails, ModelsFuncDetails.username == user).one()

                    if result:
                        if data['photograph'] is None:
                            data['photograph'] = result.photograph
                        
                        #funcionario = result[0]
                        for campo in campos.keys():
                            value = data.get(campo, None)
                            setattr(result, campo, value)

                    else:
                        #adicionando...
                        database = ModelsFuncDetails(**data)
                        self.store.add(database)
                        self.store.flush()
                    
                #Redirect back to the front page with a status message
                IStatusMessage(context.request).addStatusMessage(_(u"Thank you for your order. We will contact you shortly"), "info")
                context.request.response.redirect(success_url)
                                   
            else:
                form_data['errors'] = errors
                form_data['data'] = data
                return form_data
          
        # se for um formulario de edicao 
        elif user != 'acl_users':    
            data = self.store.find(ModelsFuncDetails, ModelsFuncDetails.username == user).one()
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
            IStatusMessage(context.request).addStatusMessage(_(u'Error to saving the register.'),"erro")
            context.request.response.redirect(access_denied)
        
class SchemaConfgMyvindula(BaseFunc):
    
    campos={'name'                  : {'required': False, 'type' : bool, 'label':'Nome',                },
            'phone_number'          : {'required': False, 'type' : bool, 'label':'Telefone',            },
            'email'                 : {'required': False, 'type' : bool, 'label':'Email',               },
            'employee_id'           : {'required': False, 'type' : bool, 'label':'ID Funcionario',      },
            'date_birth'            : {'required': False, 'type' : bool, 'label':'Data de Nacimento',   },
            'registration'          : {'required': False, 'type' : bool, 'label':'Matricula',           },
            'enterprise'            : {'required': False, 'type' : bool, 'label':'Empresa',             },
            'position'              : {'required': False, 'type' : bool, 'label':'Cargo',               },
            'admission_date'        : {'required': False, 'type' : bool, 'label':'Data Admição',        },
            'cost_center'           : {'required': False, 'type' : bool, 'label':'Centro de Custo',     },
            'job_role'              : {'required': False, 'type' : bool, 'label':'Job Role',            },
            'organisational_unit'   : {'required': False, 'type' : bool, 'label':'Organisational Unit', },
            'reports_to'            : {'required': False, 'type' : bool, 'label':'Reporta-se a',        },
            'location'              : {'required': False, 'type' : bool, 'label':'Localização',         },
            'postal_address'        : {'required': False, 'type' : bool, 'label':'Endereço Postal',     },
            'special_roles'         : {'required': False, 'type' : bool, 'label':'Special Roles',       },
            'photograph'            : {'required': False, 'type' : bool, 'label':'Foto',                },
            'nickname'              : {'required': False, 'type' : bool, 'label':'NickName',            },
            'pronunciation_name'    : {'required': False, 'type' : bool, 'label':'Como pronuncia seu nome',},
            'committess'            : {'required': False, 'type' : bool, 'label':'Commitess',             },
            'projetcs'              : {'required': False, 'type' : bool, 'label':'Projetos',              },
            'personal_information'  : {'required': False, 'type' : bool, 'label':'Informações pessoais',  },
            'skills_expertise'      : {'required': False, 'type' : bool, 'label':'Skills Expertise',      },
            'license_plate_numbers' : {'required': False, 'type' : bool, 'label':'License Plate Numbers', },
            'profit_centre'         : {'required': False, 'type' : bool, 'label':'Profil Centre',         },
            'languages'             : {'required': False, 'type' : bool, 'label':'Linguages',             },
            'availability'          : {'required': False, 'type' : bool, 'label':'Avaliação',             },
            'papers_published'      : {'required': False, 'type' : bool, 'label':'Artigo Publicados',     },
            'teaching_research'     : {'required': False, 'type' : bool, 'label':'Teaching Research',     },
            'delegations'           : {'required': False, 'type' : bool, 'label':'Delegação',             },
            'resume'                : {'required': False, 'type' : bool, 'label':'Resumo',                },
            'blogs'                 : {'required': False, 'type' : bool, 'label':'Blogs',                 },
            'customised_message'    : {'required': False, 'type' : bool, 'label':'Menssagem Costumizada', },

            'Department_id'         : {'required': False, 'type' : bool,  'label':'Departamento',         },}         
    
    
    def configuration_processes(self,context):
        success_url = context.context.absolute_url() + '/@@overview-controlpanel'
        access_denied = context.context.absolute_url() + '/@@myvindulaconfgs'
        form = context.request # var tipo 'dict' que guarda todas as informacoes do formulario (keys,items,values)
        form_keys = form.keys() # var tipo 'list' que guarda todas as chaves do formulario (keys)
        campos = self.campos
        config = ModelsConfgMyvindula().get_configuration()
       
        # divisao dos dicionarios "errors" e "convertidos"
        form_data = {
            'errors': {},
            'data': {},
            'campos':campos,}
        
        # se clicou no botao "Voltar"
        if 'form.voltar' in form_keys:
            context.request.response.redirect(success_url)
        
        # se clicou no botao "Salvar"
        elif 'form.submited' in form_keys:
              # Inicia o processamento do formulario
              # chama a funcao que valida os dados extraidos do formulario (valida_form) 
              errors, data = valida_form(campos, context.request.form)  
              
              if not errors:
                  if config:
                      for campo in campos.keys():
                          value = data.get(campo, None)
                          setattr(config, campo, value)

                  else:
                      # adicionando...
                      configuration = ModelsConfgMyvindula(**data)
                      self.store.add(configuration)
                      self.store.flush()
                  
                  
                  context.request.response.redirect(success_url)        
                       
              else:
                  form_data['errors'] = errors
                  form_data['data'] = data
                  return form_data
          
        # se for um formulario de edicao
        elif config:    
            D = {}
            for campo in campos.keys():
                D[campo] = getattr(config, campo, '')
            
            form_data['data'] = D
            return form_data
              
        # se for um formulario de adicao
        else:
            return form_data
