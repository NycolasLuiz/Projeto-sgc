from models.pedido import Pedido
from repositories import pedido_repository
from repositories import cliente_repository
from repositories import produto_repository
from datetime import date


def cadastro_novoPedido(clienteTelefone,produto):

    id_pedido = pedido_repository.geradorDeId()

    data_Pedido = date.today().isoformat()

    busca_cliente = cliente_repository.buscar_telefone(clienteTelefone)

    busca_produto = produto_repository.puxando_produto(produto)

    if not busca_cliente:
        return None

    novoPedido = Pedido(
        id_pedido,
        busca_cliente,
        busca_produto,
        0,
        data_Pedido,
        None
    )

    pedido_repository.cadastro_novoPedido(novoPedido)

    return novoPedido