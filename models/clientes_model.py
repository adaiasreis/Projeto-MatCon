# importar a classe cliente
from utils.clientes import Cliente

import sqlite3

# Pega todos os clientes do banco de dados


def getClientes():
    # cria a conexão
    conn = sqlite3.connect('models/db_matcon.db')
    # se comunicar com o BD
    cursor = conn.cursor()
    # executa o comando de seleção dos clientes
    cursor.execute("""SELECT * FROM Clientes;""")
    # Coloca o resultado em uma lista de objetos clientes
    lista_clientes = []
    for l in cursor.fetchall():
        id = l[0]
        nome = l[1]
        cpf = l[2]
        telefone = l[3]
        email = l[4]
        endereco = l[5]
        #cria novo objeto
        novoCliente = Cliente(id, nome, cpf, telefone, email, endereco)
        lista_clientes.append(novoCliente)
    # fecha conexão
    conn.close()
    # retorna a lista
    return lista_clientes


def getCliente(id):
    print("retorna um cliente específico")


def addCliente(cliente):
    print("Novo cliente os campos do cliente")


def editCliente(cliente):
    print("Edita um cliente os campos do cliente")


def delCliente(id):
    print("Deleta um cliente específico")
