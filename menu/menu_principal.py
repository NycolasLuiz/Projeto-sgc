from services import cliente_service

def cadastro():
    
    while True:
        
        print("--------------------------------------")
        print("__________ESCOLHA A OPÇÃO_____________")
        print("______________1-NOVO/CLIENTE__________")
        print("______________0-SAIR__________________")
        print("--------------------------------------")
        
        print("__________________________________")
        opcao = input("OPÇÃO DESEJADA: ")
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
            

def busca ():
    
    while True:
        print('='*62)
        print('ESCOLHA A OPÇÃO')
        print('_'*62)
        print('_____________1-LISTAR CLINTES_________________')
        print('_____________2-BUSCAR CLIENTE/ID______________')
        print('_____________3-BUSCAR CLIENTE/TELEFONE________')
        print('='*62)
        
        opcao = input ("OPÇÃO DESEJADA: ")
        opcao_valida = ['1','2','3']
        if opcao not in  opcao_valida:
            print("_________________________________")
            print("ERRO!! (ESCOLHA UMA OPÇÃO VÁLIDA)")
            print("_________________________________")
        else: 
            if opcao == '1':
                dados = cliente_service.listar_clientes()
            elif  opcao == '2':
                user = input ("INFORME O ID: ")
                dados = cliente_service.buscar_id(user)
            elif opcao == '3':
                user = input("INFORME O TELEFONE (DDD)999999999: ")
                dados = cliente_service.buscar_telefone (user)
            print('='*62)
            print('_____________1-VOLTAR_____________________') 
            print('_____________0-SAIR_______________________')
            print('='*62)
            
            validacao = input ("OPÇÃO DESEJADA: ")
            validacao_valida = ['0','1']
            if validacao not in  validacao_valida:
                print("_________________________________")
                print("ERRO!! (ESCOLHA UMA OPÇÃO VÁLIDA)")
                print("_________________________________")
            else: 
                if validacao == "1":
                    continue
                elif validacao == "0":
                    break
            
                
            