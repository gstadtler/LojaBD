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
        self.mProduto = ModelProduto()
        self.quantidade = 0
        
    def validaProduto(self):
        self.validaPreco(self.preco_venda, self.preco_compra)
        self.validaQtdEstoque(self.qtd_estoque)
    
    def dadosEdicaoProd(self, nome, preco_venda, preco_compra, qtd_estoque ):
        if self.nome == "":
            self.nome = nome
        if self.preco_venda == "":
            self.preco_venda = preco_venda
        if self.preco_compra == "":
            self.preco_compra = preco_compra
        if self.qtd_estoque  == "":
            self.qtd_estoque = qtd_estoque
                
    def operacaoProduto(self, operacao):
        if operacao == "I":
            self.mProduto.procIADProduto(self, operacao)
        else:
            dadosProd = self.mProduto.recuperaDados(self.id)
            self.dadosEdicaoProd(*dadosProd)
            self.mProduto.procIADProduto(self, operacao)
    
    def validaPrecos(self):
        if self.preco_venda < self.preco_compra:
            print("O preço de venda não deve ser menor que o preço de compra do produto")
            return False

    def validaQtdEstoque(self):
        estoque = int(self.qtd_estoque)
        if estoque < 0:
            print("Quantidade de produtos inválida!")
            return False
        else:
            return True
        
    def validaQtdEstoqueVenda(self):
        estoque = int(self.qtd_estoque)
        if self.quantidade > estoque:
            print("Quantidade de produtos inválida!")
            return False
        else:
            return True
    
    def listaProdutos(self):
        self.mProduto.retornaProdutos()
        
    def buscaProduto(self, idProduto):
        return self.mProduto.recuperaProduto(idProduto)
    
    def relatProdutos(self, op, limite):
        if op == 1:
            params = ("DESC", limite)
        elif op == 2:
            params = ("ASC", limite)
        else:
            print("Operação inválida!")
            return False
        self.mProduto.relatProdutosVendidos(params)