
from utils.venda import Venda
from utils.item_venda import ItemVenda

import models.database as db
import models.produtos_model as ProdutoModel
import models.clientes_model as ClienteModel


def addVenda(venda):
    """ OLHAR: Gatilhos
    https://www.sqlitetutorial.net/sqlite-trigger/"""

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
    #print(id_venda)

    # adicionar os itens
    sql_addItens = "INSERT INTO ItensVenda (id_venda, id_produto, qtd, valor_unit) VALUES (?,?,?,?)"

    listaItens = venda.getItens()
    for item in listaItens:
        valuesItem = [id_venda, item.produto.id,
                      item.quantidade, item.getValorUnitario()]
        cursor.execute(sql_addItens, valuesItem)
        conn.commit()

    conn.close

def getVendasCliente(id_cliente):
    conn = db.connect_db()
    cursor = conn.cursor()
    lista_de_vendas = []
    # busca as vendas e seus respectivos clientes
    # ORDER BY data DESC - ordernação decrescente - PROBLEMA PORQUE A DATA É UMA STRING
    sql = "SELECT * FROM Vendas WHERE id_cliente = ? ORDER BY data ASC;"
    cursor.execute(sql,[id_cliente])
    for v in cursor.fetchall(): # para cada venda faz:
        id_venda = v[0]
        id_cliente = v[1]
        valortotal = v[2]
        data = v[3]

        # para cada venda busca seus itens
        lista_de_itens = []
        sql_itens = "SELECT * FROM ItensVenda WHERE id_venda = ?;"
        valuesItens = [id_venda]
        cursor.execute(sql_itens, valuesItens)
        for i in cursor.fetchall():
            # a posição zero, i[0], é o id da venda.
            # Não precisamos porque já temos esse dado 
            id_produto = i[1]
            qtd = i[2]
            valor_unitario = i[3]

            produto = ProdutoModel.getProduto(id_produto)  # pega o produto
            item = ItemVenda(qtd, produto, valor_unitario)
            lista_de_itens.append(item)

        cliente = ClienteModel.getCliente(id_cliente)
        venda = Venda(id_venda, cliente, lista_de_itens, valortotal, data)
        lista_de_vendas.append(venda)
    conn.close()
    return lista_de_vendas

def getVendas():
    conn = db.connect_db()
    cursor = conn.cursor()
    lista_de_vendas = []
    # busca as vendas e seus respectivos clientes
    sql = "SELECT * FROM Vendas ORDER BY data desc;"
    cursor.execute(sql)
    for v in cursor.fetchall(): # para cada venda faz:
        id_venda = v[0]
        id_cliente = v[1]
        valortotal = v[2]
        data = v[3]

        # para cada venda busca seus itens
        lista_de_itens = []
        sql_itens = "SELECT * FROM ItensVenda WHERE id_venda = ?;"
        valuesItens = [id_venda]
        cursor.execute(sql_itens, valuesItens)
        for i in cursor.fetchall():
            # a posição zero, i[0], é o id da venda.
            # Não precisamos porque já temos esse dado 
            id_produto = i[1]
            qtd = i[2]
            valor_unitario = i[3]

            produto = ProdutoModel.getProduto(id_produto)  # pega o produto
            item = ItemVenda(qtd, produto, valor_unitario)
            lista_de_itens.append(item)

        cliente = ClienteModel.getCliente(id_cliente)
        venda = Venda(id_venda, cliente, lista_de_itens, valortotal, data)
        lista_de_vendas.append(venda)
    conn.close()
    return lista_de_vendas
