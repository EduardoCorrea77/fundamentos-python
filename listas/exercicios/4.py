def remover_produto(produtos, produto):
    produtos.remove(produto)

produtos = ["Mouse", "Teclado", "Monitor"]

remover_produto(produtos, "Teclado")

print(produtos)