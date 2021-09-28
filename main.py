import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QWidget, QListWidgetItem
from PyQt5 import uic

from layouts.ui_produtos import CadProdutos
from layouts.ui_clientes import CadClientes
from layouts.ui_nova_venda import NovaVenda
from layouts.ui_vendas import Vendas

from qt_material import apply_stylesheet

# CONFIGURAÇÃO DO LINUX
os.environ['XDG_SESSION_TYPE'] = 'Wayland'

def tema(app):
    # Open the qss styles file and read in the css-alike styling code
    breeze_light = 'style/light/stylesheet.qss'
    breeze_dark = 'style/dark/stylesheet.qss'
    meu_style = 'style/my_style.qss'
    with open(meu_style, 'r') as f:
        style = f.read()

        # Set the stylesheet of the application
        app.setStyleSheet(style)

# ICONE CUSTOMIADO PARA A LISTA - ALTERE COMO DESEJAR - PODE IMPORTAR UM .UI NORMALMENTE 
class CustomQWidget(QWidget):
    def __init__(self, icon, text, parent=None):
        super(CustomQWidget, self).__init__(parent)

        label_icon = QLabel(icon)
        label_text = QLabel(text)

        layout = QHBoxLayout()
        layout.addWidget(label_icon)
        layout.addWidget(label_text)
        layout.addWidget(label_icon)

        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/mainwindow.ui", self)

        # define os itens da lista
        # itens personalizados
        item = QListWidgetItem(self.listWidget)
        item_widget = CustomQWidget("+", "PRODUTOS")
        item.setSizeHint(item_widget.sizeHint())
        self.listWidget.insertItem(0,item)
        self.listWidget.setItemWidget(item, item_widget)

        item = QListWidgetItem(self.listWidget)
        item_widget = CustomQWidget("+", "CLIENTES")
        item.setSizeHint(item_widget.sizeHint())
        self.listWidget.insertItem(1,item)
        self.listWidget.setItemWidget(item, item_widget)

        item = QListWidgetItem(self.listWidget)
        item_widget = CustomQWidget("+", "VENDAS")
        item.setSizeHint(item_widget.sizeHint())
        self.listWidget.insertItem(2,item)
        self.listWidget.setItemWidget(item, item_widget)
        
        item = QListWidgetItem(self.listWidget)
        item_widget = CustomQWidget("+", "NOVA VENDA")
        item.setSizeHint(item_widget.sizeHint())
        self.listWidget.insertItem(3,item)
        self.listWidget.setItemWidget(item, item_widget)

        # seleciona o primeiro item como padrão
        self.listWidget.setCurrentRow(0)

        # carrega todas as janelas de uma só vez
        self.carregaJanelas()

        # evento para selecionar a página
        self.listWidget.currentRowChanged.connect(self.display)

        self.entrar_btn.clicked.connect(self.iniciarSistema)
    
    def iniciarSistema(self):
        self.stackedWidget_geral.setCurrentIndex(1)


    def carregaJanelas(self):
        """obs.: é possível carregar as janelas por demanda. 
            Ou seja, verifica qual o index do listWidget selecionado e insere a janela na respectiva posição """
        self.stackedWidget.insertWidget(0, CadProdutos())
        self.stackedWidget.insertWidget(1, CadClientes())
        self.stackedWidget.insertWidget(2, Vendas(self))
        self.stackedWidget.insertWidget(3, NovaVenda())

    def display(self, index):
        # necessário carregar as janelas a cada trasição para atualizar as informações
        self.carregaJanelas()
        self.stackedWidget.setCurrentIndex(index)
        self.listWidget.setCurrentRow(index)


app = QApplication(sys.argv)
apply_stylesheet(app, theme='dark_blue.xml')
#tema(app)

window = MainWindow()
window.show()

app.exec()
