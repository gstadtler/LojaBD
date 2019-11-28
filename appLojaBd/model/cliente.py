from model import connection as conexao
class Cliente(object):
    '''
    classdocs
    '''


    def __init__(self, cliente):
        '''
        Constructor
        '''
        self.cliente = cliente
    
    def procIADCliente(self, operacao):
        procValores = (operacao, self.cliente.cpf, self.cliente.nome, 
                       self.cliente.email, self.cliente.rua, self.cliente.numero,
                       self.cliente.bairro, self.cliente.cidade)
        
        conexao = conexao.Connection()
        conexao.callProCedure(self, "insere_atualiza_deleta_cliente" , procValores)
        conexao.close()