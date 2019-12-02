from model import connection as conexao

class Fornecedor(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor    
        '''
    
    def procIADFornecedor(self, fornecedor, operacao):
        procValores = (operacao, fornecedor.cnpj, fornecedor.nome, 
                       fornecedor.email, fornecedor.rua, fornecedor.numero,
                       fornecedor.bairro, fornecedor.cidade)
        
        conexao = conexao.Connection()
        conexao.callProCedure(self, "insere_atualiza_deleta_fornecedor" , procValores)
        conexao.commit()
        conexao.close()
        
    def retornaFornecedores(self):
        conect = conexao.Connection()
        print('')
        conect.query('SELECT * FROM fornecedor')
        conect.queryResult()
        conect.close()