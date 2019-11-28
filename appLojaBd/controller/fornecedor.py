from validacoes import validaCnpj, validaNome, validaEmail
from model.fornecedor import Cliente as ModelFornecedor
class Cliente(object):
    
    def __init__(self, cnpj="", nome="", email="", rua="", numero="" ,bairro="", cidade=""):
        '''
        Constructor
        '''
        self.cnpj = cnpj
        self.nome = nome
        self.email = email
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        
    def validaFornecedor(self):
        validaCnpj(self.cnpj)
        validaNome(self.nome)
        validaEmail(self.email)
    
    def operacaoFornecedor(self, operacao):
        mFornecedor = ModelFornecedor(self)
        mFornecedor.procIADFornecedor(operacao)