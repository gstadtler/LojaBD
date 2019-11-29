from model.produto import Produto as ModelProduto
from controller.validacoes import validaPreco, validaQtdEstoque, validaNome
class Produto(object):
    '''
    classdocs
    '''


    def __init__(self, id_produto="", nome="", preco_venda="", preco_compra="", qtd_estoque="" ):
        '''
        Constructor
        '''
        self.id = id_produto
        self.nome = nome
        self.preco_venda = preco_venda
        self.preco_compra = preco_compra
        self.qtd_estoque = qtd_estoque
        self.mProduto = ModelProduto(self)
        
    def validaProduto(self):
        validaPreco(self.preco_venda, self.preco_compra)
        validaQtdEstoque(self.qtd_estoque)
        validaNome(self.nome)
            
    def operacaoProduto(self, operacao):
        self.mProduto(operacao)
    
             
        