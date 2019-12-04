from model import connection as conex
import pandas as pd
from tabulate import tabulate
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)

class Gerente(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def verificaSupervisionados(self, cpfGerente):
        conexao = conex.Connection()
        print('')
        
        data = pd.read_sql('''SELECT "verifica_supervisionados"(%(cpfGerente)s);''', conexao.conn, 
                            params={"cpfGerente":cpfGerente})        
        data = data.rename({"verifica_supervisionados":"(CPF,Nome)"}, axis='columns')
        
        print('')
        print(tabulate(data, showindex=False, headers=data.columns, numalign="left"))
        conexao.close()
        
    def retornaGerentes(self):
        conexao = conex.Connection()
        print('')
        conexao.query('SELECT * FROM gerente')
        conexao.queryResult()
        conexao.close()    