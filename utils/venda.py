
class Venda():
    def __init__(self, id, cliente):
        self.id = -1
        self.cliente = cliente
        self.produtos = []  # lista de produtos
    
    # adicionar um item no carrinho
    def addItem(self, item):
        self.produtos.append(item)

    # quantidade de itens no carrinho
    def qtdItens(self):
        return len(self.produtos)
    
    # lista de itens
    def getItens(self):
        return self.produtos
    
    def valorTotal(self):
        soma = 0
        for i in self.produtos:
            soma += i.preco_venda
        return soma
    