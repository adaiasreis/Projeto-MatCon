import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

from layouts.ui_produtos import CadProdutos
from layouts.ui_clientes import CadClientes
from layouts.ui_vendas import NovaVenda

from qt_material import apply_stylesheet


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/mainwindow.ui", self)

        # define os itens da lista
        self.listWidget.insertItem(0, "PRODUTOS")
        self.listWidget.insertItem(1, "CLIENTES")
        self.listWidget.insertItem(2, "NOVA VENDA")
        #self.listWidget.insertItem(3, "LISTA DE VENDAS")

        # seleciona o primeiro item como padrão
        self.listWidget.setCurrentRow(0)

        # carrega todas as janelas de uma só vez
        self.carregaJanelas()

        # evento para selecionar a página
        self.listWidget.currentRowChanged.connect(self.display)

    def carregaJanelas(self):
        """obs.: é possível carregar as janelas por demanda. 
            Ou seja, verifica qual o index do listWidget selecionado e insere a janela na respectiva posição """
        self.stackedWidget.insertWidget(0, CadProdutos())
        self.stackedWidget.insertWidget(1, CadClientes())
        self.stackedWidget.insertWidget(2, NovaVenda())

    def display(self, index):
        # necessário carregar as janelas a cada trasição para atualizar as informações
        self.carregaJanelas()
        self.stackedWidget.setCurrentIndex(index)


app = QApplication(sys.argv)
# aplicar o tema no programa
apply_stylesheet(app, theme='dark_blue.xml')

window = MainWindow()
window.show()

app.exec()
