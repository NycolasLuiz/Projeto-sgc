from menu.menu_clientes import menu_principal
from menu.menu_produtos import menuDeProdutos

while True:
    print("="*62)
    print(" 1 - MENU/CLIENTES")
    print(" 2 - MENU/PRODUTOS")
    print(" 3 - MENU/PEDIDO")
    print(" 4 - MENU/COMISSÃO")
    print(" 5 - VOLTAR")
    print(" 0 - SAIR")
    print("="*62)
    
    opcao = input("OPÇÃO DESEJADA:")

    if opcao == "1":
        menu_principal()
    elif opcao == "2":
        menuDeProdutos()
    elif opcao == "3":
        print("FUNÇÃO EM DESENVOLVIMENTO")    
    elif opcao == "4":
        print("FUNÇÃO EM DESENVOLVIMENTO")
    elif opcao == "5":
        continue    
    elif opcao == "0":
        print("SAINDO....")
        break
    else:
        print("ERRO! ESCOLHA UMA OPÇÃO VÁLIDA")
        continue