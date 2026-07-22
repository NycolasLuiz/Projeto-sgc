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

def recadastrando(identifiador, novo_nome, novo_telefone):
    cliente = cliente_repository.buscar_id(identifiador)

    if not cliente:
        return False

    return cliente_repository.atualizar_cliente(
        identifiador,
        novo_nome,
        novo_telefone
    )
    if cliente:
        print("CADASTRO ALTERADO")
    else:
        print("ERRO!! ID NÃO ENCONTRADO")