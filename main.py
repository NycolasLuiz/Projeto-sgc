from servicos.pedido_service import novo_pedido

pedido = novo_pedido()

print("\nPedido criado com sucesso!")

print(f"Cliente: {pedido.cliente.nome}")
print(f"Telefone: {pedido.cliente.telefone}")
print(f"Produto: {pedido.produto.nome}")
print(f"Valor: R$ {pedido.valor_total:.2f}")
print(f"Entrega: {pedido.periodo_entrega}")
print(f"Pagamento: {pedido.pagamento}")