# --  ARQUIVO PRINCIPAL -- #
# Futuramente será substituído pela UI

from models.clientes_model import *
import pandas as pd

# tratamento de erros
"""try:
    lista_clientes = getClientes()
except Exception as e:
    print("Erro ao consultar a tabela Cliente!")
    print(">> ", e)"""

id = int(input("Digite o id: "))
cliente = getCliente(id)
#cliente.print()

"""for clientes in lista_clientes:
    clientes.print()
"""

headers = ["id", "Nome"]
df = pd.DataFrame(cliente.getInfo(), headers)
print(df)