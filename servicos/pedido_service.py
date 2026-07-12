from modelos.cliente import cliente
from modelos.pedido import pedido
from modelos.produto import produto


def novo_pedido():
    nome = input("Nome: ")
    telefone = int(input("Telefone: "))
    novo_cliente = cliente(nome, telefone)

    nome_produto = input("Produto: ")
    valor_produto = float(input("Valor: "))
    novo_produto = produto(nome_produto, valor_produto)

    periodo_entrega = input("Manhã/Tarde/Noite: ")
    forma_pagamento = input("Débito,Crédito,Pix: ")

    meu_pedido = pedido(
        novo_cliente,
        novo_produto,
        periodo_entrega,
        forma_pagamento
    )
    return meu_pedido