import uuid

class Produto:
    def __init__(self,nome, preco):
        
        self.id = str(uuid.uuid4())
        self.nome = nome
        self.preco = preco

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "preco": self.preco
        } 