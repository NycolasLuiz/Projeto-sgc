import json

def carregar_produto():
    PASTA = "data/produtos.json"
    with open(PASTA,'r', encoding='utf-8') as arquivo:
        try: produtos = json.load(arquivo)
        except json.JSONDecodeError:
            produtos = []
            
