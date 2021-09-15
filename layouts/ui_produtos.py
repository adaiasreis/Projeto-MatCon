from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

from ui.table_produtos import TabelaProdutos
from utils.produto import Produto

class CadProdutos(QWidget):
    def __init__(self):
        super(). __init__()
        uic.loadUi("ui/ui_produtos.ui", self)
        # insere a tabela no layout
        self.table = TabelaProdutos(self)

        # insere a table no layout do main_window
        self.verticalLayout.addWidget(self.table)

        # mantém a referencia do item selecionado atualmente
        self.produtoAtual = None

        # eventos dos botões
        self.setEventos()

    # define os eventos de todos os botões
    def setEventos(self):
        self.salvar_btn.clicked.connect(self.salvar)
        self.limpar_btn.clicked.connect(self.limpaCampos)
        self.excluir_btn.clicked.connect(self.excluir)

    def salvar(self):
        # adiciona os campos na tabela
        novo = self.getProduto()
        # verifica os campos vazios
        if novo != None:
            # é um novo contato
            if self.produtoAtual == None:
                # manda add no banco de dados
                self.table.add(novo)
            else:
                # manda editar no bando de dados
                novo.id = self.produtoAtual.id
                self.table.update(novo)
            # limpa os campos
            self.limpaCampos()

    # pega as informações digitadas nos campos do Contato
    def getProduto(self):
        nome = self.nome.text()
        marca = self.marca.text()
        descricao = self.descricao.text()
        preco_compra = self.preco_compra.text()
        preco_venda = self.preco_venda.text()
        quantidade = self.quantidade.text()

        if((nome != "") and (marca != "") and (descricao != "") and (preco_compra != "") and (preco_venda != "") and (quantidade != "")):
            return Produto(id, nome, marca, descricao, preco_compra, preco_venda, quantidade)
        return None

    # limpa os campos e restaura os valores originais dos componentes
    def limpaCampos(self):
        self.produtoAtual = None
        self.nome.setText("")
        self.marca.setText("")
        self.descricao.setText("")
        self.preco_compra.setText("")
        self.preco_venda.setText("")
        self.quantidade.setText("")

        self.salvar_btn.setText("Salvar")
        self.excluir_btn.setEnabled(False)

    # utilizado para preencher os campos na janela principal
    def insereInfo(self, produto):
        self.produtoAtual = produto
        self.nome.setText(produto.nome)
        self.marca.setText(produto.marca)
        self.descricao.setText(produto.descricao)
        self.preco_compra.setText(str(produto.preco_compra))
        self.preco_venda.setText(str(produto.preco_venda))
        self.quantidade.setText(str(produto.quantidade))

        # muda o nome do botão para atualizar (já que existe o Contato)
        self.salvar_btn.setText("Atualizar")
        self.excluir_btn.setEnabled(True)

    def excluir(self):
        self.table.delete(self.produtoAtual)
        # limpa os campos
        self.limpaCampos()
