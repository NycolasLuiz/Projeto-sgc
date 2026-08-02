from services import produto_service

def cadastra_produto():
    print("=" * 62)
    nome = input("NOME PRODUTO: ").strip()
    if not nome:
        print("ERRO!")
        return
    
    try: preco = float(input("VALOR PRODUTO: "))
    except ValueError as erro:
        erro
        print("ERRO, DIGITE UM NÚMERO!")
        return 
    
    if  preco <= 0:
        print("ERRO!")
        return
    print("=" * 62)
    
    novo_produto = produto_service.cadastroDeproduto(nome,preco)
    
    if novo_produto:
        print(f"PRODUTO: {novo_produto.nome} FOI CADASTRADO!")
    else:
        print("ERRO!!")
    menu_secundario()

def leitura_produtos():
    print("=" * 62)
    listagem = produto_service.lista_produtos()
   
    for produtos in listagem:
        print(f"PRODUTO: {produtos['nome']} \n VALOR:{produtos['preco']}")
        print('_'*62)
    menu_secundario() 

def buscar_produto():
    nome_produto = input ("INFORME O NOME DO PRODUTOS: ")
    retorno_produto = produto_service.procuraDeproduto(nome_produto)
    if retorno_produto:
        print (f"INFORMAÇÕES: {retorno_produto['nome']}\n {retorno_produto['preco']} ")
    else: 
        print("PRODUTO NÃO ENCONTRADO")
    menu_secundario()

def altera_produto():
    id_produto = input("INFORME O ID DO PODUTO: ")
    novo_nome = input("NOVO NOME:  ")
    try:
        novo_preco = float(input("NOVO PREÇO: "))
    except ValueError:
        print("Preço inválido.")
        return
    atualizacao = produto_service.alteraProduto(id_produto,novo_nome,novo_preco)

    if atualizacao:
        print(f"NOME:{atualizacao['nome']}\n {atualizacao['preco']}")
    else:
        print("ERRO, PRODUTO NÃO ENCONTRADO!")

    menu_secundario()
 
def delet_produto():
    id_produto = input ("INFORME O ID DO PRODUTO: ")

    remove = produto_service.cancelaCadastro(id_produto)
    
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


def menuDeProdutos():
    while True:

        cabecalho("MENU DE PRODUTOS")

        print("1 - CADASTRAR PRODUTO")
        print("2 - MOSTRAR PRODUTOS DISPONÍVEIS")
        print("3 - PESQUISAR PRODUTO")
        print("4 - ALTERAR PRODUTO")
        print("5 - EXCLUIR PRODUTO")
        print("0 - VOLTAR")

        opcao = pedir_opcao()

        if opcao == "1":
            cadastra_produto()

        elif opcao == "2":
            leitura_produtos()

        elif opcao == "3":
            buscar_produto()

        elif opcao == "4":
            altera_produto()

        elif opcao == "5":
            delet_produto()

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