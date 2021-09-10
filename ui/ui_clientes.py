from PyQt5.QtWidgets import QWidget
from PyQt5 import uic


class CadClientes(QWidget):
    def __init__(self):
        super(). __init__()
        uic.loadUi("ui/ui_clientes.ui",self)
        self.b_salvar.clicked.connect(self.salvarCliente)
        self.b_excluir.clicked.connect(self.excluirCliente)

    def salvarCliente(self):
        nome = self.nome.text()
        cpf = self.cpf.text()
        telefone = self.telefone.text()
        email = self.email.text()
        endereco = self.endereco.text()

        print("Salvar cliente...")
        self.informe.setText("Cliente salvo com sucesso!")
        self.limparCampos()

    def excluirCliente(self):
        print("Excluir cliente")
        self.informe.setText("Cliente excluido com sucesso!")
        self.limparCampos()

    def limparCampos(self):
        self.nome.setText("")
        self.cpf.setText("")
        self.telefone.setText("")
        self.email.setText("")
        self.endereco.setText("")
