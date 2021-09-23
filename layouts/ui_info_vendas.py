from PyQt5.QtWidgets import QLabel, QVBoxLayout, QHeaderView, QTableWidget, QTableWidgetItem, QWidget, QHBoxLayout, QPushButton

from PyQt5 import uic

class InfoVenda(QWidget):
    def __init__(self, venda):
        super().__init__()
        uic.loadUi("ui/ui_info_vendas.ui", self)

        self.venda = venda

        self.cliente.setText(self.venda.cliente.nome)
        self.data.setText(self.venda.data)
        self.qtd.setText(str(self.venda.qtdItens()))
        self.valortotal.setText("R$ "+str(self.venda.getValorTotal()))
        