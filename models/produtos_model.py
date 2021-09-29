# IMPORTA A CLASSE PRODUTO
from utils.produto import Produto
import models.database as db

# PEGA TODOS OS PRODUTOS DO BANCO DE DADOS
def getProdutos():
    conn = db.connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Produtos ORDER BY nome;")
    lista_produtos = []
    for l in cursor.fetchall():
        id = l[0]
        nome = l[1]
        marca = l[2]
        descricao = l[3]
        precocompra = l[4]
        precovenda = l[5]
        quantidade = l[6]
        novoProduto = Produto(id, nome, marca, descricao, precocompra, precovenda, quantidade)
        lista_produtos.append(novoProduto)
    conn.close()
    return lista_produtos

def getProduto(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """SELECT * FROM Produtos WHERE ID = ?;"""
    cursor.execute(sql, [id])
    l = cursor.fetchall()[0]
    id = l[0]
    nome = l[1]
    marca = l[2]
    descricao = l[3] 
    precocompra = l[4]
    precovenda = l[5]
    quantidade = l[6]
    novoProduto = Produto(id, nome, marca, descricao, precocompra, precovenda, quantidade)
    conn.close
    return novoProduto

def addProduto(produto):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """INSERT INTO produtos (nome, marca, descricao, preco_compra, preco_venda, quantidade) VALUES (?, ?, ?, ?, ?, ?);"""
    cursor.execute(sql,[produto.nome, produto.marca, produto.descricao, produto.preco_compra, produto.preco_venda, produto.quantidade])
    conn.commit()
    conn.close()

def editProduto(produto):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """UPDATE produtos SET nome = ?, marca = ?, descricao = ?, preco_compra = ?, preco_venda = ?, quantidade = ? WHERE id = ?"""
    cursor.execute(sql,[produto.nome, produto.marca, produto.descricao, produto.preco_compra, produto.preco_venda, produto.quantidade, produto.id])
    conn.commit()
    conn.close()

def delProduto(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """ DELETE FROM produtos WHERE id = ?"""
    cursor.execute(sql, [id])
    conn.commit()
    conn.close()