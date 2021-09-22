from utils.venda import Venda
import models.database as db


def addVenda(venda):
    conn = db.connect_db()
    cursor = conn.cursor()

    # adiciona os campos na tabela vendas
    sql_addVenda = "INSERT INTO Vendas (id_cliente, valor_total, data) VALUES (?,?,?)"
    valuesVenda = [venda.cliente.id, venda.getValorTotal(), venda.data]
    cursor.execute(sql_addVenda, valuesVenda)
    conn.commit()

    # pega o ID do último elemento adicionado
    sql_id_venda = "SELECT LAST_INSERT_ROWID() AS id;"
    cursor.execute(sql_id_venda)
    rowID = cursor.fetchall()[0]
    id_venda = rowID[0]
    print(id_venda)

    # adicionar os itens
    sql_addItens = "INSERT INTO ItensVenda (id_venda, id_produto, qtd, valor_unit) VALUES (?,?,?,?)"

    listaItens = venda.getItens()
    for item in listaItens:
        valuesItem = [id_venda, item.produto.id, item.quantidade, item.getValorUnitario()]
        cursor.execute(sql_addItens, valuesItem)
        conn.commit()

    conn.close

def getVendas():
    sql ="SELECT v.id, c.nome as cliente, c.telefone, v.valor_total FROM Vendas v, Clientes c WHERE v.id_cliente = c.id;"
