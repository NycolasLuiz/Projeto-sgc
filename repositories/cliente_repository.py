import json

def salvar(cliente):
    PASTA = "data/clientes.json"
    dados_cleintes = cliente.to_dict()
    with open (PASTA, "r",encoding="utf-8") as arquivos:
        existe_cliente = json.load(arquivos)
        existe_cliente.append(dados_cleintes)
    with open(PASTA, "w", encoding="utf-8")as arquivos:
        json.dump (existe_cliente, arquivos, indent=4, ensure_ascii=False) 
        
def listar_clientes ():
    PASTA = "data/clientes.json"
    with open ( PASTA,"r",encoding="utf-8") as arquivos:
        clientes = json.load(arquivos)
        return clientes
    

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

def atualizar_cliente(identifiador,
        novo_nome,
        novo_telefone):
    PASTA = "data/clientes.json"
    with open (PASTA,"r",encoding="utf-8") as arquivos:
            clientes = json.load(arquivos)
            for cliente in clientes:
                if cliente['id'] == identifiador:
                    cliente['nome'] == novo_nome
                    cliente['telefone'] == novo_telefone
                with open(PASTA,"w",encoding="utf-8") as arquivos:
                    json.dump(novo_nome,novo_telefone,indent=4,ensure_ascii=False)