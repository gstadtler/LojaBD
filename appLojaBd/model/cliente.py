from model import connection as conex

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
        
        conexao = conex.Connection()
        conexao.callProCedure("insere_atualiza_deleta_cliente" , procValores)
        conexao.commit()
        conexao.close()
        
    def retornaClientes(self):
        conexao = conex.Connection()
        print('')
        conexao.query('SELECT * FROM cliente')
        conexao.queryResult()
        conexao.close()