def remover_item(itens, posicao):
    return itens.pop(posicao)

itens = ["Mouse", "Teclado", "Monitor"]

item_removido = remover_item(itens, 1)

print("Item removido:", item_removido)
print("Lista atualizada:", itens)