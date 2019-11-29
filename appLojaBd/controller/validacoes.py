'''
Arquivo de validações genéricas para os demais objetos
'''

def validaNome(nome):
    if nome == "":
        print("Nome em branco!")
        break
    elif nome.isalpha() == False:
        print("Nome só pode conter letras!")
        break  
    elif len(nome) > 20:
        print("Nome possui mais de 20 caracteres!")
        break
        
def validaEmail(email):
    if email == "":
        print("E-Mail em branco!")
        break
    elif len(email) > 30:
        print("E-Mail possui mais de 30 caracteres!")
        break
    
def validaCpf(cpf):
    if cpf == "":
        print("CPF em branco!")
        break
    elif cpf.isdigit() == False:
        print("CPF só pode conter numeros!")
        break
    elif len(cpf) > 11:
        print("CPF possui mais de 11 digitos!")
        break
        
def validaCnpj(cnpj):
    if cnpj == "":
        print("CNPJ em branco!")
        break
    elif cnpj.isdigit() == False:
        print("CNPJ só pode conter numeros!")
        break
    elif len(cnpj) > 14:
        print("CNPJ possui mais de 14 digitos!")
        break