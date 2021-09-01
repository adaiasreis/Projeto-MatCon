# classe cliente
# atributos do cliente = aos campos da tabela cliente

class Cliente:
    def __init__(self, id, nome, cpf, telefone, email, endereco):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def print(self):
        print("* --------------------------- *")
        print("id: ", self.id)
        print("nome: ", self.nome)
        print("cpf: ", self.cpf)
        print("telefone: ", self.telefone)
        print("email: ", self.email)
        print("endereço: ", self.endereco)
        print("* --------------------------- *")

