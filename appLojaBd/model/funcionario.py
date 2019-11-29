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
        
    def verificaGerente(self):
        conexao = conexao.Connection()
        conexao.execute('SELECT tagGerente FROM funcionario WHERE cpf = %s', (self.funcionario.cpf))
        ret = conexao.cur.fetchone()
        conexao.close()
        return ret