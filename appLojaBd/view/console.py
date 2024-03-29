import os
import sys
import time
from datetime import datetime
from controller.sessao import setUsuario
from controller.cliente import Cliente 
from controller.fornecedor import Fornecedor
from controller.funcionario import Funcionario
from controller.produto import Produto
from controller.compra import Compra
from controller.venda import Venda
import getpass
from controller.vendedor import Vendedor
from controller.gerente import Gerente

def limparTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def menuLogin():
    print('''
    1 - Efetuar Login  
    2 - Fechar Programa ''')
    op = input("Operação: ")
    if op != "1" and op != "2":
        limparTerminal()
        print("Operação inválida!")
        return False
    elif op == "1":
        while not False:
            # descomentar após teste
            email = input("Email: ")
            senha = getpass.getpass(prompt='Senha: ', stream=None) 
            
            #gerente
            #email = "regis@funcionario.com"
            #senha = "4321regis"
            
            #vendedor
            #email = "gustavo@funcionario.com"
            #senha = "4321gustavo"
            usuario = setUsuario(email, senha)
            if usuario != False:
                return usuario
    elif op == "2":
        sys.exit()
        
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
                False   
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
            # limparTerminal()
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
                False    
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
            
def edtIstDelFuncionario(op, usuario):
    nome = ""
    email = ""
    senha = ""
    flagGerente = False
    cpfGerente = usuario.cpf
    cpf = input("CPF: ")
    if op == "A" or op == "I":
        nome = input("Nome: ")
        email = input("E-Mail: ")
        senha = input("Senha: ")
        flagGerente = input("O funcionário é um gerente? (s/n) ")
        flagGerente = flagGerente.lower()
        if flagGerente == "s":
            flagGerente = True
    func = Funcionario(cpf, nome, email, senha, flagGerente)
    func.operacaoFuncionario(op, cpfGerente)
    
