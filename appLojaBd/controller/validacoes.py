'''
Arquivo de validações genéricas para os demais objetos
'''

def validaNome(nome):
    if nome == "":
        print("Nome em branco!")
    elif len(nome) > 20:
        print("Nome possui mais de 20 caracteres!")
        
def validaEmail(email):
    if email == "":
        print("E-Mail em branco!")
    elif len(email) > 30:
        print("E-Mail possui mais de 30 caracteres!")
    
def validaCpf(cpf):
    if cpf == "":
        print("CPF em branco!")
    elif len(cpf) > 11:
        print("CPF possui mais de 11 digitos!")
        
def validaCnpj(cnpj):
    if cnpj == "":
        print("CNPJ em branco!")
    elif len(cnpj) > 14:
        print("CNPJ possui mais de 14 digitos")

def validaPreco(venda, compra):
    if venda < compra:
        print("O preço de venda não deve ser menor que o preço de compra do produto")

def validaQtdEstoque(quantidade):
    if quantidade < 0:
        print("Quantidade de produtos inválida!")
    
    
    