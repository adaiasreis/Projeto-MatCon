from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem, QWidget, QHBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize, QRect


class TabelaItens():
    def __init__(self, tableWidget, parent):
        # ATRIBUTO DA CLASSE
        self.tableWidget = tableWidget
        self.parent = parent

        self.itemAtual = None
        self.listaItens = []

        # Configuração da tabela
        self.configTable()

        self.tableWidget.setRowCount(0)

    def configTable(self):
        self.tableWidget.verticalHeader().setVisible(False)
        #ajusta a altura das linhas
        self.tableWidget.verticalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents)
        # ajusta as colunas ao tamanho da tela
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                 QHeaderView.Stretch)

        # desabilita a edição dos campos
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        # seleciona toda a linha
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        # evento ao selecionar uma linha
        self.tableWidget.clicked.connect(self.on_click)

    def on_click(self):
        # linha onde foi clicado
        selected_row = self.tableWidget.currentRow()
        self.itemAtual = self.listaItens[selected_row]
        self.parent.btn_remover_item.setEnabled(True)

    # item - Objeto ItemVenda
    def _addRow(self, item):
        self.listaItens.append(item)
        rowCount = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowCount)
        # fixa a linha e muda a coluna conforme os valores
        qtd = QTableWidgetItem(str(item.quantidade))
        nome_produto = QTableWidgetItem(item.getNomeProduto())
        uni = QTableWidgetItem(str(item.getValorUnitario()))
        valor = QTableWidgetItem(str(item.getValor()))
        # insere os itens na tabela
        self.tableWidget.setItem(rowCount, 0, qtd)
        self.tableWidget.setItem(rowCount, 1, nome_produto)
        self.tableWidget.setItem(rowCount, 2, uni)
        self.tableWidget.setItem(rowCount, 3, valor)

        self.tableWidget.setCellWidget(rowCount, 4, CustomQWidget(item,self))

        self.calculaValorTotal()

    def calculaValorTotal(self):
        valorTotal = 0
        desconto = self.parent.desconto.text()
        if desconto == "":
            desconto = "0"

        # calcula o valor total
        for item in self.listaItens:
            valorTotal += (float(item.getValor()))

        # aplica o desconto
        desconto = float(desconto)  # converte para float
        if desconto < valorTotal:
            valorTotal = valorTotal - desconto

        # SE QUISER COLOCAR ALGUMA REGRA PARA O DESCONTO FAZER AQUI
        # EX.: O DESCONTO NÃO PODE SER MAIOR QUE 50% DO VALOR DO PRODUTO
        # EX.: APLICAR O DESCONTO DE 10%

        self.parent.valor_total.setText("%.2f" % valorTotal)

    def limparItens(self):
        self.tableWidget.setRowCount(0)
        self.itemAtual = None
        self.listaItens = []
        # desativo os botões
        self.parent.btn_remover_item.setEnabled(False)
        self.parent.btn_limpar_itens.setEnabled(False)
        # recarrea o combobox dos produtos
        self.parent.carregaDadosProdutos()
        self.calculaValorTotal()

    def limparSelecionado(self):
        self.listaItens.remove(self.itemAtual)
        novaLista = self.listaItens

        self.limparItens()
        # a lista não está vazia, logo pode limpar todos
        self.parent.btn_limpar_itens.setEnabled(True)
        # adiciona os elementos novamente na tabela
        for p in novaLista:
            self._addRow(p)


class CustomQWidget(QWidget):
    def __init__(self, item, parent):
        super(CustomQWidget, self).__init__()
        self.item = item
        self.parent = parent
        self.btn = QPushButton(self)
        self.btn.setText("")          #text
        self.btn.setIcon(QIcon("icons/delete.png"))  # icon
        self.btn.setShortcut('Ctrl+D')  # shortcut key
        self.btn.clicked.connect(self.remover)
        self.btn.setToolTip("Remover item "+str(self.item.produto.nome)+"?")  # Tool tip
        self.btn.setStyleSheet('QPushButton {background-color: #00FFFFFF; border:  none}') #remove a cor de fundo do botão e a borda
        self.btn.setIconSize(QSize(20,20))
        
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 10)
        layout.addWidget(self.btn)
        self.setLayout(layout)

    def remover(self):
        self.parent.itemAtual = self.item
        self.parent.limparSelecionado()
        print("Remover o item: ", self.item.produto.nome)
