# coding: utf-8
from five import grok
from plone.directives import form

from zope import schema
from z3c.form import button
from plone import namedfile

from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone.dexterity.utils import createContentInContainer

from zope.app.component.hooks import getSite
from Products.CMFCore.utils import getToolByName
from plone.scale.storage import IImageScaleStorage

from vindula.myvindula import MessageFactory as _

#Imports regarding the connection of the database 'strom'
from storm.locals import *
from zope.component import getUtility
from storm.zope.interfaces import IZStorm
from storm.locals import Store
from plone.i18n.normalizer.interfaces import IIDNormalizer
from Products.statusmessages.interfaces import IStatusMessage
from vindula.myvindula.validation import valida_form
from datetime import date , datetime 


#import sys
#from storm.tracer import debug #debug(True, stream=sys.stdout)

class BaseStore(object):
   
    def __init__(self, *args, **kwargs):
        self.store = getUtility(IZStorm).get('myvindula')
        
        #Lazy initialization of the object
        for attribute, value in kwargs.items():
            if not hasattr(self, attribute):
                raise TypeError('unexpected argument %s' % attribute)
            else:
                setattr(self, attribute, value)        
  
        # divide o dicionario 'convertidos'
        for key in kwargs:
            setattr(self,key,kwargs[key])
        # adiciona a data atual
        self.date_creation = datetime.now()    
  
    
class ModelsFuncDetails(Storm, BaseStore):    
    __storm_table__ = 'vin_myvindula_funcdetails'
    
    id = Int(primary=True)
    name = Unicode()
    phone_number = Unicode()
    cell_phone = Unicode()
    email = Unicode()
    employee_id = Unicode()
    username = Unicode()
    date_birth = Date()
    registration = Unicode()
    enterprise = Unicode()
    position = Unicode()
    admission_date = Date()
    cost_center = Unicode()
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
    #skills_expertise = Unicode()
    profit_centre = Unicode()
    #languages = Unicode()
    availability = Unicode()
    papers_published = Unicode()
    teaching_research =Unicode()
    delegations = Unicode()
    resume = Unicode()
    blogs = Unicode()
    customised_message = Unicode()
    #vin_myvindula_department_id = Int()
    
    departamento = Reference(username, "ModelsDepartment.vin_myvindula_funcdetails_id")
    
    def set_FuncDetails(self, **kwargs):
        # adicionando...
        funcDetails = ModelsFuncDetails(**kwargs)
        self.store.add(funcDetails)
        self.store.flush()        
    
    def get_allFuncDetails(self):
        data = self.store.find(ModelsFuncDetails, ModelsFuncDetails.username!=u'admin').order_by(ModelsFuncDetails.name)
        if data.count() == 0:
            return None
        else:
            return data
    
    def get_FuncDetails(self, user):
        data = self.store.find(ModelsFuncDetails, ModelsFuncDetails.username==user).one()
        if data:
            return data
        else:
            return None
        
    def get_FuncBusca(self,name,department_id,phone):
        if department_id == u'0' and name == '' and phone == '':
            data = self.store.find(ModelsFuncDetails).order_by(ModelsFuncDetails.name)
         
        elif department_id != u'0':
            origin = [ModelsFuncDetails, Join(ModelsDepartment, ModelsDepartment.vin_myvindula_funcdetails_id==ModelsFuncDetails.username)]
            data = self.store.using(*origin).find(ModelsFuncDetails,  ModelsFuncDetails.name.like("%" + name + "%"),
                                                                   ModelsFuncDetails.phone_number.like("%" + phone + "%"),
                                                                   ModelsDepartment.uid_plone==department_id).order_by(ModelsFuncDetails.name)
        elif department_id == u'0' and name != '':
            data = self.store.find(ModelsFuncDetails, ModelsFuncDetails.name.like("%" + name + "%")).order_by(ModelsFuncDetails.name)
            

        else:
            data = self.store.find(ModelsFuncDetails, ModelsFuncDetails.name.like("%" + name + "%"),
                                                      ModelsFuncDetails.phone_number.like("%" + phone + "%")).order_by(ModelsFuncDetails.name)
        
        if data.count() == 0:
            return None
        else:
            return data    

    def get_FuncBusca_Portlet(self,name,phone):
        if name == '' and phone == '':
            data = self.store.find(ModelsFuncDetails).order_by(ModelsFuncDetails.name)

        elif name != '':
            data = self.store.find(ModelsFuncDetails, ModelsFuncDetails.name.like("%" + name + "%")).order_by(ModelsFuncDetails.name)

        else:
            data = self.store.find(ModelsFuncDetails, ModelsFuncDetails.name.like("%" + name + "%"),
                                                      ModelsFuncDetails.phone_number.like("%" + phone + "%")).order_by(ModelsFuncDetails.name)
        
        if data.count() == 0:
            return None
        else:
            return data    
            
    
    def get_FuncBirthdays(self, date_start, date_end):
        data = self.store.execute('SELECT * FROM vin_myvindula_funcdetails WHERE DATE_FORMAT(date_birth, "%m-%d") BETWEEN DATE_FORMAT("'+date_start+'", "%m-%d") AND DATE_FORMAT("'+date_end+'", "%m-%d") ORDER BY MONTH(date_birth) ASC, DAY(date_birth) ASC;')

        if data.rowcount != 0:
            result=[]
            for obj in data.get_all():
                D={}
                i = 0
                columns = self.store.execute('SHOW COLUMNS FROM vin_myvindula_funcdetails;')
                for column in columns.get_all():
                    if str(column[0]) == 'date_birth':
                        D[str(column[0])] = obj[i].strftime('%d/%m')
                    else:
                        D[str(column[0])] = obj[i]
                    i+=1
            
                result.append(D)       
            
            return result
        else:
            return None
          
    def get_FuncUpcomingBirthdays(self):
        data = self.store.execute("SELECT * FROM vin_myvindula_funcdetails WHERE concat_ws('-',year(now()),month(date_birth),day(date_birth)) >= NOW() ORDER BY MONTH(date_birth) ASC , DAY(date_birth) ASC;")
        
        if data.rowcount != 0:
            result=[]
            for obj in data.get_all():
                D={}
                i = 0
                columns = self.store.execute('SHOW COLUMNS FROM vin_myvindula_funcdetails;')
                for column in columns.get_all():
                    if str(column[0]) == 'date_birth':
                        D[str(column[0])] = obj[i].strftime('%d/%m')
                    else:
                        D[str(column[0])] = obj[i]
                    i+=1
            
                result.append(D)       
            
            return result
        else:
            return None

         
