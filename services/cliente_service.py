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

def recadastrando(
        id_cliente,
        novo_nome,
        novo_telefone
    ):
    return cliente_repository.atualiza_cadastro(id_cliente,novo_nome,novo_telefone)

def deletando_cadastro(id_cliente):
    return cliente_repository.delt_cliente(id_cliente)