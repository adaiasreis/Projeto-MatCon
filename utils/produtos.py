class Produto:
    def __init__(self, id, nome, marca, descricao, preco_compra, preco_venda, quantidade):
        self.id = id
        self.nome = nome
        self.marca = marca
        self.descricao = descricao
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.quantidade = quantidade

    def prints(self):
        info = [self.id, self.nome, self.marca, self.descricao, self.preco_compra, self.preco_venda, self.quantidade]