class ModelsDepartment(Storm, BaseStore):
    __storm_table__ = 'vin_myvindula_department'
 
    __storm_primary__ = "uid_plone", "vin_myvindula_funcdetails_id"
    
    #id = Int(primary=True)
    uid_plone = Unicode()
    vin_myvindula_funcdetails_id = Unicode()

    def set_department(self, **kwargs):
        D={}
        D['uid_plone'] = kwargs.get('UID','')
        D['vin_myvindula_funcdetails_id'] = kwargs.get('funcdetails_id')
        
        # adicionando...
        department = ModelsDepartment(**D)
        self.store.add(department)
        self.store.flush()        
    
    #loads data into the combo "departamento_id"    
    def get_department(self):
        urltool = getSite().portal_url
        caminho = urltool.getPortalPath() #+'/jornal-da-caixa/banners-do-jornal';
        ctool = getSite().portal_catalog
        data = ctool(portal_type='OrganizationalStructure', 
                      review_state='published',
                      path=caminho)   
        
        #data = self.store.find(ModelsDepartment)
        if data: 
            return data
        else:
            return []
        
    def get_departmentByUsername(self,user):
        catalog = getToolByName(getSite(), 'portal_catalog')
        datas = self.store.find(ModelsDepartment, ModelsDepartment.vin_myvindula_funcdetails_id==user)
        if datas.count() != 0:
            L=[]
            for data in datas:
                obj = catalog({'UID':data.uid_plone})
                if obj:
                    L.append(obj[0])
            if L:
                return L
            else:
                return []
        else:
            return []

#    def get_departmentByID(self,id):
#        data = self.store.find(ModelsDepartment, ModelsDepartment.id==int(id)).one()
#        if data:
#            return data
#        else:
#            return None
        
    def del_department(self, user):
        results = self.store.find(ModelsDepartment, ModelsDepartment.vin_myvindula_funcdetails_id==user)
        if results:
            for result in results:
                self.store.remove(result)
                self.store.flush()


class ModelsFuncHolerite(Storm, BaseStore):
    __storm_table__ = 'vin_myvindula_holerite'
    
    id = Int(primary=True)
    nome = Unicode()
    matricula = Unicode() 
    cargo= Unicode()
    cod_cargo = Unicode()
    date_creation = DateTime()
    competencia = Unicode()
    empresa = Unicode()
    cod_empresa = Unicode()
    endereco_empresa = Unicode()
    cidade_empresa = Unicode()
    estado_empresa = Unicode()
    cnpj_empresa = Unicode()
    total_vencimento = Unicode()
    total_desconto = Unicode()
    valor_liquido = Unicode()
    salario_base = Unicode()
    base_Inss = Unicode()
    base_fgts = Unicode()
    fgts_mes = Unicode()
    base_irrf = Unicode()
    
    descricao = Reference(id, "ModelsFuncHoleriteDescricao.vin_myvindula_holerite_id")
    
    def set_FuncHolerite(self, **kwargs):
        # adicionando...
        funcHolerite = ModelsFuncHolerite(**kwargs)
        self.store.add(funcHolerite)
        self.store.flush()
        
        return funcHolerite.id       
    
    def get_FuncHolerites_byMatricula(self, matricula):
        data = self.store.find(ModelsFuncHolerite, ModelsFuncHolerite.matricula==matricula).order_by(ModelsFuncHolerite.competencia)
        if data.count() > 0:
            return data
        else:
            return None    
    
    def get_FuncHolerites_byMatriculaAndCompetencia(self, matricula, competencia):
        data = self.store.find(ModelsFuncHolerite, ModelsFuncHolerite.matricula==matricula, ModelsFuncHolerite.competencia==competencia).one()
        if data:
            return data
        else:
            return None    

    def get_FuncHolerites_byData(self, data):
        data = self.store.find(ModelsFuncHolerite, ModelsFuncHolerite.date_creation==data)
        if data.count() > 1:
            return data
        else:
            return None        
    
    def get_FuncHolerites_Import(self):
        data = self.store.find(ModelsFuncHolerite)
        if data.count() > 0:
            return data.group_by(ModelsFuncHolerite.date_creation)
        else:
            return None    

    def del_HoleritesLote(self, date):
        results = self.store.find(ModelsFuncHolerite, ModelsFuncHolerite.date_creation==date)
        if results:
            for result in results:
                ModelsFuncHoleriteDescricao().del_HoleritesDescricao(result.id)
                self.store.remove(result)
                self.store.flush()        
    
    
    
class ModelsFuncHoleriteDescricao(Storm, BaseStore):
    __storm_table__ = 'vin_myvindula_descricao_holerite'
    
    id = Int(primary=True)    
    codigo = Unicode()
    descricao = Unicode()
    ref = Unicode()
    vencimentos = Unicode()
    descontos = Unicode()
    vin_myvindula_holerite_id = Int()
    
    def set_FuncHoleriteDescricao(self, **kwargs):
        # adicionando...
        funcHoleriteDescricao = ModelsFuncHoleriteDescricao(**kwargs)
        self.store.add(funcHoleriteDescricao)
        self.store.flush()          
    
    def get_FuncHoleriteDescricoes_byid(self, id):
        data = self.store.find(ModelsFuncHoleriteDescricao, ModelsFuncHoleriteDescricao.vin_myvindula_holerite_id==id)
        if data.count() > 0:
            return data
        else:
            return None        
    
    def del_HoleritesDescricao(self, holerite_id):
        results = self.store.find(ModelsFuncHoleriteDescricao, ModelsFuncHoleriteDescricao.vin_myvindula_holerite_id==holerite_id)
        if results:
            for result in results:
                self.store.remove(result)
                self.store.flush()
        

class ModelsConfgMyvindula(Storm, BaseStore):
    __storm_table__ = 'vin_myvindula_confgfuncdetails'
    
    id = Int(primary=True)
    name = Bool()
    phone_number = Bool()
    cell_phone = Bool()
    email = Bool()
    employee_id = Bool()
    #username = Bool()
    date_birth = Bool()
    registration = Bool()
    enterprise = Bool()
    position = Bool()
    admission_date = Bool()
    cost_center = Bool()
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
    profit_centre = Bool()
    languages = Bool()
    availability = Bool()
    papers_published = Bool()
    teaching_research =Bool()
    delegations = Bool()
    resume = Bool()
    blogs = Bool()
    customised_message = Bool()
    vin_myvindula_department = Bool()  

    #loads data into DataBase    
    def get_configuration(self):
        data = self.store.find(ModelsConfgMyvindula).one()
        if data:
            return data
        else:
            return None
    
    def set_configuration(self,**kwargs):
        # adicionando...
        config = ModelsConfgMyvindula(**kwargs)
        self.store.add(config)
        self.store.flush()                

    
