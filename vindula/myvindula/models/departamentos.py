from storm.locals import *
from vindula.myvindula.models.base import BaseStore


class Departamentos(Storm, BaseStore):
    __storm_table__ = 'departamentos'
    
    id = Int(primary=True)
    nome = Unicode()
    descricao = Unicode()
    
    # carrega dados para o combo "departamento_id"    
    def get_departamento(self):
        data = self.store.find(Departamentos)
        if data.count() == 0:
            return []
        else:
            return data  