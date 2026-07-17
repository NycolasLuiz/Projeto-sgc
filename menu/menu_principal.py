from services import cliente_service

def cadastro():
    
    while True:
        
        print("--------------------------------------")
        print("__________ESCOLHA A OPÇÃO_____________")
        print("______________1-NOVO/CLIENTE__________")
        print("______________0-SAIR__________________")
        print("--------------------------------------")
        
        print("__________________________________")
        opcao = input("INFORME A OPÇÃO DESEJADA: ")
        print("__________________________________")
        
        opcao_validas = ["0", "1"]
        
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
             
            elif opcao == "0":
                print("SAINDO...")        
                break
            

