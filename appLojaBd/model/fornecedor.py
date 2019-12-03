import psycopg2
from model import connection as conex
import pandas as pd
from tabulate import tabulate

class Fornecedor(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor    
        '''
    
    def procIADFornecedor(self, fornecedor, operacao):
        procValores = (operacao, fornecedor.cnpj, fornecedor.nome, 
                       fornecedor.email, fornecedor.rua, fornecedor.numero,
                       fornecedor.bairro, fornecedor.cidade)
        
        conexao = conex.Connection()
        try:
            conexao.callProCedure("insere_atualiza_deleta_fornecedor" , procValores)
            conexao.commit()
            print("Operação concluida!")
        except (Exception, psycopg2.DatabaseError) as error:
            conexao.rollBack()
            print(error)
        finally:
            if conexao is not None:
                conexao.close()
        
    def recuperaDados(self, cnpj):
        param = (cnpj,)
        conexao = conex.Connection()
        conexao.execute( '''SELECT nome, email, rua, numero,
                            bairro, cidade 
                            FROM fornecedor WHERE cnpj = %s ''' , param)
        ret = conexao.cur.fetchone()
        conexao.close()
        return ret
    
    def retornaFornecedores(self):
        conexao = conex.Connection()
        print('')
        data = pd.read_sql('SELECT * FROM fornecedor', conexao.conn)
        data = data.rename({"cnpj":"CNPJ","nome":"Nome",
                            "email":"E-Mail","rua":"Rua",
                            "numero":"Numero","bairro":"Bairro",
                            "cidade":"Cidade"}, axis='columns')
        
        print("")
        print(tabulate(data, showindex=False, headers=data.columns, numalign="left"))
        conexao.close()
        