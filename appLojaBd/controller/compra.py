from datetime import datetime
from model.fornecedor import Fornecedor as modelFornecedor
from model.compra import Compra as modelCompra

class Compra(object):
    '''
    classdocs
    '''


    def __init__(self, cnpjFornecedor, idEntrada=0, dataCompra=datetime.today().strftime('%Y-%m-%d'), valorTotal=0):
        '''
        Constructor
        '''
        self.idEntrada = idEntrada
        self.cnpjFornecedor = cnpjFornecedor
        self.dataCompra = dataCompra
        self.valorTotal = valorTotal
        self.produtosCompra = []
        self.mFornecedor = modelFornecedor()
        self.mCompra = modelCompra()
    
    def addProduto(self, produto):
        self.produtosCompra.append(produto)
    
    def delProduto(self, numProduto):
        try:
            del(self.produtosCompra[numProduto])
        except IndexError:
            print("Este produto não existe na lista de produtos!")
        
    def iniciaCompra(self):
        ret = self.mFornecedor.VerificaFornecedor(self.cnpjFornecedor)
        if ret == "":
            print("Fornecedor não encontrado!")
            return False
    
    def abreCompra(self):
        idCompra = self.mCompra.abreCompra(self)
        return idCompra[0]
        
    def fechaCompra(self):
        self.mCompra.fechaCompra(self)
        
    def listaCompraProdutos(self, idCompra):
        self.mCompra.retornaCompraProdutos(idCompra)
    
    def listaCompras(self):
        self.mCompra.retornaCompras()
        
    def relatoriosCompras(self, op, parametros):
        if op == 1:
            self.mCompra.relatComprasPeriodo(*parametros)
        elif op == 2:
            self.mCompra.relatComprasFornecedorPeriodo(*parametros)
        else:
            print("Operação inválida!")
            return False
        
        