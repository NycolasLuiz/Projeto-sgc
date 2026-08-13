from services import pedido_service

#ajustar função para permitir somente 1 produto
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
    menu_secundario()

def opcaoes_produtos():
    
    linha()
    catalogo = pedido_service.lista_produtos()
   
    for produtos in catalogo:
        print(f"PRODUTO: {produtos['nome']} \n VALOR:{produtos['preco']}")
        print('_'*62)
    linha()
    
def altera_produto():
    id_pedido = int (input("INFORME O ID DO PEDIDO: "))    
    alteraCliente = input("INFORME O TELEFONE (DDD)999999999: ").strip()
    if not alteraCliente:
        print("ERRO!")
        return
    elif not len(alteraCliente) == 11:
        print("ERRO!")
        return    
    novo_iten = input("NOVO PRODUTO:  ")

    atualizacao = pedido_service.alteraPedido(id_pedido,alteraCliente,novo_iten)

    if atualizacao:
        print(f"TELEFONE:{atualizacao['telefone']}\n PRODUTO: {atualizacao['nome']}")
    else:
        print("ERRO, PRODUTO NÃO ENCONTRADO!")

    menu_secundario()    
    
def cancela_pedido():
    id_pedido = int (input ("INFORME O ID DO PEDIDO: "))

    remove = pedido_service.cancelaCadastro(id_pedido)
    
    if remove:
        print("PRODUTO DELETADO COM SUCESSO!")
    else:
        print("ERRO, ID NÃO ENCONTRADO...")
    menu_secundario()    
        


def linha():
    print("=" * 62)


def cabecalho(titulo):
    linha()
    print(titulo.center(62))
    linha()


def rodape():
    linha()


def pedir_opcao():
    rodape()
    return input("Digite a opção: ").strip()


def mensagem(texto):
    print(f"\n{texto}\n")


def menuDePedidos():
    while True:

        cabecalho("MENU DE PEDIDO")

        print("1 - CADASTRAR PEDIDO")
        print("2 - CATÁLOGO DE PRODUTOS")
        print("3 - CANCELAR PEDIDO")
        print("4 - EM DESENVOLVIMENTO")
        print("5 - EM DESENVOLVIMENTO")
        print("0 - VOLTAR")

        opcao = pedir_opcao()

        if opcao == "1":
            cadastro_novoPedido()

        elif opcao == "2":
            opcaoes_produtos()

        elif opcao == "3":
            cancela_pedido()

        elif opcao == "4":
            print("EM DESENVOLVIMENTO")

        elif opcao == "5":
            print("EM DESENVOLVIMENTO")

        elif opcao == "0":
            mensagem("Voltando ao menu principal...")
            break

        else:
            mensagem("ERRO! ESCOLHA UMA OPÇÃO VÁLIDA.")


def menu_secundario():

    while True:

        cabecalho("MENU")

        print("1 - VOLTAR")
        print("0 - SAIR")

        opcao = pedir_opcao()

        if opcao == "1":
            return

        elif opcao == "0":
            print("Saindo...")
            exit()

        else:
            mensagem("ERRO! ESCOLHA UMA OPÇÃO VÁLIDA.")

