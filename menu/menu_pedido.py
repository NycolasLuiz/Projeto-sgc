from services import pedido_service


def cadastro_novoPedido():
    
    clienteTelefone = input("INFORME O TELEFONE DO CLIENTE: ")
    print("="*62)
    print("1 - INFORMAR MODELO")
    print("2 - VER OPÇÕES DISPONÍVEIS")
    print("="*62)

    opcao = input("INFORME A OPÇÃO DESEJADA: ")

    if opcao == "1":
        produto = input("INFORME O NOME DO PRODUTO DESEJADO: ")
    elif opcao == "2":
        print("EM DESENVOLVIMENTO")
    else: 
        print("ESCOLHA UMA OPÇÃO VÁLIDA")
        return opcao
    
    registroPedido = pedido_service.cadastro_novoPedido(clienteTelefone,produto)
    if registroPedido:
        print(f"LOCALIZADO/SENDO IMPLEMENTADO {produto}"   )
    else:
        print("NÃO LOCALIZADO/SENDO IMPLEMENTADO")
