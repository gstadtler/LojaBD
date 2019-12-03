import psycopg2
from model import connection as conex
import pandas as pd
from tabulate import tabulate
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)

class Produto(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def procIADProduto(self, produto, operacao):
        conexao = conex.Connection()
        
        if operacao == "I":
            conexao.callProCedure("get_lastId_produto",())
            codProd = conexao.cur.fetchone()
            conexao.close()
        else:
            codProd = produto.id
        
        procValores = (operacao, codProd, produto.nome, 
                       produto.preco_venda, produto.preco_compra, produto.qtd_estoque)
        try:
            conexao.callProCedure("insere_atualiza_deleta_produto" , procValores)
            conexao.commit()
            print("Operação concluida!")
        except psycopg2.errors.lookup("23503"):
            conexao.rollBack()
            print("Não será possivel excluir este produto.")
            print("Produto associado a uma compra ou venda.")
        finally:
            if conexao is not None:
                conexao.close()
        
    def recuperaDados(self, idProduto):
        param = (idProduto,)
        conexao = conex.Connection()
        conexao.execute( '''SELECT nome, preco_venda, preco_compra, qtd_estoque 
                            FROM produto WHERE id_produto = %s ''' , param)
        ret = conexao.cur.fetchone()
        conexao.close()
        return ret
    
    def retornaProdutos(self):
        conexao = conex.Connection()
        print("")
        data = pd.read_sql('SELECT * FROM produto', conexao.conn)
        data = data.rename({"id_produto":"ID","nome":"Nome",
                            "preco_venda":"Preço Venda","preco_compra":"Preço Compra",
                            "qtd_estoque":"Quantidade"}, axis='columns')
        
        print("")
        print(tabulate(data, showindex=False, headers=data.columns, numalign="left"))
        conexao.close()
                
    def relatProdutosVendidos(self, params): 
        conexao = conex.Connection()
        print('')
        data = pd.read_sql('''SELECT vp.id_produto_produto, p.nome, sum(vp.quantidade) AS qtd_total
                            FROM venda_produto AS vp
                            INNER JOIN produto AS p ON ( p.id_produto = vp.id_produto_produto )
                            GROUP BY vp.id_produto_produto, p.nome
                            ORDER BY
                            qtd_total '''+params[0]+" LIMIT "+params[1]+" ", conexao.conn)
        
        data = data.rename({"id_produto_produto":"ID","nome":"Nome",
                            "qtd_total":"Total"}, axis='columns')
        print("")
        print(tabulate(data, showindex=False, headers=data.columns, numalign="left"))
        conexao.close()
