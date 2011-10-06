# coding: utf-8

from datetime import date

from vindula.myvindula.browser.validation import valida_form
from vindula.myvindula.browser.baseview import BaseView
from vindula.myvindula.models.funcionarios import Funcionarios
from vindula.myvindula.models.departamentos import Departamentos
from vindula.myvindula.models.config_myvindula import ConfigMyvindula

def to_utf8(value):
    return unicode(value, 'utf-8')

class ManagerUser(BaseView):

    def load_form(self):
          success_url = self.context.absolute_url() + '/list-User'
          form = self.request # var tipo 'dict' que guarda todas as informacoes do formulario (keys,items,values)
          form_keys = form.keys() # var tipo 'list' que guarda todas as chaves do formulario (keys)
          campos = {'name'                  : {'required': False, 'type' : to_utf8, 'label':'Nome',                    'decription':u'Digite o Nome deste funcionaro'             }, #Campo Obrigatorio
                    'phone_number'          : {'required': False, 'type' : to_utf8, 'label':'Telefone',                'decription':u'Digite o Telefone do funcionaro'            },
                    'email'                 : {'required': False, 'type' : to_utf8, 'label':'Email',                   'decription':u'Digite o Email do funcionaro'               }, #Campo Obrigatorio
                    'employee_id'           : {'required': False, 'type' : to_utf8, 'label':'ID Funcionario',          'decription':u'Digite o ID do funcionaro'                  },
                    'data_nascimento'       : {'required': False, 'type' : date,    'label':'Data de Nacimento',       'decription':u'Digite a data de nascimneto do funcionaro'  }, #Campo Obrigatorio
                    'matricula'             : {'required': False, 'type' : to_utf8, 'label':'Matricula',               'decription':u'Digite a matricula do funcionaro'           },
                    'empresa'               : {'required': False, 'type' : to_utf8, 'label':'Empresa',                 'decription':u'Digite o nome da empresa do funcionaro'     },
                    'cargo'                 : {'required': False, 'type' : to_utf8, 'label':'Cargo',                   'decription':u'Digite o cargo do funcionaro'               },
                    'data_admissao'         : {'required': False, 'type' : date,    'label':'Data Admição',            'decription':u'Digite a data de admição do funcionaro'     },
                    'centro_custo'          : {'required': False, 'type' : to_utf8, 'label':'Centro de Custo',         'decription':u'Digite o centro de custo do funcionaro'     },
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
                    'departamentos_id'      : {'required': False, 'type' : int,     'label':'Departamento'           },} #Campo Obrigatorio
          
          # divisao dos dicionarios "errors" e "convertidos"
          form_data = {
              'errors': {},
              'data': {},
              'campos':campos,
              'departametos': Departamentos().get_departamento(),
              'usernames' : self.context.acl_users.getUsers(),
              'config_myvindula':ConfigMyvindula().get_configiracao()}
          
          # se clicou no botao "Voltar"
          if 'form.voltar' in form_keys:
              self.request.response.redirect(success_url)
            
          # se clicou no botao "Salvar"
          elif 'form.submited' in form_keys:
                # Inicia o processamento do formulario
                # chama a funcao que valida os dados extraidos do formulario (valida_form) 
                errors, convertidos = valida_form(campos, self.request.form)  

                if not errors:
                    # verifica se tem foto
                    if 'photograph' in form_keys:
                        if type(form['photograph']) == str:
                            convertidos['photograph'] = to_utf8(form['photograph'])
                        else:
                            if form['photograph'].filename != '': 
                                convertidos['photograph'] = self.salva_arquivo(form['photograph'])
                            else:
                                convertidos['photograph'] = None      
                    
                    if 'id' in self.request.form.keys():
                        # editando...
                        id = int(self.request.get('id'))
                        result = self.store.find(Funcionarios, Funcionarios.id == id)
                        
                        if result.count() > 0:
                            funcionario = result[0]
                            
                            for campo in campos.keys():
                                value = convertidos.get(campo, None)
                                setattr(funcionario, campo, value)

                            self.request.response.redirect(success_url)           
                    else:
                        # adicionando...
                        funcionario = Funcionarios(**convertidos)
                        self.store.add(funcionario)
                        self.store.flush()
                    
                        self.request.response.redirect(success_url)        
                         
                else:
                    form_data['errors'] = errors
                    form_data['data'] = convertidos
                    return form_data
            
          # se for um formulario de edicao
          elif 'id' in self.request.keys():    
              id = self.request.id
              id = int(id)
              data = self.store.find(Funcionarios, Funcionarios.id == id).any()
              D = {}
              for campo in campos.keys():
                  D[campo] = getattr(data, campo, '')
                
              if data:
                 form_data['data'] = D
                 return form_data
              else:
                 return form_data
                
          # se for um formulario de adicao
          else:
               return form_data
