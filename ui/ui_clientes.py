from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

class CadClientes(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ui_clientes.ui", self)