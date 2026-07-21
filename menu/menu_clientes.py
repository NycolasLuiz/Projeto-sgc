from services import cliente_service


def cadastro_clientes():
    try:
        print("=" * 62)

        nome = input("Nome: ").strip()
        if not nome:
            print("ERRO! Nome inválido.")
            return

        telefone = input("Telefone: ").strip()
        if not telefone:
            print("ERRO! Telefone inválido.")
            return

        print("=" * 62)

        novo_cliente = cliente_service.cadastrar_cliente(nome, telefone)

        print(f"Cliente: {novo_cliente.nome}, cadastro aprovado!")

        menu_secundario()

    except ValueError as erro:
        print(erro)


def listar_clientes():
    dados = cliente_service.listar_clientes()

    print("=" * 62)
    print("LISTA DE CLIENTES")
    print("=" * 62)

    for cliente in dados:
        print("-" * 30)
        print(f"ID: {cliente['id']}")
        print(f"NOME: {cliente['nome']}")
        print(f"TELEFONE: {cliente['telefone']}")

    menu_secundario()


def buscar_id():
    user = input("INFORME O ID: ")

    dados = cliente_service.buscar_id(user)

    menu_secundario()


def buscar_telefone():
    user = input("INFORME O TELEFONE (DDD)999999999: ")

    dados = cliente_service.buscar_telefone(user)

    menu_secundario()


def menu_principal():

    while True:

        print("=" * 62)
        print("                    MENU CLIENTES")
        print("=" * 62)
        print("1 - CADASTRAR CLIENTE")
        print("2 - LISTAR CLIENTES")
        print("3 - BUSCAR CLIENTE POR ID")
        print("4 - BUSCAR CLIENTE POR TELEFONE")
        print("0 - SAIR")
        print("=" * 62)

        opcao = input("OPÇÃO DESEJADA: ").strip()

        if opcao == "1":
            cadastro_clientes()

        elif opcao == "2":
            listar_clientes()

        elif opcao == "3":
            buscar_id()

        elif opcao == "4":
            buscar_telefone()

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("ERRO!! (ESCOLHA UMA OPÇÃO VÁLIDA)")


def menu_secundario():

    while True:

        print("=" * 62)
        print("1 - VOLTAR")
        print("0 - SAIR")
        print("=" * 62)

        opcao = input("OPÇÃO DESEJADA: ").strip()

        if opcao == "1":
            return

        elif opcao == "0":
            print("Saindo...")
            exit()

        else:
            print("ERRO!! (ESCOLHA UMA OPÇÃO VÁLIDA)")