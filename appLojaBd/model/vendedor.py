import psycopg2
from model import connection as conex
from tabulate import tabulate
import pandas as pd
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)

class Vendedor(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def verificaMeta(self, procValores):
        conexao = conex.Connection()
        conexao.callProCedure("verifica_meta_vendedor" , procValores)
        ret = conexao.cur.fetchone()
        conexao.close()
        return ret
    
    def verificaSupervisor(self, cpfVendedor):
        conexao = conex.Connection()
        print('')
        
        data = pd.read_sql('''SELECT "verifica_supervisor"(%(cpfVendedor)s);''', conexao.conn, 
                            params={"cpfVendedor":cpfVendedor})        
        data = data.rename({"verifica_supervisor":"(CPF,Nome)"}, axis='columns')
        
        print('')
        print(tabulate(data, showindex=False, headers=data.columns, numalign="left"))
        conexao.close()
        
    def editarMeta(self, meta, cpfVendedor):
        try:
            conexao = conex.Connection()
            param = (meta, cpfVendedor)
            conexao.execute('UPDATE vendedor SET meta = %s WHERE cpf = %s ', param)
            conexao.commit()
            print("Operação concluida!")
        except (Exception, psycopg2.DatabaseError) as error:
            conexao.rollBack()
            print(error)
        finally:
            if conexao is not None:
                conexao.close()
    
    def retornaVendedores(self):
        conexao = conex.Connection()
        print('')
        conexao.query('SELECT * FROM vendedor')
        conexao.queryResult()
        conexao.close()
        
    def retornaMeta(self, cpfVendedor):
        conexao = conex.Connection()
        print('')
        
        data = pd.read_sql('''SELECT v.cpf, f.nome, CAST(v.meta AS MONEY) FROM vendedor v
                              INNER JOIN funcionario f ON f.cpf = v.cpf
                              WHERE v.cpf = %(cpfVendedor)s;''', conexao.conn, 
                            params={"cpfVendedor":cpfVendedor})        
        data = data.rename({"cpf":"CPF", "nome":"Nome", "meta":"Meta"}, axis='columns')
        
        print('')
        print(tabulate(data, showindex=False, headers=data.columns, numalign="left"))
        conexao.close()