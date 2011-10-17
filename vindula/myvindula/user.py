from five import grok
from plone.directives import form

from zope import schema
from z3c.form import button
from plone.namedfile.field import NamedImage

from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from vindula.myvindula import MessageFactory as _

#Imports regarding the connection of the database 'strom'
from storm.locals import *
from zope.component import getUtility
from storm.zope.interfaces import IZStorm
from storm.locals import Store





class BaseStore(object):
   
    def __init__(self, *args, **kwargs):
        self.store = getUtility(IZStorm).get('myvindula')
        
        #Lazy initialization of the object
        for attribute, value in kwargs.items():
            if not hasattr(self, attribute):
                
                raise TypeError('unexpected argument %s' % attribute)
            else:
                setattr(self, attribute, value)        


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
    
    
    

    )
    
    
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

