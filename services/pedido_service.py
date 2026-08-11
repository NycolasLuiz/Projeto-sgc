from models.pedido import Pedido
from repositories import pedido_repository
from repositories import cliente_repository
from datetime import date


def cadastro_novoPedido(clienteTelefone):

    id_pedido = pedido_repository.geradorDeId()

    data_Pedido = date.today().isoformat()

    busca_cliente = cliente_repository.buscar_telefone(clienteTelefone)

    if not busca_cliente:
        return None

    novoPedido = Pedido(
        id_pedido,
        busca_cliente,
        [],
        0,
        data_Pedido,
        None
    )

    pedido_repository.cadastro_novoPedido(novoPedido)

    return novoPedido