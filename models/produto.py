import uuid

class Produto:
    def __init__(self,id,nome, preco,estoque):
        
        self.id = id
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "preco": self.preco,
            "estoque": self.estoque
        } 