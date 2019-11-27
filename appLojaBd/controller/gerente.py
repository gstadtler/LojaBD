import controller.funcionario as func
from controller.vendedor import Vendedor
class Gerente(func.Funcionario):
    '''
    classdocs
    '''


    def __init__(self, cpf="", nome="", email="", senha="", flagGerente=True):
        super().__init__(cpf, nome, email, senha, flagGerente)
        '''
        Constructor
        '''
        
    def novoGerente(self,flagGerente, operacao):
        if self.validaCargo(flagGerente) == True:
            self.validaFuncionario(self.cpf, self.nome, self.email, self.senha)
            self.operacaoFuncionario(operacao)
        else:
            print("Você não tem permissão para efetuar essa operação!")
            
    def criarFuncionario(self, cpf, nome, email, senha, flagGerente, operacao):
        if flagGerente == True:
            gerente = Gerente(cpf, nome, email, senha, flagGerente)
            gerente.novoGerente(self.flagGerente, operacao)
        else:
            vendedor = Vendedor(cpf, nome, email, senha, flagGerente)
            vendedor.novoVendedor(self.flagGerente, operacao)
             
        
        