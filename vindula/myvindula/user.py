from five import grok
from plone.directives import form

from zope import schema
from z3c.form import button
from plone.namedfile.field import NamedImage

from vindula.myvindula import MessageFactory as _

class IFuncDetails(form.Schema):
    
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
    data_nascimento = schema.TextLine(
    title=_(u"Data de Nascimento"),
    description=_(u"Digite a data de nascimneto do funcionario"),
    required=False,
    )
    empresa = schema.TextLine(
    title=_(u"Empresa"),
    description=_(u"Digite o nome da empresa do funcionario"),
    required=False,
    )                
    cargo = schema.TextLine(
    title=_(u"Cargo"),
    description=_(u"Digite o cargo do funcionario"),
    required=False,
    )    
    data_admissao = schema.TextLine(
    title=_(u"Data de Admissao"),
    description=_(u"Digite a data de admissao do funcionario"),
    required=False,
    )    
    centro_custo = schema.TextLine(
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
    username = schema.TextLine(
        title=_(u"Username"),
        description=_(u"Digite uma username do funcionario"),
        required=False,
        )
    departamentos_id = schema.Set(
        title=_(u"departamentos_id"),
        description=_(u"Selecione o departamento do funcionario"),
            value_type=schema.Choice(values=[_(u'Margherita'), _(u'Pepperoni'), _(u'Hawaiian')]),
        required=False,
    ) 
    
    
    
