from services import cliente_service
from menu import menu_principal
def busca ():
    
    while True:
        print("="*62)
        print("         MENU CLIENTES")
        print("="*62)
        print("1 - CADASTRAR CLIENTE")
        print("2 - LISTAR CLIENTES")
        print("3 - BUSCAR CLIENTE POR ID")
        print("4 - BUSCAR CLIENTE POR TELEFONE")
        print("0 - VOLTAR")
        
        opcao = input ("OPÇÃO DESEJADA: ")
        opcao_valida = ['1','2','3','4','0']
        if opcao not in  opcao_valida:
            print("_________________________________")
            print("ERRO!! (ESCOLHA UMA OPÇÃO VÁLIDA)")
            print("_________________________________")
        else: 
            if opcao == '1':
                menu_principal.cadastro()
            elif opcao == '2':
                dados = cliente_service.listar_clientes()
                print("LISTA DE CLIENTES: ")
                for clientes in dados:
                    print('-'*30)
                    print(f"ID: {clientes['id']}")
                    print(f"NOME: {clientes['nome']}")
                    print(f"TELEFONE: {clientes['telefone']}")
            elif  opcao == '3':
                user = input ("INFORME O ID: ")
                dados = cliente_service.buscar_id(user)
            elif opcao == '4':
                user = input("INFORME O TELEFONE (DDD)999999999: ")
                dados = cliente_service.buscar_telefone (user) 
            print('='*62)
            print('_____________1-VOLTAR/MENU________________') 
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
                    print("SAINDO...")
                    break
            
                
            