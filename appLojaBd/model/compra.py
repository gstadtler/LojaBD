import psycopg2
from model import connection as conex
import pandas as pd
from tabulate import tabulate
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)

class Compra(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def insereCompra(self, compra):
        try:        
            procValores = (compra.cnpjFornecedor, compra.dataCompra, compra.valorTotal)
            conexao = conex.Connection()
            conexao.callProCedure("insere_compra" , procValores)
            codCompra = conexao.cur.fetchone()
            
            procValores = None
            for produto in compra.produtosCompra:
                procValores = (codCompra, codCompra, produto.qtd_estoque)
                conexao.execute('INSERT INTO compra_produto(id_produto_produto, id_entrada_compra, quantidade) VALUES(%s,%s,%s)', procValores)
                
            conexao.commit()
            print("Operação concluida!")
        except (Exception, psycopg2.DatabaseError) as error:
            conexao.rollBack()
            print(error)
        finally:
            if conexao is not None:
                conexao.close()
    
    def retornaCompras(self):
        conexao = conex.Connection()
        print('')
        conexao.query('SELECT * FROM compra_entrada')
        conexao.queryResult()
        conexao.close()

    def relatComprasPeriodo(self, dataInicial, dataFinal):
        conexao = conex.Connection()
        params = (dataInicial, dataFinal)
        conexao.execute('''SELECT * FROM compra_entrada 
                            WHERE data_compra BETWEEN %s 
                            AND %s ''', params)
        conexao.queryResult()
        conexao.close()
    
    def relatComprasFornecedorPeriodo(self, dataInicial, dataFinal, cnpjFornecedor):
        conexao = conex.Connection()
        params = (cnpjFornecedor, dataInicial, dataFinal)
        conexao.execute('''SELECT * FROM compra_entrada 
                            WHERE cnpj_fornecedor = %s
                            AND data_compra BETWEEN %s 
                            AND %s''', params)
        conexao.queryResult()
        conexao.close()