def menuFuncionarios(usuario):
    while not False:
        print('''Menu de Funcionarios: 
                     1 - Listar Funcionários
                     2 - Cadastrar Funcionários 
                     3 - Voltar''')
        op = input("Opção: ")
        if op != "1" and op != "2" and op != "3":
            print("Opção inválida!")
            False
        elif op == "1":
            func = Funcionario()
            func.listaFuncionarios()
            print('''
                     1 - Editar Funcionário
                     2 - Ver Meta do Funcionario
                     3 - Excluir Funcionário 
                     4 - Voltar''')
            op = input("Opção: ")
            if op != "1" and op != "2" and op != "3" and op != "4":
                print("Opção inválida!")
                False   
            elif op == "1":
                print("Os Valores que não deseja editar, deixe vazio!")
                edtIstDelFuncionario("A", usuario)
            elif op == "2":
                vCpf = input("CPF: ")
                vend = Vendedor(vCpf,"","","",False, 0)
                vend.exibeMeta()
                print('''
                     1 - Editar Meta
                     2 - Voltar''')
                op = input("Opção: ")
                if op != "1" and op != "2":
                    print("Opção inválida!")
                    False
                elif op == "1":
                    vMeta = input("Meta: ")
                    vend.meta = vMeta
                    vend.editaMeta()
                elif op == "2":
                    False
            elif op == "3":
                edtIstDelFuncionario("D")
            elif op == "4":
                False
        elif op == "2":
            edtIstDelFuncionario("I")
        elif op == "3":
            return False
            
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
                    2 - Relatórios
                    3 - Voltar ''')
        op = input("Opção: ")
        if op != "1" and op != "2" and op != "3":
            print("Opção inválida!")
            False
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
        elif op =="2":
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
        elif op == "3":
            return False
                
def IstCompra():
    id_entrada = 0
    cnpjFornecedor = input("CNPJ do Fornecedor: ")
    data_compra = datetime.today().strftime('%Y-%m-%d')
    valor_total = input("Valor total da compra: ")
    compra = Compra(cnpjFornecedor, id_entrada, data_compra, valor_total)
    compra.idEntrada = compra.abreCompra()
    prodLista = Produto()
    prodLista.listaProdutos()
    while not False:
        codProd = compra.idEntrada -1
        print('''
                 1 - Adiciona Produto
                 2 - Finalizar Compra
                 3 - Cancelar Compra ''')
        op = input("Opção: ")
        if op == "1":
            opLista = input("O produto está na lista? (s/n) ")
            if opLista == "s":
                idProd = input("ID do Produto: ")
                dadosProduto = prodLista.buscaProduto(idProd)
                produto = Produto(*dadosProduto)
                quantidade = input("Quantidade de Produtos: ")
                produto.quantidade = quantidade
                compra.addProduto(produto)
                False
            elif opLista == "n":
                nome = input("Nome: ")
                preco_compra = input("Preço da Compra: ")
                preco_venda = input("Preço para Venda: ")
                qtd_estoque = input("Quantidade de Produtos: ")
                prod = Produto(0, nome, preco_venda, preco_compra, qtd_estoque)
                prod.quantidade = qtd_estoque
                # recuperar o id do produto inserido para add na lista
                codProd = codProd +1
                prod.id = codProd
                prod.operacaoProduto("I")
                compra.addProduto(prod)
                False
            else:
                False
                
        elif op == "2":
            compra.fechaCompra()
            return False
        elif op == "3":
            return False
            
def menuCompras():
    while not False:
        print('''
                 1 - Listar Compras
                 2 - Cadastrar Compras
                 3 - Relatórios 
                 4 - Voltar ''')
        op = input("Opção: ")
        if op != "1" and op != "2" and op != "3" and op != "4":
            print("Opção inválida!")
            False
        elif op == "1":
            compra = Compra("")
            compra.listaCompras()
            print('''
                     1 - Listar Produtos da Compra
                     2 - Voltar''')
            op = input("Opção: ")
            if op != "1" and op != "2":
                print("Opção inválida!")
                False  
            elif op == "1":
                idCompra = input("ID da compra: ")
                compra.listaCompraProdutos(idCompra)
                print(''' 
                        1 - Voltar ''')
                op = input("Opção: ")
                if op != "1":
                    print("Opção inválida!")
                else:
                    False
            elif op == "2":
                False  
        elif op == "2":
            IstCompra()
        elif op =="3":
            compra = Compra("")
            print('''
                    1 - Relatório de compras por período
                    2 - Relatório de compras por período e fornecedor
                    3 - Voltar ''')
            opRelatorio = input("Opção: ")
            if opRelatorio != "1" and opRelatorio != "2" and opRelatorio != "3":
                print("Opção inválida!")
            elif opRelatorio == "1":
                inicio = input("Data de início(ano-mes-dia): ")
                fim = input("Data do término(ano-mes-dia): ")
                compra.relatoriosCompras(1, (inicio,fim))
            elif opRelatorio == "2":
                inicio = input("Data de início(ano-mes-dia): ")
                fim = input("Data do término(ano-mes-dia): ")
                cnpj_forn = input("CNPJ do fornecedor: ")
                compra.relatoriosCompras(2, (inicio,fim,cnpj_forn))
            elif opRelatorio == "3":
                False
        elif op == "4":
            return False
        
def IstVenda(usuario):
    cpf_cliente = input("CPF do Cliente: ")
    venda = Venda()
    venda.cpfFuncionario = usuario.cpf
    venda.cpfCliente = cpf_cliente
    venda.iniciaVenda(usuario.cpf, cpf_cliente)
    return venda
    
    
def menuVendas(usuario):
    while not False:
        print('''Menu de Vendas: 
                1 - Listar Vendas 
                2 - Cadastrar Vendas 
                3 - Relatórios 
                4 - Voltar ''')
        op = input("Opção: ")
        if op != "1" and op != "2" and op != "3" and op != "4":
            print("Opção inválida!")
        elif op == "1" or op == "3":
            venda = Venda()
            
        if op == "1":
            venda.listaVendas()
            print('''
                     1 - Listar Produtos da Venda
                     2 - Voltar''')
            op = input("Opção: ")
            if op != "1" and op != "2":
                print("Opção inválida!")
                False    
            elif op == "1":
                idVenda = input("ID da venda: ")
                venda.listaVendaProdutos(idVenda)
                print(''' 
                        1 - Voltar ''')
                op = input("Opção: ")
                if op != "1":
                    print("Opção inválida!")
                else:
                    False
            elif op == "2":
                False
        elif op == "2":
            venda = IstVenda(usuario)
            prodLista = Produto()
            prodLista.listaProdutos()
            lacoVenda = True
            while lacoVenda == True:
                print('''
                        1 - Adicionar Produto
                        2 - Remover Produto
                        3 - Fechar Venda
                        4 - Cancelar Venda ''')
                op = input("Opção: ")
                if op == "1":
                    lacoProd = True
                    while lacoProd == True:
                        idProd = input("ID do Produto: ")
                        dadosProduto = prodLista.buscaProduto(idProd)
                        produto = Produto(*dadosProduto)
                        valida = True
                        while valida == True:
                            quantidade = int(input("Quantidade: "))
                            produto.quantidade = quantidade
                            if produto.validaQtdEstoqueVenda() == True: 
                                venda.addProduto(produto)
                                valida = False
                        sair = input("Deseja inserir outro? (s/n) ")
                        sair = sair.lower()
                        if sair == "s":
                            lacoProd = True
                        else:
                            lacoProd = False
                elif op =="2":
                    pass
                elif op == "3":
                    venda.fechaVenda()
                    lacoVenda = False
                elif op == "4":
                    del(venda)
                    lacoVenda = False
                    False
        elif op =="3":
            print('''
                    1 - Relatório de vendas por período
                    2 - Relatório de vendas por período e funcionário
                    3 - Relatório de total de vendas por período e funcionário 
                    4 - Voltar ''')
            opRelatorio = input("Opção: ")
            if opRelatorio != "1" and opRelatorio != "2" and opRelatorio != "3" and opRelatorio != "4":
                print("Opção inválida!")
                False
            
            inicio = input("Data de início(ano-mes-dia): ")
            fim = input("Data do término(ano-mes-dia): ")   
            if opRelatorio == "1":
                params = (inicio, fim)
                venda.relatoriosVendas(1, params)
            elif opRelatorio == "2":
                cpfFunc = input("CPF do funcionário: ")
                params = (inicio, fim, cpfFunc)
                venda.relatoriosVendas(2, params)
            elif opRelatorio == "3":
                cpfFunc = input("CPF do funcionário: ")
                params = (inicio, fim, cpfFunc)
                venda.relatoriosVendas(3, params)
            elif opRelatorio == "4":
                False
        elif op == "4":
            return False
        
def menuSupervisionamento(tagGerente, usuario):
    while not False:
        if tagGerente == True:
            print('''Menu Supervisionamento:
                       1 - Listar Supervisionados
                       2 - Voltar''')
        else:
            print('''Menu Supervisionamento:
                       1 - Listar Supervisor
                       2 - Verificar Meta
                       3 - Voltar''')    
        op = input("Opção: ")
        if op != "1" and op != "2" and op!= "3":
            print("Opção inválida!")
            False
        
        elif op == "1":
            if tagGerente == True:
                ger = Gerente(usuario.cpf, usuario.nome, usuario.email)
                ger.listaSupervisionados()
            else:
                vend = Vendedor(usuario.cpf, usuario.nome, usuario.email)
                vend.verificaSupervisor()
            print('''
                     1 - Voltar''')
            op = input("Opção: ")
            if op != "1":
                print("Opção inválida!")
                False    
            elif op == "1":
                False
        elif op == "2":
            if tagGerente == True:
                return False
            else:
                vend = Vendedor(usuario.cpf, usuario.nome, usuario.email)
                mes = input("Mês: ")
                ano = input("Ano: ")
                vend.verificaMeta(mes, ano)
        elif op == "3":
            return False
def menuPrincipal(): 
    while not False:           
        print("Bem vindo ao Akatsuki Vendas.")
        print("Por favor, selecione a opção desejada.")
        usuario = menuLogin()
        if usuario != False:
            print("Olá",usuario.nome,"Selecione a opção desejada: ") 
            logado = True
        else:
            logado = False
        while logado == True:
            print('''Menu Inicial:
                     1 - Clientes
                     2 - Fornecedores
                     3 - Funcionarios
                     4 - Produtos 
                     5 - Compras 
                     6 - Vendas
                     7 - Supervisionamento
                     8 - Sair ''')
            opcao = input("Opção: ")
            
            if opcao == "1":
                menuclientes()
            elif opcao == "2":
                menuFornecedores()
            elif opcao == "3":
                if usuario.validaCargo() == True:
                    menuFuncionarios(usuario)
                else:
                    print("Opção disponivel apenas para gerentes!")
                    False
            elif opcao == "4":
                menuProdutos()
            elif opcao == "5":
                menuCompras()
            elif opcao == "6":
                menuVendas(usuario)
            elif opcao == "7":
                if usuario.validaCargo() == True:
                    menuSupervisionamento(True, usuario)
                else:
                    menuSupervisionamento(False, usuario)
            elif opcao == "8":
                usuario = None
                logado = False
            else:
                print("Opção inválida!")
