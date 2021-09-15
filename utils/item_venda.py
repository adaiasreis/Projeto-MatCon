
class ItemVenda:
    def __init__(self,quantidade, produto):
        self.quantidade = quantidade
        self.produto = produto
    
    def getNomeProduto(self):
        return self.produto.nome
    
    def getValorUnitario(self):
        return self.produto.preco_venda
    
    def getValor(self):
        return float(self.produto.preco_venda) * float(self.quantidade)
