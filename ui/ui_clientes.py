from PyQt5.QtWidgets import QWidget
from PyQt5 import uic


class CadClientes(QWidget):
    def __init__(self):
        super().__init__()
        # carrega os componentes (Widgets) para dentro da classe
        uic.loadUi("ui/ui_clientes.ui", self)

        # definindo os eventos dos botões
        self.b_salvar.clicked.connect(self.salvarCliente)
        self.b_excluir.clicked.connect(self.excluirCliente)

    def salvarCliente(self):
        nome = self.nome.text()
        rg = self.rg.text()
        cpf = self.cpf.text()
    
        print("Salvar cliente...")
        self.informe.setText("Cliente salvo com sucesso!")
        self.limparCampos()

    def excluirCliente(self):
        print("Excluir cliente")

    def limparCampos(self):
        self.nome.setText("")
        self.rg.setText("")
        self.cpf.setText("")
