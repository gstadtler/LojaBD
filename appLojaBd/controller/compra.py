from datetime import datetime
from model.funcionario import Funcionario as modelFuncionario
from model.fornecedor import Fornecedor as modelFornecedor

class Compra(object):
    '''
    classdocs
    '''


    def __init__(self, cpfFuncionario, cnpjFornecedor):
        '''
        Constructor
        '''
        self.idSaida = 0
        self.cpfFuncionario = cpfFuncionario
        self.cnpjFornecedor = cnpjFornecedor
        self.dataCompra = datetime.now()
        self.valorTotal = 0
        self.produtosCompra = []
        self.mFornecedor = modelFornecedor()
        self.mFuncionario = modelFuncionario()
    
    def addProduto(self, produto):
        self.produtosCompra.append(produto)
    
    def delProduto(self, numProduto):
        try:
            del(self.produtosCompra[numProduto])
        except IndexError:
            print("Este produto não existe na lista de produtos!")
        
    def iniciaCompra(self):
        ret = self.mFuncionario.verificaFuncionario(self.cpfFuncionario)
        if ret == "":
            print("Funcionario não encontrado!")
            break
        ret = self.mFornecedor.VerificaFornecedor(self.cnpjFornecedor)
        if ret == "":
            print("Fornecedor não encontrado!")
            break
    
    def fechaCompra(self):
        pass