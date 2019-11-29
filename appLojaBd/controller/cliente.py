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
        self.mCliente = ModelCliente(self)
        
    def validaCliente(self):
        validaCpf(self.cpf)
        validaNome(self.nome)
        validaEmail(self.email)
    
    def operacaoCliente(self, operacao):
        self.mCliente.procIADCliente(operacao)