class ModelsMyvindulaHowareu(Storm, BaseStore):
    __storm_table__ = 'vin_myvindula_howareu'
    
    _name_class = "ModelsMyvindulaHowareu" 
    
    id = Int(primary=True)
    username = Unicode()
    date_creation = DateTime()
    visible_area = Unicode()
    text = Unicode()
        
    def set_myvindula_howareu(self,**kwargs):
        D={}
        D['username'] = unicode(kwargs.get('username',''), 'utf-8')
        D['visible_area'] = unicode(kwargs.get('visible_area',''), 'utf-8')
        D['text'] = unicode(kwargs.get('text',''), 'utf-8')
        
        # adicionando...
        howareu = ModelsMyvindulaHowareu(**D)
        self.store.add(howareu)
        self.store.flush()
    
    def get_myvindula_howareu(self,**kwargs):
        if kwargs.get('username',None):
            user = kwargs.get('username','')
            if type(user) != unicode:
                user = unicode(kwargs.get('username',''), 'utf-8')
            data = self.store.find(ModelsMyvindulaHowareu, ModelsMyvindulaHowareu.username==user).order_by(Desc(ModelsMyvindulaHowareu.date_creation))
        
        elif kwargs.get('visible_area',None):
            visible_area = kwargs.get('visible_area','')
            if type(visible_area) != unicode:
                visible_area = unicode(kwargs.get('visible_area',''), 'utf-8')
            data = self.store.find(ModelsMyvindulaHowareu, ModelsMyvindulaHowareu.visible_area==visible_area)
        
        if data.count() > 0:
            return data
        else:
            return None    
        
class ModelsMyvindulaRecados(Storm, BaseStore):
    __storm_table__ = 'vin_myvindula_recados'
    
    _name_class = "ModelsMyvindulaRecados" 
    
    id = Int(primary=True)
    username = Unicode()
    date_creation = DateTime()
    destination = Unicode()
    text = Unicode()
        
    def set_myvindula_recados(self,**kwargs):
        D={}
        D['username'] = unicode(kwargs.get('username',''), 'utf-8')
        D['destination'] = unicode(kwargs.get('destination',''), 'utf-8')
        D['text'] = unicode(kwargs.get('text',''), 'utf-8')
        
        # adicionando...
        recados = ModelsMyvindulaRecados(**D)
        self.store.add(recados)
        self.store.flush()
    
    def get_myvindula_recados(self,**kwargs):
        if kwargs.get('destination',None):
            user = kwargs.get('destination','')
            if type(user) != unicode:
                user = unicode(kwargs.get('destination',''), 'utf-8')
            data = self.store.find(ModelsMyvindulaRecados, ModelsMyvindulaRecados.destination==user).order_by(Desc(ModelsMyvindulaRecados.date_creation))
        
            if data.count() > 0:
                return data
            else:
                return None
        else:
            return None            
                                  

class ModelsMyvindulaComments(Storm, BaseStore):
    __storm_table__ = 'vin_myvindula_comments'
    
    _name_class = "ModelsMyvindulaComments"     
    
    id = Int(primary=True)
    username = Unicode()
    date_creation = DateTime()
    type = Unicode()
    id_obj = Unicode()
    isPlone = Bool()
    text = Unicode()
    
    def set_myvindula_comments(self,**kwargs):
        D={}
        D['username'] = unicode(kwargs.get('username',''), 'utf-8')
        D['type'] = unicode(kwargs.get('type',''), 'utf-8')
        D['id_obj'] = unicode(kwargs.get('id_obj',''), 'utf-8')
        D['isPlone'] = kwargs.get('isPlone',False)
        D['text'] = unicode(kwargs.get('text',''), 'utf-8')
        
        # adicionando...
        comments = ModelsMyvindulaComments(**D)
        self.store.add(comments)
        self.store.flush()        

    def get_myvindula_comments(self,**kwargs):
        id_obj = kwargs.get('id_obj','')
        type_obj = kwargs.get('type','')
        if type(id_obj) != unicode:
            id_obj = unicode(id_obj)
        if type(type_obj) != unicode:
            type_obj = unicode(type_obj)
        data = self.store.find(ModelsMyvindulaComments, ModelsMyvindulaComments.id_obj==id_obj,ModelsMyvindulaComments.type==type_obj)

        if data.count > 0:
            return data
        else:
            return None   

class ModelsMyvindulaLike(Storm, BaseStore):
    __storm_table__ = 'vin_myvindula_like'
    
    id = Int(primary=True)
    username = Unicode()
    date_creation = DateTime()
    type = Unicode()
    id_obj = Unicode()
    isPlone = Bool()
     
    def set_myvindula_like(self,**kwargs):
        D={}
        D['username'] = unicode(kwargs.get('username',''), 'utf-8')
        D['type'] = unicode(kwargs.get('type',''), 'utf-8')
        D['id_obj'] = unicode(kwargs.get('id_obj',''), 'utf-8')
        D['isPlone'] = eval(kwargs.get('isPlone','False'))
        
        # adicionando...
        comments = ModelsMyvindulaLike(**D)
        self.store.add(comments)
        self.store.flush()        

    def get_myvindula_like(self,**kwargs):
        id_obj = kwargs.get('id_obj','')
        type_obj = kwargs.get('type','')
        if type(id_obj) != unicode:
            id_obj = unicode(id_obj)
        if type(type_obj) != unicode:
            type_obj = unicode(type_obj)
        data = self.store.find(ModelsMyvindulaLike, ModelsMyvindulaLike.id_obj==id_obj,ModelsMyvindulaLike.type==type_obj)

        if data.count > 0:
            return data
        else:
            return None   

    def del_myvindula_like(self, **kwargs):
        id_obj = kwargs.get('id_obj','')
        username = kwargs.get('username','')
        type_obj = kwargs.get('type','')
        
        if type(id_obj) != unicode:
            id_obj = unicode(id_obj)
        if type(username) != unicode:
            username = unicode(username)
        if type(type_obj) != unicode:
            type_obj = unicode(type_obj)
        
        record = self.store.find(ModelsMyvindulaLike, ModelsMyvindulaLike.id_obj==id_obj,
                                                      ModelsMyvindulaLike.type==type_obj,
                                                      ModelsMyvindulaLike.username==username).one()
        self.store.remove(record)
        self.store.flush()


class ModelsMyvindulaCourses(Storm, BaseStore):
    __storm_table__ = 'vin_myvindula_courses'
    
    id = Int(primary=True)
    title = Unicode()
    length = Unicode()
    
    def get_allCourses(self):
        data = self.store.find(ModelsMyvindulaCourses)
        if data:
            return data
        else:
            return None
    
    def set_courses(self,**kwargs):
        # adicionando...
        couses = ModelsMyvindulaCourses(**kwargs)
        self.store.add(couses)
        self.store.flush() 
        
    def get_courses_byID(self,id):
        data = self.store.find(ModelsMyvindulaCourses, ModelsMyvindulaCourses.id==id).one()
        if data:
            return data
        else:
            return None
        
        
