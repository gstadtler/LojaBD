import controller.funcionario as func

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
      
    def validaMeta(self):
        if (self.meta == 0):
            print("Informe uma meta para o vendedor!")
              
    def validaVendedor(self):
        self.validaFuncionario(self.cpf, self.nome, self.email, self.senha)
        self.validaMeta(self.meta)
            
    def novoVendedor(self,flagGerente, operacao):
        if self.validaCargo(flagGerente) == True:
            self.validaVendedor()
            self.operacaoFuncionario(operacao)
        else:
            print("Você não tem permissão para efetuar essa operação!")