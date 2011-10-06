from storm.locals import *
from vindula.myvindula.models.base import BaseStore


class Funcionarios(Storm, BaseStore):
    __storm_table__ = 'funcionarios'
    
    id = Int(primary=True)
    name = Unicode()
    phone_number = Unicode()
    email = Unicode()
    employee_id = Unicode()
    username = Unicode()
    data_nascimento = Date()
    matricula = Unicode()
    empresa = Unicode()
    cargo = Unicode()
    data_admissao = Date()
    centro_custo = Unicode()
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
    departamentos_id = Int()  
  
    departamento = ReferenceSet(id, "Departamentos.departamentos_id")
    
    # carrega dados de todos os  funcionario"    
    def get_funcionarios(self):
        data = self.store.find(Funcionarios)
        if data.count() == 0:
            return []
        else:
            return data  