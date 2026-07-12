# modelos/cliente.py
class cliente:
    def __init__(self, nome_cliente, telefone):
        self.nome = nome_cliente
        self.telefone = telefone

    def to_dict(self):
        return {
            "nome": self.nome,
            "telefone": self.telefone
        }