from services import cliente_service
from menu import menu_clientes

def cadastro():
    
    while True:
        
        print("--------------------------------------")
        print("__________ESCOLHA A OPÇÃO_____________")
        print("______________1-NOVO/CLIENTE__________")
        print("______________0-SAIR__________________")
        print("______________2-VOLTAR/MENU___________")
        print("--------------------------------------")
        
        print("__________________________________")
        opcao = input("OPÇÃO DESEJADA: ")
        print("__________________________________")
        
        opcao_validas = ["0", "1","2"]
        
        if opcao not in opcao_validas :
            print("_________________________________")
            print("ERRO!! (ESCOLHA UMA OPÇÃO VÁLIDA)")
            print("_________________________________")
        else:
            if opcao == "1":
                
                try:
                    nome = input("Nome: ").strip()
                    if not nome:
                        print("ERRO!")
                        continue
                    telefone = (input("Telefone: ")).strip()
                    if not telefone:
                        print("ERRO!")
                        continue
                    
                    novo_cliente = cliente_service.cadastrar_cliente(nome,telefone)
                    print(f"Cliente: {novo_cliente.nome}, cadastro aprovado!")
                except ValueError as erro:
                    print(f"{erro}")
            elif opcao == "2":
                menu_clientes.busca
                break
             
            elif opcao == "0":
                print("SAINDO...")        
                break
            

