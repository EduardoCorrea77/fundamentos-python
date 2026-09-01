def adicionar_produtos(compras, produtos):
    compras.extend(produtos)
    print(f"Lista de compras: {compras}")

def cancelar_compra(compras, produto):
    compras.remove(produto)
    print(f"O produto {produto} foi removido")

    print(f"Lista atualizada: {compras}")
compras = ["Arroz", "Feijão"]

novos_produtos = ["Café", "Leite", "Açúcar"]

adicionar_produtos(compras, novos_produtos)
cancelar_compra(compras, "Café")