# --  ARQUIVO PRINCIPAL -- #
# Futuramente será substituído pela UI

from models.clientes_model import *
"""uma edição quq""""
"banana amassada"
"""try:
    lista_clientes = getClientes()
except Exception as e:
    print("Erro ao consultar a tabela Cliente!")
    print(">> ", e)"""

"""id = int(input("Digite o id: "))
cliente = getCliente(id)
cliente.print()"""

"""for clientes in lista_clientes:
    clientes.print()
"""

"""novo = Cliente(-1, "Rafa Santos", "45678978987", "75 889988777", "rafasantos@email", "rua a")
novo.print()
addCliente(novo)"""


"""cliente = getCliente(2)
cliente.nome = "Maria José"
cliente.endereco = "Rua ABC, n78"

cliente.print()

editCliente(cliente)"""

print("\n\n")

delCliente(4)

try:
    lista_clientes = getClientes()
except Exception as e:
    print("Erro ao consultar a tabela Cliente!")
    print(">> ", e)

for clientes in lista_clientes:
    clientes.print()
