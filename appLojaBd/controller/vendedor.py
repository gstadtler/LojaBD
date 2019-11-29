import controller.funcionario as func
from model.vendedor import Vendedor as modelVendedor

class Vendedor(func.Funcionario):
    '''
    classdocs
    '''


    def __init__(self, cpf="", nome="", email="", senha="", flagGerente=False, meta=0, cpfGerente):
        super().__init__(cpf, nome, email, senha, flagGerente)
        '''
        Constructor
        '''
        self.meta = meta
        self.mVendedor = modelVendedor(self)
        self.cpfGerente = cpfGerente
        
    def validaMeta(self):
        if self.meta.isdigit() == False:
            print("Meta só pode conter numeros!")
            break
        if (self.meta == 0):
            print("Informe uma meta para o vendedor!")
            break

    def validaCpfGerente(self):
        if self.cpfGerente == "":
            print("CPF do gerente em branco!")
            break
        elif self.cpfGerente.isdigit() == False:
            print("CPF do gerente só pode conter numeros!")
            break
        elif len(self.cpfGerente) > 11:
            print("CPF do gerente possui mais de 11 digitos!")
            break

    def validaVendedor(self):
        self.validaFuncionario(self.cpf, self.nome, self.email, self.senha)
        self.validaMeta(self.meta)
        self.validaCpfGerente(self.cpfGerente)
            
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
        
    def verificaSupervisor(self):
        print(self.mVendedor.verificaSupervisor(self.cpf)) 