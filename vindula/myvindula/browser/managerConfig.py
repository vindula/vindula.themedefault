# coding: utf-8

from datetime import date

from vindula.myvindula.browser.validation import valida_form
from vindula.myvindula.browser.baseview import BaseView
from vindula.myvindula.models.funcionarios import Funcionarios
from vindula.myvindula.models.departamentos import Departamentos
from vindula.myvindula.models.config_myvindula import ConfigMyvindula

def to_utf8(value):
    return unicode(value, 'utf-8')

class ConfigUser(BaseView):

    def load_form(self):
          success_url = self.context.absolute_url() + '/plone_control_panel'
          form = self.request # var tipo 'dict' que guarda todas as informacoes do formulario (keys,items,values)
          form_keys = form.keys() # var tipo 'list' que guarda todas as chaves do formulario (keys)
          campos = {'name'                  : {'required': False, 'type' : bool, 'label':'Nome',                }, #Campo Obrigatorio
                    'phone_number'          : {'required': False, 'type' : bool, 'label':'Telefone',            },
                    'email'                 : {'required': False, 'type' : bool, 'label':'Email',               }, #Campo Obrigatorio
                    'employee_id'           : {'required': False, 'type' : bool, 'label':'ID Funcionario',      },
                    'data_nascimento'       : {'required': False, 'type' : bool, 'label':'Data de Nacimento',   }, #Campo Obrigatorio
                    'matricula'             : {'required': False, 'type' : bool, 'label':'Matricula',           },
                    'empresa'               : {'required': False, 'type' : bool, 'label':'Empresa',             },
                    'cargo'                 : {'required': False, 'type' : bool, 'label':'Cargo',               },
                    'data_admissao'         : {'required': False, 'type' : bool, 'label':'Data Admição',        },
                    'centro_custo'          : {'required': False, 'type' : bool, 'label':'Centro de Custo',     },
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
                    
                    'username'              : {'required': False, 'type' : bool,  'label':'Username',             }, #Campo Obrigatorio
                    'departamentos_id'      : {'required': False, 'type' : bool,  'label':'Departamento',         },} #Campo Obrigatorio
          
          # divisao dos dicionarios "errors" e "convertidos"
          form_data = {
              'errors': {},
              'data': {},
              'campos':campos,}
          
          # se clicou no botao "Voltar"
          if 'form.voltar' in form_keys:
              self.request.response.redirect(success_url)
          
          # se clicou no botao "Salvar"
          elif 'form.submited' in form_keys:
                # Inicia o processamento do formulario
                # chama a funcao que valida os dados extraidos do formulario (valida_form) 
                errors, convertidos = valida_form(campos, self.request.form)  
                
                if not errors:
                    if 'id' in self.request.form.keys():
                        # editando...
                        id = int(self.request.get('id'))
                        result = self.store.find(ConfigMyvindula, ConfigMyvindula.id == id)
                        
                        if result.count() > 0:
                            funcionario = result[0]
                            
                            for campo in campos.keys():
                                value = convertidos.get(campo, None)
                                setattr(funcionario, campo, value)

                            self.request.response.redirect(success_url)
                                      
                        else:
                            # adicionando...
                            configuracao = ConfigMyvindula(**convertidos)
                            self.store.add(configuracao)
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
              data = self.store.find(ConfigMyvindula, ConfigMyvindula.id == id).any()
              D = {}

              if data:
                 for campo in campos.keys():
                     D[campo] = getattr(data, campo, '')
                 
                 form_data['data'] = D
                 return form_data
              else:
                 return form_data
                
          # se for um formulario de adicao
          else:
              campos['id']={'required': True, 'type' : int,}
              data = self.store.find(ConfigMyvindula).one()
              D = {}

              if data:
                 for campo in campos.keys():
                     D[campo] = getattr(data, campo, '')
                 
                 form_data['data'] = D
                 return form_data
              else:
                 return form_data