class ModelsMyvindulaLanguages(Storm, BaseStore):
    __storm_table__ = 'vin_myvindula_languages'
    
    id = Int(primary=True)
    title = Unicode()
    level = Unicode()
    
    def get_allLanguages(self):
        data = self.store.find(ModelsMyvindulaLanguages)
        if data:
            return data
        else:
            return None

    def set_languages(self,**kwargs):
        # adicionando...
        languages = ModelsMyvindulaLanguages(**kwargs)
        self.store.add(languages)
        self.store.flush()         

    def get_languages_byID(self,id):
        data = self.store.find(ModelsMyvindulaLanguages, ModelsMyvindulaLanguages.id==id).one()
        if data:
            return data
        else:
            return None        

class ModelsMyvindulaFuncdetailCouses(Storm, BaseStore):
    __storm_table__ = 'vin_myvindula_funcdetail_couses'
    __storm_primary__ = "vin_myvindula_funcdetail_username", "vin_myvindula_courses_id"
    
    #id = Int(primary=True)
    vin_myvindula_funcdetail_username = Unicode()
    vin_myvindula_courses_id = Int()
    
    def get_funcdetailCouserByUsername(self, user):
        data = self.store.find(ModelsMyvindulaFuncdetailCouses, ModelsMyvindulaFuncdetailCouses.vin_myvindula_funcdetail_username==user)
        
        if data:
            return data
        else:
            return None
    
    def set_funcdetailCouser(self,**kwargs):
        D={}
        D['vin_myvindula_funcdetail_username']= kwargs.get('username','')
        D['vin_myvindula_courses_id'] = int(kwargs.get('id_courses',''))
    
        # adicionando...
        funcdetailCouser = ModelsMyvindulaFuncdetailCouses(**D)
        self.store.add(funcdetailCouser)
        self.store.flush()   
        
    
    def del_funcdetailCouser(self, user):
        results = self.store.find(ModelsMyvindulaFuncdetailCouses, ModelsMyvindulaFuncdetailCouses.vin_myvindula_funcdetail_username==user)
        if results:
            for result in results:
                self.store.remove(result)
                self.store.flush()        


class ModelsMyvindulaFuncdetailLanguages(Storm, BaseStore):
    __storm_table__ = 'vin_myvindula_funcdetail_languages'
    __storm_primary__ = "vin_myvindula_funcdetail_username", "vin_myvindula_languages_id"

    #id = Int(primary=True)
    vin_myvindula_funcdetail_username = Unicode(primary=True)
    vin_myvindula_languages_id = Int()
    
    def get_funcdetailLanguagesByUsername(self, user):
        data = self.store.find(ModelsMyvindulaFuncdetailLanguages, ModelsMyvindulaFuncdetailLanguages.vin_myvindula_funcdetail_username==user)
        
        if data:
            return data
        else:
            return None
    
    
    def set_funcdetailLanguages(self,**kwargs):
        D={}
        D['vin_myvindula_funcdetail_username']= kwargs.get('username','')
        D['vin_myvindula_languages_id'] = int(kwargs.get('id_courses',''))
    
        # adicionando...
        funcdetaillanguages = ModelsMyvindulaFuncdetailLanguages(**D)
        self.store.add(funcdetaillanguages)
        self.store.flush()   
    
    def del_funcdetailLanguages(self, user):
        results = self.store.find(ModelsMyvindulaFuncdetailLanguages, ModelsMyvindulaFuncdetailLanguages.vin_myvindula_funcdetail_username==user)
        if results:
            for result in results:
                self.store.remove(result)
                self.store.flush()         
    
        
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
          
    #pega o valor entre dois campos
    def checaValor(self, x, y):
        if not x and not y:
            return ''
        elif x:
             return x
        elif y:
             return y
        else:
             return '' 
          
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
    
    def getValueList(self,campo,request,data):
        if campo in request.keys():
            if request.get(campo, None):
                return request.get(campo,[])
            else:
                return []
        elif data:
            L = []
            for i in data:
                if campo == 'languages':
                    L.append(i.vin_myvindula_languages_id)
                elif campo == 'skills_expertise':
                    L.append(i.vin_myvindula_courses_id)
                else:
                    L.append(i.id)
                    
            return L
        else:
            return []    
        
    def getParametersFromURL(self, ctx):
        traverse = ctx.context.REQUEST.get('traverse_subpath')
        vars = {}
        if traverse != None:
            size = len(traverse)
            counter = 0
            for i in range(size/2):
                position = i+counter
                vars.update({traverse[position]:traverse[position+1]})
                counter+=1
        return vars
                
    
    def getPhoto(self,campo,request,data):
        if campo in request.keys():
