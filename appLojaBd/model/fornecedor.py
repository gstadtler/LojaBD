from model import connection as conexao

class Fornecedor(object):
    '''
    classdocs
    '''


    def __init__(self, fornecedor):
        '''
        Constructor    
        '''
        self.fornecedor = fornecedor
    
    def procIADFornecedor(self, operacao):
        procValores = (operacao, self.fornecedor.cnpj, self.fornecedor.nome, 
                       self.fornecedor.email, self.fornecedor.rua, self.fornecedor.numero,
                       self.fornecedor.bairro, self.fornecedor.cidade)
        
        conexao = conexao.Connection()
        conexao.callProCedure(self, "insere_atualiza_deleta_fornecedor" , procValores)
        conexao.close()