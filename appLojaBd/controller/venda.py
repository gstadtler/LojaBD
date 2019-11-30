from datetime import datetime
from model.funcionario import Funcionario as modelFuncionario
from model.cliente import Cliente as modelCliente

class Venda(object):
    '''
    classdocs
    '''


    def __init__(self, cpfFuncionario, cpfCliente):
        '''
        Constructor
        '''
        self.idSaida = 0
        self.cpfFuncionario = cpfFuncionario
        self.cpfCliente = cpfCliente
        self.dataVenda = datetime.now()
        self.valorTotal = 0
        self.produtosVenda = []
        self.mCliente = modelCliente()
        self.mFuncionario = modelFuncionario()
    
    def addProduto(self, produto):
        self.produtosVenda.append(produto)
    
    def delProduto(self, numProduto):
        try:
            del(self.produtosVenda[numProduto])
        except IndexError:
            print("Este produto não existe na lista de produtos!")
        
    def iniciaVenda(self):
        ret = self.mFuncionario.verificaFuncionario(self.cpfFuncionario)
        if ret == "":
            print("Funcionario não encontrado!")
            break
        ret = self.mCliente.VerificaCliente(self.cpfCliente)
        if ret == "":
            print("Cliente não encontrado!")
            break
    
    def fechaVenda(self):
        pass