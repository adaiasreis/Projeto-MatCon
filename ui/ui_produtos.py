from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

from ui.table_produtos import TabelaProdutos

class CadProdutos(QWidget):
    def __init__(self):
        super(). __init__()
        uic.loadUi("ui/ui_produtos.ui",self)
        # insere a tabela no layout
        self.table = TabelaProdutos(self)
        
        # insere a table no layout do main_window
        self.verticalLayout.addWidget(self.table)
        

    

