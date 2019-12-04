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
    
    def retornaVendedores(self):
        conexao = conex.Connection()
        print('')
        conexao.query('SELECT * FROM vendedor')
        conexao.queryResult()
        conexao.close()