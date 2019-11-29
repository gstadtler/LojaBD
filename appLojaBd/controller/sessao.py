from model import sessao as session
from controller import funcionario as func

def setUsuario(email, senha):
    
    usuario = session.checaUsuário(email, senha)
    if usuario == ():
        print("Email ou senha incorreto!")
        break
    else:
        funcionario = func.Funcionario(*usuario)
    
    return funcionario