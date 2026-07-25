class Produto:
    def __init__(self,id, nome, valor):
        
        self.id = id
        self.nome = nome
        self.valor = valor

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "valor": self.valor
        } 