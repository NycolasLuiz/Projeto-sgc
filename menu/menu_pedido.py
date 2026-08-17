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
        print('='*62)
        print("PEDIDO CADASTRADO COM SUCESSO!")
        print('-'*62)
        print(f"PEDIDO: #{registroPedido.id_pedido}")
        print(f"DATA: {registroPedido.data_pedido}")
        print(f"CLIENTE: {registroPedido.cliente['nome']}")
        print(f"VALOR TOTAL: R$ {registroPedido.valor_total:.2f}")
        print('-'*62)
        print("PRODUTOS:")
        for produto in registroPedido.itens_pedido:
            print(f"- {produto['nome']} | R$ {produto['preco']:.2f}")
        print('='*62)    
    else:
        print("NÃO FOI POSSÍVEL CADASTRAR O PEDIDO.")
        menu_secundario()

def opcaoes_produtos():
    catalogo = pedido_service.lista_produtos()
   
    for produtos in catalogo:
        print(f"PRODUTO: {produtos['nome']} \n VALOR:{produtos['preco']}")
        print('_'*62)
    menu_secundario()
    
def cancela_pedido():
    id_pedido = int (input ("INFORME O ID DO PEDIDO: "))

    remove = pedido_service.cancelaCadastro(id_pedido)
    
    if remove:
        print("PRODUTO DELETADO COM SUCESSO!")
    else:
        print("ERRO, ID NÃO ENCONTRADO...")
    menu_secundario()    
        
def procura_pedido():
    id_informado = int(input("INFORME O ID DO PEDIDO: "))
    pedido = pedido_service.buscaDePedido(id_informado)

    if pedido:
        print(f"PEDIDO: #{pedido['id_pedido']}")
        print(f"CLIENTE: {pedido['cliente']['nome']}")
        print(f"TELEFONE: {pedido['cliente']['telefone']}")
        print(f"VALOR TOTAL: R$ {pedido['valor_total']:.2f}")
        print("-" * 62)
        print("PRODUTOS:")

        for produto in pedido["itens_pedido"]:
            print(f"- {produto['nome']} | R$ {produto['preco']:.2f}")

        print("=" * 62)

    else:
        print("ERRO, PEDIDO NÃO ENCONTRADO...")

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
        print("4 - BUSCA PEDIDO")
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
            procura_pedido()

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

