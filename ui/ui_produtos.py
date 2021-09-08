from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

class ui_produtos(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui_produtos.ui", self)