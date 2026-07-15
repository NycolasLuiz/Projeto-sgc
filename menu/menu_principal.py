from models.cliente import Cliente

def cadastro ():
    while True:
        print('---------------------------------------')
        print('1-cadastras cliente')
        print('0-Sair')
        menu= input ('DIGITE A OPÇÃO DESEJADA: ')
        
        if menu not in ["0","1"]:
            print('OPÇÃO INVÁLIDA')   
        else:
            if menu == "1":
                
                nome = input ('Nome:')
                telefone = input ('Telefone: ')
                
                novo_cliente = Cliente(nome,telefone)
                
                print(novo_cliente.nome)
                print(novo_cliente.telefone)
            elif menu == "0":
                break
                
            

