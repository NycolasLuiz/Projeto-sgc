from models.pedido import Pedido
from repositories import pedido_repository
from repositories import cliente_repository
from datetime import date

def cadastro_novoPedido():
    id_pedido = pedido_repository.geradorDeId()
    data_Pedido = date.today().isoformat()
    busca_cliente = cliente_repository.buscar_telefone()
    novoPedido = Pedido(id_pedido,data_Pedido,busca_cliente)
    pedido_repository.cadastro_novoPedido(novoPedido)
    
    return novoPedido