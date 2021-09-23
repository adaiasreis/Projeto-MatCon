from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem, QWidget, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5.QtGui import QIcon
from PyQt5 import uic

import models.vendas_model as VendasModel

TYPE = {'remove': 0, 'info': 1}


class Vendas(QWidget):
    def __init__(self, parent):
        super(). __init__()
        uic.loadUi("ui/ui_vendas.ui", self)

        self.parent = parent

        self.configTable()

        self.lista_de_vendas = []
        self.carregaVendas()

        self.nova_btn.clicked.connect(self.novaVenda)

    def novaVenda(self):
        self.parent.display(3)

    def configTable(self):
        self.tableWidget.verticalHeader().setVisible(False)
        # ajusta a altura das linhas
        self.tableWidget.verticalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents)
        # ajusta as colunas ao tamanho da tela
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                 QHeaderView.Stretch)

        # desabilita a edição dos campos
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        # seleciona toda a linha
        self.tableWidget.setSelectionBehavior(False)

    def carregaVendas(self):
        self.lista_de_vendas = VendasModel.getVendas()
        self.tableWidget.setRowCount(0)
        for v in self.lista_de_vendas:
            self._addRow(v)

    # item - Objeto ItemVenda
    def _addRow(self, item):
        rowCount = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowCount)
        # fixa a linha e muda a coluna conforme os valores
        id = QTableWidgetItem(str(item.id))
        data = QTableWidgetItem(item.data)
        nome = QTableWidgetItem(item.cliente.nome)
        fone = QTableWidgetItem(item.cliente.telefone)
        valor = QTableWidgetItem(str(item.getValorTotal()))

        # insere os itens na tabela
        self.tableWidget.setCellWidget(
            rowCount, 0, CustomQWidget(item, self, TYPE['info']))
        self.tableWidget.setItem(rowCount, 1, id)
        self.tableWidget.setItem(rowCount, 2, data)
        self.tableWidget.setItem(rowCount, 3, nome)
        self.tableWidget.setItem(rowCount, 4, fone)
        self.tableWidget.setItem(rowCount, 5, valor)
        self.tableWidget.setCellWidget(
            rowCount, 6, CustomQWidget(item, self, TYPE['remove']))


class CustomQWidget(QWidget):
    def __init__(self, item, parent, type):
        super(CustomQWidget, self).__init__()
        self.item = item
        self.parent = parent
        self.btn = QPushButton(self)
        self.btn.setText("")  # text

        if type == TYPE['remove']:
            self.typeDelete()
        else:
            self.typeInfo()

        # remove a cor de fundo do botão e a borda
        self.btn.setStyleSheet(
            'QPushButton {background-color: #00FFFFFF; border:  none}')
        

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 10)
        layout.addWidget(self.btn)
        self.setLayout(layout)

    def typeInfo(self):
        self.btn.setIcon(QIcon("icons/info.png"))  # icon
        self.btn.setShortcut('Ctrl+I')  # shortcut key
        self.btn.clicked.connect(self.maisInfo)
        self.btn.setToolTip(
            "Mais informações sobre a venda.")  # Tool tip
        self.btn.setIconSize(QSize(25, 25))

    def typeDelete(self):
        self.btn.setIcon(QIcon("icons/delete.png"))  # icon
        self.btn.setShortcut('Ctrl+D')  # shortcut key
        self.btn.clicked.connect(self.remover)
        self.btn.setToolTip(
            "Remover venda?")  # Tool tip
        self.btn.setIconSize(QSize(20, 20))

    def remover(self):
        pass

    def maisInfo(self):
        pass
