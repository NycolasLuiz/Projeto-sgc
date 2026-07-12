from modelos.cliente import Cliente
from modelos.pedido import Pedido
from modelos.produto import Produto


def novo_pedido():

    nome = input('Nome do cliente: ')
    telefone = input('Telefone do cliente: ')

    cliente = Cliente(nome, telefone)

    nome_produto = input('Nome do Produto: ')
    valor_produto = float(input('Valor do produto: '))

    produto = Produto(nome_produto, valor_produto)

    periodo_entrega = input('Período de entrega (Manhã/Tarde/Noite): ')
    pagamento = input('Forma de pagamento (Débito/Crédito/Pix): ')

    pedido = Pedido(
        cliente,
        produto,
        valor_produto,
        periodo_entrega,
        pagamento
    )

    return pedido