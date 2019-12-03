from datetime import datetime
from controller.sessao import setUsuario
from controller.cliente import Cliente 
from controller.fornecedor import Fornecedor
from controller.funcionario import Funcionario
from controller.produto import Produto
from controller.compra import Compra
from controller.venda import Venda
import getpass
#from aifc import data

def menuLogin():
    while not False:
        email = input("Email: ")
        senha = getpass.getpass(prompt='Senha: ', stream=None) 
        usuario = setUsuario(email, senha)
        if usuario != False:
            return usuario
        
def edtIstDelCliente(op):
    nome = ""
    email = ""
    rua = "" 
    numero = ""
    bairro = "" 
    cidade = ""
    cpf = input("CPF: ")
    if op == "A" or op == "I":
        nome = input("Nome: ")
        email = input("E-Mail: ")
        rua = input("Rua: ") 
        numero = input("Numero: ")
        bairro = input("Bairro: ") 
        cidade = input("Cidade: ")
    cli = Cliente(cpf, nome, email, rua, numero, bairro, cidade)
    cli.operacaoCliente(op)   
    
def menuclientes():
    while not False:
        print('''Menu de Clientes:
                 1 - Listar clientes
                 2 - Cadastrar Clientes
                 3 - Voltar''')
        op = input("Opção: ")
        if op != "1" and op != "2" and op != "3":
            print("Opção inválida!")
        elif op == "1":
            cli = Cliente()
            cli.listaClientes()
            print('''
                     1 - Editar cliente
                     2 - Excluir Cliente
                     3 - Voltar''')
            op = input("Opção: ")
            if op != "1" and op != "2" and op != "3":
                print("Opção inválida!")    
            elif op == "1":
                print("Os Valores que não deseja editar, deixe vazio!")
                edtIstDelCliente("A")
            elif op == "2":
                edtIstDelCliente("D")
            elif op == "3":
                False
        elif op == "2":
            edtIstDelCliente("I")
        elif op == "3":
            return False
            
def edtIstDelFornecedor(op):
    nome = ""
    email = ""
    rua = "" 
    numero = ""
    bairro = "" 
    cidade = ""
    cnpj = input("CNPJ: ")
    if op == "A" or op == "I":
        nome = input("Nome: ")
        email = input("E-Mail: ")
        rua = input("Rua: ") 
        numero = input("Numero: ")
        bairro = input("Bairro: ") 
        cidade = input("Cidade: ")
    forn = Fornecedor(cnpj, nome, email, rua, numero, bairro, cidade)
    forn.operacaoFornecedor(op)
    
def menuFornecedores():
    while not False:
        print('''Menu de Fornecedores: 
                     1 - Listar Fornecedores 
                     2 - Cadastrar Fornecedores 
                     3 - Voltar''')
        op = input("Opção: ")
        if op != "1" and op != "2" and op != "3":
            print("Opção inválida!")
        elif op == "1":
            forn = Fornecedor()
            forn.listaFornecedores()
            print('''
                     1 - Editar Fornecedor
                     2 - Excluir Fornecedor
                     3 - Voltar''')
            op = input("Opção: ")
            if op != "1" and op != "2" and op != "3":
                print("Opção inválida!")    
            elif op == "1":
                print("Os Valores que não deseja editar, deixe vazio!")
                edtIstDelFornecedor("A")
            elif op == "2":
                edtIstDelFornecedor("D")
            elif op == "3":
                False
        elif op == "2":
            edtIstDelFornecedor("I")
        elif op == "3":
            return False
            
def edtIstDelFuncionario(op):
    nome = ""
    email = ""
    senha = ""
    flagGerente = False
    cpf = input("CPF: ")
    if op == "A" or op == "I":
        nome = input("Nome: ")
        email = input("E-Mail: ")
        senha = input("Senha: ")
        flagGerente = input("O funcionário é um gerente? S/N")
        if flagGerente == "S":
            flagGerente = True
    func = Funcionario(cpf, nome, email, senha, flagGerente)
    func.operacaoFuncionario(op)
    
