def vender_produto(estoque, produto):

    if produto in estoque:
        estoque.remove(produto)
        print(f"O produto {produto} foi vendido")
    else:
        print("O produto não está disponível")

    return estoque

estoque = ["Mouse", "Teclado", "Monitor", "Webcam"]

estoque_atualizado = vender_produto(estoque, "Monitor")

print(f"Estoque atualizado: {estoque_atualizado}")