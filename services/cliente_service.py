from models.cliente import Cliente
from repositories import cliente_repository

def cadastrar_cliente(nome, telefone):
    cliente = Cliente(nome,telefone)
    cliente_repository.salvar(cliente)
    return cliente

def listar_clientes():
    listagem = cliente_repository.listar_clientes()
    return listagem

def cliente_telefone(telefone):
    return cliente_repository.buscar_telefone(telefone)