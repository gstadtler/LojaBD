from controller.validacoes import validaCpf, validaNome, validaEmail
from model.cliente import Cliente as ModelCliente

class Cliente(object):
    '''
    classDocs
    '''
    
    def __init__(self, cpf="", nome="", email="", rua="", numero="" ,bairro="", cidade=""):
        '''
        Constructor
        '''
        self.cpf = cpf
        self.nome = nome
        self.email = email
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.mCliente = ModelCliente()
        
    def validaCliente(self):
        if validaCpf(self.cpf) == False:
            return False
        if validaNome(self.nome) == False:
            return False
        if validaEmail(self.email) == False:
            return False
    
    def operacaoCliente(self, operacao):
        if operacao != "D":
            if self.validaCliente() == False:
                return False
        else:
            self.mCliente.procIADCliente(self, operacao)
    
    def listaClientes(self):
        self.mCliente.retornaClientes()