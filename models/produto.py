import uuid

class Produto:
    def __init__(self, nome, valor):
        self.id = str(uuid.uuid4())
        self.nome = nome
        self.valor = valor

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "valor": self.valor
        }