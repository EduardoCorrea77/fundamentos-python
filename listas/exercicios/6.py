def encontrar_produto(produtos, produto):
    return produtos.index(produto)

produtos = ["Mouse", "Teclado", "Monitor"]

posicao = encontrar_produto(produtos, "Teclado")

print("O produto está na posição:", posicao)