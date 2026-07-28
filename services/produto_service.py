from models.produto import Produto
from repositories import produto_repository

def cadastroDeproduto(nome,preco):
    novo_produto = Produto(nome,preco)
    produto_repository.cadastroNovoProduto(novo_produto)
    return novo_produto

def lista_produtos():
    listagem = produto_repository.listagemDePodutos()
    return listagem
