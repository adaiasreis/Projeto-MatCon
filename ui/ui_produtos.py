from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

class CadProdutos(QWidget):
    def __init__(self):
        super(). __init__()
        uic.loadUi("ui/ui_produtos.ui",self)
        self.b_salvar.clicked.connect(self.salvarProduto)
        self.b_excluir.clicked.connect(self.excluirProduto)

    def salvarProduto(self):
        nome = self.nome.text()
        marca = self.marca.text()
        descricao = self.descricao.text()
        preco_compra = self.preco_compra.text()
        preco_venda = self.preco_venda.text()
        quantidade = self.quantidade.text()

        print("Salvar cliente...")
        self.informe.setText("Produto salvo com sucesso!")
        self.limparCampos()

    def excluirProduto(self):
        print("Excluir cliente")
        self.informe.setText("Produto excluido com sucesso!")
        self.limparCampos()

    def limparCampos(self):
        self.nome.setText("")
        self.marca.setText("")
        self.descricao.setText("")
        self.preco_compra.setText("")
        self.preco_venda.setText("")
        self.quantidade.setText("")