#            if request.get(campo, None):
#                return self.context.absolute_url()+'/'+request.get(campo, '').filename + '/image_thumb'
#            else:
                return self.context.absolute_url()+'/'+'defaultUser.png'
        elif campo in data.keys():
            if data.get(campo, None) and not ' ' in data.get(campo,None) and not data.get(campo,None) == '':
                #return self.context.absolute_url()+'/'+data.get(campo,'') + '/image_thumb'
                return BaseFunc().get_imageVindulaUser(data.get(campo,''))
                
            else:
                return self.context.absolute_url()+'/'+'defaultUser.png'
        else:
            return self.context.absolute_url()+'/'+'defaultUser.png'        
        
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
    
    # retorna dado convertido para o campo de valor monetario   
    def converte_valor(self, valor):
        if valor is not None:
            if type(valor) == Decimal:
                valor = str(valor)
                valor = valor.replace('R$ ','')
                valor = valor.replace('.', ',')
                #valor = 'R$ ' + valor
                return valor
            else: 
                return None  
        else:
            return None        
    
    #retorno a data de competencia no ordem coreta
    def converte_competencia(self, valor):
        if valor is not None:
            tmp = valor.split('/')
            return tmp[1]+'/'+tmp[0]
        else:
            return None
        
    # retorna dado convertido para o campos de data 
    def converte_data(self, data, data_atual=False):
        if data is not None and data != '':
            if type(data) == date:
                return data.strftime('%d/%m/%Y')
            else:
                return data
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
                return data
            
    def converte_dadosByDB(self, D):
        
        keys = D.keys()
        for item in keys:
            valor = D[item]
            if type(valor) == str: 
                valor = valor.strip()
                try:
                    D[item] = unicode(valor, 'utf-8')
                except:
                    D[item] = unicode(valor, 'ISO-8859-1')
            else:
                D[item] = valor
        return D
                 
    def geraCampos(self,form_data):
        if type(form_data) == dict:
            errors = form_data.get('errors',None)
            data = form_data.get('data',None)
            campos = form_data.get('campos',None)
            config_myvindula = form_data.get('config_myvindula',None)
            manage = form_data.get('manage',False)
            
            languages = ModelsMyvindulaLanguages().get_allLanguages()
            cursos = ModelsMyvindulaCourses().get_allCourses()
            user = form_data.get('username','')
            
            funcdetailLanguages = ModelsMyvindulaFuncdetailLanguages().get_funcdetailLanguagesByUsername(user)
            funcdetailCourse = ModelsMyvindulaFuncdetailCouses().get_funcdetailCouserByUsername(user)
            
            html=[]
            i=0
            while i < len(campos.keys())-1:
                html.append(i)
                i+=1
            for campo in campos.keys():
                if campo != 'vin_myvindula_department' and campo != 'username':
                    
                    index = campos[campo].get('ordem',0)
                    tmp = ""
                    tmp += "<!-- Campo %s -->"%(campo)
                    tmp += "<div class='%s'>"%(self.field_class(errors, campo))
                    if self.checaEstado(config_myvindula,campo) or manage:
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
                            tmp += "<input id='photograph' type='file' value='%s' name='photograph' size='25' />"%(self.getPhoto(campo,self.request,data))
                        
                        elif campo == 'date_birth' or campo == 'admission_date':
                            tmp += """<input id='%s' type='text' maxlength='10' onKeyDown='Mascara(this,Data);' onKeyPress='Mascara(this,Data);' onKeyUp='Mascara(this,Data);'
                                             value='%s' name='%s' size='25'/>"""%(campo,self.converte_data(self.getValue(campo,self.request,data),False),campo)

                        elif campo == 'customised_message':
                            tmp += "<textarea id='%s' name='%s' style='width: 100; height: 81px;'>%s</textarea>"%(campo, campo, self.getValue(campo,self.request,data)) 
                        
                        
                        elif campo == 'languages':
                            tmp += "<div class='boxSelecao' name='languages'>"
                            for language in languages:
                                if language.id in self.getValueList(campo,self.request,funcdetailLanguages):
                                    lable_language = language.title +' - '+ language.level
                                    tmp += "<input value='%s' type='checkbox' checked name='languages'/><label>%s</label><br/>"%(language.id,lable_language)
                                else:
                                    lable_language = language.title +' - '+ language.level
                                    tmp += "<input value='%s' type='checkbox' name='languages'/><label>%s</label><br/>"%(language.id,lable_language)
                            tmp += "</div>" 
                            
                        elif campo == 'skills_expertise':
                            tmp += "<div class='boxSelecao' name='skills_expertise'>"
                            for curso in cursos:
                                if curso.id in self.getValueList(campo,self.request,funcdetailCourse):
                                    lable_curso = curso.title +' - '+ curso.length
                                    tmp += "<input value='%s' type='checkbox' checked name='skills_expertise'/><label>%s</label><br/>"%(curso.id,lable_curso)
                                else:
                                    lable_curso = curso.title +' - '+ curso.length
                                    tmp += "<input value='%s' type='checkbox' name='skills_expertise'/><label>%s</label><br/>"%(curso.id,lable_curso)
                            
                            tmp += "</div>" 
                            
                        else:
                            tmp += "<input id='%s' type='text' value='%s' name='%s' size='25'/>"%(campo,self.getValue(campo,self.request,data),campo)
                    else:
                        if campo == 'date_birth' or campo == 'admission_date':
                            tmp += "<input id='%s' type='hidden' value='%s' name='%s' size='25'/>"%(campo,self.converte_data(self.getValue(campo,self.request,data),False),campo)
                        
                        elif campo == 'skills_expertise':
                            for i in self.getValueList(campo,self.request,funcdetailCourse):
                                tmp += "<input id='%s' type='hidden' value='%s' name='%s' size='25'/>"%(campo,i,campo)
                            
                        elif campo =='languages':
                            for i in self.getValueList(campo,self.request,funcdetailLanguages):
                                tmp += "<input id='%s' type='hidden' value='%s' name='%s' size='25'/>"%(campo,i,campo)
                        
                        else:
                            tmp += "<input id='%s' type='hidden' value='%s' name='%s' size='25'/>"%(campo,self.getValue(campo,self.request,data),campo)
                        
                    tmp += "</div>"
                    html.pop(index)
                    html.insert(index, tmp)    
            
            return html

    def geraConfCampos(self,form_data):
        if type(form_data) == dict:
            errors = form_data.get('errors',None)
            data = form_data.get('data',None)
            campos = form_data.get('campos',None)
            html = []
            i=0
            while i < len(campos.keys()):
                html.append(i)
                i+=1
            for campo in campos.keys():
                if campo != 'id' and campo != 'username':
                    index = campos[campo].get('ordem',0)
                    tmp = ""
                    tmp += "<!-- Campo %s -->"%(campo)
                    tmp += "<div class='%s'>"%(self.field_class(errors, campo))
                    tmp += "   <label for='%s'>%s</label>"%(campo,campos[campo]['label'])
                    tmp += "   <div class='formHelp'>Habilita a edição do campo '%s' pelo funcionário'</div>"%(campos[campo]['label'])   
                    tmp += "   <div >%s</div>"%(errors.get(campo,''))
                    tmp += "<input id='%s' type='checkbox' value='%s' name='%s' size='25' %s/>"%(campo,'true',campo,self.checked(campo,self.request,data))
                    tmp += "</div>" 
                    
                    html.pop(index)
                    html.insert(index, tmp)      
            
            return html
        
    def geraExtraCampos(self,form_data):
        if type(form_data) == dict:
            errors = form_data.get('errors',None)
            data = form_data.get('data',None)
            campos = form_data.get('campos',None)
            
            html=[]
            i=0
            while i < len(campos.keys()):
                html.append(i)
                i+=1
            for campo in campos.keys():
                   
                    index = campos[campo].get('ordem',0)
                    tmp = ""
                    tmp += "<!-- Campo %s -->"%(campo)
                    tmp += "<div class='%s'>"%(self.field_class(errors, campo))
                    tmp += "   <label for='%s'>%s</label>"%(campo,campos[campo]['label'])
                    if campos[campo]['required'] == True:
                        tmp += "   <span class='fieldRequired' title='Obrigatório'>(Obrigatório)</span>"

                    tmp += "   <div class='formHelp'>%s.</div>"%(campos[campo]['decription'])   
                    tmp += "   <div >%s</div>"%(errors.get(campo,''))
                    tmp += "<input id='%s' type='text' value='%s' name='%s' size='25'/>"%(campo,self.getValue(campo,self.request,data),campo)
                    tmp += "</div>"
                    html.pop(index)
                    html.insert(index, tmp)    
            
            return html
        
        
    def uploadFile(self,ctx, path, file):
        """ function used to upload the file to the Plone site, 
           with the parameter where the file will be saved and the file will be saved
        """
        portal_workflow = getToolByName(getSite(), 'portal_workflow')
        normalizer = getUtility(IIDNormalizer)
        name_file = normalizer.normalize(file.filename)    #unicode(file.filename, 'utf-8')) #takes the name of the file
        count = 0
        file2 = file
        while name_file in path.objectIds():
            name_file = name_file + '-' + str(count)
            count +=1
        
        #starts the upload process     
        else:
            try:
                img = file.xreadlines().read()
                imagem = namedfile.NamedImage(img, filename=unicode(file.filename))
                objects = {'type_name':'vindula.myvindula.vindulaphotouser',
                          'id': name_file,
                          'title':name_file,
                          'photograph':imagem}

