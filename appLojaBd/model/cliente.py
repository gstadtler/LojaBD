from model import connection as conexao

class Cliente(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def procIADCliente(self, cliente, operacao):
        procValores = (operacao, cliente.cpf, cliente.nome, 
                       cliente.email, cliente.rua, cliente.numero,
                       cliente.bairro, cliente.cidade)
        
        conexao = conexao.Connection()
        conexao.callProCedure(self, "insere_atualiza_deleta_cliente" , procValores)
        conexao.commit()
        conexao.close()
        
    def retornaClientes(self):
        conexao = conexao.Connection()
        print('')
        conexao.query('SELECT * FROM cliente')
        conexao.queryResult()
        conexao.close()