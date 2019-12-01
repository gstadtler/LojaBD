from model.funcionario import Funcionario as modelFuncionario
from controller.validacoes import validaCpf, validaNome, validaEmail

class Funcionario(object):
    '''
    classdocs
    '''


    def __init__(self, cpf="", nome="", email="", senha="", flagGerente="" ):
        '''
        Constructor
        '''
        self.cpf = cpf
        self.nome = nome
        self.email = email
        self.senha = senha
        self.flagGerente = flagGerente
        self.mFuncionario = modelFuncionario()
        
    def validaFuncionario(self):
        validaCpf(self.cpf)
        validaNome(self.nome)
        validaEmail(self.email)
        self.validaSenha(self.senha)
        
    def validaCargo(self):
        return self.mFuncionario.verificaGerente(self.cpf)
         
    def validaSenha(self):
        if (self.senha == ""):
            print("Senha em branco!")
        elif (len(self.senha) > 50):
            print("Senha possui mais de 50 caracteres!")
            
    def operacaoFuncionario(self, operacao):
        self.mFuncionario.procIADFuncionario(self, operacao)

    def listaFuncionarios(self):
        self.mFuncionario.retornaFuncionarios()