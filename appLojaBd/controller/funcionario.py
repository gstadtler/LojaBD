from model.funcionario import Funcionario
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
        
    def validaFuncionario(self):
        self.validaCpf(self.cpf)
        self.validaNome(self.nome)
        self.validaEmail(self.email)
        self.validaSenha(self.senha)
        
    def validaCargo(self, flagGerente):
        #verifica se é um gerente
        pass
            
    def validaNome(self):
        if (self.nome == ""):
            print("Nome em branco!")
        elif (len(self.nome) > 20):
            print("Nome possui mais de 20 caracteres!")
            
    def validaEmail(self):
        if (self.email == ""):
            print("E-Mail em branco!")
        elif (len(self.email) > 30):
            print("E-Mail possui mais de 30 caracteres!")
    
    def validaCpf(self):
        if (self.cpf == ""):
            print("CPF em branco!")
        elif (len(self.cpf) > 11):
            print("CPF possui mais de 11 digitos!")
            
    def validaSenha(self):
        if (self.senha == ""):
            print("Senha em branco!")
        elif (len(self.senha) > 50):
            print("Senha possui mais de 50 caracteres!")
            
    def operacaoFuncionario(self, operacao):
        mFuncionario = Funcionario(self)
        mFuncionario.procIADFuncionario(operacao)
    
             
        