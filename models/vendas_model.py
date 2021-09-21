from utils.venda import Venda
import models.database as db

def addVenda(venda):
    sql_addVenda = "INSERT INTO Vendas (id_cliente, valor_total) VALUES (?,?)"

    # só funciona logo após o insert
    sql_id_venda= "SELECT LAST_INSERT_ROWID() AS id;"

    for item in venda.lista_de_itens:
        #add os itens na tabela de itens
        pass