from controller.validacoes import validaCnpj, validaNome, validaEmail
from model.fornecedor import Fornecedor as ModelFornecedor

class Fornecedor(object):
    
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
        self.mFornecedor = ModelFornecedor()
     
    def dadosEdicaoForn(self, nome, email, rua, numero, bairro, cidade):
        if self.nome == "":
            self.nome = nome
        if self.email == "":
            self.email = email
        if self.rua == "":
            self.rua = rua
        if self.numero  == "":
            self.numero = numero
        if self.bairro == "":
            self.bairro = bairro
        if self.cidade == "":
            self.cidade = cidade
               
    def validaFornecedor(self):
        validaCnpj(self.cnpj)
        validaNome(self.nome)
        validaEmail(self.email)
    
    def operacaoFornecedor(self, operacao):
        if operacao == "I":
            if self.validaFornecedor() == False:
                return False
        else:
            dadosForn = self.mFornecedor.recuperaDados(self.cnpj)
            self.dadosEdicaoForn(*dadosForn)
            self.mFornecedor.procIADFornecedor(self, operacao)
    
    def listaFornecedores(self):
        self.mFornecedor.retornaFornecedores()