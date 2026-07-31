import json

def carregar_produto():
    PASTA = "data/produtos.json"
    with open(PASTA,'r', encoding='utf-8') as arquivo:
        try: produtos = json.load(arquivo)
        except json.JSONDecodeError:
            produtos = []
    return produtos     

def salva_produto(produtos):
    PASTA = "data/produtos.json"
    with open(PASTA,'w',encoding='utf-8') as arquivos:
        json.dump(produtos,arquivos,indent=4,ensure_ascii=False)   

            
def cadastroNovoProduto(novoProduto):
    produtos_novos = novoProduto.to_dict()
    produtos = carregar_produto()
    produtos.append(produtos_novos)
    salva_produto(produtos)

def listagemDePodutos():
    dados = carregar_produto()
    return dados

def puxando_produto(nome_produto):
    produtos = carregar_produto()
    for produto in produtos:
        if produto['nome'] == nome_produto:
            return produto
    return False

def modifica_produto(id_produto,novo_nome,novo_preco):
    dados =  carregar_produto()

    for produtos in dados:

        if produtos['id'] == id_produto:
            produtos['nome'] = novo_nome
            produtos['preco'] = novo_preco
            salva_produto(dados)
            return produtos 
    return None 

def apaga_produto(id_produto):
    produtos = carregar_produto()
    atualizacao = [produto for produto in produtos if produto['id'] != id_produto]
    if atualizacao != produtos:
        salva_produto(atualizacao)
        return True
    return False