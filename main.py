import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

from controllers.ui_produtos import CadProdutos
from controllers.ui_clientes import CadClientes

from qt_material import apply_stylesheet

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("mainwindow.ui", self)
        # define os eventos dos botões
        self.listWidget.insertItem(0, "PRODUTOS")
        self.listWidget.insertItem(1, "CLIENTES")
        self.listWidget.insertItem(2, "NOVA VENDA")
        self.listWidget.insertItem(3, "LISTA DE VENDAS")

        # Stacked
        self.stackedWidget.addWidget(CadProdutos()) # Pág 0
        self.stackedWidget.addWidget(CadClientes()) # Pág 1

        #evento para selecionar a página
        self.listWidget.currentRowChanged.connect(self.display)

    def display(self, index):
        self.stackedWidget.setCurrentIndex(index)


app = QApplication(sys.argv)
#aplicar o tema no programa
apply_stylesheet(app, theme='dark_blue.xml')

window = MainWindow()
window.show()

app.exec()
