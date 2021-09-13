from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

from ui.table_clientes import TabelaClientes

class CadClientes(QWidget):
    def __init__(self):
        super(). __init__()
        uic.loadUi("ui/ui_clientes.ui",self)
        #insere a tabela no layout
        self.table = TabelaClientes(self)
        
        # insere a table no layout do main_window
        self.verticalLayout.addWidget(self.table)
    