#                ctx.context.portal_membership.changeMemberPortrait(file, path.id)
                    
                path.invokeFactory(**objects)              
                #takes the url of the file to save the database  
                content = getattr(path, name_file, None)

                url = ''
                if content is not None:
                    url = '/'.join(content.getPhysicalPath()[2:])  
                
                return unicode(url)
                
            except:
                return None

    def get_imageVindulaUser(self,caminho):
        local = caminho.split('/')
        try:
            ctx= getSite()[local[0]][local[1]][local[2]]
            obj = ctx.restrictedTraverse('@@images').scale('photograph', height=150, width=120)
        
            return obj.url
        except:
            return ''

                
class SchemaFunc(BaseFunc):
    def to_utf8(value):
        return unicode(value, 'utf-8')

    campos = {'name'                  : {'required': False, 'type' : to_utf8, 'label':'Nome',                   'decription':u'Digite o nome do funcionário',                   'ordem':0},
              'nickname'              : {'required': False, 'type' : to_utf8, 'label':'Apelido',                'decription':u'Digite o apelido do funcionário',                'ordem':1},
              'phone_number'          : {'required': False, 'type' : to_utf8, 'label':'Telefone',               'decription':u'Digite o telefone do funcionário',               'ordem':2},
              'cell_phone'            : {'required': False, 'type' : to_utf8, 'label':'Celular',                'decription':u'Digite o telefone celular do funcionário',       'ordem':3},
              'email'                 : {'required': False, 'type' : 'email', 'label':'E-mail',                 'decription':u'Digite o e-mail do funcionário',                 'ordem':4},
              'employee_id'           : {'required': False, 'type' : to_utf8, 'label':'ID Funcionário',         'decription':u'Digite o ID do funcionário',                     'ordem':5},
              'date_birth'            : {'required': False, 'type' : date,    'label':'Data de Nascimento',     'decription':u'Digite a data de nascimento do funcionário',     'ordem':6},
              'registration'          : {'required': False, 'type' : to_utf8, 'label':'Matrícula',              'decription':u'Digite o número de matrícula do funcionário',    'ordem':7},
              'enterprise'            : {'required': False, 'type' : to_utf8, 'label':'Empresa',                'decription':u'Digite o nome da empresa do funcionário',        'ordem':8},
              'position'              : {'required': False, 'type' : to_utf8, 'label':'Cargo',                  'decription':u'Digite o cargo do funcionário',                  'ordem':9},
              'admission_date'        : {'required': False, 'type' : date,    'label':'Data de Admissão',       'decription':u'Digite a data de admissão do funcionário',       'ordem':10},
              'cost_center'           : {'required': False, 'type' : to_utf8, 'label':'Centro de Custo',        'decription':u'Digite o centro de custo do funcionário',        'ordem':11},
              'organisational_unit'   : {'required': False, 'type' : to_utf8, 'label':'Unidade organizacional', 'decription':u'Digite a unidade organizacional do funcionário', 'ordem':12},
              'reports_to'            : {'required': False, 'type' : to_utf8, 'label':'Reporta-se a',           'decription':u'Digite a quem o funcionário se reporta',         'ordem':13},
              'location'              : {'required': False, 'type' : to_utf8, 'label':'Localização',            'decription':u'Digite a localização do funcionário',            'ordem':14},
              'postal_address'        : {'required': False, 'type' : to_utf8, 'label':'Endereço Postal',        'decription':u'Digite o endereço postal do funcionário',        'ordem':15},
              'special_roles'         : {'required': False, 'type' : to_utf8, 'label':'Funções Especiais',      'decription':u'Digite as funções especiais do funcionário',     'ordem':16},
              'photograph'            : {'required': False, 'type' : 'file',  'label':'Foto',                   'decription':u'Coloque a foto do funcionário',                  'ordem':17},
              'pronunciation_name'    : {'required': False, 'type' : to_utf8, 'label':'Pronuncia do nome',      'decription':u'Como se pronuncia o  nome do funcionário',       'ordem':18},
              'committess'            : {'required': False, 'type' : to_utf8, 'label':'Comissão',               'decription':u'Digite a comissão do funcionário',               'ordem':19},
              'projetcs'              : {'required': False, 'type' : to_utf8, 'label':'Projetos',               'decription':u'Digite os projetos do funcionário',              'ordem':20},
              'personal_information'  : {'required': False, 'type' : to_utf8, 'label':'Informações pessoais',   'decription':u'Digite as informações pessoais do funcionário',  'ordem':21},
              'skills_expertise'      : {'required': False, 'type' : to_utf8, 'label':'Habilidades'          ,  'decription':u'Digite as habilidades do funcionário',           'ordem':22},
              'profit_centre'         : {'required': False, 'type' : to_utf8, 'label':'Centro de Lucro',        'decription':u'Digite o centro de lucro do funcionário',        'ordem':23},
              'languages'             : {'required': False, 'type' : to_utf8, 'label':'Idioma',                 'decription':u'Digite o idioma do funcionário',                 'ordem':24},
              'availability'          : {'required': False, 'type' : to_utf8, 'label':'Disponibilidade',        'decription':u'Digite a disponibilidade do funcionário',        'ordem':25},
              'papers_published'      : {'required': False, 'type' : to_utf8, 'label':'Artigos Publicados',     'decription':u'Digite os artigo publicados do funcionário',     'ordem':26},
              'blogs'                 : {'required': False, 'type' : to_utf8, 'label':'Blogs',                  'decription':u'Digite os blogs do funcionário',                 'ordem':27},
              'teaching_research'       : {'required': False, 'type' : to_utf8, 'label':'Personalizado 1',        'decription':u'Campo para personalizar',                      'ordem':28},
              'resume'                  : {'required': False, 'type' : to_utf8, 'label':'Personalizado 2',        'decription':u'Campo para personalizar',                      'ordem':29},
              'delegations'             : {'required': False, 'type' : to_utf8, 'label':'Personalizado 3',        'decription':u'Campo para personalizar',                      'ordem':30},
              'customised_message'      : {'required': False, 'type' : to_utf8, 'label':'Personalizado 4',        'decription':u'Campo para personalizar',                      'ordem':31},
              
              'username'                : {'required': False, 'type' : to_utf8, 'label':'Nome de Usuário'        },}  #Campo Obrigatorio
              #'vin_myvindula_department_id': {'required': False, 'type' : int,     'label':'Departamento'           },} #Campo Obrigatorio
                    
    def registration_processes(self,context,user,manage=False):
        success_url = context.context.absolute_url() + '/@@myvindula'
        success_url_manage = context.context.absolute_url() + '/@@myvindulamanagealluser'
        access_denied = context.context.absolute_url() + '/login'
        form = context.request # var tipo 'dict' que guarda todas as informacoes do formulario (keys,items,values)
        form_keys = form.keys() # var tipo 'list' que guarda todas as chaves do formulario (keys)
        campos = self.campos
        #user = context.context.portal_membership.getAuthenticatedMember()

        if not manage:
            try:
                user_id = unicode(user.id, 'utf-8')    
            except:
                user_id = user.id
         
        else:
            user_id = user.username
        
        # divisao dos dicionarios "errors" e "convertidos"
        form_data = {
            'errors': {},
            'data': {},
            'campos':campos,
            'departametos': ModelsDepartment().get_department(),
            'username' : user_id,
            'config_myvindula':ModelsConfgMyvindula().get_configuration(),
            'manage':manage,}
        
        # se clicou no botao "Voltar"
        if 'form.voltar' in form_keys:
            if manage:
                context.request.response.redirect(success_url_manage)
            else:
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
                        data['photograph'] = unicode(form['photograph'], 'utf-8')
                        
                    else:
                        if form['photograph'].filename != '':
                            path = context.context.portal_membership.getHomeFolder()
                            file = data['photograph']
                            if path:
                                photo = BaseFunc().uploadFile(context,path,file)
                                if photo:
                                    data['photograph'] = photo
                                else:
                                    access_denied = context.context.absolute_url() + '/@@myvindulaprefs?error=1'
                                    return context.request.response.redirect(access_denied)
                            else:
                                access_denied = context.context.absolute_url() + '/@@myvindulaprefs?error=2'
                                return context.request.response.redirect(access_denied)
                            
                        else:
                            data['photograph'] = None      
                
                if 'vin_myvindula_department' in form_keys:
                    L = []
                    ModelsDepartment().del_department(user_id)
                    if not type(form['vin_myvindula_department']) == list:
                        L.append(form['vin_myvindula_department'])
                    else:
                        L = form['vin_myvindula_department']
                    for departament in L:
                        D={}
                        D['UID'] = unicode(departament,'utf-8')
                        D['funcdetails_id'] = user_id
                        ModelsDepartment().set_department(**D)
                            
                if 'skills_expertise' in form_keys:
                    ModelsMyvindulaFuncdetailCouses().del_funcdetailCouser(user_id)
                    for curso in form['skills_expertise']:
                        D={}
                        D['username'] = user_id
                        D['id_courses'] = int(curso)
                        ModelsMyvindulaFuncdetailCouses().set_funcdetailCouser(**D)
        
                
                if 'languages' in form_keys:
                    ModelsMyvindulaFuncdetailLanguages().del_funcdetailLanguages(user_id)
                    for languages in form['languages']:
                        D={}
                        D['username'] = user_id
                        D['id_courses'] = int(languages)
                        ModelsMyvindulaFuncdetailLanguages().set_funcdetailLanguages(**D)
                
                
                if user_id != 'acl_users':
                    # editando...
                    result = self.store.find(ModelsFuncDetails, ModelsFuncDetails.username == user_id).one()
                    if result:
                        if data['photograph'] is None:
                            data['photograph'] = result.photograph
                        
                        for campo in campos.keys():
                            value = data.get(campo, None)
                            setattr(result, campo, value)

                    else:
                        #adicionando...
                        database = ModelsFuncDetails(**data)
                        self.store.add(database)
                        self.store.flush()
                        
                    #dicionario para edição do usuario do plone
                    user_plone = {'fullname':data.get('name',''),
                                  'email':data.get('email',''),
                                  'home_page':data.get('blogs',''),
                                  'location':data.get('location',''),
                                  'description':data.get('customised_message','')}
                    if not manage:
                        user.setMemberProperties(user_plone)
                            
                #Redirect back to the front page with a status message
                IStatusMessage(context.request).addStatusMessage(_(u"Seu perfil foi editado com sucesso!!"), "info")
                if manage:
                    context.request.response.redirect(success_url_manage)
                else:
                    context.request.response.redirect(success_url)
                                   
            else:
                form_data['errors'] = errors
                form_data['data'] = data
                return form_data
          
        # se for um formulario de edicao 
        elif user_id != 'acl_users':
            data = self.store.find(ModelsFuncDetails, ModelsFuncDetails.username == user_id).one()
            departaments = ModelsDepartment().get_departmentByUsername(user_id)
            
            D = {}
            for campo in campos.keys():
                D[campo] = getattr(data, campo, '')
              
            D['vin_myvindula_department'] = departaments
            
            if data:
               form_data['data'] = D
               return form_data
            else:
               return form_data
              
        # se o usuario não estiver logado
        else:
            IStatusMessage(context.request).addStatusMessage(_(u'Erro ao salvar o registro.'),"erro")
            context.request.response.redirect(access_denied)
        
