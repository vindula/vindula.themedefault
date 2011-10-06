# coding: utf-8

from storm.expr import Desc
from vindula.myvindula.browser.baseview import BaseView
from vindula.myvindula.models.funcionarios import Funcionarios

class MeusLinks(BaseView):
    
    def get_meusLinks(self):
        pasta_user = self.context.portal_membership.getHomeFolder()
        if 'meus_links' in pasta_user.keys():
            pasta_links = pasta_user['meus_links']
            links = pasta_links.objectItems('ATLink')
            L=[]
            for link in links:
                D={}
                D['title'] = link[1].Title()
                D['descricao'] = link[1].Description()
                D['url'] = link[1].getRawRemoteUrl()
                L.append(D)
            
            return L
        return []

class ListUser(BaseView):
    """ View para listagem dos usuarios do portal """  
    def load_list(self):           
        data = self.store.find(Funcionarios).order_by(Desc(Funcionarios.name)) 
        if data.count() == 0:
            return False
        else: 
            return data














