from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

import models.clientes_model as ClientesModel
import models.produtos_model as ProdutosModel

class NovaVenda(QWidget):
    def __init__(self):
        super(). __init__()
        uic.loadUi("ui/ui_novavenda.ui", self)

        self.carregaDadosClientes()
        self.carregaDadosProdutos()

    def carregaDadosClientes(self):
        # dados do cliente
        lista = ClientesModel.getClientes()
        lista_combo = []
        for c in lista:
            lista_combo.append(str(c.id) + " - "+c.nome)
        self.combo_clientes.addItems(lista_combo)
    
    def carregaDadosProdutos(self):
        # dados do cliente
        lista = ProdutosModel.getProdutos()
        lista_combo = []
        for c in lista:
            lista_combo.append(str(c.id) + " - "+c.nome)
        self.combo_produtos.addItems(lista_combo)