def menuFuncionarios():
    while not False:
        print('''
                 1 - Listar Funcionários
                 2 - Cadastrar Funcionários''')
        op = input("Opção: ")
        if op != "1" and op != "2":
            print("Opção inválida!")
        elif op == "1":
            func = Funcionario()
            func.listaFuncionarios()
            print('''
                     1 - Editar Funcionário
                     2 - Excluir Funcionário''')
            op = input("Opção: ")
            if op != "1" and op != "2":
                print("Opção inválida!")    
            elif op == "1":
                print("Os Valores que não deseja editar, deixe vazio!")
                edtIstDelFuncionario("A")
            elif op == "2":
                edtIstDelFuncionario("D")
        elif op == "2":
            edtIstDelFuncionario("I")
            
def edtIstDelProduto(op):
    idProd = ""
    nome = ""
    precoVenda = ""
    precoCompra = ""
    qtdEstoque = ""
    if op == "A" or op == "D":
        idProd = input("ID do produto: ")   
    if op == "A" or op == "I":
        nome = input("Nome: ")
        precoVenda = input("Preço de Venda: ")
        precoCompra = input("Preço de Compra: ")
        qtdEstoque = input("Quantidade de Produtos: ")
    prod = Produto(idProd, nome, precoVenda, precoCompra, qtdEstoque)
    prod.operacaoProduto(op)
    
def menuProdutos():
    while not False:
        print('''Menu de produtos: 
                    1 - Listar Produtos
                    2 - Cadastrar Produtos
                    3 - Relatórios 
                    4 - Voltar''')
        op = input("Opção: ")
        if op != "1" and op != "2" and op != "3" and op != "4":
            print("Opção inválida!")
        elif op == "1":
            prod = Produto()
            prod.listaProdutos()
            print('''
                     1 - Editar Produto
                     2 - Excluir Produto 
                     3 - Voltar''')
            op = input("Opção: ")
            if op != "1" and op != "2" and op != "3":
                print("Opção inválida!")    
            elif op == "1":
                print("Os Valores que não deseja editar, deixe vazio!")
                edtIstDelProduto("A")
            elif op == "2":
                edtIstDelProduto("D")
            elif op == "3":
                False
        elif op == "2":
            edtIstDelProduto("I")
        elif op =="3":
            prod = Produto()
            print('''Relatórios:  
                    1 - Relatório de produtos mais vendidos
                    2 - Relatório de produtos menos vendidos 
                    3 - Voltar''')
            opRelatorio = input("Opção: ")
            if opRelatorio != "1" and opRelatorio != "2" and opRelatorio != "3":
                print("Opção inválida!")
            elif opRelatorio == "1":
                opLimite = input("Quantos produtos: ")
                prod.relatProdutos(1, opLimite)
            elif opRelatorio == "2":
                opLimite = input("Quantos produtos: ")
                prod.relatProdutos(2, opLimite)
            elif opRelatorio == "3":
                False
        elif op == "4":
            return False
                
def IstCompra():
    id_entrada = ""
    cnpjFornecedor = input("CNPJ do Fornecedor: ")
    data_compra = datetime.today().strftime('%Y-%m-%d')
    valor_total = input("Valor total da compra: ")
    compra = Compra(id_entrada, cnpjFornecedor, data_compra, valor_total)
    while not False:
        op = input('''1 - Adiciona Produto
                      2 - Fechar Compra''')
        nome = input("Nome: ")
        preco_venda = input("Preço de Venda: ")
        preco_compra = input("Preço de Compra: ")
        qtd_estoque = input("Quantidade de Produtos: ")
        prod = Produto("", nome, preco_venda, preco_compra, qtd_estoque)
        if op == '1':
            compra.addProduto(prod)
        elif op == '2':
            compra.fechaCompra()
            False
            
