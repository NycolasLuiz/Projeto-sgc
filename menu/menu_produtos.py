
def menuDeProdutos():
    while True:
        print("="*62)
        print("-----------ESCOLHA A OPÇÃO DESEJADA---------------")
        print("-----------1 CADASTRAR PRODUTO--------------------")
        print("-----------2 MOSTRAR PRODUTOS DISPONÍVEIS---------")
        print("-----------3 ALTERAR PRODUTO----------------------")
        print("-----------4 EXCLUIR PRODUTO----------------------")
        print("-----------0 SAIR-------------------------------- ")

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