from models.cliente import Cliente
from repositories import cliente_repository

def cadastrar_cliente(nome, telefone):
    cliente = Cliente(nome,telefone)
    cliente_repository.salvar(cliente)
    return cliente