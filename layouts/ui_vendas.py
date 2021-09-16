from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from PyQt5 import uic


import models.clientes_model as ClientesModel
import models.produtos_model as ProdutosModel
from ui.table_itens_vendas import TabelaItens
from utils.item_venda import ItemVenda


class NovaVenda(QWidget):
    def __init__(self):
        super(). __init__()
        uic.loadUi("ui/ui_novavenda.ui", self)

        self.clienteAtual = None
        self.produtoAtual = None
        self.lista_clientes = []
        self.lista_produtos = []

        self.setEventos()

        self.carregaDadosClientes()
        self.carregaDadosProdutos()

        # classe para o controle do QTableWidget
        self.tabelaItens = TabelaItens(self.tableWidget, self)

        # para valição do campo QUANTIDADE
        # só é permitido valores inteiros e número com 5 algarismos
        """"mais exemplos: https://www.programcreek.com/python/example/106688/PyQt5.QtGui.QRegExpValidator"""
        qtd_validator = QRegExpValidator(QRegExp('^[1-9]{1}[0-9]{5}$'), self.qtd)
        self.qtd.setValidator(qtd_validator)

    def carregaDadosClientes(self):
        # dados do cliente
        self.lista_clientes = ClientesModel.getClientes()
        lista_combo = []
        for c in self.lista_clientes:
            lista_combo.append(c.nome)
        self.combo_clientes.addItems(lista_combo)

    def carregaDadosProdutos(self):
        # dados do cliente
        self.lista_produtos = ProdutosModel.getProdutos()
        lista_combo = []
        for c in self.lista_produtos:
            lista_combo.append(c.nome)
        self.combo_produtos.addItems(lista_combo)

    def setEventos(self):
        # Envia a posição atual do item
        self.combo_clientes.currentIndexChanged.connect(
            self.index_changed_cliente)
        self.combo_produtos.currentIndexChanged.connect(
            self.index_changed_produto)

        # botão add item
        self.btn_add_item.clicked.connect(self.addItem)

        # botão limpar itens
        self.btn_limpar_itens.clicked.connect(self.limparItens)

        # remove o item selecionado
        self.btn_remover_item.clicked.connect(self.limparSelecionado)

        # verifica a quantidade digitada
        self.qtd.textEdited.connect(self.qtd_edited)

    # CLIENTE
    def index_changed_cliente(self, i):  # i é a posição do item selecionado
        # a lista do comboBox e a lista de clientes possuem o mesmo tamanho e itens, logo são iguais e podemos pegar o mesmo item da lista, o objeto cliente desejado
        self.clienteAtual = self.lista_clientes[i]
        # coloca o ID no campo para visualização
        self.id_lineEdit.setText(str(self.lista_clientes[i].id))

    # PRODUTO
    def index_changed_produto(self, i):  # i é a posição do item selecionado
        self.produtoAtual = self.lista_produtos[i]
        self.marca.setText(self.lista_produtos[i].marca)
        self.valor.setText(str(self.lista_produtos[i].preco_venda))
        self.qtd_disp.setText(str(self.lista_produtos[i].quantidade))
        self.desc.setText(self.lista_produtos[i].descricao)

    # adiciona um item na tabela
    def addItem(self):
        item = ItemVenda(self.qtd.text(), self.produtoAtual)
        self.tabelaItens._addRow(item)
        self.btn_limpar_itens.setEnabled(True)
        self.btn_add_item.setEnabled(False)
        self.qtd.setText("")

    # adiciona um item na tabela
    def limparItens(self):
        self.tabelaItens.limparItens()

    # adiciona um item na tabela
    def limparSelecionado(self):
        self.tabelaItens.limparSelecionado()

    # executa a função toda vez que for digitado no campo QUANTIDADE
    def qtd_edited(self, s):
        # habilita o botão de adicionar apenas se estiver a quantidade disponível
        if s!="" and int(s) <= self.produtoAtual.quantidade:
            self.btn_add_item.setEnabled(True)
        else:
            self.btn_add_item.setEnabled(False)
