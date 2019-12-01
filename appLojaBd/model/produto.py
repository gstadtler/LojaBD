from model import connection as conexao
class Produto(object):
    '''
    classdocs
    '''


    def __init__(self, produto):
        '''
        Constructor
        '''
        self.produto = produto
    
    def procIADProduto(self, produto, operacao):
        procValores = (operacao, produto.id, produto.nome, 
                       produto.preco_venda, produto.preco_compra, produto.qtd_estoque)
        
        conexao = conexao.Connection()
        conexao.callProCedure(self, "insere_atualiza_deleta_produto" , procValores)
        conexao.close()
        
    def retornaProdutos(self):
        conexao = conexao.Connection()
        print('')
        conexao.query('SELECT * FROM produto')
        conexao.queryResult()
        conexao.close()