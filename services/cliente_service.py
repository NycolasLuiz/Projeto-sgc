from models.cliente import Cliente

def cadastrar_cliente(nome, telefone):
    return Cliente(nome, telefone)