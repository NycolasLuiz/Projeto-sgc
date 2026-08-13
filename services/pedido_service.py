from models.pedido import Pedido
from repositories import pedido_repository
from repositories import cliente_repository
from repositories import produto_repository
from datetime import date


def cadastro_novoPedido(clienteTelefone, produtos):

    id_pedido = pedido_repository.geradorDeId()

    data_Pedido = date.today().isoformat()

    busca_cliente = cliente_repository.buscar_telefone(clienteTelefone)

    if not busca_cliente:
        return None

    itens_pedido = []

    for nome_produto in produtos:

        busca_produto = produto_repository.puxando_produto(nome_produto)

        if not busca_produto:
            return None

        itens_pedido.append(busca_produto)

    valor_total = 0

    novoPedido = Pedido(
        id_pedido,
        busca_cliente,
        itens_pedido,
        valor_total,
        data_Pedido,
        None
    )

    pedido_repository.cadastro_novoPedido(novoPedido)

    return novoPedido

def lista_produtos():
    listagem = produto_repository.listagemDePodutos()
    return listagem 
    
def cancelaCadastro(id_pedido):
    atualiza =  pedido_repository.delete_pedido(id_pedido)
    return atualiza

def alteraPedido(id_pedido,alteraCliente,novo_iten):
    atualiza = pedido_repository.atualiza_pedido(id_pedido,alteraCliente,novo_iten)
    return atualiza     
    

    
    