class SchemaConfgMyvindula(BaseFunc):
    
    campos = {'vin_myvindula_department': {'required': False, 'type' : bool, 'label':'Departamento',      'ordem':0},
              'name'                    : {'required': False, 'type' : bool, 'label':'Nome',              'ordem':1},
              'nickname'                : {'required': False, 'type' : bool, 'label':'Apelido',           'ordem':2},
              'phone_number'            : {'required': False, 'type' : bool, 'label':'Telefone',          'ordem':3},
              'cell_phone'              : {'required': False, 'type' : bool, 'label':'Celular',           'ordem':4},
              'email'                   : {'required': False, 'type' : bool, 'label':'E-mail',            'ordem':5},
              'employee_id'             : {'required': False, 'type' : bool, 'label':'ID Funcionário',    'ordem':6},
              'date_birth'            : {'required': False, 'type' : bool, 'label':'Data de Nascimento',     'ordem':7},
              'registration'          : {'required': False, 'type' : bool, 'label':'Matrícula',              'ordem':8},
              'enterprise'            : {'required': False, 'type' : bool, 'label':'Empresa',                'ordem':9},
              'position'              : {'required': False, 'type' : bool, 'label':'Cargo',                  'ordem':10},
              'admission_date'        : {'required': False, 'type' : bool, 'label':'Data de Admissão',       'ordem':11},
              'cost_center'           : {'required': False, 'type' : bool, 'label':'Centro de Custo',        'ordem':12},
              'organisational_unit'   : {'required': False, 'type' : bool, 'label':'Unidade organizacional', 'ordem':13},
              'reports_to'            : {'required': False, 'type' : bool, 'label':'Reporta-se a',           'ordem':14},
              'location'              : {'required': False, 'type' : bool, 'label':'Localização',            'ordem':15},
              'postal_address'        : {'required': False, 'type' : bool, 'label':'Endereço Postal',        'ordem':16},
              'special_roles'         : {'required': False, 'type' : bool, 'label':'Funções Especiais',      'ordem':17},
              'photograph'            : {'required': False, 'type' : bool, 'label':'Foto',                   'ordem':18},
              'pronunciation_name'    : {'required': False, 'type' : bool, 'label':'Pronuncia do nome',      'ordem':19},
              'committess'            : {'required': False, 'type' : bool, 'label':'Comissão',               'ordem':20},
              'projetcs'              : {'required': False, 'type' : bool, 'label':'Projetos',               'ordem':21},
              'personal_information'  : {'required': False, 'type' : bool, 'label':'Informações pessoais',   'ordem':22},
              'skills_expertise'      : {'required': False, 'type' : bool, 'label':'Habilidades'          ,  'ordem':23},
              'profit_centre'         : {'required': False, 'type' : bool, 'label':'Centro de Lucro',        'ordem':24},
              'languages'             : {'required': False, 'type' : bool, 'label':'Idioma',                 'ordem':25},
              'availability'          : {'required': False, 'type' : bool, 'label':'Disponibilidade',        'ordem':26},
              'papers_published'      : {'required': False, 'type' : bool, 'label':'Artigos Publicados',     'ordem':27},
              'blogs'                 : {'required': False, 'type' : bool, 'label':'Blogs',                  'ordem':28},
              'teaching_research'     : {'required': False, 'type' : bool, 'label':'Personalizado 1',        'ordem':29},
              'resume'                : {'required': False, 'type' : bool, 'label':'Personalizado 2',        'ordem':30},
              'delegations'           : {'required': False, 'type' : bool, 'label':'Personalizado 3',        'ordem':31},
              'customised_message'    : {'required': False, 'type' : bool, 'label':'Personalizado 4',        'ordem':32},}
              
              #'username'              : {'required': False, 'type' : bool, 'label':'Nome de Usuário',}}
              
   
    def configuration_processes(self,context):
        success_url = context.context.absolute_url() + '/@@vindula-control-panel'
        access_denied = context.context.absolute_url() + '/@@overview-controlpanel'
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


