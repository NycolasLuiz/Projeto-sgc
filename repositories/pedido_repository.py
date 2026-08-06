import json

def carrega_pedidos():
    PASTA = "data/pedidos.json"
    with open(PASTA,'r', encoding='utf-8') as arquivo:
        try: pedido = json.load(arquivo)
        except json.JSONDecodeError:
            pedido = []
    return pedido     

def salva_pedido(pedido):
    PASTA = "data/pedidos.json"
    with open(PASTA,'w',encoding='utf-8') as arquivos:
        json.dump(pedido,arquivos,indent=4,ensure_ascii=False)   

def geradorDeId():#chamar função no serveces 
    registro_pedidos= carrega_pedidos()
    if len(registro_pedidos) == 0:
        return 1
    return max(pedido["id_pedido"] for pedido in registro_pedidos) + 1

def cadastro_novoPedido(novoPedido):#usar o mesmo parametro no serveces
    novoPedidoDICT= novoPedido.to_dict()
    registro_pedidos= carrega_pedidos()
    registro_pedidos.append(novoPedidoDICT)
    salva_pedido(registro_pedidos)

def atualiza_pedido(id_pedido):#aguardando parametros do serveces
    registro_pedidos  = carrega_pedidos()
    for pedido in registro_pedidos:
        if pedido['id_pedido'] == id_pedido:
            pedido['cliente']# =objeto vindo do menu/service
            pedido['itens_pedido']# = bjeto vindo do menu/service
            pedido['valor_total']# =objeto vindo do menu/service
            pedido['forma_pagamento']# = objeto vindo do menu/service
            salva_pedido(registro_pedidos)
            return pedido
    return 

def delete_pedido(id_pedido):#usar o mesmo parametro no serveces
    registro_pedidos  = carrega_pedidos()
    atualiza_registroPedidos = [pedido for pedido in registro_pedidos if pedido['id_pedido'] != id_pedido]
    if atualiza_registroPedidos != registro_pedidos:
        salva_pedido(atualiza_registroPedidos)
        return True
    return False
def Busca_pedido(id_informado):#usar o mesmo parametro no serveces
    registro_pedidos  = carrega_pedidos()
    for pedido in registro_pedidos:
        if pedido['id_pedido'] == id_informado:
            return pedido 
    return False
