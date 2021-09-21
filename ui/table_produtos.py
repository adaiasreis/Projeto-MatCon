from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem

import models.produtos_model as ProdutosModel


class TabelaProdutos(QTableWidget):
    def __init__(self, janela_pai):
        super().__init__(0, 6)  # config inicial da tabela(qtd_linha, qtd_colunas)
        # possui a referencia do pai
        self.janela_pai = janela_pai

        # textos do cabeçalho
        headers = ["ID", "NOME", "MARCA", "R$ COMPRA",
                   "R$ VENDA", "QUANTIDADE"]  # alterar aqui
        self.setHorizontalHeaderLabels(headers)

        # Configuração da tabela
        self.configTable()

        # referência a lista de contatos
        self.lista_contatos = []

        # Carrega os dados do banco
        self.carregaDados()

    def configTable(self):
        self.verticalHeader().setVisible(False)
        # ajusta as colunas ao tamanho da tela
        self.horizontalHeader().setStretchLastSection(False)
        self.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        # desabilita a edição dos campos
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        # seleciona toda a linha
        self.setSelectionBehavior(QTableWidget.SelectRows)
        # evento ao selecionar uma linha
        self.clicked.connect(self.on_click)

    def carregaDados(self):
        self.lista_produtos = ProdutosModel.getProdutos()
        # necessário marcar a linha como a primeira para sobreescrever os dados da tabela
        self.setRowCount(0)  # reinicia a contagem de linhas add na tabela
        # adiciona os elementos na tabela
        for produtos in self.lista_produtos:
            self._addRow(produtos)

    def _addRow(self, produtos):
        rowCount = self.rowCount()
        self.insertRow(rowCount)
        # fixa a linha e muda a coluna conforme os valores
        id = QTableWidgetItem(str(produtos.id))
        nome = QTableWidgetItem(produtos.nome)
        marca = QTableWidgetItem(produtos.marca)
        preco_compra = QTableWidgetItem(str(produtos.preco_compra))
        preco_venda = QTableWidgetItem(str(produtos.preco_venda))
        quantidade = QTableWidgetItem(str(produtos.quantidade))
        # insere os itens na tabela
        self.setItem(rowCount, 0, id)
        self.setItem(rowCount, 1, nome)
        self.setItem(rowCount, 2, marca)
        self.setItem(rowCount, 3, preco_compra)
        self.setItem(rowCount, 4, preco_venda)
        self.setItem(rowCount, 5, quantidade)

    def on_click(self):
        # linha onde foi clicado
        selected_row = self.currentRow()
        id = self.item(selected_row, 0).text()
        # preguiça
        produto = ProdutosModel.getProduto(id)
        # insere os valores nos campos na janela principal
        self.janela_pai.insereInfo(produto)

    # funções para adicionar no banco de dados
    def add(self, produto):
        ProdutosModel.addProduto(produto)
        # Carrega os dados do banco
        self.carregaDados()

    def update(self, produto):
        ProdutosModel.editProduto(produto)
        # Carrega os dados do banco
        self.carregaDados()

    def delete(self, produto):
        ProdutosModel.delProduto(produto.id)
        # Carrega os dados do banco
        self.carregaDados()
