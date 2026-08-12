from services import pedido_service

#fazer função para listar produtos e colocar dentro de um menu de escolha 
#fazer menu de seleção para o momento do pedido 
def cadastro_novoPedido():

    clienteTelefone = input("INFORME O TELEFONE DO CLIENTE: ")

    produtos = []

    produto = input("INFORME O NOME DO PRODUTO DESEJADO: ")
    produtos.append(produto)

    addProduto = input("ADICIONAR MAIS UM PRODUTO? (S/N): ").lower()

    while addProduto == "s":

        produto = input("INFORME O NOME DO PRODUTO DESEJADO: ")
        produtos.append(produto)

        addProduto = input("ADICIONAR MAIS UM PRODUTO? (S/N): ").lower()

    registroPedido = pedido_service.cadastro_novoPedido(
        clienteTelefone,
        produtos
    )

    if registroPedido:
        print(f"PEDIDO CADASTRADO COM SUCESSO!")
        print(f"PRODUTOS: {produtos}")
    else:
        print("NÃO FOI POSSÍVEL CADASTRAR O PEDIDO.")

#def opcaoes_produtos():
    
#    print("=" * 62)
#    listagem = pedido_service.lista_produtos()
   
#    for produtos in listagem:
#        print(f"PRODUTO: {produtos['nome']} \n VALOR:{produtos['preco']}")
#        print('_'*62)