def menuCompras():
    while not False:
        print('''
                 1 - Listar Compras
                 2 - Cadastrar Compras
                 3 - Relatórios ''')
        op = input("Opção: ")
        if op != "1" and op != "2" and op != "3":
            print("Opção inválida!")
        elif op == "1":
            compra = Compra()
            compra.listaCompras()
        elif op == "2":
            IstCompra()
        elif op =="3":
            compra = Compra()
            print('''
                    1 - Relatório de compras por período
                    2 - Relatório de compras por período e fornecedor ''')
            opRelatorio = input("Opção: ")
            if opRelatorio != "1" and opRelatorio != "2":
                print("Opção inválida!")
            elif opRelatorio == "1":
                inicio = input("Data de início(ano-mes-dia): ")
                fim = input("Data do término(ano-mes-dia): ")
                compra.relatoriosCompras(1, inicio, fim)
            elif opRelatorio == "2":
                inicio = input("Data de início(ano-mes-dia): ")
                fim = input("Data do término(ano-mes-dia): ")
                cnpj_forn = input("CNPJ do fornecedor: ")
                compra.relatoriosCompras(2, inicio, fim, cnpj_forn)
                
def IstVenda():
    id_saida =""
    cpfFuncionario = input("CPF do Funcionário: ")
    cpf_cliente = input("CPF do Cliente: ")
    data_venda = datetime.today().strftime('%Y-%m-%d')
    valor_total = input("Valor total da compra: ")
    venda = Venda(id_saida, cpfFuncionario, cpf_cliente, data_venda, valor_total)
    
    
def menuVendas():
    while not False:
        print('''
                 1 - Listar Vendas
                 2 - Cadastrar Vendas
                 3 - Relatórios ''')
        op = input("Opção: ")
        if op != "1" and op != "2" and op != "3":
            print("Opção inválida!")
        elif op == "1":
            venda = Venda()
            venda.listaVendas()
        elif op == "2":
            IstVenda()
        elif op =="3":
            venda = Venda()
            print('''
                    1 - Relatório de vendas por período
                    2 - Relatório de vendas por período e funcionário
                    3 - Relatório de total de vendas por período e funcionário ''')
            opRelatorio = input("Opção: ")
            if opRelatorio != "1" and opRelatorio != "2" and opRelatorio != "3":
                print("Opção inválida!")
            elif opRelatorio == "1":
                inicio = input("Data de início(ano-mes-dia): ")
                fim = input("Data do término(ano-mes-dia): ")
                venda.relatoriosVendas(1, inicio, fim)
            elif opRelatorio == "2":
                inicio = input("Data de início(ano-mes-dia): ")
                fim = input("Data do término(ano-mes-dia): ")
                cpf_func = input("CPF do funcionário: ")
                venda.relatoriosVendas(2, inicio, fim, cpf_func)
            elif opRelatorio == "3":
                inicio = input("Data de início(ano-mes-dia): ")
                fim = input("Data do término(ano-mes-dia): ")
                cpf_func = input("CPF do funcionário: ")
                venda.relatoriosVendas(3, inicio, fim, cpf_func)

print("Bem vindo ao Akatsuki Vendas.")
print("Por favor, efetue o login.")

''' Descomentar Após testes!
usuario = menuLogin()
print("Olá",usuario.nome,"Selecione a opção desejada: ") 
'''
while not False:
    print('''Menu Inicial:
             1 - Clientes
             2 - Fornecedores
             3 - Funcionarios
             4 - Produtos 
             5 - Compras 
             6 - Vendas''')
    opcao = input("Opção: ")
    
    if opcao == "1":
        menuclientes()
    elif opcao == "2":
        menuFornecedores()
    elif opcao == "3":
        menuFuncionarios()
    elif opcao == "4":
        menuProdutos()
    elif opcao == "5":
        menuCompras()
    elif opcao == "6":
        menuVendas()
    else:
        print("Opção inválida!")
