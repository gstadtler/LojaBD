from controller.sessao import setUsuario
import getpass

def login():
    while not False:
        email = input("Email: ")
        senha = getpass.getpass(prompt='Senha: ', stream=None) 
        usuario = setUsuario(email, senha)
        if usuario != False:
            return usuario
       
usuario = None 
print("Bem vindo ao Akatsuki Vendas.")
print("Por favor, efetue o login.")
login()

print("Olá",usuario.nome,"Selecione a opção desejada: ")
print('''1 - Clientes
         2 - Fornecedores
         3 - Funcionarios
         4 - Produtos
         5 - Compras
         6 - Vendas''')
opcao = input("Opção: ")

