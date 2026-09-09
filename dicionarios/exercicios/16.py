def compra():
    compra = {
        'cliente': 'Maria',
        'produtos': []
    }

    for i in range(5):
        produto = input('Produto: ')
        compra['produtos'].append(produto)

    print(compra)

compra()