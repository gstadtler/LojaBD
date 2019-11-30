from model import connection as conexao
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
            procValores = (venda.cpfFuncionario, venda.cpfCliente, venda.dataVenda)
            conexao = conexao.Connection()
            conexao.callProCedure(self, "insere_venda" , procValores)
            codVenda = conexao.cur.fetchone()
            
            procValores = None
            for produto in venda.produtosVenda:
                procValores = (produto.id, codVenda, produto.quantidade)
                conexao.execute('INSERT INTO venda_produto(id_produto_produto, id_saida_venda, quantidade) VALUES(%s,%s,%s)', procValores)
                
            conexao.commit()
        except (Exception, conexao.psycopg2.DatabaseError) as error:
            conexao.rollback()
            print(error)
        finally:
            if conexao is not None:
                conexao.close()