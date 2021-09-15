from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

from utils.cliente import Cliente
from ui.table_clientes import TabelaClientes


class CadClientes(QWidget):
    def __init__(self):
        super(). __init__()
        uic.loadUi("ui/ui_clientes.ui", self)
        # insere a tabela no layout
        self.table = TabelaClientes(self)

        # insere a table no layout do main_window
        self.verticalLayout.addWidget(self.table)

        # mantém a referencia do item selecionado atualmente
        self.clienteAtual = None

        # eventos dos botões
        self.setEventos()

    # define os eventos de todos os botões
    def setEventos(self):
        self.salvar_btn.clicked.connect(self.salvarCliente)
        self.limpar_btn.clicked.connect(self.limpaCampos)
        self.excluir_btn.clicked.connect(self.excluirItem)

    def salvarCliente(self):
        # adiciona os campos na tabela
        novo = self.getCliente()
        # verifica os campos vazios
        if novo != None:
            # é um novo contato
            if self.clienteAtual == None:
                # manda add no banco de dados
                self.table.add(novo)
            else:
                # manda editar no bando de dados
                novo.id = self.clienteAtual.id
                self.table.update(novo)
            # limpa os campos
            self.limpaCampos()

    # pega as informações digitadas nos campos do Contato
    def getCliente(self):
        nome = self.nome.text()
        cpf = self.cpf.text()
        fone = self.fone.text()
        email = self.email.text()
        end = self.endereco.text()

        if((nome != "") and (cpf != "") and (fone != "") and (email != "") and (end != "")):
            return Cliente(-1, nome, cpf, fone, email, end)
        return None

    # limpa os campos e restaura os valores originais dos componentes
    def limpaCampos(self):
        self.clienteAtual = None
        self.nome.setText("")
        self.cpf.setText("")
        self.fone.setText("")
        self.email.setText("")
        self.endereco.setText("")

        self.salvar_btn.setText("Salvar")
        self.excluir_btn.setEnabled(False)

    # utilizado para preencher os campos na janela principal
    def insereInfo(self, cliente):
        self.clienteAtual = cliente
        self.nome.setText(cliente.nome)
        self.cpf.setText(cliente.cpf)
        self.fone.setText(cliente.telefone)
        self.email.setText(cliente.email)
        self.endereco.setText(cliente.endereco)

        # muda o nome do botão para atualizar (já que existe o Contato)
        self.salvar_btn.setText("Atualizar")
        self.excluir_btn.setEnabled(True)
    
    def excluirItem(self):
        self.table.delete(self.clienteAtual)
        # limpa os campos
        self.limpaCampos()
