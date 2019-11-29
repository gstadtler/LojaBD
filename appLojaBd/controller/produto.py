from model.produto import Produto as ModelProduto
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
        self.validaPreco(self.preco_venda, self.preco_compra)
        self.validaQtdEstoque(self.qtd_estoque)
            
    def operacaoProduto(self, operacao):
        self.mProduto(operacao)
    
    def validaPreco(self, venda, compra):
        if venda < compra:
            print("O preço de venda não deve ser menor que o preço de compra do produto")

    def validaQtdEstoque(self, quantidade):
        if quantidade < 0:
            print("Quantidade de produtos inválida!")
             
        