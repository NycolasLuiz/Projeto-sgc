import json

def salvar(cliente):
    PASTA = "data/clientes.json"
    novo_cliente = cliente.to_dict()

    with open(PASTA, "r", encoding="utf-8") as arquivos:
        try:
            clientes = json.load(arquivos)
        except json.JSONDecodeError:
            clientes = []

    clientes.append(novo_cliente)

    with open(PASTA, "w", encoding="utf-8") as arquivos:
        json.dump(clientes, arquivos, indent=4, ensure_ascii=False)

def buscar_telefone(telefone):
    PASTA = "data/clientes.json"
    with open (PASTA,"r",encoding="utf-8") as arquivos:
        
        telefone_clientes = json.load(arquivos)
        for telefone_cliente in telefone_clientes:

            if telefone_cliente.get("telefone") == telefone:
                return telefone_cliente
                
            for telefone_cliente in telefone_clientes:
                if telefone_cliente.get("telefone") == telefone:
                    return telefone_cliente
            return None    

def atualiza_cadastro(id_cliente,novo_nome,novo_telefone):
    
    PASTA = "data/clientes.json"
    with open(PASTA,"r",encoding="utf-8") as arquivos:
        
        clientes = json.load(arquivos)
    for cliente in clientes:
        if cliente ['id'] == id_cliente:
            cliente['nome'] = novo_nome
            cliente['telefone'] = novo_telefone
            
            
            with open (PASTA,"w", encoding="utf-8") as arquivos:
                json.dump(clientes, arquivos, ensure_ascii=False, indent=4)
                return cliente
    return None        
    
    
def delt_cliente(id_cliente):
    PASTA = "data/clientes.json"
    with open(PASTA,"r",encoding="utf-8") as arquivos:
        clientes = json.load(arquivos)
        dados_atualizados = [cliente for cliente in clientes if  cliente['id']!= id_cliente]
        if dados_atualizados != clientes:
            with open(PASTA,"w",encoding="utf-8") as arquivos:
                json.dump(dados_atualizados,arquivos, indent=4, ensure_ascii=False)
                return True
        return False       
   
            
def listar_clientes():
    PASTA = "data/clientes.json"
    with open(PASTA,"r",encoding="utf-8") as arquivos:
        dados = json.load(arquivos)
        return dados 