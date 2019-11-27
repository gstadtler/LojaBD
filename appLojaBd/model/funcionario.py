from model import connection as conexao
class Funcionario(object):
    '''
    classdocs
    '''


    def __init__(self, funcionario):
        '''
        Constructor
        '''
        self.funcionario = funcionario
    
    def procIADFuncionario(self, operacao):
        procValores = (operacao, self.funcionario.cpf, self.funcionario.nome, 
                       self.funcionario.email, self.funcionario.senha, self.funcionario.flagGerente)
        
        conexao = conexao.Connection()
        conexao.callProCedure(self, "insere_atualiza_deleta_funcionario" , procValores)
        conexao.close()
        