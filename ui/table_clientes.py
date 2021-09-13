from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem
from PyQt5 import Qt

class TabelaClientes(QTableWidget):
    def __init__(self, janela_pai):
        super().__init__(0, 4) # config inicial da tabela(qtd_linha, qtd_colunas)
        # possui a referencia do pai
        self.janela_pai = janela_pai

         # textos do cabeçalho
        headers = ["ID", "NOME", "CPF", "TELEFONE"]  #alterar aqui
        self.setHorizontalHeaderLabels(headers)

        #Configuração da tabela
        self.configTable()
    
    def configTable(self):
        self.verticalHeader().setVisible(False)
        # ajusta as colunas ao tamanho da tela
        self.horizontalHeader().setStretchLastSection(False)
        self.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
        # desabilita a edição dos campos
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        # seleciona toda a linha
        self.setSelectionBehavior(QTableWidget.SelectRows)
        # evento ao selecionar uma linha
        #self.clicked.connect(self.on_click)
