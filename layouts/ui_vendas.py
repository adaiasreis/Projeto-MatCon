from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

import models.clientes_model as ClientesModel
import models.produtos_model as ProdutosModel


class NovaVenda(QWidget):
    def __init__(self):
        super(). __init__()
        uic.loadUi("ui/ui_novavenda.ui", self)

        self.clienteAtual = None
        self.lista_clientes = []

        self.setEventos()

        self.carregaDadosClientes()
        # self.carregaDadosProdutos()

    def carregaDadosClientes(self):
        # dados do cliente
        self.lista_clientes = ClientesModel.getClientes()
        lista_combo = []
        for c in self.lista_clientes:
            lista_combo.append(c.nome)
        self.combo_clientes.addItems(lista_combo)

    def setEventos(self):
        # Envia a posição atual do item
        self.combo_clientes.currentIndexChanged.connect(self.index_changed)

    def index_changed(self, i):  # i é a posição do item selecionado
        print(self.lista_clientes[i].nome)
        # a lista do comboBox e a lista de clientes possuem o mesmo tamanho e itens, logo são iguais e podemos pegar o mesmo item da lista, o objeto cliente desejado
        self.clienteAtual = self.lista_clientes[i]
        self.id_lineEdit.setText(str(self.lista_clientes[i].id))
