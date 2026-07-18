import json

def salvar(cliente):
    PASTA = "data/clientes.json"
    dados_cleintes = cliente.to_dict()
    with open (PASTA, "r",encoding="utf-8") as arquivos:
        existe_cliente = json.load(arquivos)
        existe_cliente.append(dados_cleintes)
    with open(PASTA, "w", encoding="utf-8")as arquivos:
        json.dump (existe_cliente, arquivos, indent=4, ensure_ascii=False) 