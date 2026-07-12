class produto:
    def __init__(self, nome_produto, valor_produto):
        self.nome = nome_produto
        self.valor = valor_produto

def to_dict(self):
    return{
        "produto": self.nome,
        "valor": self.valor
    }