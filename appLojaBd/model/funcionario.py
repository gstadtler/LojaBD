import psycopg2
from model import connection as conex
import pandas as pd
from tabulate import tabulate
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)

class Funcionario(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def procIADFuncionario(self, funcionario, operacao, cpfGerente):
        procValores = (operacao, cpfGerente, funcionario.cpf, funcionario.nome, 
                       funcionario.email, funcionario.senha, funcionario.flagGerente)
        
        conexao = conex.Connection()
        try:
            conexao.callProCedure("insere_atualiza_deleta_funcionario" , procValores)
            conexao.commit()
            print("Operação concluida!")
        except (Exception, psycopg2.DatabaseError) as error:
            conexao.rollBack()
            print(error)
        finally:
            if conexao is not None:
                conexao.close()
                
        
    def verificaGerente(self, cpf):
        conexao = conex.Connection()
        param = (cpf,)
        conexao.execute('SELECT flagGerente FROM funcionario WHERE cpf = %s', param)
        ret = conexao.cur.fetchone()
        ret = ret[0]
        conexao.close()
        return ret
    
    def verificaFuncionario(self, cpf):
        conexao = conex.Connection()
        param = (cpf,)
        conexao.execute('SELECT cpf FROM funcionario WHERE cpf = %s', param)
        ret = conexao.cur.fetchone()
        conexao.close()
        return ret
    
    def recuperaDados(self, cpf):
        conexao = conex.Connection()
        param = (cpf,)
        conexao.execute('SELECT nome, email, senha, flaggerente FROM funcionario WHERE cpf = %s', param)
        ret = conexao.cur.fetchone()
        conexao.close()
        return ret
    
    def retornaFuncionarios(self):
        conexao = conex.Connection()
        print('')
        data = pd.read_sql('SELECT cpf, nome, email, flaggerente FROM funcionario', conexao.conn)        
        data = data.rename({"cpf":"CPF","nome":"Nome",
                            "email":"E-Mail", "flaggerente":"Gerente?"}, axis='columns')
        
        print("")
        print(tabulate(data, showindex=False, headers=data.columns, numalign="left"))
        conexao.close()
        