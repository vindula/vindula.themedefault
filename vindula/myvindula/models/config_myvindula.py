from storm.locals import *
from vindula.myvindula.models.base import BaseStore


class ConfigMyvindula(Storm, BaseStore):
    __storm_table__ = 'conf_myvindula'
    
    id = Int(primary=True)
    name = Bool()
    phone_number = Bool()
    email = Bool()
    employee_id = Bool()
    username = Bool()
    data_nascimento = Bool()
    matricula = Bool()
    empresa = Bool()
    cargo = Bool()
    data_admissao = Bool()
    centro_custo = Bool()
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
    departamentos_id = Bool()  
  
        
    # carrega dados de todos os  funcionario"    
    def get_configiracao(self):
        data = self.store.find(ConfigMyvindula).one()
        if data:
            return data
        else:
            return []  