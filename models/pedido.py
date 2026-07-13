import uuid

class Pedido:
    def __init__(self, cliente, produto, quantidade):
        self.id = str(uuid.uuid4())
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade
        self.valor_total = produto.valor * quantidade

    def to_dict(self):
        return {
            "id": self.id,
            "cliente": self.cliente.to_dict(),
            "produto": self.produto.to_dict(),
            "quantidade": self.quantidade,
            "valor_total": self.valor_total
        }