class Pedido:
    def __init__(self, id_pedido,cliente,itens_pedido,valor_total,data_pedido,forma_pagamento):
        self.id_pedido =id_pedido
        self.cliente = cliente
        self.itens_pedido = itens_pedido
        self.valor_total = valor_total
        self.data_pedido = data_pedido
        self.forma_pagamento = forma_pagamento

    def to_dict(self):
        return {
            "id_pedido": self.id_pedido,
            "cliente": self.cliente,
            "itens_pedido": self.itens_pedido,
            "valor_total": self.valor_total,
            "data_pedido": self.data_pedido,
            "forma_pagamento": self.forma_pagamento
        }