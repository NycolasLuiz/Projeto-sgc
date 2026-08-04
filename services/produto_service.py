from models.produto import Produto
from repositories import produto_repository

def cadastroDeproduto(id,nome,preco,estoque):
    novo_produto = Produto(id,nome,preco,estoque)
    produto_repository.cadastroNovoProduto(novo_produto)
    return novo_produto

def lista_produtos():
    listagem = produto_repository.listagemDePodutos()
    return listagem

def procuraDeproduto(nome_produto):
    return produto_repository.puxando_produto(nome_produto)

def alteraProduto(id_produto,novo_nome,novo_preco):
    atualiza = produto_repository.modifica_produto(id_produto,novo_nome,novo_preco)
    return atualiza 

def cancelaCadastro(id_produto):
    atualiza =  produto_repository.apaga_produto(id_produto)
    return atualiza

