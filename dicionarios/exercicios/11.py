def aumentar():
    produto = {
        'nome': 'Mouse',
        'preco': 100
    }

    aumento = float(input('Aumento: '))

    produto['preco'] += produto['preco'] * aumento / 100

    print(produto)

aumentar()