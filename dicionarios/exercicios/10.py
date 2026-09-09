def estoque():
    produto = {
        'nome': 'Mouse',
        'preco': 80,
        'estoque': 10
    }
    venda = int(input('Quantidade vendida: '))

    if venda <= produto['estoque']:
        produto['estoque'] -= venda
        print(produto)
    else:
        print('Estoque insuficiente')

estoque()