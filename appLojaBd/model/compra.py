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
        self.conexCompra = conex.Connection()
        
    def abreCompra(self, compra):
        procValores = (compra.cnpjFornecedor, compra.dataCompra, compra.valorTotal)
        self.conexCompra.callProCedure("insere_compra" , procValores)
        codCompra = self.conexCompra.cur.fetchone()
        return codCompra
    
    def fechaCompra(self, compra):
        try:                    
            procValores = None
            for produto in compra.produtosCompra:
                procValores = (produto.id, compra.idEntrada, produto.qtd_estoque)
                self.conexCompra.execute('INSERT INTO compra_produto(id_produto_produto, id_entrada_compra, quantidade) VALUES(%s,%s,%s)', procValores)
                
            self.conexCompra.commit()
            print("Operação concluida!")
        except (Exception, psycopg2.DatabaseError) as error:
            self.conexCompra.rollBack()
            print(error)
        finally:
            if self.conexCompra is not None:
                self.conexCompra.close()
        
    def insereCompra(self, compra):
        try:        
            procValores = (compra.cnpjFornecedor, compra.dataCompra, compra.valorTotal)
            conexao = conex.Connection()
            conexao.callProCedure("insere_compra" , procValores)
            codCompra = conexao.cur.fetchone()
            
            procValores = None
            for produto in compra.produtosCompra:
                procValores = (produto.id, codCompra, produto.qtd_estoque)
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
        data = pd.read_sql('''SELECT id_entrada, cnpj_fornecedor, 
                              data_compra, CAST(valor_total AS MONEY) FROM compra_entrada''', conexao.conn)        
        data = data.rename({"id_entrada":"ID", "cnpj_fornecedor":"CNPJ Fornecedor",
                            "data_compra":"Data", "valor_total":"Total"}, axis='columns')
        
        print('')
        print(tabulate(data, showindex=False, headers=data.columns, numalign="left"))
        conexao.close()
        
    def retornaCompraProdutos(self, idCompra):
        conexao = conex.Connection()
        print('')
        data = pd.read_sql('''SELECT p.nome, cp.quantidade, CAST(p.preco_compra AS MONEY), 
                                CAST((cp.quantidade * p.preco_compra) AS MONEY) as total 
                              FROM compra_produto cp  
                              INNER JOIN produto p ON p.id_produto = cp.id_produto_produto 
                              WHERE cp.id_entrada_compra = '''+idCompra+" ", conexao.conn)        
        data = data.rename({"nome":"NOME","quantidade":"Quantidade",
                            "preco_compra":"Preço Unit.","total":"Total"}, axis='columns')
        
        print('')
        print(tabulate(data, showindex=False, headers=data.columns, numalign="left"))
        conexao.close() 

    def relatComprasPeriodo(self, dataInicial, dataFinal):
        conexao = conex.Connection()
        print('')
        
        data = pd.read_sql('''SELECT id_entrada, cnpj_fornecedor, 
                              data_compra, CAST(valor_total AS MONEY) FROM compra_entrada  
                              WHERE data_compra BETWEEN %(dinicio)s AND %(dfin)s ''', conexao.conn, 
                            params={"dinicio":pd.to_datetime(dataInicial, format='%Y-%m-%d'), 
                                    "dfin":pd.to_datetime(dataFinal, format='%Y-%m-%d')})        
        data = data.rename({"id_entrada":"ID", "cnpj_fornecedor":"CNPJ Fornecedor",
                            "data_compra":"Data", "valor_total":"Total"}, axis='columns')
        
        print('')
        print(tabulate(data, showindex=False, headers=data.columns, numalign="left"))
        conexao.close()
        
    
    def relatComprasFornecedorPeriodo(self, dataInicial, dataFinal, cnpjFornecedor):
        conexao = conex.Connection()
        print('')
        
        data = pd.read_sql('''SELECT id_entrada, cnpj_fornecedor, 
                              data_compra, CAST(valor_total AS MONEY) FROM compra_entrada  
                              WHERE data_compra BETWEEN %(dinicio)s AND %(dfin)s  
                              AND cnpj_fornecedor = %(cpfForn)s ''', conexao.conn, 
                            params={"dinicio":pd.to_datetime(dataInicial, format='%Y-%m-%d'), 
                                    "dfin":pd.to_datetime(dataFinal, format='%Y-%m-%d'), 
                                    "cpfForn":cnpjFornecedor})        
        data = data.rename({"id_entrada":"ID", "cnpj_fornecedor":"CNPJ Fornecedor",
                            "data_compra":"Data", "valor_total":"Total"}, axis='columns')
        
        print('')
        print(tabulate(data, showindex=False, headers=data.columns, numalign="left"))
        conexao.close()