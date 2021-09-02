# importar a classe cliente
from utils.clientes import Cliente
import models.database as db

# Pega todos os clientes do banco de dados


def getClientes():
    conn = db.connect_db()
    cursor = conn.cursor()
    # executa o comando de seleção dos clientes
    cursor.execute("""SELECT * FROM Clientes;""")
    # Coloca o resultado em uma lista de objetos clientes
    lista_clientes = []
    for l in cursor.fetchall():
        print(l)
        id = l[0]
        nome = l[1]
        cpf = l[2]
        telefone = l[3]
        email = l[4]
        endereco = l[5]
        # cria novo objeto
        novoCliente = Cliente(id, nome, cpf, telefone, email, endereco)
        # insere o novo cliente na lista
        lista_clientes.append(novoCliente)
    # fecha conexão
    conn.close()
    # retorna a lista
    return lista_clientes

# Retorna um cliente específico
def getCliente(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """SELECT * FROM Clientes WHERE id = ?;"""
    cursor.execute(sql, [id])  # lista de argumentos na mesma ordem das ?s
    # Coloca o resultado em uma lista de objetos clientes

    l = cursor.fetchall()[0]
    id = l[0]
    nome = l[1]
    cpf = l[2]
    telefone = l[3]
    email = l[4]
    endereco = l[5]
    # cria novo objeto
    novoCliente = Cliente(id, nome, cpf, telefone, email, endereco)
    # fecha conexão
    conn.close()
    # retorna a lista
    return novoCliente


def addCliente(cliente):
    sql = """INSERT INTO Clientes (nome,cpf,telefone,email, endereco) 
                VALUES (?,?,?,?,?);"""
    print("Novo cliente os campos do cliente")


def editCliente(cliente):
    print("Edita um cliente os campos do cliente")


def delCliente(id):
    print("Deleta um cliente específico")
