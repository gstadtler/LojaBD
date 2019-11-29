from model import connection as conexao

def checaUsuário(email, senha):
    param = (email, senha)
    conexao = conexao.Connection()
    conexao.execute( "SELECT cpf, nome , email, senha, flagGerente FROM funcionario WHERE email = %s AND senha = %s" , param)
    ret = conexao.cur.fetchone()
    conexao.close()
    
    return ret