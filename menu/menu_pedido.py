from services import pedido_service


def cadastro_novoPedido():
    
    clienteTelefone = (input("INFORME O TELEFONE DO CLIENTE: "))
    registroPedido = pedido_service.cadastro_novoPedido(clienteTelefone)
    if registroPedido:
        print("LOCALIZADO/SENDO IMPLEMENTADO"   )
    else:
        print("NÃO LOCALIZADO/SENDO IMPLEMENTADO")