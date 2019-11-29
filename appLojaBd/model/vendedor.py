from model import connection as conexao

class Vendedor(object):
    '''
    classdocs
    '''


    def __init__(self, vendedor):
        '''
        Constructor
        '''
        self.vendedor = vendedor
    
    def verificaMeta(self, procValores):
        conexao = conexao.Connection()
        conexao.callProCedure(self, "verifica_meta_vendedor" , procValores)
        ret = conexao.cur.fetchone()
        conexao.close()
        return ret