import uuid

class Cliente:
    def __init__(self, nome, telefone):
        self.id = str(uuid.uuid4())
        self.nome = nome
        self.telefone = telefone

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "telefone": self.telefone
        }