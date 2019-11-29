import controller.funcionario as func
from model.vendedor import Vendedor as modelVendedor

class Vendedor(func.Funcionario):
    '''
    classdocs
    '''


    def __init__(self, cpf="", nome="", email="", senha="", flagGerente=False, meta=0):
        super().__init__(cpf, nome, email, senha, flagGerente)
        '''
        Constructor
        '''
        self.meta = meta
        self.mVendedor = modelVendedor(self)
    def validaMeta(self):
        if self.meta.isdigit() == False:
            print("Meta só pode conter numeros!")
            break
        if (self.meta == 0):
            print("Informe uma meta para o vendedor!")
            break
              
    def validaVendedor(self):
        self.validaFuncionario(self.cpf, self.nome, self.email, self.senha)
        self.validaMeta(self.meta)
            
    def novoVendedor(self, cpfGerente, operacao):
        if self.validaCargo(cpfGerente) == True:
            self.validaVendedor()
            self.procIADFuncionario(operacao)
        else:
            print("Você não tem permissão para efetuar essa operação!")
            break
    
    def verificaMeta(self,mes,ano):
        parametros = (self.cpf, mes, ano)
        print(self.mVendedor.verificaMeta(parametros))       