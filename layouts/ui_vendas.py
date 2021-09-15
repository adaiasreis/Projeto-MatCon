from PyQt5.QtWidgets import QWidget
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
        self.tabelaItens = TabelaItens(self.tableWidget)
        

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
        self.combo_clientes.currentIndexChanged.connect(self.index_changed_cliente)
        self.combo_produtos.currentIndexChanged.connect(self.index_changed_produto)

        # botão add item
        self.btn_add_item.clicked.connect(self.addItem)

    # CLIENTE
    def index_changed_cliente(self, i):  # i é a posição do item selecionado
        print(self.lista_clientes[i].nome)
        # a lista do comboBox e a lista de clientes possuem o mesmo tamanho e itens, logo são iguais e podemos pegar o mesmo item da lista, o objeto cliente desejado
        self.clienteAtual = self.lista_clientes[i]
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
