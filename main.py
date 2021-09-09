import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

from ui.ui_produtos import CadProdutos
from ui.ui_clientes import CadClientes


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("mainwindow.ui", self)
        # define os eventos dos botões
        self.b_cadProdutos.clicked.connect(self.openCadProdutos)
        self.b_cadClientes.clicked.connect(self.openCadClientes)

    def openCadProdutos(self):
        self.w = CadProdutos()
        self.w.show()
    
    def openCadClientes(self):
        self.w = CadClientes()
        self.w.show()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
