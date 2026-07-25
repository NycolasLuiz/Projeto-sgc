from repositories import produto_repository
def cadastra_produto():
    print("=" * 62)
    nome = input("NOME PRODUTO: ").strip()
    if not nome:
        print("ERRO!")
        return
    
    try: preco = float (input ("VALOR PRODUTO: "))
    except ValueError as erro:
        print("ERRO, DIGITE UM NÚMERO!")
        return 
    
    if  preco <= 0:
        print("ERRO!")
        return
    print("=" * 62)
    novo_produto = produto_repository.salvar_produto(nome,preco)
    if novo_produto:
        print(f"PRODUTO {novo_produto['nome']} FOI CADASTRADO!")
    else:
        print("ERRO!!")
    menu_secundario()
    
    

def menuDeProdutos():
    while True:
        print("="*62)
        print("-----------ESCOLHA A OPÇÃO DESEJADA---------------")
        print("-----------1 CADASTRAR PRODUTO--------------------")
        print("-----------2 MOSTRAR PRODUTOS DISPONÍVEIS---------")
        print("-----------3 ALTERAR PRODUTO----------------------")
        print("-----------4 EXCLUIR PRODUTO----------------------")
        print("-----------0 SAIR-------------------------------- ")
        print("="*62)
        opcao  = input("INFORME A OPÇÃO DESEJADA: ").strip

        if opcao == "1":
            print("FUNÇÃO EM DESENVOLVIMENTO")
        elif opcao == "2":
            print("FUNÇÃO EM DESENVOLVIMENTO")
        elif opcao == "3":
            print("FUNÇÃO EM DESENVOLVIMENTO") 
        elif opcao == "4": 
            print("FUNÇÃO EM DESENVOLVIMENTO")
        elif opcao == "0":
            print("SAINDO....")
            break
        else:
            print("ERRO!!, ECOLHA UMA OPÇÃO VÁLIDA")


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