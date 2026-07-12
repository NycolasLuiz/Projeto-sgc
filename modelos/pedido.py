class pedido:
    def __init__(self, cliente, produto, periodo_entrega, pagamento):
        self.cliente = cliente
        self.produto = produto
        self.periodo_entrega = periodo_entrega
        self.pagamento = pagamento

    def to_dict(self):
        return {
            "cliente": self.cliente.to_dict(),
            "produto": self.produto.to_dict(),
            "periodo_entrega": self.periodo_entrega,
            "pagamento": self.pagamento
        }