import psycopg2
from model import connection as conex
import pandas as pd
from tabulate import tabulate
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)

class Venda(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def insereVenda(self, venda):
        try:        
            procValores = (venda.cpfFuncionario, venda.cpfCliente, venda.dataVenda, venda.valorTotal)
            conexao = conex.Connection()
            conexao.callProCedure("insere_venda" , procValores)
            codVenda = conexao.cur.fetchone()
            
            procValores = None
            for produto in venda.produtosVenda:
                procValores = (produto.id, codVenda, produto.quantidade)
                conexao.execute('''INSERT INTO venda_produto(id_produto_produto, id_saida_venda, quantidade) 
                                    VALUES(%s,%s,%s)''', procValores)
                
            conexao.commit()
            print("Operação concluida!")
        except (Exception, psycopg2.DatabaseError) as error:
            conexao.rollBack()
            print(error)
        finally:
            if conexao is not None:
                conexao.close()
                
    def retornaVendas(self):
        conexao = conex.Connection()
        print('2')
        data = pd.read_sql('SELECT * FROM venda', conexao.conn)        
        data = data.rename({"id_saida":"ID","cpf_funcionario_venda":"CPF Funcionario",
                            "cpf_cliente_venda":"CPF Cliente", "data_venda":"Data", 
                            "valor_total":"Total"}, axis='columns')
        
        print('')
        print(tabulate(data, showindex=False, headers=data.columns, numalign="left"))
        conexao.close()
        
    def retornaVendaProdutos(self, idVenda):
        conexao = conex.Connection()
        print('')
        data = pd.read_sql('''SELECT p.nome, vp.quantidade, (vp.quantidade * p.preco_venda) as total 
                              FROM venda_produto vp  
                              INNER JOIN produto p ON p.id_produto = vp.id_produto_produto 
                              WHERE vp.id_saida_venda = '''+idVenda+" ", conexao.conn)        
        data = data.rename({"nome":"NOME","quantidade":"Quantidade",
                            "total":"Total"}, axis='columns')
        
        print('')
        print(tabulate(data, showindex=False, headers=data.columns, numalign="left"))
        conexao.close()     
            
    def relatVendasPeriodo(self, dataInicial, dataFinal):
        conexao = conex.Connection()
        print('')
        
        data = pd.read_sql('''SELECT * FROM venda 
                              WHERE data_venda BETWEEN %(dinicio)s AND %(dfin)s ''', conexao.conn, 
                            params={"dinicio":pd.to_datetime(dataInicial, format='%Y-%m-%d'), 
                                    "dfin":pd.to_datetime(dataFinal, format='%Y-%m-%d')})        
        data = data.rename({"id_saida":"ID","cpf_funcionario_venda":"CPF Funcionario",
                            "cpf_cliente_venda":"CPF Cliente", "data_venda":"Data", 
                            "valor_total":"Total"}, axis='columns')
        
        print('')
        print(tabulate(data, showindex=False, headers=data.columns, numalign="left"))
        conexao.close()
            
    def relatVendasFuncionarioPeriodo(self, dataInicial, dataFinal, cpfFuncionario):
        conexao = conex.Connection()
        print('')
        
        data = pd.read_sql('''SELECT * FROM venda 
                              WHERE data_venda BETWEEN %(dinicio)s AND %(dfin)s 
                              AND cpf_funcionario_venda = %(cpfFunc)s ''', conexao.conn, 
                            params={"dinicio":pd.to_datetime(dataInicial, format='%Y-%m-%d'), 
                                    "dfin":pd.to_datetime(dataFinal, format='%Y-%m-%d'), 
                                    "cpfFunc":cpfFuncionario})        
        data = data.rename({"id_saida":"ID","cpf_funcionario_venda":"CPF Funcionario",
                            "cpf_cliente_venda":"CPF Cliente", "data_venda":"Data", 
                            "valor_total":"Total"}, axis='columns')
        
        print('')
        print(tabulate(data, showindex=False, headers=data.columns, numalign="left"))
        conexao.close()

    def relTotVendasFuncionarioPeriodo(self, dataInicial, dataFinal, cpfFuncionario):
        conexao = conex.Connection()
        print('')
        
        data = pd.read_sql('''SELECT f.nome, SUM(v.valor_total) AS total FROM venda v 
                              INNER JOIN funcionario f ON f.cpf = v.cpf_funcionario_venda
                              WHERE v.data_venda BETWEEN %(dinicio)s AND %(dfin)s 
                              AND v.cpf_funcionario_venda = %(cpfFunc)s 
                              GROUP BY f.nome, v.cpf_funcionario_venda''', conexao.conn, 
                            params={"dinicio":pd.to_datetime(dataInicial, format='%Y-%m-%d'), 
                                    "dfin":pd.to_datetime(dataFinal, format='%Y-%m-%d'), 
                                    "cpfFunc":cpfFuncionario})        
        data = data.rename({"nome":"Nome","total":"Total"}, axis='columns')
        
        print('')
        print(tabulate(data, showindex=False, headers=data.columns, numalign="left"))
        conexao.close()            