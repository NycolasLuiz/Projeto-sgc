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

def buscar_telefone_cliente():
    telefone = input("INFORME O TELEFONE (DDD)999999999: ")
    telefone_cliente = cliente_service.cliente_telefone(telefone)
    if telefone_cliente:
        print(f"NOME: {telefone_cliente['nome']}")
        print(f"TELEFONE: {telefone_cliente['telefone']}")
    else:
        print("ERRO! CLIENTE NÃO ENCONTRADO...")

    menu_secundario()
    
    
def alterar_cadastro():
    id_cliente = input("ID DO CLIENTE: ")

    novo_nome = input("NOVO NOME: ")
    novo_telefone = input("NOVO TELEFONE: ")

    resultado = cliente_service.recadastrando(
        id_cliente,
        novo_nome,
        novo_telefone
    )
    
    if resultado:
        print(f"CADASTRO ATUALIZADO!{resultado['nome']}-{resultado['telefone']}")
    else:
        print("ERRO, ID NÃO ENCONTRADO")
        
    menu_secundario()

def deletar_cadastro():
    id_cliente = input ("ID DO CLIENTE: ")
    
    delet = cliente_service.deletando_cadastro(id_cliente)
    
    if delet:
        print("CADASTRO DELETADO")
    else:
        print("ERRO, ID NÃO ENCONTRADO")    
        
    
        
def menu_principal():

    while True:

        print("=" * 62)
        print("                    MENU CLIENTES")
        print("=" * 62)
        print("1 - CADASTRAR CLIENTE")
        print("2 - LISTAR CLIENTES")
        print("3 - BUSCAR CLIENTE POR TELEFONE")
        print("4 - ATUALIZAR DADOS/CLIENTE")
        print("5 - DELETAR CLIENTE")
        print("0 - SAIR")
        print("=" * 62)

        opcao = input("OPÇÃO DESEJADA: ").strip()

        if opcao == "1":
            cadastro_clientes()

        elif opcao == "2":
            listar_clientes()

        elif opcao == "3":
            buscar_telefone_cliente()

        elif opcao == "4":
            alterar_cadastro()
        
        elif opcao == "5":
            print("FUNÇÃO INDEFINIDA AINDA")
            
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