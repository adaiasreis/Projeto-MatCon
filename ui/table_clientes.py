from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem, QPushButton, QHBoxLayout, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
import models.clientes_model as ClientesModel
from layouts.ui_historico_cliente import HistoricoCliente


class TabelaClientes(QTableWidget):
    def __init__(self, janela_pai):
        super().__init__(0, 5)  # config inicial da tabela(qtd_linha, qtd_colunas)
        # possui a referencia do pai
        self.janela_pai = janela_pai

        # textos do cabeçalho
        headers = ["ID", "NOME", "CPF", "TELEFONE",
                   ""]  # alterar aqui
        self.setHorizontalHeaderLabels(headers)

        # Configuração da tabela
        self.configTable()

        # Carrega os dados do banco
        self.carregaDados()

    def configTable(self):
        self.verticalHeader().setVisible(False)
        # ajusta as colunas ao tamanho da tela
        self.horizontalHeader().setStretchLastSection(False)
        self.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        # ajusta a altura das linhas
        self.verticalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents)
        # desabilita a edição dos campos
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        # seleciona toda a linha
        self.setSelectionBehavior(QTableWidget.SelectRows)
        # evento ao selecionar uma linha
        self.clicked.connect(self.on_click)

    def carregaDados(self):
        self.lista_clientes = ClientesModel.getClientes()
        # necessário marcar a linha como a primeira para sobreescrever os dados da tabela
        self.setRowCount(0)  # reinicia a contagem de linhas add na tabela
        # adiciona os elementos na tabela
        for clientes in self.lista_clientes:
            self._addRow(clientes)

    def _addRow(self, clientes):
        rowCount = self.rowCount()
        self.insertRow(rowCount)
        # fixa a linha e muda a coluna conforme os valores
        id = QTableWidgetItem(str(clientes.id))
        nome = QTableWidgetItem(clientes.nome)
        cpf = QTableWidgetItem(clientes.cpf)
        phone = QTableWidgetItem(clientes.telefone)
        # insere os itens na tabela
        self.setItem(rowCount, 0, id)
        self.setItem(rowCount, 1, nome)
        self.setItem(rowCount, 2, cpf)
        self.setItem(rowCount, 3, phone)
        self.setCellWidget(
            rowCount, 4, IconHistoricot(clientes))

    def on_click(self):
        # linha onde foi clicado
        selected_row = self.currentRow()
        id = self.item(selected_row, 0).text()
        # preguiça
        cliente = ClientesModel.getCliente(id)
        # insere os valores nos campos na janela principal
        self.janela_pai.insereInfo(cliente)

    # funções para adicionar no banco de dados
    def add(self, contato):
        ClientesModel.addCliente(contato)
        # Carrega os dados do banco
        self.carregaDados()

    def update(self, contato):
        ClientesModel.editCliente(contato)
        # Carrega os dados do banco
        self.carregaDados()

    def delete(self, contato):
        ClientesModel.delCliente(contato.id)
        # Carrega os dados do banco
        self.carregaDados()


class IconHistoricot(QWidget):
    def __init__(self, cliente):
        super(IconHistoricot, self).__init__()
        self.cliente = cliente
        self.btn = QPushButton(self)
        self.btn.setText("")  # text
        self.btn.setIcon(QIcon("icons/historico.png"))  # icon
        self.btn.clicked.connect(self.abrirHistorico)
        self.btn.setToolTip(
            "Histórico de compras do cliente.")  # Tool tip
        # remove a cor de fundo do botão e a borda
        self.btn.setStyleSheet(
            'QPushButton {background-color: #00FFFFFF; border:  none}')
        self.btn.setIconSize(QSize(20, 20))

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 10)
        layout.addWidget(self.btn)
        self.setLayout(layout)

    def abrirHistorico(self):
        self.hcliente = HistoricoCliente(self.cliente)
        self.hcliente.show()
