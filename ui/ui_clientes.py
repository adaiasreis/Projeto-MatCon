from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

class ui_clientes(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui_clientes.ui", self)