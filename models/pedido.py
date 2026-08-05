class Pedido:
    def __init__(self, id,cliente,itens_pedido,valor_total,data_pedido ):
        self.id =id
        self.cliente = cliente
        self.itens_pedido = itens_pedido
        self.valor_total = valor_total
        self.data_pedido = data_pedido

    def to_dict(self):
        return {
            "id": self.id,
            "cliente": self.cliente,
            "itens_pedido": self.itens_pedido,
            "valor_total": self.valor_total,
            "data_pedido": self.data_pedido
        }