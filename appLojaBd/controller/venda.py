from datetime import datetime
from model.funcionario import Funcionario as modelFuncionario
from model.cliente import Cliente as modelCliente
from model.venda import Venda as modelVenda

class Venda(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.idSaida = 0
        self.dataVenda = datetime.today().strftime('%Y-%m-%d')
        self.valorTotal = 0
        self.produtosVenda = []
        self.cpfFuncionario = ""
        self.cpfCliente = ""
        self.mCliente = modelCliente()
        self.mFuncionario = modelFuncionario()
        self.mVenda = modelVenda() 
           
    def addProduto(self, produto):
        self.produtosVenda.append(produto)
    
    def delProduto(self, numProduto):
        try:
            del(self.produtosVenda[numProduto])
        except IndexError:
            print("Este produto não existe na lista de produtos!")
            return False
        
    def iniciaVenda(self, cpfFuncionario, cpfCliente):
        ret = self.mFuncionario.verificaFuncionario(cpfFuncionario)
        if ret == ():
            print("Funcionario não encontrado!")
            return False
        ret = self.mCliente.recuperaDados(cpfCliente)
        if ret == ():
            print("Cliente não encontrado!")
            return False
    
    def fechaVenda(self):
        self.calculaTotal()
        self.mVenda.insereVenda(self)
    
    def listaVendas(self):
        self.mVenda.retornaVendas()
        
    def listaVendaProdutos(self,idVenda):
        self.mVenda.retornaVendaProdutos(idVenda)
        
    def calculaTotal(self):
        total = 0
        for produto in self.produtosVenda:
            total = total + (produto.quantidade * float(produto.preco_venda))
        self.valorTotal = total
          
    def relatoriosVendas(self, op, parametros):
        if op == 1:
            self.mVenda.relatVendasPeriodo(*parametros)
        elif op == 2:
            self.mVenda.relatVendasFuncionarioPeriodo(*parametros)
        elif op == 3:
            self.mVenda.relTotVendasFuncionarioPeriodo(*parametros)
        else:
            print("Operação inválida!")
            return False
    