class ImportUser(BaseFunc):
    
    def databaseUser(self,ctx):
        db_user = ModelsFuncDetails().get_allFuncDetails()
        plone_user = ctx.context.acl_users.getUserIds()
        cont = 0 
        D={}
        for user in db_user:
            if not user.username in plone_user: 
                cont += 1
               
        D['user_new'] = cont
        D['user_all'] = db_user.count()
        D['user_plone'] = len(plone_user) 
        return D
        
    def importUser(self,ctx,form):
        db_user = ModelsFuncDetails().get_allFuncDetails()
        plone_user = ctx.context.acl_users.getUserIds()
        portal_member = ctx.context.portal_membership
        D={}
        index = int(form.get('numb_user','0'))
        user = db_user[index]
        
        user_properties = {'fullname':user.name,
                           'email':user.email,
                           'home_page':user.blogs,
                           'location':user.location,
                           'description':user.customised_message,}
       
        if portal_member.getMemberById(user.username):
            portal_member.getMemberById(user.username).setMemberProperties(user_properties)
            
        else:
            
            if user.username != '':
                user_properties['username'] = user.username
                user_properties['password'] = user.username
                
                portal_member.addMember(id=user.username,
                                        password=user.username,
                                        roles=("Member",),
                                        domains="",
                                        properties=user_properties)
        
        D['username'] = user.username
        D['fullname'] = user.name
        D['email'] = user.email
            
        return D
    
class ManageCourses(BaseFunc):
    def to_utf8(value):
        return unicode(value, 'utf-8')
    
    campos = {'title'  : {'required': True,  'type' : to_utf8, 'label':'Nome do Curso',     'decription':u'Digite o nome do curso',    'ordem':0},
              'length' : {'required': False, 'type' : to_utf8, 'label':'Duração do Curso',  'decription':u'Digite a duração do curso', 'ordem':1},}
    
    def load_courses(self,ctx):
        data = ModelsMyvindulaCourses().get_allCourses()
        
        if data:
            return data
        else:
            return []
        
    
    def registration_processes(self,ctx):
        success_url = ctx.context.absolute_url() + '/myvindula-courses'
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
                    result = self.store.find(ModelsMyvindulaCourses, ModelsMyvindulaCourses.id == id).one()
                    if result:
                        for campo in campos.keys():
                            value = data.get(campo, None)
                            setattr(result, campo, value)

                else:
                    #adicionando...
                    database = ModelsMyvindulaCourses(**data)
                    self.store.add(database)
                    self.store.flush()
                        
                #Redirect back to the front page with a status message
                #IStatusMessage(ctx.request).addStatusMessage(_(u"Thank you for your order. We will contact you shortly"), "info")
                ctx.request.response.redirect(success_url)
                                   
            else:
                form_data['errors'] = errors
                form_data['data'] = data
                return form_data
          
        # se for um formulario de edicao 
        elif 'id' in form_keys:

            id = int(form.get('id'))
            data = self.store.find(ModelsMyvindulaCourses, ModelsMyvindulaCourses.id == id).one()
            
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
    
    
class ManageLanguages(BaseFunc):
    def to_utf8(value):
        return unicode(value, 'utf-8')
    
    campos = {'title'  : {'required': True,  'type' : to_utf8, 'label':'Nome do Idioma',   'decription':u'Digite o nome do idioma',  'ordem':0},
              'level'  : {'required': False, 'type' : to_utf8, 'label':'Nível do Idioma',  'decription':u'Digite o nível do idioma', 'ordem':1},}
    
    def load_languages(self,ctx):
        data = ModelsMyvindulaLanguages().get_allLanguages()
        
        if data:
            return data
        else:
            return []
        
    
    def registration_processes(self,ctx):
        success_url = ctx.context.absolute_url() + '/myvindula-languages'
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
                    result = self.store.find(ModelsMyvindulaLanguages, ModelsMyvindulaLanguages.id == id).one()
                    if result:
                        for campo in campos.keys():
                            value = data.get(campo, None)
                            setattr(result, campo, value)

                else:
                    #ModelsMyvindulaLanguages().set_languages(**data)
                    #adicionando...
                    database = ModelsMyvindulaLanguages(**data)
                    self.store.add(database)
                    self.store.flush()
                        
                #Redirect back to the front page with a status message
                #IStatusMessage(ctx.request).addStatusMessage(_(u"Thank you for your order. We will contact you shortly"), "info")
                ctx.request.response.redirect(success_url)
                                   
            else:
                form_data['errors'] = errors
                form_data['data'] = data
                return form_data
          
        # se for um formulario de edicao 
        elif 'id' in form_keys:

            id = int(form.get('id'))
            data = self.store.find(ModelsMyvindulaLanguages, ModelsMyvindulaLanguages.id == id).one()
            
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
        